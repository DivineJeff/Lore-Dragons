"""Inventário independente dos ZIPs; processamento não implica leitura narrativa.

Uso: python auditar_corpus.py --repo CAMINHO --out DIRETORIO [--private-output]
Somente biblioteca padrão. JSON de saída não reproduz conversas nem contas.
--private-output grava mensagens/caminhos completos apenas no diretório de trabalho.
Não atribui triagem ou consolidação sem ledger editorial externo.
"""
import argparse, collections, hashlib, json, re, zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
def sha(b): return hashlib.sha256(b).hexdigest()
def gitblob(b):return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def snowflake(mid):
 return datetime.fromtimestamp(((int(mid)>>22)+1420070400000)/1000,timezone.utc).isoformat() if mid.isdigit() else None

class Export(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.stack=[];self.messages=[];self.cur=None;self.group={};self.footer=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);cls=set(a.get('class','').split());frame={'tag':tag,'cls':cls,'attrs':a}
  if 'chatlog__message-group' in cls:self.group={}
  if 'chatlog__message-container' in cls:
   if self.cur is not None:raise ValueError('Contêiner de mensagem aninhado')
   self.cur={'id':a.get('data-message-id',''),'parts':[],'display':[],'edited':[],'attachments':[],'embeds':[],'replies':[]}
  if self.cur is not None:
   if 'chatlog__author' in cls or 'chatlog__system-notification-author' in cls:self.group={'uid':a.get('data-user-id',''),'name_parts':[],'login':a.get('title',''),'bot':False}
   if 'chatlog__author-tag' in cls:self.group['bot']=True
   if cls & {'chatlog__timestamp','chatlog__short-timestamp','chatlog__system-notification-timestamp'}:self.cur['timestamp_title']=a.get('title','')
   if 'chatlog__system-notification-content' in cls:self.cur['system']=True
   if 'chatlog__edited-timestamp' in cls:self.cur['edited'].append(a.get('title',''))
   if 'chatlog__reply-link' in cls:self.cur['replies'].append(a.get('onclick',''))
   if tag=='a' and any('attachment' in v for v in cls):self.cur['attachments'].append(a.get('href',''))
   if tag in {'br','li','p'} and self.inside('chatlog__content'):self.cur['parts'].append('\n')
  if tag not in VOID:self.stack.append(frame)
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  if tag not in VOID:self.handle_endtag(tag)
 def inside(self,c):return any(c in f['cls'] for f in self.stack)
 def handle_data(self,data):
  if self.inside('postamble'):self.footer.append(data)
  if self.cur is None:return
  if self.inside('chatlog__author') or self.inside('chatlog__system-notification-author'):self.group.setdefault('name_parts',[]).append(data)
  if self.inside('chatlog__content') or self.inside('chatlog__system-notification-content'):self.cur['parts'].append(data)
  if self.inside('chatlog__embed'):self.cur['embeds'].append(data)
  if self.inside('chatlog__timestamp') or self.inside('chatlog__short-timestamp') or self.inside('chatlog__system-notification-timestamp'):self.cur['display'].append(data)
 def handle_endtag(self,tag):
  if tag in VOID:return
  i=next((i for i in range(len(self.stack)-1,-1,-1) if self.stack[i]['tag']==tag),None)
  if i is None:return
  closed=self.stack[i:];self.stack=self.stack[:i]
  if any('chatlog__message-container' in f['cls'] for f in closed):
   m=self.cur;self.cur=None
   if m is None:raise ValueError('Fim sem mensagem')
   m['text']=''.join(m.pop('parts')).strip();m['timestamp_display']=''.join(m.pop('display')).strip();m['timestamp_utc']=snowflake(m['id'])
   m['actor_uid']=self.group.get('uid','');m['actor_name']=''.join(self.group.get('name_parts',[])).strip();m['bot']=self.group.get('bot',False)
   m['embeds']=''.join(m['embeds']).strip();self.messages.append(m)

def registry(repo):
 text=(repo/'docs/pesquisa/fase-3/Fontes-e-Evidencias.md').read_text(encoding='utf8');rows={}
 for sid,body in re.findall(r'^### ((?:S|PWR)\d+)\s*\n(.*?)(?=^### |\Z)',text,re.M|re.S):
  z=re.search(r'\[`([^`]+\.zip)`\]',body);o=re.search(r'ordinal, base 1\): \*\*(\d+)\*\*',body);h=re.search(r'SHA-256 do HTML: `([0-9a-f]+)`',body);n=re.search(r'Mensagens: (\d+)',body)
  if not all([z,o,h,n]):raise ValueError('Registro incompleto '+sid)
  key=(z[1],int(o[1]));assert key not in rows
  dates=re.search(r'Limites UTC: (.*?) — (.*?)\.',body)
  rows[key]={'source':sid,'sha256':h[1],'messages':int(n[1]),'body':body}
 for sid,n,ordinal,h in re.findall(r'>((?:PWR)\d+) \| (\d+) \| (\d+) \| `([0-9a-f]+)`',text):
  key=('Poderes Jogadores.zip',int(ordinal));assert key not in rows
  rows[key]={'source':sid,'sha256':h,'messages':int(n),'body':''}
 return rows

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--private-output',action='store_true');args=p.parse_args();repo=args.repo;out=args.out;out.mkdir(parents=True,exist_ok=True)
 reg=registry(repo);entries=[];sources=[];archives=[];allids=collections.defaultdict(list);allhash=collections.defaultdict(list);issues=[];priv=[];private_paths=[]
 for path in sorted(repo.glob('*.zip'),key=lambda x:x.name.casefold()):
  raw=path.read_bytes();ar={'archive':path.name,'bytes':len(raw),'sha256':sha(raw),'git_blob_sha1':gitblob(raw),'central_entries':0,'directories':0,'files':0,'crc_checked':False,'html_files':0,'messages':0}
  with zipfile.ZipFile(path) as z:
   ar['central_entries']=len(z.infolist());ar['directories']=sum(i.is_dir() for i in z.infolist());ar['files']=ar['central_entries']-ar['directories']
   names=collections.Counter(i.filename for i in z.infolist())
   ar['duplicate_names']=[sha(n.encode()) for n,c in names.items() if c>1]
   for ordinal,i in enumerate(z.infolist(),1):
    b=z.read(i);row={'archive':path.name,'ordinal':ordinal,'directory':i.is_dir(),'bytes':len(b),'crc32':f'{i.CRC:08x}','sha256':sha(b),'internal_path_sha256':sha(i.filename.encode()),'extension':Path(i.filename).suffix.lower()}
    private_paths.append({**row,'internal_path':i.filename})
    if not i.is_dir():allhash[row['sha256']].append([path.name,ordinal])
    if row['extension']=='.html' and not i.is_dir():
     ar['html_files']+=1;text=b.decode('utf8');parser=Export();parser.feed(text);parser.close();assert parser.cur is None
     msgs=parser.messages;direct=len(re.findall(r'\bdata-message-id\s*=',text));ids=[m['id'] for m in msgs]
     assert direct==len(msgs),(path.name,ordinal,direct,len(msgs))
     assert all(re.fullmatch(r'\d{18,19}',mid) for mid in ids),(path.name,ordinal,'ID inválido')
     r=reg.get((path.name,ordinal));sid=r['source'] if r else 'UNREGISTERED-'+str(ordinal)
     match=bool(r and r['sha256']==row['sha256'] and r['messages']==len(msgs))
     if not match:issues.append({'type':'registry_mismatch','archive':path.name,'ordinal':ordinal,'source':sid})
     times=[m['timestamp_utc'] for m in msgs]
     if r and times:
      dates=re.search(r'Limites UTC: (\S+) — (\S+)\.',r['body'])
      if dates and (dates[1]!=min(times) or dates[2].rstrip('.')!=max(times)):issues.append({'type':'registry_date_mismatch','source':sid})
     edited=sum(bool(m['edited']) for m in msgs);noactor=sum(not m['actor_uid'] for m in msgs)
     if noactor:issues.append({'type':'missing_actor','source':sid,'count':noactor})
     footer=''.join(parser.footer);footer_n=re.search(r'(?:Exported|Exportadas|exportadas).*?(\d[\d,.]*)\s+message(?:\(s\)|s)?',footer,re.I)
     if footer_n and int(re.sub(r'\D','',footer_n[1]))!=len(msgs):issues.append({'type':'footer_mismatch','source':sid})
     source={**row,'source':sid,'channel_id':re.search(r'\[(\d{17,19})\]',i.filename)[1] if re.search(r'\[(\d{17,19})\]',i.filename) else None,'messages':len(msgs),'empty_export':not msgs,'registry_match':match,'first_utc':min(times) if times else None,'last_utc':max(times) if times else None,'edited_marker_messages':edited,'messages_without_text':sum(not m['text'] for m in msgs),'messages_with_embeds':sum(bool(m['embeds']) for m in msgs),'messages_with_attachments':sum(bool(m['attachments']) for m in msgs),'system_notifications':sum(bool(m.get('system')) for m in msgs),'messages_without_actor':noactor,'html_container_count':direct,'inventory_complete':True,'processing_complete':True,'narrative_review_messages_this_run':0,'consolidation_review_messages_this_run':0,'message_id_sequence_sha256':sha('\n'.join(ids).encode()),'footer_count_available':bool(footer_n)}
     for index,m in enumerate(msgs):
      allids[m['id']].append([sid,index]);priv.append({'source':sid,'index':index,**m})
     sources.append(source);ar['messages']+=len(msgs)
    entries.append(row)
   ar['crc_checked']=True
  archives.append(ar)
 found={(s['archive'],s['ordinal']) for s in sources};missing=set(reg)-found
 if missing:issues.append({'type':'registered_file_missing','files':sorted(missing)})
 narrative=[s for s in sources if s['source'].startswith('S')];powers=[s for s in sources if s['source'].startswith('PWR')]
 nids={m['id'] for m in priv if m['source'].startswith('S')};pids={m['id'] for m in priv if m['source'].startswith('PWR')}
 summary={'schema':1,'method':'direct ZIP bytes + CRC + independent HTMLParser + data-message-id crosscount','archives':archives,'counts':{'zip_archives':len(archives),'central_entries':len(entries),'directories':sum(e['directory'] for e in entries),'files':sum(not e['directory'] for e in entries),'zero_byte_files':sum(not e['directory'] and e['bytes']==0 for e in entries),'narrative_exports_including_character_sheets':len(narrative),'nonempty_narrative_exports':sum(not s['empty_export'] for s in narrative),'empty_narrative_exports':sum(s['empty_export'] for s in narrative),'narrative_message_occurrences':sum(s['messages'] for s in narrative),'narrative_unique_message_ids':len(nids),'powers_exports':len(powers),'powers_message_occurrences':sum(s['messages'] for s in powers),'powers_unique_message_ids':len(pids),'cross_corpus_repeated_ids':len(nids&pids),'all_unique_message_ids':len(allids),'edited_marker_messages':sum(s['edited_marker_messages'] for s in sources),'inventoried_HTML':len(sources),'processed_message_occurrences':len(priv),'narrative_review_messages_this_run':0,'consolidation_review_messages_this_run':0},'duplicate_message_ids':{k:v for k,v in allids.items() if len(v)>1},'duplicate_file_sha256':{k:v for k,v in allhash.items() if len(v)>1},'issues':issues,'limitations':['Edit marker does not recover pre-edit text or revision history.','Snowflake dates are documentary creation time, not fictional calendar.','Processing completeness is checked against accessible message containers, not deleted/remote content.','Attachment/embedding references do not fetch remote media.','Empty export contains HTML but no exported messages.','Automated extraction is not narrative triage.','Names and full internal paths are available only in optional local private manifest; public locators use ZIP ordinal/channel/content and path hashes.']}
 for name,obj in [('manifesto-corpus.json',{'archives':archives,'entries':entries,'sources':sources}),('resultado-processamento.json',summary)]:
  (out/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 if args.private_output:
  (out/'caminhos-internos-local.json').write_text(json.dumps(private_paths,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
  with (out/'mensagens-reextraidas-local.jsonl').open('w',encoding='utf8') as f:
   for row in priv:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(json.dumps({'counts':summary['counts'],'archives':archives,'issues':issues,'duplicate_ids':len(summary['duplicate_message_ids']),'duplicate_files':len(summary['duplicate_file_sha256'])},ensure_ascii=False))
 if issues:raise SystemExit(1)
if __name__=='__main__':main()
