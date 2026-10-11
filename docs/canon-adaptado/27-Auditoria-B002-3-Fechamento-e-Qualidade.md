# B002.3 — fechamento crítico, controle de qualidade e preparação de B003

**11/10/2026 · B002 CONCLUÍDO NO ESCOPO CRÍTICO ABAIXO. Auditoria global EM ANDAMENTO. B003 somente planejado.**

## Base e preservação

Partida na `main` `78b4972edbda7341f8f93bb6be6174d483054054`, merge do [PR #17](https://github.com/DivineJeff/Lore-Dragons/pull/17); árvore `7d4ad6ebe25c615243214df3eb2634cd80288522`. Base conferida: corpus combinado 89.313, C=D=10.431, C sem D=0, principal sem C=78.882; 22 fontes completas, 14 parciais, 162 não vazias sem C, 16 vazias. Matrizes: 40 PS, 40 CRIT, 19 ARC, 12 protagonistas, nenhum com revisão global completa. Registros anteriores preservados.

## Cobertura efetivamente executada

| Métrica | B002.3 |
| --- | --- |
| IDs novas C | 9131 |
| IDs anteriores revisitadas | 197 |
| IDs novas D | 9131 |
| IDs distintas examinadas nesta rodada | 9328 |
| C acumulada / D acumulada | 19562 / 19562 |
| C sem D | 0 |
| Principal com C | 19404 / 89.155 |
| Principal ainda sem C | 69751 |
| Poderes com C/D | 158 / 158 |
| Combinado com C/D | 21.902747% |

A/B continuam inventário/processamento completos; C/D não são contagem de fatos. IDs deduplicadas por união; acessos sobrepostos/releituras não inflaram números. 9333 acessos nos intervalos registrados mais 92 acessos internos para conferir a atribuição da prisão; estes 92 não geram progresso. Buscas lexicais orientadoras não foram contadas. Nenhuma leitura truncada permanece certificada.

Cada intervalo traz IDs extremos, hash do HTML/texto, relação com documentos e disposição no [ledger aditivo](auditoria-fontes/triagem-B002.3.json). `coverage_C/D` de intervalo inclui sobreposições; métricas globais derivam de rows únicas. Núcleos sistemáticos e fronteiras conservados no [plano](auditoria-fontes/plano-varredura.json).

| Intervalo | Fonte | Índices inclusivos | Frente | Confronto |
| --- | --- | --- | --- | --- |
| K01 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 0–549 | dirigida | CONT-014/015, Henry/Ymir, ARC-010 |
| K02 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 550–1149 | dirigida | CONT-015, Henry/Ymir, PS-037 |
| K03 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 1150–1699 | dirigida | CONT-015, PS-036/037, Henry/Bytes/Lilith |
| K04 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 1941–2404 | dirigida | CONT-016, PS-021/023/034/036, CRIT-003/006/025 |
| K05 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 2466–2649 | dirigida | CONT-016, PS-021/023, CRIT-003/006 |
| K06 | [S184](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184) | 0–289 | dirigida | Kian, ARC-015, PS-021, CRIT-030 |
| K07 | [S184](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184) | 290–577 | dirigida | Kian, ARC-015, PS-021, CRIT-030 |
| K08 | [S051](../pesquisa/fase-3/Fontes-e-Evidencias.md#s051) | 0–8 | dirigida | Kian, PS-001/021 |
| K09 | [S052](../pesquisa/fase-3/Fontes-e-Evidencias.md#s052) | 0–233 | dirigida | Kian/Lúcifer, PS-021, CRIT-006 |
| K10 | [S070](../pesquisa/fase-3/Fontes-e-Evidencias.md#s070) | 0–269 | dirigida | PERÍODO-01, Kian/Harry/Henry, ARC-001 |
| K11 | [S070](../pesquisa/fase-3/Fontes-e-Evidencias.md#s070) | 270–549 | dirigida | PERÍODO-01, PS-001/002/037, ARC-001 |
| K12 | [S070](../pesquisa/fase-3/Fontes-e-Evidencias.md#s070) | 550–801 | dirigida | PERÍODO-01, PS-001, CRIT-038 |
| K13 | [S161](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161) | 0–499 | dirigida | CONT-008, ARC-010, Henry/Michael/Bytes/God |
| K14 | [S161](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161) | 500–999 | dirigida | CONT-008, ARC-010, Michael/Lilith/God/Kian |
| K15 | [S161](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161) | 1000–1499 | dirigida | CONT-008, PS-035, CRIT-016, Harry/ARC-017 |
| K16 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 0–429 | dirigida | CONT-004/005, OM-002/005, PS-020, Mulack/Nyxis |
| K17 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 430–859 | dirigida | CONT-005, Mulack, ARC-006, CRIT-004/039 |
| K18 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 860–1279 | dirigida | CONT-005, Mulack, PS-020, ARC-006 |
| K19 | [S004](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004) | 0–57 | sistemática | apoio/Stark, PS-001 |
| K20 | [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | 0–199 | sistemática | CONT-014, Ymir, PS-004/026 |
| K21 | [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | 200–399 | sistemática | CONT-014, Nefa/Altruístas, PS-026 |
| K22 | [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | 400–599 | sistemática | CONT-014, Ymir/Note, PS-018/026 |
| K23 | [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | 600–799 | sistemática | CONT-014/018, Ymir/Bia/Nefa, PS-018/024/026 |
| K24 | [S005](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005) | 800–990 | sistemática | CONT-018, Ymir/Nefa/Balenon/Coleros, ARC-007 |
| K25 | [S010](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010) | 0–219 | sistemática | apoio/Richard/Maya, PS-001 |
| K26 | [S010](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010) | 220–439 | sistemática | apoio/Richard/Maya/Cot |
| K27 | [S010](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010) | 440–634 | sistemática | apoio/Richard/orbe, PS-001 |
| K28 | [S040](../pesquisa/fase-3/Fontes-e-Evidencias.md#s040) | 0–12 | dirigida Harry | Harry, PS-017/022, ARC-017 |
| K29 | [S090](../pesquisa/fase-3/Fontes-e-Evidencias.md#s090) | 0–150 | dirigida Harry | Harry, ARC-017, PS-022, CONT-001 |
| K30 | [S090](../pesquisa/fase-3/Fontes-e-Evidencias.md#s090) | 151–279 | dirigida Harry | Harry, ARC-017, CONT-001 |
| K31 | [S090](../pesquisa/fase-3/Fontes-e-Evidencias.md#s090) | 280–427 | dirigida Harry | Harry, ARC-017, CONT-001 |
| K32 | [S138](../pesquisa/fase-3/Fontes-e-Evidencias.md#s138) | 1090–1294 | dirigida Harry | Harry/Zex/Stifen, CONT-004, ARC-017 |
| K33 | [S118](../pesquisa/fase-3/Fontes-e-Evidencias.md#s118) | 78–100 | dirigida Mulack | CRIT-039, PS-020, ARC-006 |
| K34 | [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | 81–89 | controle de qualidade | CONT-019, Michael |
| K35 | [S182](../pesquisa/fase-3/Fontes-e-Evidencias.md#s182) | 111–119 | controle de qualidade | CONT-006, God/Kian |
| K36 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 520–528 | controle de qualidade | CONT-018, Ymir |
| K37 | [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | 303–311 | controle de qualidade | Harry/Astro, ARC-017 |
| K38 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 416–424 | controle de qualidade | Rans/Hermione, PS-038 |
| K39 | [S174](../pesquisa/fase-3/Fontes-e-Evidencias.md#s174) | 5–12 | controle de qualidade | Bytes, CRIT-020, PS-031 |
| K40 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 1377–1385 | controle de qualidade | Mulack, CONT-005 |
| K41 | [S037](../pesquisa/fase-3/Fontes-e-Evidencias.md#s037) | 297–305 | controle de qualidade | HAB-009, Henry, Rans |
| K42 | [S178](../pesquisa/fase-3/Fontes-e-Evidencias.md#s178) | 456–464 | controle de qualidade | CONT-010, HAB-014, Henry |
| K43 | [S155](../pesquisa/fase-3/Fontes-e-Evidencias.md#s155) | 475–483 | controle de qualidade | HAB-004, Michael |
| K44 | [S028](../pesquisa/fase-3/Fontes-e-Evidencias.md#s028) | 61–69 | controle de qualidade | HAB-002, Michael/Rans |
| K45 | [S123](../pesquisa/fase-3/Fontes-e-Evidencias.md#s123) | 221–229 | controle de qualidade | HAB-004, CONT-003, Michael |
| K46 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 2241–2249 | controle de qualidade | Kian, CONT-017 |
| K47 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 2371–2379 | controle de qualidade | Kian, CONT-017 |
| K48 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 738–746 | controle de qualidade | Beatriz, CONT-020, OM-014 |
| K49 | [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | 207–215 | controle de qualidade | Astro, CONT-020 |
| K50 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 758–766 | controle de qualidade | Myria, CONT-018 |
| K51 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 547–555 | controle de qualidade | Ymir, OM-013, CRIT-027 |
| K52 | [PWR001](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr001) | 0–4 | controle de qualidade | HAB-001, Michael |
| K53 | [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) | 0–4 | controle de qualidade | Mulack, OM-002, CRIT-004 |
| K54 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 1845–1853 | controle de qualidade | Kian, OM-011, CRIT-006 |
| K55 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 2301–2313 | controle de qualidade | Kian, OM-011, CONT-017 |
| K56 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 835–843 | controle de qualidade | Ymir, OM-010, CRIT-027 |
| K57 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 871–880 | controle de qualidade | Ymir/Beatriz, OM-014 |
| K58 | [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) | 0–4 | controle de qualidade | Mulack, S198 |
| K59 | [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) | 12–16 | controle de qualidade | S198, PS-032 |
| K60 | [S155](../pesquisa/fase-3/Fontes-e-Evidencias.md#s155) | 468–474 | expansão QA | HAB-004, Q10 |

## Disposições do confronto D

**K01 — S187:** Olta, combates e intervenção coletiva documentados. Decapitação parcial não equivale a morte; Henry mata homens apesar de intenção de nocaute. Fala/proposta e resultado separados; não atribuir toda devastação a um golpe de Henry.

**K02 — S187:** Projetos MaK, escavador e míssil são pesquisa/propostas, não obras concluídas. Desaparecimento dimensional no combate e negativa de habilidade nova permanecem situados. Tarkaros explode; Topher protege. Não atribuir a Henry vitória exclusiva nem unificar jovem do pântano a Tarkaros.

**K03 — S187:** Frank promete recursos, não pagamento recuperado. Alerta de veneno e cancelamento do festival não provam mortes em massa. Razões de tempo Inferno/Arca são locais. Gwierlan construiu escola; Lilith salva da bomba. Henry desmaia por exaustão e acorda, sem morte. Espada de Tarkaros e aula Dark de Bytes já documentadas; não conferem maestria universal.

**K04 — S187:** Henry e Michael matam cultista; controle de força é problema assumido. Torre/arma continuam projeto. Edward define Disare/calamidade como NPC, não cosmologia objetiva. Alegação sobre Gwierlan não prova morte. Último portão aberto e posterior todos abertos conflitam, sem retificação conclusiva. Nenhuma ponte adulto–bebê recuperada.

**K05 — S187:** Combate com Edward e soterramento da entrada do terceiro salão não provam morte da entidade. Henry/Ymir acordam antes da sequência fatal posterior já revisada; não contar ressurreição extra. Debate OOC sobre escolhas não acrescenta acontecimentos nem explica transição de Kian.

**K06 — S184:** Terras roxas, espada, ave e sombra têm resultados específicos. Mestre distingue servidão da sombra de união. Corpo/mão restaurados e sonho são narrados; espada permanece depois de acordar, logo não anular tudo como sonho. Ellen diz achou acordado, perspectiva distinta do desmaio anterior. Elemento não definido, limites de magia preservados.

**K07 — S184:** Sombra emerge, custa força; retirada de sombras de seres vivos falha. Galinha morta submete-se, transporte se realiza ao grito de Henry e conecta S187 adulto. Mestre chama Ymir em cena de Kian; lapso nominal não entrada de Ymir confirmada. Propostas de garras/monstro permanente recusadas. OM-017 complementa capacidades sem divinização.

**K08 — S051:** Despertar aéreo e retomada na água preservados sem mecanismo único. Chamada e spam não são canon. Não inferir infância ou morte pela descontinuidade.

**K09 — S052:** Troca anterior ao ramo de minhocas; nome Lúcifer e conhecimento limitado na biblioteca. Exaustão/desejo de proteção não são poderes adquiridos por reflexão. Wilbur guarda pessoal não apaga retificação do Wilbur coletivo. Informação monetária local não sistema universal.

**K10 — S070:** Água, culto/bandana Deus Dragão, explosão, captura e ferimentos. Harry cuida dos feridos; Kian sofre raspão. Avião parecido com WWI não viagem temporal. Assassino traumatizado anônimo não identificado como Kian por comentário. Desmaios não mortes dos protagonistas.

**K11 — S070:** Carroceiro pago/incriminado, escravização/marca/dívida e prazo anunciado, não vivido. Amputação não remove marca, que migra. Cura do guarda não apaga socorro de Harry. Chamada para troca de Kian sem resolução não manifestação completa de Lúcifer.

**K12 — S070:** Marca, Ária/Draconia e barreira mineira registrados; falas religiosas são situadas. Raiva de Henry não transforma automaticamente. Cena rio/boca 794–795 anulada como chat errado em 797: excluída deste local. Pings finais não avançam cena.

**K13 — S161:** Treino de Henry com limites e recuperação parcial, não atributos sem teto. Diplomacia Olta/Mouran; Hermest Brown rank S; Gotter representa Baran temporariamente, não identidade única. Michael propõe união; autodeclaração de sucesso não implantação política universal.

**K14 — S161:** Conselho aprovado como ideia; distribuição/rotações ainda propostas. Kian segue Gotter/God para treino. Voz Patrick é humor Bob Esponja, não retorno do morto. Torre de 100 milhões ainda avaliação. Árvore vulnerável na transferência, elfos auxiliam domínio sem fornecer custo energético; mapa representativo não cartografia confirmada.

**K15 — S161:** Colar de Michael falha neste uso. Hermest decapita rei verdadeiro de Olta; acusação de falso rei é rejeitada. Cerimônia de Michael é feinte, não coroação Hermest consumada. Harry salva Michael, asas/abdômen feridos, cura de queimaduras falha. Michael decapita Hermest Rozz; Brown/Rozz lapso preservado, Dimitri não fundido. Pizza é incorporada pelo mestre, não descarte automático de toda brincadeira.

**K16 — S158:** Domo não contém explosão; área planificada, não toda Mouran. Nyxis é nome retificado; busca Trevor não prova morte dele. Mulack ajuda mercador, chega a Olta e se hospeda. Fundação/anexação de Olta são falas de funcionário, não história universal conciliada. Antecedentes complementam vínculo, sem resolver dungeon.

**K17 — S158:** Cristal explode e rank S é atribuído, não poder infinito. Elemento não repele mana segundo mestre. Hermest Brown e Dimitri Rozz são distintos. Driade Fistine é nome próprio, não raça; negociação de servidão é reformulada, sem selo mágico demonstrado. Flor de Neve recebe nome em homenagem ao frio de Mouran; armadura produzida por partes.

**K18 — S158:** Grupo selecionado A+B soma dez acompanhantes, mais Mulack; Yakkatsu só OOC, não integrante. Recompensa por contribuição, não todo efetivo da guilda. Jin Mu-Won/memória perfeita é referência/alegação do jogador, não concessão. Circulação quebra, limite de 13 mil e percepção de meio km não ilimitados. Espécie de Nyxis desconhecida; livros/PV não inventados. Nenhuma adjudicação do último combate.

**K19 — S004:** Leonard usa Stark; menina Emma não automaticamente filha de Lilith. Joias recolhíveis, baú não levantado; carona oferecida, não jornada concluída. Note comenta fora de personagem, sem Ymir presente.

**K20 — S005:** Captura por moradores da aldeia em árvores, gaiola/barreira; atribuição à Árvore Rainha na Bíblia não sustentada. Equipamentos retirados, tanga retifica nudez. Treino interrompido em cinco minutos não cria magia. Canibais matam mulher; Ymir mata/perfura adversários, cuja sobrevivência depois alegada exige cautela. OM-015 corrige agente da prisão.

**K21 — S005:** Nefa acolhe e trata Ymir; fotografias são desenhos, privacidade negada. Trai-o para proteger aldeia segundo sua fala, depois também capturada. Altruístas dizem sobreviver a corações perfurados: divergência não imunidade universal. Inferno é hipótese de Ymir rejeitada por Nefa.

**K22 — S005:** Moon citada, não unificada a Bluemoon. Recuperação de equipamento, máscara/nome e proteção de Nefa; posse aparente é interpretação dos canibais sobre alimento, não romance aprovado. Ymir explode é zueira cancelada. Mestre corrige método de absorção; não amplificar reservatório sem resultado.

**K23 — S005:** Exaustão e auxílio de Nefa; Ymir retorna ao lago diante da Árvore, que desconhece Nefa/Altruístas e suspeita efeito da mana. Hipótese não anula toda aventura. Bia coma, mãos marcadas B não morte identificada. Henry apaga bombas locais. Bluemoon/Balenon aparecem em retomada documental, sem calendário global unificado.

**K24 — S005:** Balenon questiona luta interminável; alegria da criança não cura mágica. Treino sete dias/noites, pausas/conversas ambíguas; espada Dokato prometida, não concluída. Nefa recusa condução passiva. Coleros lidera doze; metade morre, não todos. Ymir luta com dois tigres e cai exausto; pergunta final sobre Nefa fica sem resposta. OM-016 recupera motivações e custos.

**K25 — S010:** Richard desperta na água sem memórias, faz ferramentas/treina com fadiga; nudez retificada para roupas. Maya avisa perigo e recusa abrigo. Humor com vaca não morte narrada nem autoria divina literal da metáfora universo.

**K26 — S010:** Cão Cot/Cop curado por Maya e lobo negro de quatro olhos não identidade comprovada. Casa e memória de construção não memória autobiográfica restaurada. Lobo destrói casa e fere mão; Maya morreu é especulação OOC, não morte canônica.

**K27 — S010:** Carne da mão arrancada, lobo morto por mestre; mudança de personalidade e amnésia da luta propostas pelo jogador, sem diagnóstico. Orbe vermelha exala gás, entra no corpo e causa sono; força/fadiga melhoradas depois, mecanismo incompleto. Chakram é projeto, martelo feito, não arma concluída. Internação de Rans é conversa pessoal OOC. Último grunhido sem resultado.

**K28 — S040:** Despertar Harry10km/água sem mecanismo; comentário chat errado e spam não criam morte ou troca. Fonte inteira não prova identidade Astro.

**K29 — S090:** Harry hospital, gosma escura relatada, pacto com criatura negra reconhecida; gratidão por libertação, voto finalizado e despertar. Médico afirma estava morto: declaração NPC sem certificação omnisciente de ressurreição. Mestre chama Henry na percepção mental em cena Harry; lapso contextual explicitado, não novo poder Henry. Dez mensagens excluídas notificadas, conteúdo não recuperado.

**K30 — S090:** Zaraph convida/financia roupa e conduz encontro; Dom Ray Harry é apresentação social. Jakaw Fierra rede de informação e coroa controladora por relato. Sem ponte corporal ou entrada em hospedeira; aparência alusiva não identidade do pesadelo confirmada.

**K31 — S090:** Pingente, cálice e percepção de mentes repetida em contexto Harry. Sem identificar Jakaw como criatura anterior. Zaraph nomeia general e extrai recursos; previsão ruínaMouran24h não catástrofe universal realizada. Saída subterrânea/superfície narrada. Associação Harry–Astro permanece provável.

**K32 — S138:** Retorno a Mouran com Zex ativo, ruas com médicos; cancelamento de impressão inicial preservado. Henry passa com autorização, não tudo ilusão. Harry rompe parceria de robôs, microchip Zex retirado; retira pingente, sai voando, cidade ao longe sem entrada. Não consertar Zex retrospectivamente nem transferir memória dele a Harry/Astro. Bloco anterior0–1089 continua pendente.

**K33 — S118:** Mestre retifica primeira alegação de morte: braço quebrado. Fonte de janeiro distinta do final da dungeon; comentário/memorial não resolve armadura intacta contra declaração posterior. Bíblia e proposta21 já preservam diferença; nenhuma correção factual nova.

## Kian / Lúcifer / Azazel

**FATO DOCUMENTADO:** despertar e troca nominal em dezembro; S052 nome Lúcifer e estudo limitado; S182 já completo alterna Kian/Lúcifer na mesma sequência. S184 registra sombra própria servil, espada que persiste após despertar, cura corporal situada e transporte por galinha de sombra para encontrar Henry. S187 adulto prossegue com Henry/Michael/Lilith; capacidades/força/fadiga preservadas, sem morte adulta narrada inequívoca por flecha de fogo.

**DECLARAÇÃO AUTORAL:** EXT-003 confirma continuidade pessoal dos três nomes. **RECONSTRUÇÃO PROVÁVEL:** recordações/corpos/capacidades guardam relação, sem exigir memória integral. **MECANISMO NÃO RECUPERADO NO ESCOPO:** passagem adulto–bebê. S013 infância, doze anos pessoais, mente ainda Kian com limites, ilusão de Westia e cabana com velha dormindo continuam corretos. S184 sonho e espada persistente não permitem anular toda sequência nem instituir divindade. Lapso Ymir na resposta sobre sombra é conservado como lapso contextual. Corpo servil/absorvido não automaticamente fusão total. OM-017 complementa limites.

Revisão crítica inicial suficiente em S013/S182/S187/S184/S051/S052/S070; não biografia global concluída. S032 e outros percursos ainda podem esclarecer natureza e intermediários, previstos na varredura.

## Harry / Astro

| Condição | Conclusão e limite |
| --- | --- |
| Nominal | Harry nomeado em S040/S070/S090/S138/S161; Astro apresenta-se em S008. Nomes não encerram a identidade. |
| Pessoal | Associação Harry–Astro PROVÁVEL, sustentada pelo comentário OOC de S008 já auditado; sem confirmação mecânica. |
| Corporal | Harry tem penas/asas, ferimentos e cura limitada. Entrada na hospedeira não recuperada; mulher sai viva, homem ocupado ainda moribundo. |
| Memória | Reconhecimento da criatura negra é narrado em S090. Não prova transferência íntegra para Astro; versões de lembrança de S008 permanecem. Memória do chip pertence a Zex, não automaticamente a Harry. |
| Manifestações/transições | Experiência/pacto, despertar no hospital, saída física com Zaraph, ruptura com Stifen e socorro a Michael têm contexto. Não demonstram mecanismo de ocupação de corpo. |
| Hospedeira | Sobrevivência após saída preservada; agência, Lyone e continuação posteriores em aberto. |

S161 completo mostra Harry salvando Michael, ferimentos de asas/abdômen e falha de cura em queimaduras, sem novo nome Astro. S090 completo traz médico dizendo morto, não narração omnisciente de morte/ressurreição: não acrescentar uma morte certificada. O nome Henry na percepção mental é lapso dentro da cena Harry, corroborado pela repetição em Harry; não transferir poder. Sem identidade demonstrada entre Jakaw e criatura negra. S1381090–1294 confirma Zex deixado inerte e pingente retirado; reparo posterior ausente. S177 continua vazio, não cena revisada.

O recorte encerra investigação inicial das transições conhecidas de B002, sem certificar S041/S043/S089 nem S1380–1089. Pesquisa textual de Astro/Lyone/hospedeira orientou seleção, mas ocorrências em outros ramos podem ser nome do mestre/OOC e não foram certificadas por pesquisa. A ausência de ponte nesses recortes não afirma inexistência em todos os 214 arquivos. Antecedentes adicionais integram o plano B003.

## Mulack

S158 inteiro agora confrontado. Nyxis é nome retificado; Driade Fistine, Flor de Neve/armadura por partes, motivação financeira/equipamento, seleção A+B de dez companheiros, contribuição e limites de circulação estão documentados. Yakkatsu não integra a dungeon por aparecer em comentário OOC. Pesquisa racial e Philip Glorian permanecem OM-005, sem nova descoberta duplicada. Nyxis deixada com Driade não desaparece por falta de cena posterior.

OM-002, ficha/memorial S198, primeira correção de janeiro S11878–100, PS-020, CRIT-004/039, perfil e ARC-006 foram confrontados. A alegação de morte corrigida para braço quebrado não resolve a disputa final de fevereiro. Morte autodeclarada, pulmão inicialmente perfurado, armadura intacta/ação refeita e recusa continuam contraditórios. Sem sobrevivência original adjudicada. **Sobrevivência adaptada já aprovada e preservada.** OM-018 só recupera preparação/limites.

## Henry, Rans e Ymir

Henry: S187 completo distingue desmaios/exaustão da morte posterior efetivamente narrada. O velho não nomeado de maio e conhecido salvador relatado em junho continuam sem identidade comum demonstrada; S016/S023 já inteiros não foram reiniciados. Projetos MaK/escavador/míssil/torre não todos executados. Controle da força e mortes apesar de intenção não letal têm consequências locais; habilidades/construções fora do lote passam a B003.

Rans: nenhuma nova resolução de selo/Hermione foi recuperada. S003 inteiro e correção já propagada ao documento12 mantêm experiência com voz materna/divina e pedido de remover os próprios selos, sem resultado confirmado ou Feuhs identificado como interlocutor. Menção à internação de Rans em S010 é conversa pessoal fora de personagem e foi excluída da história. Falsa morte e relações anteriores exigem fontes do plano B003.

Ymir: S005 inteiro recupera agência de Nefa, proteção, privacidade, Balenon e confronto entre viver e lutar. Corrigida autoria da prisão (OM-015). Voltar ao lago e ouvir hipótese da Árvore não prova que toda aventura foi sonho. Mãos marcadas B não identificação de morte de Beatriz/Henry. Treino/caça não restauração automática do braço; última pergunta de Nefa aberta. Ymir/Note e Beatriz esposa por informação autoral permanecem; coma/tempos subjetivos e cronologia conjugal não foram conciliados artificialmente.

**Classificação dos protagonistas:** Bytes, God e EREN passam a parcial apenas pelos atos específicos agora lidos (aula/espada; representação/partida; pagamento na captura). Isto não executa suas frentes B003. Yakkatsu permanece não iniciado na trajetória ampla: comentário OOC em S158 não conta como presença ou investigação pessoal.

## Amostragem de qualidade

**26 IDs-alvo, com contexto relido; 12 selecionados por hash e 14 complementos dirigidos.** População: 10.431 IDs com C/D de B001/B002.1/B002.2. Seed `DRAGONS-B002.3-QA-v1`: em cada estado histórico de fonte integral/parcial, ordenar fontes pelo SHA256(seed+estado+source), selecionar seis; em cada fonte selecionar menor SHA256(seed+ID). Seleção dirigida de correções, diálogo, definição auxiliar, mensagem sem texto e spam declarada no JSON; seleção por hash sem filtros semânticos prévios. Contexto normalmente ±4, ampliado para retificação; limites e IDs publicados.

Fontes/períodos variados de dezembro a julho, incluindo ficha/poder, fonte integral/parcial, narração, diálogo, proposta, retificação, metajogo, auxiliares, irrelevantes, fatos já corrigidos e sem mudanças. **Não existiam rótulos individuais completos em B002.1/2**: verificados seus intervalos/categorias/disposições, sem inventar classificação anterior de cada ID. “Correção” nos candidatos dirigidos indica intervalo pretendido; após leitura Q17 é diálogo de Myria, não despertar de poder, e a classificação efetiva é publicada. A amostra não é segundo avaliador independente nem estimativa estatística da qualidade global.

**Resultado:** 25 classificações/tratamentos mantidos, um rótulo individual corrigido (Q10), zero falsa confirmação canônica encontrada na amostra, zero conclusão importante omitida nesse confronto amostral. Q10 letra isolada S155479 tinha rótulo muito amplo de ação/fala no B001; recebe auxiliar sem conteúdo ficcional. C/D preservados por leitura/disposição real, não excluídos do denominador. Expansão S155468–483 verifica contestação de mana e derrota por Baran, sem alteração omitida. O problema localizado é taxonomia; genericidade dos templates é limite estrutural que exige conferência e não permite concluir que todos os demais rótulos estão corretos. Ledger histórico imutável; correção aditiva no [registro QA](auditoria-fontes/qualidade-B002.3.json).

| Caso | Fonte/índice/ID | Classe efetiva | Documento/conclusão |
| --- | --- | --- | --- |
| Q01 | [S016 · 1250984815877161011](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) · 85 | METAJOGO SEM EFEITO | CONT-019; Michael: Discussão Gojo/Black Flash fora de personagem; combate vizinho não concede habilidade. Mantido D por tratamento de exclusão. |
| Q02 | [S182 · 1208541824352780319](../pesquisa/fase-3/Fontes-e-Evidencias.md#s182) · 115 | RESOLUÇÃO DO MESTRE | CONT-006; God/Kian: Aprende chamar elevador por documentos; detalhe operacional do percurso, não viagem dimensional. Contexto já coberto. |
| Q03 | [S001 · 1248799900477689876](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) · 524 | AÇÃO/FALA; RESULTADO LIMITADO | CONT-018; Ymir: Cura tentada/alívio não garante sobrevivência da mãe alce. Morte posterior conservada, sem omissão causal. |
| Q04 | [S008 · 1267311219405094912](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) · 307 | AÇÃO DE DESLOCAMENTO | Harry/Astro; ARC-017: Caminha becos do mercado; não novo plano cósmico ou ponte nominal. Contexto e geografia suficientes. |
| Q05 | [S003 · 1266967745287688192](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) · 420 | METAJOGO DE PERSONALIDADE | Rans/Hermione; PS-038: Referência Geto não alteração ficcional automática; entorno definição Vento separado. Mantido. |
| Q06 | [S174 · 1239762446936182894](../pesquisa/fase-3/Fontes-e-Evidencias.md#s174) · 9 | REAÇÃO AMBÍGUA | Bytes; CRIT-020; PS-031: Reação não explica esfera; toque posterior sem resposta. Classificação B001 mantida. |
| Q07 | [S158 · 1200994056684175390](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) · 1381 | PERGUNTA OOC | Mulack; CONT-005: Pergunta sobre fases da dungeon, não evento futuro executado. Philip/formação tratados no contexto. |
| Q08 | [S037 · 1189750160436248686](../pesquisa/fase-3/Fontes-e-Evidencias.md#s037) · 301 | CORREÇÃO OOC DO MESTRE | HAB-009; Henry; Rans: Pergunta/retificação: era preparação, não ataque consumado; contraste percebido não percepção ilimitada. Mantido. |
| Q09 | [S178 · 1214381016207069236](../pesquisa/fase-3/Fontes-e-Evidencias.md#s178) · 460 | AÇÃO/DIÁLOGO | CONT-010; HAB-014; Henry: Conduz pássaro e comenta vapor; asa-delta falha, não nova habilidade universal. D mantido. |
| Q10 | [S155 · 1210458560560107581](../pesquisa/fase-3/Fontes-e-Evidencias.md#s155) · 479 | AUXILIAR SEM CONTEÚDO FICCIONAL | HAB-004; Michael: Letra isolada em conversa sobre contagem de mana. Rótulo B001 contexto de ação/fala demasiadamente amplo; corrigido para auxiliar. Não remove C/D nem altera derrota narrada. |
| Q11 | [S028 · 1186853483962441748](../pesquisa/fase-3/Fontes-e-Evidencias.md#s028) · 65 | METAJOGO/MECÂNICA | HAB-002; Michael/Rans: Alegação de purificar mana não prova superioridade universal; mestre explica Perfurar e diz básico. Mantido. |
| Q12 | [S123 · 1198737140071289004](../pesquisa/fase-3/Fontes-e-Evidencias.md#s123) · 225 | AÇÃO PROPOSTA | HAB-004; CONT-003; Michael: Barragem/clones/velocidade são autodeclaração, não concessão automática. Bíblia já distingue proposta de resultado. |
| Q13 | [S013 · 1256034729728413797](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) · 2245 | ESCLARECIMENTO AUXILIAR | Kian; CONT-017: Reação à explosão dos braços e demonificação posterior; não identidade nova nem conhecimento universal. Mantido. |
| Q14 | [S013 · 1264714281186885642](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) · 2375 | NARRAÇÃO DE ESTADO | Kian; CONT-017: Desmaia/acorda em céu roxo; não morte real ou descanso na cabana. Mantido. |
| Q15 | [S023 · 1265827765341519953](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) · 742 | DIÁLOGO NPC | Beatriz; CONT-020; OM-014: Autonomia e nove livros; tratamento pequena não idade infantil ou cerimônia. Mantido. |
| Q16 | [S008 · 1266951386948435969](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) · 211 | AÇÃO DE SAÍDA | Astro; CONT-020: Sai do cassino; não prova saída do corpo feminino nesse ID. Disposição de intervalo válida no conjunto, sem atribuir todo evento a cada mensagem. |
| Q17 | [S001 · 1249466921376550962](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) · 762 | DIÁLOGO NPC | Myria; CONT-018: Menina diz magia Natureza ensinada pela mãe; não novo poder Ymir. Estrato inicial era indicativo do intervalo, corrigido aqui para conteúdo efetivo. |
| Q18 | [S023 · 1264750464344522823](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) · 551 | LIMITE DO MESTRE | Ymir; OM-013; CRIT-027: Pode levar anos: não treino concluído até grau7. Bíblia mantém leitura distinta de execução. |
| Q19 | [PWR001 · 1184158911138385961](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr001) · 0 | DEFINIÇÃO DO MESTRE | HAB-001; Michael: Punhos de Ferro +25/0maestria; não invulnerabilidade. Referência coincide com definição publicada. |
| Q20 | [S198 · 1191935255842652281](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) · 0 | FICHA EDITADA | Mulack; OM-002; CRIT-004: Morto em ficha editada não data a inserção; memorial conflita com retificação. Mantido. |
| Q21 | [S013 · 1253899431401492600](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) · 1849 | NARRAÇÃO/DEFINIÇÃO | Kian; OM-011; CRIT-006: Mente ainda Kian, pouco conhecimento; correção incorporada à Bíblia e02/15/19. Mantido. |
| Q22 | [S013 · 1256055716578590780](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) · 2305 | RETIFICAÇÃO DO MESTRE | Kian; OM-011; CONT-017: Explosão da cabeça foi ilusão que Westia desfaz; aparente morte é de Azazel. Correção anterior correta. |
| Q23 | [S001 · 1249503535641526303](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) · 839 | DEFINIÇÃO/RESULTADO | Ymir; OM-010; CRIT-027: Raio6m com custo grave; 10m posterior permanece distinto. Correção anterior mantida. |
| Q24 | [S023 · 1266903430354702428](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) · 875 | DIÁLOGO CONJUGAL | Ymir/Beatriz; OM-014: Chama esposa antes de casados nesse diálogo; declaração autoral preservada, cronologia não resolvida. |
| Q25 | [S198 · 1208627711023644682](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) · 3 | SEM TEXTO | Mulack; S198: Não acrescenta fato; contexto memorial analisado, D válido pela disposição explícita. |
| Q26 | [S198 · 1319339050569695234](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) · 16 | SPAM NÃO CANÔNICO | S198; PS-032: Mensagem comercial sem papel ficcional; irrelevância contextual confirmada. Não abrir link nem produzir acontecimento. |

## Omissões e propagação documental

**OM-015 — Agente da prisão de Ymir:** CONT-014 atribuía à Árvore a jaula e entrega aos Altruístas. A fonte descreve moradores em cidade nas árvores e homem que decreta escravidão; a Árvore Rainha posteriormente diz não conhecer Nefa/Altruístas. Corrigida atribuição, sem concluir que todas as cenas eram sonho. **Impacto:** CORREÇÃO FACTUAL NECESSÁRIA.

**OM-016 — Nefa, Balenon e custos da caçada:** A Bíblia resumia traição/treino sem motivação e contraponto moral suficientes. Nefa justifica entregar Ymir para proteger aldeia; sua privacidade/recusas são demonstradas. Balenon questiona luta interminável; encontro com criança não é cura automática. Metade dos doze de Coleros morre; última pergunta sobre Nefa não tem resolução. Recuperados detalhes, sem destino inventado ou calendário universal. **Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO.

**OM-017 — Limites da sombra adulta de Kian:** Perfil tratava poderes genericamente sem servidão versus união e retirada impossível de sombra viva. Sombra própria custa força; galinha morta submete-se e transporta Kian. Elemento ainda não definido; lapso Ymir não muda protagonista. Acrescentado complemento com espada persistente após despertar, sem fechar adulto–bebê. **Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO.

**OM-018 — Mulack, Driade e preparação delimitada:** Flor de Neve/armadura e expedição já constavam, mas faltavam homenagem ao frio de Mouran, espécie de Nyxis desconhecida, seleção de dez companheiros A+B e limite corporal/circulação. Driade Fistine é nome, não raça; negociar servidão não comprova selo. Elemento não repele mana. Complementados preparação e limites, sem nova solução da contradição. **Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO.

**OM-019 — Ramos de Stark e Richard:** Apoios eram apenas enumerados. Recuperado encontro de Stark com Emma e carona oferecida; sem unificar menina à filha de Lilith. Richard constrói, recebe aviso de Maya, mata lobo e encontra orbe; melhora física é narrada depois do gás, sem mecanismo completo. Maya morreu é OOC; Cot/Cop não unificado ao lobo. Último grunhido e projeto de arma continuam abertos. **Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO.

OM-001–014 preservadas, sem repetir como descobertas. Rechecados os complementos de Colapso, Stwart/STWART LITTLE, Sexto Sentido, livros, casamento, escala do mercado, Mulack/Philip e quatro correções de Azazel; definição de HAB-014 permanece. Bíblia, índice, matriz, propostas02/12/15/19 e auditoria23 já incorporavam correções necessárias anteriores. Não reescrever aprovação para produzir novo acontecimento.

| Canon adaptado | Classificação | Tratamento |
| --- | --- | --- |
| Ymir/Árvore prisão | CORREÇÃO FACTUAL NECESSÁRIA | Corrigida base original; não atribuir o cativeiro à guardiã em desenvolvimento posterior. |
| Ymir/Nefa/Balenon | AJUSTE DE INTERPRETAÇÃO RECOMENDADO | Preservar contraponto à luta, proteção e autonomia; D/B, supremacia futura e Trajetória I intactos. |
| Kian | AJUSTE DE INTERPRETAÇÃO RECOMENDADO | Servidão/limites de sombra não obrigam integração total; A+D/consequências B intactos. |
| Mulack | NENHUMA ALTERAÇÃO NECESSÁRIA na escolha aprovada | Sobrevivência adaptada mantida; antecedentes enriquecidos, sem original adjudicado. |
| Rans | NENHUMA ALTERAÇÃO NECESSÁRIA | Correção da remoção já propagada; mecanismo/voz/Hermione permanecem pendentes. |
| Harry | DECISÃO AUTORAL AINDA NECESSÁRIA | Identidade/mecanismo Astro precisam de escolha própria posterior; não atribuir automaticamente ao pacto. |
| Michael/Lilith/Henry/Bytes/God/EREN/Yakkatsu | NENHUMA ALTERAÇÃO NECESSÁRIA nas direções | Propostas políticas/técnicas e comentários não viram feitos; novos limites documentados para futura consulta. |

Todas as direções dos doze/DD-01–43, Beatriz esposa, Mulack sobrevivente adaptado, supremacia Ymir, D/B, Trajetória I e autonomia NPC preservadas. Zero guerras/eras/mortes/divindades/transformações futuras novas aprovadas.

## Matrizes e cobertura qualitativa

Estado narrativo original permanece distinto da revisão documental global e do encerramento crítico do lote. PS-020/021/022/023/038 e CRIT-003/004/005/006/040 recebem **revisão do escopo crítico inicial concluída, sem solução do mistério e sem revisão global certificada**. Entradas com fontes adicionais continuam parciais. Nenhum protagonista globalmente concluído por ter arquivo inteiro lido.

**PS:** {"PARCIALMENTE REVISADO": 22, "NÃO INICIADO": 17, "EM INVESTIGAÇÃO": 1}.

**CRIT:** {"NÃO INICIADO": 20, "PARCIALMENTE REVISADO": 20}.

**ARC:** {"PARCIALMENTE REVISADO": 11, "NÃO INICIADO": 8}.

**protagonists:** {"PARCIALMENTE REVISADO": 11, "NÃO INICIADO": 1}.

| Grupo | ID/nome | Revisão global | Resultado desta rodada / limite |
| --- | --- | --- | --- |
| PS | PS-001 · Origem da Surgência | PARCIALMENTE REVISADO | Entradas e calendários locais sem origem universal. |
| PS | PS-002 · Saída física versus marca | PARCIALMENTE REVISADO | Marca migra com amputação; liberdade física não remoção. |
| PS | PS-003 · Rio e conclusão do ramo de minhocas | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-004 · Prisão inicial ou minas de Mouran | PARCIALMENTE REVISADO | Prisões distinguidas; OM-015 corrige agente de S005. |
| PS | PS-005 · Resultado do primeiro altar | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-006 · Núcleo, lembranças e cristal da força | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-007 · Ellen e prefeito | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-008 · Trevor e Patrick supostamente traidores | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-009 · Cristal ou Veneno de Ymir | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-010 · Noah desaparecido | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-011 · Figura negra, laboratório e sombras | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-012 · Título e coroa de EREN | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-013 · Morte de Rans no segundo altar | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-014 · Lilith e Hads | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-015 · Gás azul | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-016 · Quatro altares e desfecho de Mouran | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-017 · Harry, God-Zilla e entradas pouco documentadas | PARCIALMENTE REVISADO | Harry ampliado; ramo God permanece pendente. |
| PS | PS-018 · Note: nome, máscara e anonimato | PARCIALMENTE REVISADO | Note é Ymir; máscara/equipamento não apagamento universal de identidade. |
| PS | PS-019 · Ponte à Guilda/Piferme/Olta e fim da campanha | PARCIALMENTE REVISADO | Guerras e governos locais, sem fim universal da campanha. |
| PS | PS-020 · Final de Mulack | PARCIALMENTE REVISADO | Dungeon inteira e antiga correção confrontadas; contradição final preservada. |
| PS | PS-021 · Adulto Kian → bebê Azazel | PARCIALMENTE REVISADO | Antecedentes adultos e sombra ampliados; mecanismo adulto–bebê ausente no escopo. |
| PS | PS-022 · Harry → Astro e hospedeira | PARCIALMENTE REVISADO | Harry nominal/pacto/corpo/memória não produzem ponte confirmada para Astro. |
| PS | PS-023 · Henry volta à vida | PARCIALMENTE REVISADO | Exaustões/despertares locais não ressurreições extras; morte/retorno sem agente identificado. |
| PS | PS-024 · Beatriz: coma e memória | PARCIALMENTE REVISADO | Coma/pernas/relatos situados; causalidade integral e cronologia conjugal abertas. |
| PS | PS-025 · Irmã de Beatriz / Quimera / Milena | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-026 · Nefa e Altruístas | PARCIALMENTE REVISADO | Nefa/Altruístas/Balenon ampliados; não anular toda aventura como sonho. |
| PS | PS-027 · Líder Pantera | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-028 · Emma e pai alegado | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-029 · God depois da caça | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-030 · Yakkatsu sai do Inferno | EM INVESTIGAÇÃO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-031 · Bytes: favor e Nairóbi | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-032 · Exclusões e tópicos privados | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-033 · Golems roubados no Inferno | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-034 · Gwierlan morto segundo Edward | PARCIALMENTE REVISADO | Edward alega morte; não confirmação, demais fontes pendentes. |
| PS | PS-035 · Wilbur e Hermest | PARCIALMENTE REVISADO | Hermest Brown/Rozz lapso, distinto de Dimitri; Wilbur morto, conselho ainda proposta. |
| PS | PS-036 · Culto do Deus Dragão / Deus Demônio | PARCIALMENTE REVISADO | Culto/Disare como falas, não identidade Deus Demônio demonstrada. |
| PS | PS-037 · Escalas e calendários | PARCIALMENTE REVISADO | Fallhebe, moedas, calendários/razões locais e limites preservados. |
| PS | PS-038 · Rans, Hermione e selo | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-039 · Coiote e governo de Piferme | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| PS | PS-040 · Michael, Mytria e conquista | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-001 · Rans sobrevive e retorna publicamente | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-002 · Lilith → Hads → Lilith | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-003 · Henry morre em maio e reaparece em junho | PARCIALMENTE REVISADO | Morte e retorno de Henry continuam sem mecanismo. |
| CRIT | CRIT-004 · Mulack: morte / armadura intacta / memorial | PARCIALMENTE REVISADO | Antecedentes completos não adjudicam retificação versus memorial. |
| CRIT | CRIT-005 · Astro associado a Harry | PARCIALMENTE REVISADO | Pessoal provável, corpo/memória sem ponte segura; associação Astro não confirmada. |
| CRIT | CRIT-006 · Kian/Lúcifer/Azazel é continuidade confirmada externamente | PARCIALMENTE REVISADO | Identidade externa preservada; estados adultos/sombra, sem renascimento explicado. |
| CRIT | CRIT-007 · Note é Ymir, antes da máscara | PARCIALMENTE REVISADO | Note/Ymir alternam antes/depois de máscara; não pessoa nova. |
| CRIT | CRIT-008 · Ellen resgatada viva | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-009 · Gwierlan vivo; Michael rei | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-010 · Quarto altar destruído pela besta | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-011 · Terceiro altar e contagem global | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-012 · Ritual e Patrick | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-013 · Karl morto; Edward foge | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-014 · Marca: permanência confirmada e última referência de Henry | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-015 · Garold morre e Lilith governa | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-016 · Wilbur e Dimitri | PARCIALMENTE REVISADO | Hermest mata Wilbur, Michael mata Hermest, Dimitri distinto e posterior vivo. |
| CRIT | CRIT-017 · God: auxílio à Árvore e última caçada | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-018 · Henry recusa Fogo Demoníaco | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-019 · Yakkatsu: Linhas, Bardock e Inferno | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-020 · Bytes: favor e esfera | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-021 · Bytes e Nairóbi | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-022 · Beatriz viva, princesa e recuperada | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-023 · Emma e raízes | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-024 · Pantera e Quimera | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-025 · Deus Dragão e Deus Demônio | PARCIALMENTE REVISADO | Falas religiosas/culto não cosmologia universal. |
| CRIT | CRIT-026 · Westia e velho de maio | PARCIALMENTE REVISADO | Azazel vivo na cabana; velho e Edward não identificados por hipótese. |
| CRIT | CRIT-027 · MUTON, Sexto Sentido e livros | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-028 · Henry em canal vazio | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-029 · Fim recuperável | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-030 · Natureza de Kian: concessão e contestação | PARCIALMENTE REVISADO | Elemento não definido, sombra servil; concessão antiga em S032 ainda pendente. |
| CRIT | CRIT-031 · Ceifador, Froid e Tengetsu | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-032 · Sombras do orbe de Piferme | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-033 · Previsão de Ymir | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-034 · Henry/Harry no núcleo inicial | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-035 · Crescimento lunar de Henry | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-036 · Controle Magnético de Lilith | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-037 · Mortes e controles alheios no final de S046 | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| CRIT | CRIT-038 · Ária, Draconia e sugadores de alma | PARCIALMENTE REVISADO | Ária/Draconia na mina como fala situada; outras fontes permanecem. |
| CRIT | CRIT-039 · Primeira alegação de morte de Mulack versus dungeon final | PARCIALMENTE REVISADO | Correção braço quebrado de janeiro não decide dungeon final. |
| CRIT | CRIT-040 · Rans: pedido de remoção e voz materna/divina | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-001 · Surgência, aparente resgate e escravização | PARCIALMENTE REVISADO | Captura/escravização expandida; ramo de saída S025 não recomeçado. |
| ARC | ARC-002 · Exploração do ramo de minhocas e retorno ao rio | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-003 · Controle de energia lunar e proteção dos companheiros | PARCIALMENTE REVISADO | Limites de força/exaustão e combate, não domínio lunar total. |
| ARC | ARC-004 · Descoberta de capacidade e vínculo de EREN | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-005 · Briga da rua B e crescimento involuntário | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-006 · Busca de saída de Mulack e integração de Yakkatsu | PARCIALMENTE REVISADO | Integração antiga com Yakkatsu não presença dele na dungeon. |
| ARC | ARC-007 · Anonimato e consolidação de Note | PARCIALMENTE REVISADO | Anonimato, Nefa/Balenon e custos ampliados, sem divindade original. |
| ARC | ARC-008 · Busca de renda, serpente e novo cativeiro de Lilith | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-009 · Preparação e missão contra os altares de Mouran | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-010 · Culto e crise política entre Mouran, Olta e Piferme | PARCIALMENTE REVISADO | Política, culto, explosões e projetos separados de implantação. |
| ARC | ARC-011 · Guerra, treino e golems do Inferno | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-012 · Lilith rainha e proteção de Emma | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-013 · Bytes e Nairóbi | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-014 · Yakkatsu e busca por sair do Inferno | NÃO INICIADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-015 · Kian, Lúcifer e infância de Azazel | PARCIALMENTE REVISADO | Adulto e sombra confrontados, infância preservada sem ponte mecânica. |
| ARC | ARC-016 · Rans, sobrevivência e Hermione | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-017 · Harry e ramo Astro | PARCIALMENTE REVISADO | Harry nominal antecede Astro provável; pacto não causa automática de troca. |
| ARC | ARC-018 · Beatriz, família real e Quimera | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| ARC | ARC-019 · Michael e campanha de Mytria | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| protagonists | Michael Uchiyama ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Rans ·  | PARCIALMENTE REVISADO | Estado anterior preservado; sem conclusão adicional. |
| protagonists | Henry Chambers ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | God-Zilla ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Harry ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Kian / Lúcifer / Azazel ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Mulack ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Bytes Sky ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | EREN ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Lilith Chipper ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Ymir / Note ·  | PARCIALMENTE REVISADO | Estados locais confrontados; fontes/intervalos fora do lote permanecem pendentes. |
| protagonists | Yakkatsu Tenshin ·  | NÃO INICIADO | Comentários OOC em S158 não revisão da trajetória; B003 pendente. |

**Fontes por estado:** {"TRIAGEM INTEGRAL": 34, "SEM MENSAGENS": 16, "NÃO INICIADA": 152, "PARCIAL": 12}.

**TRIAGEM INTEGRAL:** S001, S002, S003, S004, S005, S008, S010, S013, S016, S023, S040, S051, S052, S070, S090, S158, S161, S174, S182, S184, S187, S198, PWR001, PWR002, PWR003, PWR004, PWR005, PWR006, PWR007, PWR008, PWR009, PWR010, PWR011, PWR012.

**PARCIAL:** S025, S028, S037, S068, S106, S118, S123, S138, S146, S155, S166, S178.

**NÃO INICIADA:** S012, S014, S022, S024, S026, S027, S029, S030, S031, S032, S033, S034, S035, S036, S038, S039, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S069, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S107, S108, S110, S111, S112, S113, S114, S115, S116, S117, S119, S120, S121, S122, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S139, S140, S141, S142, S143, S144, S145, S148, S149, S150, S151, S152, S153, S154, S156, S157, S159, S160, S162, S164, S165, S167, S168, S169, S170, S171, S172, S173, S175, S176, S179, S181, S183, S185, S186, S188, S189, S191, S192, S193, S194, S195, S196, S197, S199, S200, S201, S202.

**SEM MENSAGENS:** S006, S007, S009, S011, S015, S017, S018, S019, S020, S021, S109, S147, S163, S177, S180, S190.

## Encerramento fundamentado de B002

| Critério | Evidência e conclusão |
| --- | --- |
| 1 Sequências críticas suficientes | Kian S013/S182/S187/S184/S051/S052/S070; Harry S008/S040/S090/S161 e terminalS138; Mulack S158/S198 e retificaçãoS118; Henry morte/retornoS187/S016/S023; RansS003 e YmirS001/S002/S005/S023. Suficientes para conclusão inicial delimitada, sem mecanismo universal ou biografias completas. |
| 2 Intervalos rastreáveis | Quatro ledgers e recortes K/Q, IDs/hash/extremos/disposições. |
| 3 Estados conhecidos confrontados | CONT/perfis/ARC/PS/CRIT, suplementos e premissas adaptadas; distinção de evento/fala/proposta. |
| 4 Omissões corrigidas | OM-015–019, com antes/depois e fontes; OM-001–014 preservadas. |
| 5 Contradições visíveis | Mulack, portões, Altruístas, escalas/nomes e conjugalidade conservados. |
| 6 Lacunas classificadas | Identidade pessoal versus corpo/memória/mecanismo; ausência nos recortes não ausência global. |
| 7 C/D reconciliados | União de IDs/hashes/HTML; zero diferença. |
| 8 Qualidade testada | 26 alvos relidos, um rótulo corrigido, expansão e limites explícitos. |
| 9 Sistemática ampliada | S004/S005/S010 inteiras; vazios não cenas; próximaS012. |
| 10 Handoff | Matrizes e planoB003 com complementos de intervalos, objetivos e critérios. |

**Encerrado B002, sem prolongar indefinidamente a busca de mecanismos não demonstrados.** Questões fora desse escopo passam a B003/varredura/deliberação; nenhuma afirmação de todas as fontes relevantes globalmente revistas. Mistérios de Kian, Harry, Henry, Mulack, Rans/Hermione e cronologia Ymir/Beatriz continuam abertos. Auditoria de 89.313 mensagens e revisão completa dos doze não encerradas.

## B003 — plano, sem execução

Intervalos abaixo são complementos exatos da união C/D atual, calculados pelo manifesto; fontes completas são puladas, não recontadas. [Plano técnico](auditoria-fontes/plano-B003.json) conserva cada intervalo, relacionado e critério. Trabalhar em núcleos do plano sistemático de até200 com contexto; fontes extensas não devem ser aprovadas por busca lexical. Planejamento não acrescenta C/D.

| Prioridade | Fonte | Intervalos sem C/D | Objetivo e risco | PS/CRIT/ARC |
| --- | --- | --- | --- | --- |
| Bytes | [S014](../pesquisa/fase-3/Fontes-e-Evidencias.md#s014) | 0–243 | Nairóbi, favor, esfera, capacidades e consequências; distinguir autocura, Nines, pedido e concessão. | PS-031; CRIT-020/021; ARC-013 |
| Bytes | [S126](../pesquisa/fase-3/Fontes-e-Evidencias.md#s126) | 0–1230 | Nairóbi, favor, esfera, capacidades e consequências; distinguir autocura, Nines, pedido e concessão. | PS-031; CRIT-020/021; ARC-013 |
| Bytes | [S173](../pesquisa/fase-3/Fontes-e-Evidencias.md#s173) | 0–2445 | Nairóbi, favor, esfera, capacidades e consequências; distinguir autocura, Nines, pedido e concessão. | PS-031; CRIT-020/021; ARC-013 |
| Bytes | [S174](../pesquisa/fase-3/Fontes-e-Evidencias.md#s174) | COMPLETA — pular | Nairóbi, favor, esfera, capacidades e consequências; distinguir autocura, Nines, pedido e concessão. | PS-031; CRIT-020/021; ARC-013 |
| Yakkatsu | [S022](../pesquisa/fase-3/Fontes-e-Evidencias.md#s022) | 0–2040 | Bardock, Stwart, Inferno e último estado; não fundir STWART LITTLE ou dragões por cor. | PS-030; CRIT-019; ARC-006/014 |
| Yakkatsu | [S081](../pesquisa/fase-3/Fontes-e-Evidencias.md#s081) | 0–570 | Bardock, Stwart, Inferno e último estado; não fundir STWART LITTLE ou dragões por cor. | PS-030; CRIT-019; ARC-006/014 |
| Yakkatsu | [S118](../pesquisa/fase-3/Fontes-e-Evidencias.md#s118) | 0–77, 101–116, 122–122, 128–212 | Bardock, Stwart, Inferno e último estado; não fundir STWART LITTLE ou dragões por cor. | PS-030; CRIT-019; ARC-006/014 |
| God-Zilla | [S117](../pesquisa/fase-3/Fontes-e-Evidencias.md#s117) | 0–192 | Gotter/Árvore, caçada e vínculos; não transformar pedido de ajuda em nomeação de guardião. | PS-017/029; CRIT-017; ARC-010 |
| God-Zilla | [S133](../pesquisa/fase-3/Fontes-e-Evidencias.md#s133) | 0–153 | Gotter/Árvore, caçada e vínculos; não transformar pedido de ajuda em nomeação de guardião. | PS-017/029; CRIT-017; ARC-010 |
| God-Zilla | [S134](../pesquisa/fase-3/Fontes-e-Evidencias.md#s134) | 0–224 | Gotter/Árvore, caçada e vínculos; não transformar pedido de ajuda em nomeação de guardião. | PS-017/029; CRIT-017; ARC-010 |
| God-Zilla | [S135](../pesquisa/fase-3/Fontes-e-Evidencias.md#s135) | 0–213 | Gotter/Árvore, caçada e vínculos; não transformar pedido de ajuda em nomeação de guardião. | PS-017/029; CRIT-017; ARC-010 |
| God-Zilla | [S178](../pesquisa/fase-3/Fontes-e-Evidencias.md#s178) | 0–428, 434–455, 465–474, 480–1166, 1173–1187, 1194–1194, 1205–1421 | Gotter/Árvore, caçada e vínculos; não transformar pedido de ajuda em nomeação de guardião. | PS-017/029; CRIT-017; ARC-010 |
| EREN | [S032](../pesquisa/fase-3/Fontes-e-Evidencias.md#s032) | 0–196 | Ana, título Natureza, coroa, capacidades/últimos estados; título autodeclarado não ascensão. | PS-012; CRIT-002/010; ARC-004 |
| EREN | [S084](../pesquisa/fase-3/Fontes-e-Evidencias.md#s084) | 0–463 | Ana, título Natureza, coroa, capacidades/últimos estados; título autodeclarado não ascensão. | PS-012; CRIT-002/010; ARC-004 |
| EREN | [S095](../pesquisa/fase-3/Fontes-e-Evidencias.md#s095) | 0–347 | Ana, título Natureza, coroa, capacidades/últimos estados; título autodeclarado não ascensão. | PS-012; CRIT-002/010; ARC-004 |
| EREN | [S159](../pesquisa/fase-3/Fontes-e-Evidencias.md#s159) | 0–439 | Ana, título Natureza, coroa, capacidades/últimos estados; título autodeclarado não ascensão. | PS-012; CRIT-002/010; ARC-004 |
| EREN | [S166](../pesquisa/fase-3/Fontes-e-Evidencias.md#s166) | 0–1789, 1795–1822, 1828–2699 | Ana, título Natureza, coroa, capacidades/últimos estados; título autodeclarado não ascensão. | PS-012; CRIT-002/010; ARC-004 |
| Lilith | [S037](../pesquisa/fase-3/Fontes-e-Evidencias.md#s037) | 0–296, 306–318, 324–324, 330–937 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S057](../pesquisa/fase-3/Fontes-e-Evidencias.md#s057) | 0–360 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S076](../pesquisa/fase-3/Fontes-e-Evidencias.md#s076) | 0–791 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S077](../pesquisa/fase-3/Fontes-e-Evidencias.md#s077) | 0–413 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S087](../pesquisa/fase-3/Fontes-e-Evidencias.md#s087) | 0–773 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S102](../pesquisa/fase-3/Fontes-e-Evidencias.md#s102) | 0–31 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S151](../pesquisa/fase-3/Fontes-e-Evidencias.md#s151) | 0–690 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S166](../pesquisa/fase-3/Fontes-e-Evidencias.md#s166) | 0–1789, 1795–1822, 1828–2699 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S173](../pesquisa/fase-3/Fontes-e-Evidencias.md#s173) | 0–2445 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Lilith | [S185](../pesquisa/fase-3/Fontes-e-Evidencias.md#s185) | 0–1810 | Hads, Emma, governos e relações; autonomia de NPCs, ordem versus resultado e braço não regenerado por plano. | PS-014/028/039; CRIT-002/015/023; ARC-008/012 |
| Michael | [S155](../pesquisa/fase-3/Fontes-e-Evidencias.md#s155) | 0–439, 445–445, 451–467, 484–738 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Michael | [S159](../pesquisa/fase-3/Fontes-e-Evidencias.md#s159) | 0–439 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Michael | [S166](../pesquisa/fase-3/Fontes-e-Evidencias.md#s166) | 0–1789, 1795–1822, 1828–2699 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Michael | [S170](../pesquisa/fase-3/Fontes-e-Evidencias.md#s170) | 0–679 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Michael | [S175](../pesquisa/fase-3/Fontes-e-Evidencias.md#s175) | 0–469 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Michael | [S185](../pesquisa/fase-3/Fontes-e-Evidencias.md#s185) | 0–1810 | Governo/conflitos/projetos; alianças pretendidas não anexação consumada. Gwierlan vivo não adjudica cada relato. | PS-034/035/040; CRIT-009/016; ARC-010/019 |
| Rans | [S075](../pesquisa/fase-3/Fontes-e-Evidencias.md#s075) | 0–174 | Falsa morte, Hermione e relações anteriores; não fundir voz materna/divina com Feuhs, nem supor selo removido. | PS-013/038; CRIT-001/040; ARC-003/016 |
| Rans | [S076](../pesquisa/fase-3/Fontes-e-Evidencias.md#s076) | 0–791 | Falsa morte, Hermione e relações anteriores; não fundir voz materna/divina com Feuhs, nem supor selo removido. | PS-013/038; CRIT-001/040; ARC-003/016 |
| Rans | [S104](../pesquisa/fase-3/Fontes-e-Evidencias.md#s104) | 0–164 | Falsa morte, Hermione e relações anteriores; não fundir voz materna/divina com Feuhs, nem supor selo removido. | PS-013/038; CRIT-001/040; ARC-003/016 |
| Rans | [S165](../pesquisa/fase-3/Fontes-e-Evidencias.md#s165) | 0–198 | Falsa morte, Hermione e relações anteriores; não fundir voz materna/divina com Feuhs, nem supor selo removido. | PS-013/038; CRIT-001/040; ARC-003/016 |
| Rans | [S166](../pesquisa/fase-3/Fontes-e-Evidencias.md#s166) | 0–1789, 1795–1822, 1828–2699 | Falsa morte, Hermione e relações anteriores; não fundir voz materna/divina com Feuhs, nem supor selo removido. | PS-013/038; CRIT-001/040; ARC-003/016 |
| Henry | [S037](../pesquisa/fase-3/Fontes-e-Evidencias.md#s037) | 0–296, 306–318, 324–324, 330–937 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S046](../pesquisa/fase-3/Fontes-e-Evidencias.md#s046) | 0–284 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S074](../pesquisa/fase-3/Fontes-e-Evidencias.md#s074) | 0–276 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S106](../pesquisa/fase-3/Fontes-e-Evidencias.md#s106) | 0–670, 676–703, 709–714, 722–1514, 1520–1523, 1529–1629, 1635–1643, 1649–1684, 1690–1701, 1707–1737, 1743–1847 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S134](../pesquisa/fase-3/Fontes-e-Evidencias.md#s134) | 0–224 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S172](../pesquisa/fase-3/Fontes-e-Evidencias.md#s172) | 0–2244 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S173](../pesquisa/fase-3/Fontes-e-Evidencias.md#s173) | 0–2445 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S178](../pesquisa/fase-3/Fontes-e-Evidencias.md#s178) | 0–428, 434–455, 465–474, 480–1166, 1173–1187, 1194–1194, 1205–1421 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Henry | [S179](../pesquisa/fase-3/Fontes-e-Evidencias.md#s179) | 0–2432 | Construções/habilidades/consequências; projeto não produção, morte/retorno sem nomear salvador por semelhança. | PS-002/023/033; CRIT-003/018/035; ARC-003/011 |
| Harry, Zex, Stifen e rede | [S041](../pesquisa/fase-3/Fontes-e-Evidencias.md#s041) | 0–930 | Antecedentes ainda fora do recorte, construção de Zex e fontes de memória; procurar ponte sem certificar Astro por autoria. | PS-017/022; CRIT-005; ARC-017 |
| Harry, Zex, Stifen e rede | [S043](../pesquisa/fase-3/Fontes-e-Evidencias.md#s043) | 0–847 | Antecedentes ainda fora do recorte, construção de Zex e fontes de memória; procurar ponte sem certificar Astro por autoria. | PS-017/022; CRIT-005; ARC-017 |
| Harry, Zex, Stifen e rede | [S089](../pesquisa/fase-3/Fontes-e-Evidencias.md#s089) | 0–2216 | Antecedentes ainda fora do recorte, construção de Zex e fontes de memória; procurar ponte sem certificar Astro por autoria. | PS-017/022; CRIT-005; ARC-017 |
| Harry, Zex, Stifen e rede | [S138](../pesquisa/fase-3/Fontes-e-Evidencias.md#s138) | 0–1089 | Antecedentes ainda fora do recorte, construção de Zex e fontes de memória; procurar ponte sem certificar Astro por autoria. | PS-017/022; CRIT-005; ARC-017 |
| Apoios e organizações | [S012](../pesquisa/fase-3/Fontes-e-Evidencias.md#s012) | 0–69 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |
| Apoios e organizações | [S057](../pesquisa/fase-3/Fontes-e-Evidencias.md#s057) | 0–360 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |
| Apoios e organizações | [S119](../pesquisa/fase-3/Fontes-e-Evidencias.md#s119) | 0–171 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |
| Apoios e organizações | [S156](../pesquisa/fase-3/Fontes-e-Evidencias.md#s156) | 0–372 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |
| Apoios e organizações | [S172](../pesquisa/fase-3/Fontes-e-Evidencias.md#s172) | 0–2244 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |
| Apoios e organizações | [S185](../pesquisa/fase-3/Fontes-e-Evidencias.md#s185) | 0–1810 | Stark/Richard/Maya, Altruístas, Nefa, Pantera e religião; não criar homônimos unificados ou mortes por OOC. | PS-001/007/027; CRIT-024/038; ARC-009/018 |

**Conclusão por investigação:** recortes prioritários e fronteiras lidos/confrontados; estados/resultados/contradições/últimas presenças registrados; documentação global somente concluída se todo escopo relevante disponível for recuperado. Retomar S012 na frente sistemática; equilibrar personagens pouco documentados e NPCs, sem exclusão por menor volume. Nenhum grande acontecimento definitivo escrito.

## Validação e publicação

[Validação técnica](auditoria-fontes/validacao-B002.3.json): hashes dos oito ZIPs e HTMLs usados, IDs/textos, links/âncoras, união de cobertura, plano/matrizes, documentos protegidos e decisões autorais. Publicação por branch/commit/PR; confirmação de merge e commit final entregue no recibo da execução, sem inserir antecipadamente um resultado ainda não ocorrido.
