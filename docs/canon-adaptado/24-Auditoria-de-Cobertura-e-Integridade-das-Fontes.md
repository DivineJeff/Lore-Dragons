# Auditoria de cobertura e integridade das fontes — Etapa A

**Estado atual:** Etapa A concluída; B001 concluído; checkpoint B002.1 concluído e lote B002 em andamento. Auditoria final inteira ainda em andamento. Esta entrega não autoriza os grandes acontecimentos definitivos nem a Fase 6. A ressalva do PR #14 foi investigada, preservada e aprofundada; não foi descartada.

## Base histórica do B001 e preservação

Main examinada: `db7134a506ae52ba4e5bc9686af66bb8a09cbf6d`, merge do [PR #14](https://github.com/DivineJeff/Lore-Dragons/pull/14). O [PR #13](https://github.com/DivineJeff/Lore-Dragons/pull/13) está mesclado em `e9367b73b926328705e945b8f8f2180a1c61ffd1`; PRs #1–14 possuem data de integração. Inventário da base: 40 blobs, 32 Markdown e oito ZIPs. A cópia local foi reconciliada com os dois acréscimos do PR #14 e todos os blobs comparados por hash Git antes de criar a branch desta auditoria. Nenhum ZIP foi alterado. Diferenças entre versões de documentos foram preservadas pelo histórico.

Oito arquivos binários foram acessados localmente e seus hashes Git coincidem com os blobs da main. Portanto, limitação do conector para download binário não impediu a inspeção. Cada entrada foi realmente descomprimida; CRC verificado pelo leitor ZIP, bytes e SHA-256 registrados. Nenhuma fonte indisponível dentre esses arquivos. Anexos remotos, versões anteriores de mensagens editadas e mensagens excluídas não foram recuperados.

## Inventário direto dos ZIPs

| ZIP | Entradas centrais | Pastas | HTMLs | Mensagens exportadas | Integridade |
| --- | --- | --- | --- | --- | --- |
| Chats Privados.zip | 6 | 1 | 5 | 3888 | CRC e hash Git conferidos |
| Dragons cap 1 a 2 - ultimos chats.zip | 19 | 1 | 18 | 8085 | CRC e hash Git conferidos |
| Dragons Cap 1 a 2 temporada 1.zip | 50 | 1 | 49 | 14146 | CRC e hash Git conferidos |
| Dragons Cap 1 a 2 temporada 2.zip | 51 | 1 | 50 | 26535 | CRC e hash Git conferidos |
| Dragons Cap 1 a 2 temporada 3.zip | 50 | 1 | 49 | 20014 | CRC e hash Git conferidos |
| Dragons Cap 3 a 4 temporada 1.zip | 20 | 1 | 19 | 16328 | CRC e hash Git conferidos |
| jogadores.zip | 13 | 1 | 12 | 159 | CRC e hash Git conferidos |
| Poderes Jogadores.zip | 25 | 13 | 12 | 158 | CRC e hash Git conferidos |

Totais: **234 entradas, 20 pastas, 214 arquivos, todos HTML**; zero arquivos de zero bytes. As 202 fontes principais incluem **190 exports de chats e 12 fichas de jogadores**. Não são 202 cenas ou 202 canais narrativos distintos comprovados. As fichas somam 159 mensagens; os outros 190 exports somam 88.996. Os 12 HTMLs de poderes, com 158 mensagens, são corpus separado.

**Confirmado por contagem direta:** principal 89.155 ocorrências e 89.155 IDs únicos; poderes 158 ocorrências/IDs únicos; total 89.313, sem repetição de ID dentro ou entre corpora. Os 214 localizadores de Fontes e Evidências coincidem com ordinal, SHA-256 e contagem; limites UTC das 202 fontes S conferidos. Todas as mensagens têm IDs e timestamp documental derivável do snowflake.

**Vazios:** 16 exports principais com HTML válido e zero mensagens: S006, S007, S009, S011, S015, S017, S018, S019, S020, S021, S109, S147, S163, S177, S180, S190. Não são arquivos de zero bytes. S019 e S020 são duas entradas byte a byte idênticas: últimos chats, ordinais 15 e 16, SHA-256 `a70880fc2f500a73bab6b3bcd2de0ecccb5b83e9d37886115c406d5a993f33cb`. Como não contêm mensagens, a duplicação não infla a contagem de IDs. Não foi encontrada duplicação de nomes internos na mesma lista central.

**Edições:** 2.199 mensagens com marcador de edição — 2.189 principais e dez de poderes. Isso não conta quantas vezes foram editadas nem recupera o conteúdo anterior. Data de criação não data a inserção de um status ou frase editada. Há 55 notificações de sistema incluídas no denominador principal. Conversa, bots, fichas, spam e metajogo também continuam no denominador; ele não é contagem de fatos canônicos.

Nomes e caminhos internos completos foram examinados e preservados no manifesto local de trabalho. A versão pública usa nome do ZIP, ordinal, canal quando disponível e hash do caminho, para não republicar aliases de contas. O script pode reproduzir o manifesto integral local com `--private-output`; os ordinais permitem recuperar exatamente a entrada. Não há perda de localizador por essa apresentação pública. O [manifesto técnico](auditoria-fontes/manifesto-corpus.json) contém todos os arquivos e pastas, seus hashes, tamanhos, contagens e estado de cobertura por fonte.

## Protocolo e testes reproduzíveis

O [script](auditoria-fontes/auditar_corpus.py) usa somente a biblioteca padrão Python e lê os ZIPs da própria cópia do repositório. Exemplo, a partir da raiz:

```text
python docs/canon-adaptado/auditoria-fontes/auditar_corpus.py --repo . --out auditoria-local --private-output
```

O diretório de saída é material de trabalho: não publicar o JSONL de conversas nem o manifesto privado. Reexecutar sem `--private-output` produz somente metadados. A revisão narrativa B001 é um ledger editorial separado; não é criada automaticamente pelo parser.

Procedimento: ler a lista central; descomprimir cada entrada e validar CRC; decodificar HTML em UTF-8; percorrer contêineres sem herdar o filtro do parser anterior; manter mensagens normais e notificações de sistema, texto visível, marcadores de edição, referências de anexos/embeds e reply; conferir número de contêineres com contagem independente de `data-message-id`; conferir os 214 totais declarados no rodapé; verificar IDs, datas, duplicações e relação com Fontes e Evidências. Não baixar conteúdo remoto referenciado.

A extração antiga e a nova têm os mesmos **89.313 IDs e textos após normalização apenas de espaço em branco**. Zero diferenças nessa comparação. Esse teste sustenta ausência de perda conhecida de texto visível entre esses processamentos, sem garantir preservação de todo DOM, imagem remota, versão editada ou compreensão semântica. O [resultado de processamento](auditoria-fontes/resultado-processamento.json) e os [controles documentais/históricos](auditoria-fontes/controles-documentais-e-historicos.json) registram resultados e limitações.

Foram também encontrados e localizados na reextração 967 referências publicadas no formato fonte + mensagem, com 557 pares únicos; nenhum par aponta para fonte diferente ou ID inexistente. Há 19 ARC, 40 PS, 39 CRIT, 18 HAB e DD-01–DD-43. **Esse teste é de existência e estrutura, não auditoria semântica completa desses itens.** Não há documento duplicado byte a byte entre os 32 Markdown da base; documentos de alternativas e panoramas têm finalidades distintas. As anotações intermediárias locais contêm estados antigos e não substituem o registro atual. Nos documentos antigos 01–06/10–21, recomendações são históricas/propostas; decisões atuais estão em 13 e 22. A varredura editorial completa de todas as frases de aprovação ainda integra a etapa seguinte.

## Quatro coberturas separadas

| Cobertura | Principal | Poderes | Evidência e limite |
| --- | --- | --- | --- |
| A — inventário | 202/202 fontes; 89.155 mensagens | 12/12; 158 | Manifesto dos oito ZIPs; arquivos reais e hashes verificados. |
| B — processamento | 89.155/89.155 contêineres/IDs | 158/158 | Reextração direta, rodapés, registro e comparação de texto; apenas material acessível. |
| C — triagem narrativa nesta auditoria | **279/89.155 = 0,312938%** | **158/158** | B001: leitura contextual de S174/S198 e testemunhos selecionados dos HAB; dirigido, não varredura integral. |
| D — confronto/consolidação nesta auditoria | Os mesmos 279 IDs de B001 comparados em seu escopo | 158 IDs confrontados com definições/estados HAB | Duas omissões contextuais corrigidas; não significa adjudicar toda informação possível dos arquivos parcialmente lidos. |

Total B001: **437/89.313 = 0,489290%**. Os 249 testemunhos RP foram lidos com vizinhança de duas mensagens antes/depois de âncoras HAB, com sobreposições removidas; esse recorte não garante cenas inteiras ou ausência de ocorrências anteriores. S174 (13) e S198 (17) foram atravessadas integralmente; os demais 249 são intervalos dirigidos. O [ledger B001](auditoria-fontes/triagem-B001.json) preserva cada ID, índice base zero, hash do HTML, hash do texto, tipo de contexto e tratamento editorial. A contagem de triagem inclui mensagens periféricas não canônicas realmente vistas. Não são 437 fatos novos.

## Reconciliação das métricas históricas

| Registro preservado | Fontes declaradas completas | Mensagens dessas fontes, recalculadas | Percentual do principal |
| --- | --- | --- | --- |
| H01 — antes da espinha | 47 não vazias | 6.767 | 7,590% |
| H02 — checkpoint da espinha | 87 não vazias | 32.922 | 36,927% |
| H03 — fechamento | 186 não vazias | 89.155 | 100% **declarado por fontes** |

Hashes e listas de fontes de cada snapshot estão nos controles técnicos. Os números de 7,59% e 36,93% eram a soma das mensagens em fontes **declaradas integralmente lidas**, incluindo OOC/bots/spam/fichas; não eram percentual de fatos incorporados ou mensagens individualmente classificadas. O arredondamento de 36,927% para 36,93% não é divergência material. Não era, naquele momento, leitura de todas as mensagens.

Há prova de trabalho após H02: 36 arquivos de notas de fechamento, registro ampliado de novas leituras e relatório complementar 03A com **1.475 IDs distintos**, todos presentes nas fontes. As notas possuem resultados, retificações e limites específicos. Isso demonstra continuação efetiva e torna incorreto afirmar que a investigação parou em 36,927%. A diferença H02→H03 é 99 fontes e 56.233 mensagens; a soma dessas fontes existe e foi reprocessada agora.

Entretanto, o script histórico `finalize_phase3.py`, função `coverage()`, atribui incondicionalmente a todas as fontes não vazias os campos “integralmente lido”, `classified=True` e `cross_review=True`; o ledger final não contém um tratamento editorial individual por mensagem. O validador histórico confere esses campos e as âncoras, sem adjudicar independentemente cada interpretação. As notas sustentam muitos contextos, mas seus 1.475 IDs não equivalem a 1.475 mensagens apenas lidas, nem demonstram sozinhos leitura de todos os intervalos adjacentes.

**Respostas metodológicas:** houve processamento de todo o material disponível e continuidade da pesquisa além do checkpoint. Saturação estrutural é uma avaliação de suficiência dos arcos/dossiês, não prova automática de leitura exaustiva. A afirmação histórica de leitura integral é coerente com os totais e apoiada por notas de trabalho, mas **continua sem comprovação independente mensagem a mensagem**. Não foi demonstrada falsa; também não deve ser certificada somente pelo ledger gerado em fechamento. Há mensagens processadas sem análise narrativa individual demonstrável no material preservado. Não é possível quantificar retrospectivamente essa parcela como “não lida”: ausência de registro individual não prova ausência de leitura.

O processamento completo, o limite de rastreabilidade da triagem histórica e o novo B001 são três resultados distintos. A ressalva do PR #14 é procedente como limite de método e permanece aplicável. A Bíblia e o README de pesquisa passam a atribuir a leitura integral ao registro histórico, preservando a versão anterior e apontando para esta investigação.

## Cobertura por arquivo

“I/P” significa inventário/processamento executados. “C/D” conta somente IDs efetivamente examinados/confrontados em B001; zero não declara ausência de análise antiga. Vazios não contam mensagens lidas. SHA-256, ordinal, caminho interno por hash, datas, edição e demais campos estão no manifesto técnico, sem abreviar seus valores.

| Fonte | ZIP / ordinal | Mensagens | I/P | C/D B001 | Situação |
| --- | --- | --- | --- | --- | --- |
| [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | Chats Privados.zip / 2 | 1040 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S002](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002) | Chats Privados.zip / 3 | 783 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | Chats Privados.zip / 4 | 1016 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S004](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004) | Chats Privados.zip / 5 | 58 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | Chats Privados.zip / 6 | 991 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S006](../pesquisa/fase-3/Fontes-e-Evidencias.md#s006) | Dragons cap 1 a 2 - ultimos chats.zip / 2 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S007](../pesquisa/fase-3/Fontes-e-Evidencias.md#s007) | Dragons cap 1 a 2 - ultimos chats.zip / 3 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | Dragons cap 1 a 2 - ultimos chats.zip / 4 | 471 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S009](../pesquisa/fase-3/Fontes-e-Evidencias.md#s009) | Dragons cap 1 a 2 - ultimos chats.zip / 5 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S010](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010) | Dragons cap 1 a 2 - ultimos chats.zip / 6 | 635 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S011](../pesquisa/fase-3/Fontes-e-Evidencias.md#s011) | Dragons cap 1 a 2 - ultimos chats.zip / 7 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S012](../pesquisa/fase-3/Fontes-e-Evidencias.md#s012) | Dragons cap 1 a 2 - ultimos chats.zip / 8 | 70 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | Dragons cap 1 a 2 - ultimos chats.zip / 9 | 2486 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S014](../pesquisa/fase-3/Fontes-e-Evidencias.md#s014) | Dragons cap 1 a 2 - ultimos chats.zip / 10 | 244 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S015](../pesquisa/fase-3/Fontes-e-Evidencias.md#s015) | Dragons cap 1 a 2 - ultimos chats.zip / 11 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | Dragons cap 1 a 2 - ultimos chats.zip / 12 | 581 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S017](../pesquisa/fase-3/Fontes-e-Evidencias.md#s017) | Dragons cap 1 a 2 - ultimos chats.zip / 13 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S018](../pesquisa/fase-3/Fontes-e-Evidencias.md#s018) | Dragons cap 1 a 2 - ultimos chats.zip / 14 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S019](../pesquisa/fase-3/Fontes-e-Evidencias.md#s019) | Dragons cap 1 a 2 - ultimos chats.zip / 15 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S020](../pesquisa/fase-3/Fontes-e-Evidencias.md#s020) | Dragons cap 1 a 2 - ultimos chats.zip / 16 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S021](../pesquisa/fase-3/Fontes-e-Evidencias.md#s021) | Dragons cap 1 a 2 - ultimos chats.zip / 17 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S022](../pesquisa/fase-3/Fontes-e-Evidencias.md#s022) | Dragons cap 1 a 2 - ultimos chats.zip / 18 | 2041 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | Dragons cap 1 a 2 - ultimos chats.zip / 19 | 1557 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S024](../pesquisa/fase-3/Fontes-e-Evidencias.md#s024) | Dragons Cap 1 a 2 temporada 1.zip / 2 | 61 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S025](../pesquisa/fase-3/Fontes-e-Evidencias.md#s025) | Dragons Cap 1 a 2 temporada 1.zip / 3 | 6428 | Sim/Sim | 65/65 | B001 dirigido, restante pendente |
| [S026](../pesquisa/fase-3/Fontes-e-Evidencias.md#s026) | Dragons Cap 1 a 2 temporada 1.zip / 4 | 25 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S027](../pesquisa/fase-3/Fontes-e-Evidencias.md#s027) | Dragons Cap 1 a 2 temporada 1.zip / 5 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S028](../pesquisa/fase-3/Fontes-e-Evidencias.md#s028) | Dragons Cap 1 a 2 temporada 1.zip / 6 | 163 | Sim/Sim | 5/5 | B001 dirigido, restante pendente |
| [S029](../pesquisa/fase-3/Fontes-e-Evidencias.md#s029) | Dragons Cap 1 a 2 temporada 1.zip / 7 | 18 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S030](../pesquisa/fase-3/Fontes-e-Evidencias.md#s030) | Dragons Cap 1 a 2 temporada 1.zip / 8 | 3 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S031](../pesquisa/fase-3/Fontes-e-Evidencias.md#s031) | Dragons Cap 1 a 2 temporada 1.zip / 9 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S032](../pesquisa/fase-3/Fontes-e-Evidencias.md#s032) | Dragons Cap 1 a 2 temporada 1.zip / 10 | 197 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S033](../pesquisa/fase-3/Fontes-e-Evidencias.md#s033) | Dragons Cap 1 a 2 temporada 1.zip / 11 | 7 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S034](../pesquisa/fase-3/Fontes-e-Evidencias.md#s034) | Dragons Cap 1 a 2 temporada 1.zip / 12 | 30 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S035](../pesquisa/fase-3/Fontes-e-Evidencias.md#s035) | Dragons Cap 1 a 2 temporada 1.zip / 13 | 263 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S036](../pesquisa/fase-3/Fontes-e-Evidencias.md#s036) | Dragons Cap 1 a 2 temporada 1.zip / 14 | 28 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S037](../pesquisa/fase-3/Fontes-e-Evidencias.md#s037) | Dragons Cap 1 a 2 temporada 1.zip / 15 | 938 | Sim/Sim | 15/15 | B001 dirigido, restante pendente |
| [S038](../pesquisa/fase-3/Fontes-e-Evidencias.md#s038) | Dragons Cap 1 a 2 temporada 1.zip / 16 | 37 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S039](../pesquisa/fase-3/Fontes-e-Evidencias.md#s039) | Dragons Cap 1 a 2 temporada 1.zip / 17 | 248 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S040](../pesquisa/fase-3/Fontes-e-Evidencias.md#s040) | Dragons Cap 1 a 2 temporada 1.zip / 18 | 13 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S041](../pesquisa/fase-3/Fontes-e-Evidencias.md#s041) | Dragons Cap 1 a 2 temporada 1.zip / 19 | 931 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S042](../pesquisa/fase-3/Fontes-e-Evidencias.md#s042) | Dragons Cap 1 a 2 temporada 1.zip / 20 | 9 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S043](../pesquisa/fase-3/Fontes-e-Evidencias.md#s043) | Dragons Cap 1 a 2 temporada 1.zip / 21 | 848 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S044](../pesquisa/fase-3/Fontes-e-Evidencias.md#s044) | Dragons Cap 1 a 2 temporada 1.zip / 22 | 64 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S045](../pesquisa/fase-3/Fontes-e-Evidencias.md#s045) | Dragons Cap 1 a 2 temporada 1.zip / 23 | 21 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S046](../pesquisa/fase-3/Fontes-e-Evidencias.md#s046) | Dragons Cap 1 a 2 temporada 1.zip / 24 | 285 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S047](../pesquisa/fase-3/Fontes-e-Evidencias.md#s047) | Dragons Cap 1 a 2 temporada 1.zip / 25 | 185 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S048](../pesquisa/fase-3/Fontes-e-Evidencias.md#s048) | Dragons Cap 1 a 2 temporada 1.zip / 26 | 9 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S049](../pesquisa/fase-3/Fontes-e-Evidencias.md#s049) | Dragons Cap 1 a 2 temporada 1.zip / 27 | 82 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S050](../pesquisa/fase-3/Fontes-e-Evidencias.md#s050) | Dragons Cap 1 a 2 temporada 1.zip / 28 | 26 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S051](../pesquisa/fase-3/Fontes-e-Evidencias.md#s051) | Dragons Cap 1 a 2 temporada 1.zip / 29 | 9 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S052](../pesquisa/fase-3/Fontes-e-Evidencias.md#s052) | Dragons Cap 1 a 2 temporada 1.zip / 30 | 234 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S053](../pesquisa/fase-3/Fontes-e-Evidencias.md#s053) | Dragons Cap 1 a 2 temporada 1.zip / 31 | 9 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S054](../pesquisa/fase-3/Fontes-e-Evidencias.md#s054) | Dragons Cap 1 a 2 temporada 1.zip / 32 | 26 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S055](../pesquisa/fase-3/Fontes-e-Evidencias.md#s055) | Dragons Cap 1 a 2 temporada 1.zip / 33 | 15 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S056](../pesquisa/fase-3/Fontes-e-Evidencias.md#s056) | Dragons Cap 1 a 2 temporada 1.zip / 34 | 43 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S057](../pesquisa/fase-3/Fontes-e-Evidencias.md#s057) | Dragons Cap 1 a 2 temporada 1.zip / 35 | 361 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S058](../pesquisa/fase-3/Fontes-e-Evidencias.md#s058) | Dragons Cap 1 a 2 temporada 1.zip / 36 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S059](../pesquisa/fase-3/Fontes-e-Evidencias.md#s059) | Dragons Cap 1 a 2 temporada 1.zip / 37 | 53 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S060](../pesquisa/fase-3/Fontes-e-Evidencias.md#s060) | Dragons Cap 1 a 2 temporada 1.zip / 38 | 222 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S061](../pesquisa/fase-3/Fontes-e-Evidencias.md#s061) | Dragons Cap 1 a 2 temporada 1.zip / 39 | 11 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S062](../pesquisa/fase-3/Fontes-e-Evidencias.md#s062) | Dragons Cap 1 a 2 temporada 1.zip / 40 | 17 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S063](../pesquisa/fase-3/Fontes-e-Evidencias.md#s063) | Dragons Cap 1 a 2 temporada 1.zip / 41 | 10 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S064](../pesquisa/fase-3/Fontes-e-Evidencias.md#s064) | Dragons Cap 1 a 2 temporada 1.zip / 42 | 124 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S065](../pesquisa/fase-3/Fontes-e-Evidencias.md#s065) | Dragons Cap 1 a 2 temporada 1.zip / 43 | 21 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S066](../pesquisa/fase-3/Fontes-e-Evidencias.md#s066) | Dragons Cap 1 a 2 temporada 1.zip / 44 | 77 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S067](../pesquisa/fase-3/Fontes-e-Evidencias.md#s067) | Dragons Cap 1 a 2 temporada 1.zip / 45 | 29 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S068](../pesquisa/fase-3/Fontes-e-Evidencias.md#s068) | Dragons Cap 1 a 2 temporada 1.zip / 46 | 1121 | Sim/Sim | 5/5 | B001 dirigido, restante pendente |
| [S069](../pesquisa/fase-3/Fontes-e-Evidencias.md#s069) | Dragons Cap 1 a 2 temporada 1.zip / 47 | 11 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S070](../pesquisa/fase-3/Fontes-e-Evidencias.md#s070) | Dragons Cap 1 a 2 temporada 1.zip / 48 | 802 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S071](../pesquisa/fase-3/Fontes-e-Evidencias.md#s071) | Dragons Cap 1 a 2 temporada 1.zip / 49 | 1 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S072](../pesquisa/fase-3/Fontes-e-Evidencias.md#s072) | Dragons Cap 1 a 2 temporada 1.zip / 50 | 14 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S073](../pesquisa/fase-3/Fontes-e-Evidencias.md#s073) | Dragons Cap 1 a 2 temporada 2.zip / 2 | 1390 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S074](../pesquisa/fase-3/Fontes-e-Evidencias.md#s074) | Dragons Cap 1 a 2 temporada 2.zip / 3 | 277 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S075](../pesquisa/fase-3/Fontes-e-Evidencias.md#s075) | Dragons Cap 1 a 2 temporada 2.zip / 4 | 175 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S076](../pesquisa/fase-3/Fontes-e-Evidencias.md#s076) | Dragons Cap 1 a 2 temporada 2.zip / 5 | 792 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S077](../pesquisa/fase-3/Fontes-e-Evidencias.md#s077) | Dragons Cap 1 a 2 temporada 2.zip / 6 | 414 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S078](../pesquisa/fase-3/Fontes-e-Evidencias.md#s078) | Dragons Cap 1 a 2 temporada 2.zip / 7 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S079](../pesquisa/fase-3/Fontes-e-Evidencias.md#s079) | Dragons Cap 1 a 2 temporada 2.zip / 8 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S080](../pesquisa/fase-3/Fontes-e-Evidencias.md#s080) | Dragons Cap 1 a 2 temporada 2.zip / 9 | 111 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S081](../pesquisa/fase-3/Fontes-e-Evidencias.md#s081) | Dragons Cap 1 a 2 temporada 2.zip / 10 | 571 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S082](../pesquisa/fase-3/Fontes-e-Evidencias.md#s082) | Dragons Cap 1 a 2 temporada 2.zip / 11 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S083](../pesquisa/fase-3/Fontes-e-Evidencias.md#s083) | Dragons Cap 1 a 2 temporada 2.zip / 12 | 15 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S084](../pesquisa/fase-3/Fontes-e-Evidencias.md#s084) | Dragons Cap 1 a 2 temporada 2.zip / 13 | 464 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S085](../pesquisa/fase-3/Fontes-e-Evidencias.md#s085) | Dragons Cap 1 a 2 temporada 2.zip / 14 | 17 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S086](../pesquisa/fase-3/Fontes-e-Evidencias.md#s086) | Dragons Cap 1 a 2 temporada 2.zip / 15 | 4066 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S087](../pesquisa/fase-3/Fontes-e-Evidencias.md#s087) | Dragons Cap 1 a 2 temporada 2.zip / 16 | 774 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S088](../pesquisa/fase-3/Fontes-e-Evidencias.md#s088) | Dragons Cap 1 a 2 temporada 2.zip / 17 | 1454 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S089](../pesquisa/fase-3/Fontes-e-Evidencias.md#s089) | Dragons Cap 1 a 2 temporada 2.zip / 18 | 2217 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S090](../pesquisa/fase-3/Fontes-e-Evidencias.md#s090) | Dragons Cap 1 a 2 temporada 2.zip / 19 | 428 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S091](../pesquisa/fase-3/Fontes-e-Evidencias.md#s091) | Dragons Cap 1 a 2 temporada 2.zip / 20 | 36 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S092](../pesquisa/fase-3/Fontes-e-Evidencias.md#s092) | Dragons Cap 1 a 2 temporada 2.zip / 21 | 300 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S093](../pesquisa/fase-3/Fontes-e-Evidencias.md#s093) | Dragons Cap 1 a 2 temporada 2.zip / 22 | 49 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S094](../pesquisa/fase-3/Fontes-e-Evidencias.md#s094) | Dragons Cap 1 a 2 temporada 2.zip / 23 | 109 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S095](../pesquisa/fase-3/Fontes-e-Evidencias.md#s095) | Dragons Cap 1 a 2 temporada 2.zip / 24 | 348 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S096](../pesquisa/fase-3/Fontes-e-Evidencias.md#s096) | Dragons Cap 1 a 2 temporada 2.zip / 25 | 103 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S097](../pesquisa/fase-3/Fontes-e-Evidencias.md#s097) | Dragons Cap 1 a 2 temporada 2.zip / 26 | 50 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S098](../pesquisa/fase-3/Fontes-e-Evidencias.md#s098) | Dragons Cap 1 a 2 temporada 2.zip / 27 | 383 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S099](../pesquisa/fase-3/Fontes-e-Evidencias.md#s099) | Dragons Cap 1 a 2 temporada 2.zip / 28 | 84 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S100](../pesquisa/fase-3/Fontes-e-Evidencias.md#s100) | Dragons Cap 1 a 2 temporada 2.zip / 29 | 54 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S101](../pesquisa/fase-3/Fontes-e-Evidencias.md#s101) | Dragons Cap 1 a 2 temporada 2.zip / 30 | 42 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S102](../pesquisa/fase-3/Fontes-e-Evidencias.md#s102) | Dragons Cap 1 a 2 temporada 2.zip / 31 | 32 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S103](../pesquisa/fase-3/Fontes-e-Evidencias.md#s103) | Dragons Cap 1 a 2 temporada 2.zip / 32 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S104](../pesquisa/fase-3/Fontes-e-Evidencias.md#s104) | Dragons Cap 1 a 2 temporada 2.zip / 33 | 165 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S105](../pesquisa/fase-3/Fontes-e-Evidencias.md#s105) | Dragons Cap 1 a 2 temporada 2.zip / 34 | 10 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S106](../pesquisa/fase-3/Fontes-e-Evidencias.md#s106) | Dragons Cap 1 a 2 temporada 2.zip / 35 | 1848 | Sim/Sim | 52/52 | B001 dirigido, restante pendente |
| [S107](../pesquisa/fase-3/Fontes-e-Evidencias.md#s107) | Dragons Cap 1 a 2 temporada 2.zip / 36 | 3104 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S108](../pesquisa/fase-3/Fontes-e-Evidencias.md#s108) | Dragons Cap 1 a 2 temporada 2.zip / 37 | 230 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S109](../pesquisa/fase-3/Fontes-e-Evidencias.md#s109) | Dragons Cap 1 a 2 temporada 2.zip / 38 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S110](../pesquisa/fase-3/Fontes-e-Evidencias.md#s110) | Dragons Cap 1 a 2 temporada 2.zip / 39 | 118 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S111](../pesquisa/fase-3/Fontes-e-Evidencias.md#s111) | Dragons Cap 1 a 2 temporada 2.zip / 40 | 193 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S112](../pesquisa/fase-3/Fontes-e-Evidencias.md#s112) | Dragons Cap 1 a 2 temporada 2.zip / 41 | 1836 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S113](../pesquisa/fase-3/Fontes-e-Evidencias.md#s113) | Dragons Cap 1 a 2 temporada 2.zip / 42 | 88 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S114](../pesquisa/fase-3/Fontes-e-Evidencias.md#s114) | Dragons Cap 1 a 2 temporada 2.zip / 43 | 28 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S115](../pesquisa/fase-3/Fontes-e-Evidencias.md#s115) | Dragons Cap 1 a 2 temporada 2.zip / 44 | 1410 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S116](../pesquisa/fase-3/Fontes-e-Evidencias.md#s116) | Dragons Cap 1 a 2 temporada 2.zip / 45 | 1062 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S117](../pesquisa/fase-3/Fontes-e-Evidencias.md#s117) | Dragons Cap 1 a 2 temporada 2.zip / 46 | 193 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S118](../pesquisa/fase-3/Fontes-e-Evidencias.md#s118) | Dragons Cap 1 a 2 temporada 2.zip / 47 | 213 | Sim/Sim | 10/10 | B001 dirigido, restante pendente |
| [S119](../pesquisa/fase-3/Fontes-e-Evidencias.md#s119) | Dragons Cap 1 a 2 temporada 2.zip / 48 | 172 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S120](../pesquisa/fase-3/Fontes-e-Evidencias.md#s120) | Dragons Cap 1 a 2 temporada 2.zip / 49 | 78 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S121](../pesquisa/fase-3/Fontes-e-Evidencias.md#s121) | Dragons Cap 1 a 2 temporada 2.zip / 50 | 75 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S122](../pesquisa/fase-3/Fontes-e-Evidencias.md#s122) | Dragons Cap 1 a 2 temporada 2.zip / 51 | 935 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S123](../pesquisa/fase-3/Fontes-e-Evidencias.md#s123) | Dragons Cap 1 a 2 temporada 3.zip / 2 | 1494 | Sim/Sim | 20/20 | B001 dirigido, restante pendente |
| [S124](../pesquisa/fase-3/Fontes-e-Evidencias.md#s124) | Dragons Cap 1 a 2 temporada 3.zip / 3 | 3 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S125](../pesquisa/fase-3/Fontes-e-Evidencias.md#s125) | Dragons Cap 1 a 2 temporada 3.zip / 4 | 32 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S126](../pesquisa/fase-3/Fontes-e-Evidencias.md#s126) | Dragons Cap 1 a 2 temporada 3.zip / 5 | 1231 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S127](../pesquisa/fase-3/Fontes-e-Evidencias.md#s127) | Dragons Cap 1 a 2 temporada 3.zip / 6 | 616 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S128](../pesquisa/fase-3/Fontes-e-Evidencias.md#s128) | Dragons Cap 1 a 2 temporada 3.zip / 7 | 123 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S129](../pesquisa/fase-3/Fontes-e-Evidencias.md#s129) | Dragons Cap 1 a 2 temporada 3.zip / 8 | 10 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S130](../pesquisa/fase-3/Fontes-e-Evidencias.md#s130) | Dragons Cap 1 a 2 temporada 3.zip / 9 | 13 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S131](../pesquisa/fase-3/Fontes-e-Evidencias.md#s131) | Dragons Cap 1 a 2 temporada 3.zip / 10 | 13 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S132](../pesquisa/fase-3/Fontes-e-Evidencias.md#s132) | Dragons Cap 1 a 2 temporada 3.zip / 11 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S133](../pesquisa/fase-3/Fontes-e-Evidencias.md#s133) | Dragons Cap 1 a 2 temporada 3.zip / 12 | 154 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S134](../pesquisa/fase-3/Fontes-e-Evidencias.md#s134) | Dragons Cap 1 a 2 temporada 3.zip / 13 | 225 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S135](../pesquisa/fase-3/Fontes-e-Evidencias.md#s135) | Dragons Cap 1 a 2 temporada 3.zip / 14 | 214 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S136](../pesquisa/fase-3/Fontes-e-Evidencias.md#s136) | Dragons Cap 1 a 2 temporada 3.zip / 15 | 863 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S137](../pesquisa/fase-3/Fontes-e-Evidencias.md#s137) | Dragons Cap 1 a 2 temporada 3.zip / 16 | 155 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S138](../pesquisa/fase-3/Fontes-e-Evidencias.md#s138) | Dragons Cap 1 a 2 temporada 3.zip / 17 | 1295 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S139](../pesquisa/fase-3/Fontes-e-Evidencias.md#s139) | Dragons Cap 1 a 2 temporada 3.zip / 18 | 32 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S140](../pesquisa/fase-3/Fontes-e-Evidencias.md#s140) | Dragons Cap 1 a 2 temporada 3.zip / 19 | 44 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S141](../pesquisa/fase-3/Fontes-e-Evidencias.md#s141) | Dragons Cap 1 a 2 temporada 3.zip / 20 | 372 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S142](../pesquisa/fase-3/Fontes-e-Evidencias.md#s142) | Dragons Cap 1 a 2 temporada 3.zip / 21 | 64 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S143](../pesquisa/fase-3/Fontes-e-Evidencias.md#s143) | Dragons Cap 1 a 2 temporada 3.zip / 22 | 143 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S144](../pesquisa/fase-3/Fontes-e-Evidencias.md#s144) | Dragons Cap 1 a 2 temporada 3.zip / 23 | 22 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S145](../pesquisa/fase-3/Fontes-e-Evidencias.md#s145) | Dragons Cap 1 a 2 temporada 3.zip / 24 | 166 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S146](../pesquisa/fase-3/Fontes-e-Evidencias.md#s146) | Dragons Cap 1 a 2 temporada 3.zip / 25 | 71 | Sim/Sim | 15/15 | B001 dirigido, restante pendente |
| [S147](../pesquisa/fase-3/Fontes-e-Evidencias.md#s147) | Dragons Cap 1 a 2 temporada 3.zip / 26 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S148](../pesquisa/fase-3/Fontes-e-Evidencias.md#s148) | Dragons Cap 1 a 2 temporada 3.zip / 27 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S149](../pesquisa/fase-3/Fontes-e-Evidencias.md#s149) | Dragons Cap 1 a 2 temporada 3.zip / 28 | 39 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S150](../pesquisa/fase-3/Fontes-e-Evidencias.md#s150) | Dragons Cap 1 a 2 temporada 3.zip / 29 | 82 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S151](../pesquisa/fase-3/Fontes-e-Evidencias.md#s151) | Dragons Cap 1 a 2 temporada 3.zip / 30 | 691 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S152](../pesquisa/fase-3/Fontes-e-Evidencias.md#s152) | Dragons Cap 1 a 2 temporada 3.zip / 31 | 649 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S153](../pesquisa/fase-3/Fontes-e-Evidencias.md#s153) | Dragons Cap 1 a 2 temporada 3.zip / 32 | 677 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S154](../pesquisa/fase-3/Fontes-e-Evidencias.md#s154) | Dragons Cap 1 a 2 temporada 3.zip / 33 | 326 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S155](../pesquisa/fase-3/Fontes-e-Evidencias.md#s155) | Dragons Cap 1 a 2 temporada 3.zip / 34 | 739 | Sim/Sim | 15/15 | B001 dirigido, restante pendente |
| [S156](../pesquisa/fase-3/Fontes-e-Evidencias.md#s156) | Dragons Cap 1 a 2 temporada 3.zip / 35 | 373 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S157](../pesquisa/fase-3/Fontes-e-Evidencias.md#s157) | Dragons Cap 1 a 2 temporada 3.zip / 36 | 57 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | Dragons Cap 1 a 2 temporada 3.zip / 37 | 2116 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S159](../pesquisa/fase-3/Fontes-e-Evidencias.md#s159) | Dragons Cap 1 a 2 temporada 3.zip / 38 | 440 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S160](../pesquisa/fase-3/Fontes-e-Evidencias.md#s160) | Dragons Cap 1 a 2 temporada 3.zip / 39 | 406 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S161](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161) | Dragons Cap 1 a 2 temporada 3.zip / 40 | 1716 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S162](../pesquisa/fase-3/Fontes-e-Evidencias.md#s162) | Dragons Cap 1 a 2 temporada 3.zip / 41 | 121 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S163](../pesquisa/fase-3/Fontes-e-Evidencias.md#s163) | Dragons Cap 1 a 2 temporada 3.zip / 42 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S164](../pesquisa/fase-3/Fontes-e-Evidencias.md#s164) | Dragons Cap 1 a 2 temporada 3.zip / 43 | 38 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S165](../pesquisa/fase-3/Fontes-e-Evidencias.md#s165) | Dragons Cap 1 a 2 temporada 3.zip / 44 | 199 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S166](../pesquisa/fase-3/Fontes-e-Evidencias.md#s166) | Dragons Cap 1 a 2 temporada 3.zip / 45 | 2700 | Sim/Sim | 10/10 | B001 dirigido, restante pendente |
| [S167](../pesquisa/fase-3/Fontes-e-Evidencias.md#s167) | Dragons Cap 1 a 2 temporada 3.zip / 46 | 354 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S168](../pesquisa/fase-3/Fontes-e-Evidencias.md#s168) | Dragons Cap 1 a 2 temporada 3.zip / 47 | 21 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S169](../pesquisa/fase-3/Fontes-e-Evidencias.md#s169) | Dragons Cap 1 a 2 temporada 3.zip / 48 | 22 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S170](../pesquisa/fase-3/Fontes-e-Evidencias.md#s170) | Dragons Cap 1 a 2 temporada 3.zip / 49 | 680 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S171](../pesquisa/fase-3/Fontes-e-Evidencias.md#s171) | Dragons Cap 1 a 2 temporada 3.zip / 50 | 203 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S172](../pesquisa/fase-3/Fontes-e-Evidencias.md#s172) | Dragons Cap 3 a 4 temporada 1.zip / 2 | 2245 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S173](../pesquisa/fase-3/Fontes-e-Evidencias.md#s173) | Dragons Cap 3 a 4 temporada 1.zip / 3 | 2446 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S174](../pesquisa/fase-3/Fontes-e-Evidencias.md#s174) | Dragons Cap 3 a 4 temporada 1.zip / 4 | 13 | Sim/Sim | 13/13 | B001 integral |
| [S175](../pesquisa/fase-3/Fontes-e-Evidencias.md#s175) | Dragons Cap 3 a 4 temporada 1.zip / 5 | 470 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S176](../pesquisa/fase-3/Fontes-e-Evidencias.md#s176) | Dragons Cap 3 a 4 temporada 1.zip / 6 | 616 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S177](../pesquisa/fase-3/Fontes-e-Evidencias.md#s177) | Dragons Cap 3 a 4 temporada 1.zip / 7 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S178](../pesquisa/fase-3/Fontes-e-Evidencias.md#s178) | Dragons Cap 3 a 4 temporada 1.zip / 8 | 1422 | Sim/Sim | 37/37 | B001 dirigido, restante pendente |
| [S179](../pesquisa/fase-3/Fontes-e-Evidencias.md#s179) | Dragons Cap 3 a 4 temporada 1.zip / 9 | 2433 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S180](../pesquisa/fase-3/Fontes-e-Evidencias.md#s180) | Dragons Cap 3 a 4 temporada 1.zip / 10 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S181](../pesquisa/fase-3/Fontes-e-Evidencias.md#s181) | Dragons Cap 3 a 4 temporada 1.zip / 11 | 1 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S182](../pesquisa/fase-3/Fontes-e-Evidencias.md#s182) | Dragons Cap 3 a 4 temporada 1.zip / 12 | 394 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S183](../pesquisa/fase-3/Fontes-e-Evidencias.md#s183) | Dragons Cap 3 a 4 temporada 1.zip / 13 | 181 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S184](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184) | Dragons Cap 3 a 4 temporada 1.zip / 14 | 578 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S185](../pesquisa/fase-3/Fontes-e-Evidencias.md#s185) | Dragons Cap 3 a 4 temporada 1.zip / 15 | 1811 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S186](../pesquisa/fase-3/Fontes-e-Evidencias.md#s186) | Dragons Cap 3 a 4 temporada 1.zip / 16 | 42 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | Dragons Cap 3 a 4 temporada 1.zip / 17 | 2962 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S188](../pesquisa/fase-3/Fontes-e-Evidencias.md#s188) | Dragons Cap 3 a 4 temporada 1.zip / 18 | 25 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S189](../pesquisa/fase-3/Fontes-e-Evidencias.md#s189) | Dragons Cap 3 a 4 temporada 1.zip / 19 | 689 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S190](../pesquisa/fase-3/Fontes-e-Evidencias.md#s190) | Dragons Cap 3 a 4 temporada 1.zip / 20 | 0 | Sim/Sim | 0/0 | Vazio conferido |
| [S191](../pesquisa/fase-3/Fontes-e-Evidencias.md#s191) | jogadores.zip / 2 | 1 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S192](../pesquisa/fase-3/Fontes-e-Evidencias.md#s192) | jogadores.zip / 3 | 19 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S193](../pesquisa/fase-3/Fontes-e-Evidencias.md#s193) | jogadores.zip / 4 | 3 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S194](../pesquisa/fase-3/Fontes-e-Evidencias.md#s194) | jogadores.zip / 5 | 27 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S195](../pesquisa/fase-3/Fontes-e-Evidencias.md#s195) | jogadores.zip / 6 | 1 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S196](../pesquisa/fase-3/Fontes-e-Evidencias.md#s196) | jogadores.zip / 7 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S197](../pesquisa/fase-3/Fontes-e-Evidencias.md#s197) | jogadores.zip / 8 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) | jogadores.zip / 9 | 17 | Sim/Sim | 17/17 | B001 integral |
| [S199](../pesquisa/fase-3/Fontes-e-Evidencias.md#s199) | jogadores.zip / 10 | 40 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S200](../pesquisa/fase-3/Fontes-e-Evidencias.md#s200) | jogadores.zip / 11 | 5 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S201](../pesquisa/fase-3/Fontes-e-Evidencias.md#s201) | jogadores.zip / 12 | 6 | Sim/Sim | 0/0 | Triagem nova pendente |
| [S202](../pesquisa/fase-3/Fontes-e-Evidencias.md#s202) | jogadores.zip / 13 | 29 | Sim/Sim | 0/0 | Triagem nova pendente |
| [PWR001](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr001) | Poderes Jogadores.zip / 3 | 13 | Sim/Sim | 13/13 | B001 integral |
| [PWR002](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr002) | Poderes Jogadores.zip / 5 | 3 | Sim/Sim | 3/3 | B001 integral |
| [PWR003](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr003) | Poderes Jogadores.zip / 7 | 5 | Sim/Sim | 5/5 | B001 integral |
| [PWR004](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr004) | Poderes Jogadores.zip / 9 | 1 | Sim/Sim | 1/1 | B001 integral |
| [PWR005](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr005) | Poderes Jogadores.zip / 11 | 1 | Sim/Sim | 1/1 | B001 integral |
| [PWR006](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr006) | Poderes Jogadores.zip / 13 | 2 | Sim/Sim | 2/2 | B001 integral |
| [PWR007](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr007) | Poderes Jogadores.zip / 15 | 1 | Sim/Sim | 1/1 | B001 integral |
| [PWR008](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr008) | Poderes Jogadores.zip / 17 | 4 | Sim/Sim | 4/4 | B001 integral |
| [PWR009](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr009) | Poderes Jogadores.zip / 19 | 111 | Sim/Sim | 111/111 | B001 integral |
| [PWR010](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr010) | Poderes Jogadores.zip / 21 | 3 | Sim/Sim | 3/3 | B001 integral |
| [PWR011](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr011) | Poderes Jogadores.zip / 23 | 13 | Sim/Sim | 13/13 | B001 integral |
| [PWR012](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr012) | Poderes Jogadores.zip / 25 | 1 | Sim/Sim | 1/1 | B001 integral |

## Checkpoint, prontidão e continuação necessária

**Concluído:** inventário dos oito ZIPs, processamento independente, correspondência das 214 fontes, reconciliação quantitativa dos snapshots, localização das evidências citadas e primeiro lote contextual. Não há bloqueio de acesso aos oito ZIPs.

**Ainda necessário:** varredura narrativa sistemática por intervalos verificáveis; nova análise factual completa dos doze; revisão semântica dos 40 PS/39 CRIT/19 ARC; poderes posteriores fora de PWR; NPCs/governos/geografia; pontes históricas completas; auditoria de todas as aprovações autorais e parecer final de prontidão. Os testes estruturais acima não marcam essas tarefas como concluídas.

O [documento 25](25-Omissoes-Descobertas-e-Correcoes-Checkpoint.md) registra o que foi confirmado, incompleto e corrigido no lote. Documentos C–E serão acrescentados ou conciliados com equivalentes após investigação; não recebem tabelas com respostas inventadas nesta entrega.

**Parecer provisório: NÃO APTO para declarar encerrada esta auditoria final e liberar a construção histórica global.** O impedimento é cobertura semântica independente ainda insuficiente para o compromisso desta auditoria; não foi encontrada falha material de integridade dos ZIPs nem prova de que toda a pesquisa anterior seja inválida. A classificação final de prontidão será revista ao concluir B–D. Não há decisão criativa imediata exigida para continuar a investigação de fontes.

Próximo lote: morte/retorno de Henry; Harry–Astro; adulto–bebê de Kian; término completo da dungeon; Ymir/Beatriz e Hermione/selo; depois Nairóbi/favor e últimos estados restantes. Cada lote deve registrar índices/IDs e intervalo realmente lido, tipos/contexto, tratamento nos cinco casos, omissão por gravidade e atualização proporcional. Reunir achados dirigidos não substitui a varredura do restante. Nenhuma guerra, destino, nova divindade ou era foi escolhida.

## Validação editorial do checkpoint

O [relatório de validação](auditoria-fontes/validacao-checkpoint.json) registra 2.128 links relativos/âncoras, 976 referências fonte–ID na versão corrigida, 437 hashes do ledger e 34 blobs anteriores protegidos, incluindo todos os oito ZIPs e o registro de decisões. Sem erros nesses controles. A contagem de referências da base anterior (967) permanece distinta da versão corrigida. Os testes não certificam a revisão semântica integral.

## Continuação B002.1 — checkpoint publicado, lote em andamento

C acumulada: **4.542 IDs distintas**, das quais 4.105 novas neste checkpoint; 17 revisitas de B001 sem dupla contagem. Principal 4.384/89.155; poderes 158/158; cobertura combinada 5.085486%. D acumulada 3.973 (4.448401%), conservadora e separada. A/B permanecem concluídas; C/D parciais.

[Relatório B002.1, intervalos e matrizes](26-Auditoria-B002-Continuidades-e-Varredura.md); [ledger](auditoria-fontes/triagem-B002.json); [cobertura por todas as fontes](auditoria-fontes/cobertura-acumulada.json); [plano sistemático](auditoria-fontes/plano-varredura.json). Números/tabela B001 acima permanecem históricos, não representam a cobertura atual.

Cinco ocorrências OM-003–007: premissa de selo corrigida, experiência materna/divina recuperada, Philip/pesquisa racial incluídos, mercado Submundo delimitado e condição/afeto de Hermione qualificados. Dez PS, onze CRIT anteriores e sete ARC parcialmente investigados; CRIT-040 adicional. Sete protagonistas parcialmente revisados, cinco não iniciados no exame factual amplo; nenhum concluído.


B002 continua aberto pelos intervalos explicitamente pendentes. B003 está planejado, não executado. Prontidão global provisória NÃO APTO por cobertura insuficiente; decisões criativas protegidas. [Validação deste checkpoint](auditoria-fontes/validacao-B002.json).
