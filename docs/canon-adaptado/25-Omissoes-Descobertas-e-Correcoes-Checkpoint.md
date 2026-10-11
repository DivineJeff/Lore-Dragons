# Omissões, descobertas e correções — checkpoints B001, B002.1 e B002.2

Auditoria independente de Dragons · 10/10/2026 · Etapa B iniciada, sem encerramento global.

**Atualização 11/10/2026:** OM-008–014 e COR-E01 em [registro adicional B002.2](#registro-adicional-b0022); seções anteriores conservam os estados históricos.

## Escopo e método

Base anterior: main `db7134a506ae52ba4e5bc9686af66bb8a09cbf6d`, após PR #14. O [documento 24](24-Auditoria-de-Cobertura-e-Integridade-das-Fontes.md) contém inventário, integridade e reconciliação das métricas. Este registro documenta diferenças comprovadas e conferências dirigidas, sem substituir a Bíblia ou a auditoria dos doze.

Foram examinadas em contexto **437 mensagens distintas**: todas as 158 de PWR001–PWR012, todas as 13 de S174 e 17 de S198, mais 249 mensagens em intervalos ao redor de testemunhos dos HAB. Os intervalos dirigidos incluem duas mensagens antes/depois da âncora, com sobreposições removidas. Não equivalem a cenas completas ou varredura dos canais restantes. O [ledger](auditoria-fontes/triagem-B001.json) preserva fonte, índice base zero, ID, data UTC e hashes; não republica conversas brutas. Principal: 279/89.155 (0,312938%); combinado: 437/89.313 (0,489290%). Nenhuma amostragem certifica o restante.

A natureza da evidência é examinada no contexto: resultado do mestre; fala de NPC; tentativa do jogador; descrição mecânica; conversa OOC; correção; rolagem; conversa auxiliar. `/` e `//` são pistas, não filtros infalíveis. As categorias amplas do ledger indicam natureza contextual e não conferem aprovação automática. Comentários auxiliares sem afirmação canônica são registrados como contexto, não como fatos recuperados.

Tratamentos: **CASO 1**, afirmação existente confirmada no recorte; **CASO 2**, registro incompleto; **CASO 3**, informação relevante ainda não documentada; **CASO 4**, conflito com conclusão anterior; **CASO 5**, ambiguidade preservada. Quando uma mensagem contém apenas conversa auxiliar, a ausência de correção no lote não declara que a Bíblia incorporou literalmente seu texto. As duas omissões abaixo são CASO 2; não houve descoberta de acontecimento novo definitivo neste lote.

## OM-001 — Maestria de Fortalecimento Corporal Geral com Mana

**Importância:** MÉDIA. **Confiança:** ALTA na condição mecânica expressa; sem generalização a todos os poderes. **Afetado:** Bíblia, HAB-014 (Rans). Não é Escudo de Mana.

**Contexto:** PWR009 contém discussão extensa sobre ligar a habilidade e obter maestria. A referência a uma vez por hora aparece em `1198533178529419266`; a pergunta sobre meia hora não cria um direito automático. Depois, o mestre reafirma que decide se concede maestria em `1198533275191349318` e sugere estudar/melhorar a habilidade em `1198533324440883250`, admitindo pontos em `1198533338915405925`. São regras discutidas fora de personagem, não uma nova evolução narrada. A definição e o despertar no RP continuam sustentados por S166.

**Anterior:** “Uso de mana; ganho de maestria não por ligar/desligar indefinidamente, discussão fixa uma vez por hora.”

**Corrigido:** “Uso de mana; ganho de maestria não por ligar/desligar indefinidamente. A discussão menciona uma vez por hora, mas a concessão permanece a critério do mestre, que também admite avaliar estudo e melhoria da habilidade. Não constitui progressão automática por tempo ligado nem tabela universal de pontos.”

**Justificativa e impacto histórico:** o trecho anterior preservava a frequência, mas omitia a avaliação final do mestre; poderia sustentar uma progressão passiva garantida numa futura continuidade. A regra não concede nível novo, potência ilimitada ou mecanismo futuro. A referência à discricionariedade já aparecia entre fontes complementares da Bíblia; agora está expressa na conclusão local. Acrescentadas três âncoras ao HAB-014. [PWR009](../pesquisa/fase-3/Fontes-e-Evidencias.md#pwr009).

## OM-002 — Manifestação retrospectiva do mestre sobre Mulack

**Importância:** ALTA para a interpretação da disputa documental. **Confiança:** ALTA na existência e natureza retrospectiva do comentário; não confirma desfecho ficcional único. **Afetados:** perfil de Mulack na Bíblia, CRIT-004 e PS-020 na matriz.

**Contexto:** S198 é memorial e conversa sobre Mulack. Há declaração do participante e reprodução da resposta de que ele não morreu, em `1208629609906704394`. Em maio, o mestre indica que só então leu o texto (`1239836014919553084`) e comenta “O cara se matou e me culpou” (`1239836048151019552`). Esse comentário posterior precisa acompanhar o memorial, mas não é uma cena em que Mulack executa um ato nem explica como a retificação da armadura foi anulada. A cena da dungeon S158 permanece sujeita a nova releitura completa na próxima investigação; esta entrega não declara ter relido todas as suas mensagens.

**Anterior:** CRIT-004 afirmava “Retificação e recusa de continuar impedem escolher destino único.” PS-020 registrava “Morte/memorial versus retificação de armadura intacta e ação refeita. O abandono do jogador não resolve a versão ficcional.” O perfil apresentava essas versões e o memorial, sem o comentário posterior do mestre.

**Corrigido por complemento explícito, preservando esses textos:** “Em maio, o mestre comenta que só então leu o memorial e atribui a morte à ação do jogador. É comentário fora de personagem sobre o conflito, não nova cena de morte nem resolução inequívoca da retificação da dungeon. A contradição permanece; a sobrevivência escolhida para a adaptação tem origem autoral separada.” Duas âncoras novas acompanham o complemento em cada destino.

**Impacto histórico:** a leitura das posições no conflito fica mais completa. Não se canoniza suicídio, morte definitiva ou sobrevivência original. Não há novo retorno ficcional recuperado neste lote. **PS-020 continua CONTRADIÇÃO NÃO RESOLVIDA**, com evidência adicional. A sobrevivência adaptada aprovada em DD-38 permanece intacta; sua aprovação não apaga o conflito do original. [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198); [PS-020](../canon-original/19-Matriz-Canon-Critico.md#ps-020).

## COR-M01 — Qualificação da afirmação de leitura integral

**Importância:** ALTA metodológica. **Confiança:** ALTA nos totais e no limite dos registros; não adjudica a sinceridade ou ocorrência da leitura histórica. **Afetados:** critérios da Bíblia e abertura do README da pesquisa. Não modifica acontecimentos.

**Anterior na Bíblia:** “A reconstrução abrange 202 exportações narrativas: 186 não vazias, integralmente lidas, com 89.155 mensagens, e 16 vazias. A fonte adicional de poderes contém 12 exportações e 158 mensagens. Cobertura integral significa leitura do material disponível; não significa recuperar mensagens apagadas ou obter respostas para todos os mistérios.”

**Formulação corrigida na Bíblia:** “A reconstrução abrange 202 exportações narrativas: 186 não vazias, com 89.155 mensagens, e 16 vazias. A fonte adicional de poderes contém 12 exportações e 158 mensagens. A Fase 3 registrou leitura integral e encerramento por saturação estrutural. A auditoria independente posterior confirmou inventário e processamento desses totais, encontrou registros de investigação após o checkpoint de 36,93%, mas não comprovou nem refutou retrospectivamente a leitura semântica de cada mensagem. Inventário, processamento, triagem e consolidação são coberturas distintas; consulte a [auditoria de fontes](../canon-adaptado/24-Auditoria-de-Cobertura-e-Integridade-das-Fontes.md). Mensagens apagadas ou conteúdo não exportado permanecem inacessíveis.”

**Revisado:** os mesmos totais são preservados; leitura integral e saturação passam a ser atribuídas ao registro histórico da Fase 3. A reextração independente confirma inventário/processamento, e os registros posteriores provam continuação após 36,93%; não comprovam nem refutam análise semântica individual de cada mensagem. O texto aponta ao documento 24 e distingue as quatro coberturas. No README, “A leitura foi encerrada…” torna-se “A Fase 3 registrou o encerramento da leitura…”, com complemento independente. A ressalva inteira do PR #14 é preservada.

**Justificativa:** o ledger histórico final marca leitura/classificação/revisão de todas as fontes não vazias incondicionalmente. Os snapshots, notas e âncoras existentes sustentam investigação real e quantitativamente compatível; o ledger sozinho não certifica compreensão de 89.155 mensagens. Não se deduz que a investigação parou em 36,93% nem que somente as 1.475 âncoras do relatório complementar foram lidas. Hashes e resultados estão nos [controles históricos](auditoria-fontes/controles-documentais-e-historicos.json).

## Conferências dos poderes — alcance dirigido

A tabela compara as definições PWR integralmente lidas com testemunhos narrativos selecionados e a formulação da Bíblia. “Sem correção no recorte” não certifica todas as aplicações/evoluções posteriores. As referências completas estão em [HAB-001–018](../canon-original/17-Biblia-Canon-Original.md#poderes) e no ledger. O custo de uma descrição não prova que todo uso posterior respeitou esse custo; aplicações adicionais fora destas janelas permanecem pendentes.

| Item | Resultado do confronto neste lote |
| --- | --- |
| HAB-001, Punhos de Ferro de Michael | Definição e uso distinguem mecânica de resultado; sem correção no recorte. |
| HAB-002, Penetração/Perfurar | Associação nominal continua provável; não demonstra atravessar toda dureza. Sem promoção a certeza. |
| HAB-003, Aura/Passo Sombrio | S106 inclui técnica inicialmente sem registro; controle/força condicionam efeito. Ausência de ficha não elimina a narração. |
| HAB-004, Barragem Estelar | PWR registra proposta; S123 sustenta ataque com resultado parcial. Não confirma todas as vantagens alegadas pelo jogador. |
| HAB-005, Instinto de Caça | Definição e testemunhos mantidos; alcance universal ou evolução posterior não certificados. |
| HAB-006, Diable Jumble | Nomenclatura da descrição e uso preservados; não cria técnica adicional pela grafia. |
| HAB-007, Punhos de Ferro de Harry | Definição separada do homônimo de Michael; sem fusão de usuários ou poder. |
| HAB-008, Berserker | Definição PWR não demonstra aplicação narrativa recuperada no recorte. Mantém limite da Bíblia. |
| HAB-009, espirais de Mulack | Tentativa de terceira espiral e absorção contextual não garantem mana ambiental ilimitada ou perda zero permanente. |
| HAB-010, Punhos de Mana | Aquisição e efeitos não tornam todo golpe acerto garantido; resultado contextual preservado. |
| HAB-011, Sombra | Definição e testemunhos selecionados não permitem universalizar domínio; sem correção no recorte. |
| HAB-012, Intenção Assassina | Condições registradas preservadas; não confundir intenção com submissão automática. |
| HAB-013, Método dos Batimentos | Oito passos propostos em PWR009 não demonstram aprovação só pelo ZIP. A ponte narrativa completa e usos posteriores ainda exigem lote próprio. |
| HAB-014, Fortalecimento Geral | OM-001 explicita concessão discricionária de maestria; sem evolução nova. |
| HAB-015, Voadora Mortal | Voadora participa do combo; Henry finaliza escorpião. Não atribuir toda vitória isoladamente a Bytes. |
| HAB-016, Tourada | Investida e efeitos recuperados sob cansaço/energia lunar; sem generalização ao corpo em qualquer condição. |
| HAB-017, Propulsão Explosiva | Pedido do jogador e comentário de outro jogador não são concessão do mestre. Propulsão de fogo posterior não comprova equivalência nominal. |
| HAB-018, Tigre Infernal | Descrição do jogador tem definição equivalente do mestre em S178; arma, recuo e ferimento condicionam o disparo. Não concede autoridade geral sobre Fogo Demoníaco. |

PWR002, PWR004, PWR007 e PWR012 têm material muito limitado, inclusive conversa auxiliar. Isso não prova que God-Zilla, Kian, Lilith ou Ymir não tenham outras capacidades. Os doze receberam confronto de suas fontes PWR, **não** uma nova auditoria factual completa dos doze perfis.

## Pendências e confirmações sem alteração

S174 foi lida integralmente: Bytes toca a esfera em `1239764239644626994`, sem resultado posterior recuperado nessa fonte. Mantém-se a distinção entre tocar, ter efeito e concluir compromisso. Não demonstradas morte, absorção ou venda de alma. Essa conferência não encerra a investigação de Nairóbi e do favor em outros canais.

S198 foi lida integralmente: o memorial comprova declaração retrospectiva do participante; não data automaticamente o acontecimento na data original de uma ficha editada. OM-002 acrescenta a posição posterior do mestre. As demais 39 PS e os 39 CRIT/19 ARC receberam contagem/localização estrutural, **não reavaliação semântica completa**. Ainda não se apresenta uma classificação nova para cada um.

O lote mantém diferenças entre ação, proposta, definição e resolução. Não encontrou necessidade de escolher novos destinos. A afirmação “não foram encontradas correções necessárias” só se aplica aos recortes identificados acima. Não há garantia de ausência de omissões fora deles. NPCs, organizações, regiões e aplicações posteriores permanecem para a investigação sistemática.

## Registro de alterações e próximos controles

| Identificação | Alteração real | Origem e limite |
| --- | --- | --- |
| OM-001 | Bíblia HAB-014: limite contextual e três âncoras acrescentados | Regra discutida; não evolução demonstrada. |
| OM-002 | Perfil de Mulack, CRIT-004 e PS-020: complemento e duas âncoras em cada | Comentário retrospectivo; conflito preservado. |
| COR-M01 | Critérios da Bíblia e README da pesquisa: atribuição histórica e ressalva | Cobertura independente; sem modificação de fatos. |
| Índices/estados | README raiz, índice original e README adaptado apontam aos documentos 24/25 | Auditoria em andamento. |

Não alterados o registro DD-01–43, a auditoria 23 do PR #14, o panorama 22, as alternativas e os oito ZIPs. Casamento autoral Ymir/Beatriz com cronologia aberta, sobrevivência adaptada de Mulack e supremacia futura de Ymir permanecem nos registros aprovados. Essa preservação por bytes não substitui a auditoria frase a frase da compatibilidade, ainda pendente.

Antes do encerramento global: revisar morte/retorno de Henry, Harry/Astro, Kian adulto–bebê, dungeon completa, Ymir/Beatriz, Hermione/selo, Nairóbi/favor, últimos estados de todos; verificar NPCs/organizações/planos; reavaliar 40 PS e 39 CRIT, confrontar 19 ARC; validar todas as aprovações e produzir base temporal/pontes e parecer de prontidão. Registrar cobertura por intervalos e evidência, sem classificar lacuna como irrecuperável após uma busca curta.

**Prontidão provisória: NÃO APTO para encerrar esta auditoria e liberar a construção histórica global.** O checkpoint não encontrou corrupção do corpus. Faltam verificações semânticas previstas no pedido, não decisões criativas imediatas do autor. Não se recomenda ainda escolher guerras, ascensões ou núcleos definitivos; a ordem acima é de investigação documental. Documentos C–E permanecem por produzir após análise, em vez de repetir a auditoria antiga como se fosse uma nova conferência integral.

## Continuação B002.1 — checkpoint publicado, lote em andamento

C acumulada: **4.542 IDs distintas**, das quais 4.105 novas neste checkpoint; 17 revisitas de B001 sem dupla contagem. Principal 4.384/89.155; poderes 158/158; cobertura combinada 5.085486%. D acumulada 3.973 (4.448401%), conservadora e separada. A/B permanecem concluídas; C/D parciais.

[Relatório B002.1, intervalos e matrizes](26-Auditoria-B002-Continuidades-e-Varredura.md); [ledger](auditoria-fontes/triagem-B002.json); [cobertura por todas as fontes](auditoria-fontes/cobertura-acumulada.json); [plano sistemático](auditoria-fontes/plano-varredura.json). Números/tabela B001 acima permanecem históricos, não representam a cobertura atual.

Cinco ocorrências OM-003–007: premissa de selo corrigida, experiência materna/divina recuperada, Philip/pesquisa racial incluídos, mercado Submundo delimitado e condição/afeto de Hermione qualificados. Dez PS, onze CRIT anteriores e sete ARC parcialmente investigados; CRIT-040 adicional. Sete protagonistas parcialmente revisados, cinco não iniciados no exame factual amplo; nenhum concluído.

## Ocorrências B002.1

### OM-003 — CASO 4 · importância ALTA

**Formulação anterior:** Rans pede receber selo/auxílio de Feuhs; selo proposto não adquirido.

**Evidência/contexto:** Pedido de remover seus próprios selos à voz que se apresenta como deusa/mãe. Não há execução narrada.

**Fonte e mensagens:** [S003 · 1268024904721367103](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268026920851734598](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268027634508632125](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003).

**Avaliação/confiança:** ALTA na correção factual; insuficiente no efeito.

**Correção/pendência:** Bíblia perfil Rans/ARC-016, PS-038 e auditoria 23 corrigidos; CRIT-040 criado.

### OM-004 — CASO 3 · importância ALTA

**Formulação anterior:** Experiência materna/divina de Rans ausente da síntese; religião reduzida a alusões gerais.

**Evidência/contexto:** Luz, clamores, pressão sobre alma, auréola e voz narrados; autoidentificação como deusa/mãe não prova ontologia universal.

**Fonte e mensagens:** [S003 · 1268012124324495423](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268014702361968735](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268017801680125952](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268023655271501864](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268024014497124485](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003).

**Avaliação/confiança:** ALTA como experiência narrada; identidade INCERTA.

**Correção/pendência:** Acrescentada ao perfil e cosmologia, preservando original e R-C pendente na adaptação.

### OM-005 — CASO 3 · importância ALTA

**Formulação anterior:** Dungeon sintetizada por evacuação, rei goblin e término, sem Philip ou pesquisa racial.

**Evidência/contexto:** Philip Glorian coordena grupo; laboratório conserva estudo de união de raças incompleto e descrição de experiência antiga. NPC pesquisador relata hipóteses; criatura final não identificada por palpite.

**Fonte e mensagens:** [S158 · 1201247314430398575](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1201343623753637968](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1201348863215272056](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1208218569981169665](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1208234996578385950](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158).

**Avaliação/confiança:** ALTA na presença/documento; limitada nas teorias do NPC.

**Correção/pendência:** Perfil de Mulack ampliado com NPC e pesquisa, sem alterar morte contraditória ou sobrevivência adaptada.

### OM-006 — CASO 2 · importância ALTA

**Formulação anterior:** Submundo descrito como natureza não demonstrada, devastação sem delimitação espacial.

**Evidência/contexto:** S008 apresenta mercado negro subterrâneo de Olta, acesso por alçapão e devastação desse espaço; não prova destruição de cidade ou plano inteiro.

**Fonte e mensagens:** [S008 · 1266940783303327875](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008); [S008 · 1267990903079960598](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008); [S008 · 1267995370349396029](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008); [S008 · 1268013849811091457](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008); [S008 · 1268014413290536961](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008); [S008 · 1268018113236963443](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008).

**Avaliação/confiança:** ALTA no local/destruição narrados.

**Correção/pendência:** Geografia, perfil Harry, CONT-020 e ARC-017 delimitados ao mercado local; associação Harry/Astro permanece provável.

### OM-007 — CASO 2 / CASO 5 · importância MÉDIA

**Formulação anterior:** Hermione sintetizada apenas inconsciente/protegida; origem dessa descrição não qualificada.

**Evidência/contexto:** Reencontro e treino mostram afeto/atividade; inconsciência está na ação editada do jogador, sem transição causal ou cura/morte do mestre.

**Fonte e mensagens:** [S003 · 1266925927590531114](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1266930702725812356](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268001974817919078](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003); [S003 · 1268027634508632125](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003).

**Avaliação/confiança:** ALTA nos registros; insuficiente na causa/desfecho.

**Correção/pendência:** Perfil Rans e auditoria 23 recuperam afeto/atividade e qualificam estado; não inventam casamento nem cura.

B002 continua aberto pelos intervalos explicitamente pendentes. B003 está planejado, não executado. Prontidão global provisória NÃO APTO por cobertura insuficiente; decisões criativas protegidas. [Validação deste checkpoint](auditoria-fontes/validacao-B002.json).

## Registro adicional B002.2

OM-001–007 e checkpoints anteriores preservados. Os casos novos distinguem complemento, informação omitida, erro e insuficiência; não apagam contradições ou decisões autorais.

<a id="om-008"></a>

### OM-008 — Colapso e custo de alma

**Classificação:** CASO 2 — complemento documental. **Confiança:** ALTA no relato; INSUFICIENTE para uso.

**Antes, descoberta, impacto e correção:** A Bíblia preservava nome/contexto, mas não explicitava o custo e a ponte preexistente. Berthold atribui a Belphegor uma técnica que consome parte da alma como tijolos, esgota e exige mais energia/força mental do que Ymir possui. Relato de NPC, sem aquisição ou uso demonstrado. Complemento na Bíblia, poderes, PS-026 e PS-037; nenhuma nova cosmologia aprovada.

**Fonte/contexto:** [S023 · 1267291152055537777](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1267291238357536790](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1267292607780884511](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1267292668371931230](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1267292808889237527](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-009"></a>

### OM-009 — STWART LITTLE e Stwart

**Classificação:** CASO 5 — identidade insuficiente. **Confiança:** ALTA nas cenas; INSUFICIENTE na equivalência.

**Antes, descoberta, impacto e correção:** A Bíblia tinha Stwart vivo no ramo de Yakkatsu e não distinguia o nome encontrado no ramo florestal. O mestre narra Ymir matando o prisioneiro STWART LITTLE. Registrados como entradas contextuais distintas até surgir ponte; não se declara morte do companheiro de Yakkatsu nem se refaz seu arco. Complemento de NPCs e ressalva em PS-030; B003 não executado.

**Fonte/contexto:** [S023 · 1250995109940564018](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1250996371771756586](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-010"></a>

### OM-010 — Sexto Sentido: seis e dez metros

**Classificação:** CASO 2 — limite local adicional. **Confiança:** ALTA; causa da diferença INSUFICIENTE.

**Antes, descoberta, impacto e correção:** Bíblia/CRIT-027 limitavam a descrição a seis metros. S023 confirma uso de dez metros e gasto de energia. Mantidas ambas medidas em seus contextos; progressão, erro ou circunstância causadora não explicitados. Corrigidos poderes/CRIT-027, PS-037 mantém escalas abertas.

**Fonte/contexto:** [S001 · 1249503535641526303](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001); [S023 · 1253510297570775060](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1253510981565550622](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-011"></a>

### OM-011 — Azazel: mente, ilusão e último estado

**Classificação:** CASO 4 — erros factuais corrigidos. **Confiança:** ALTA.

**Antes, descoberta, impacto e correção:** A síntese atribuía morte ilusória a Westia, dizia que a mente de Kian ainda não voltou, inventava sono final de Azazel e chamava absorção da ave de núcleo. O mestre mantém a mente de Kian com conhecimento limitado; a cabeça de Azazel aparentemente explode antes da ilusão de Westia; absorção por contato não menciona núcleo; a velha dorme e Azazel observa a casa. Correções em CONT-017, perfil, ARC-015, panorama/retificações, CRIT-026, índice e bases factuais dos documentos adaptados 02/15/19. Direções e DD não alterados.

**Fonte/contexto:** [S013 · 1253899431401492600](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1256055535262765096](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1256055716578590780](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1264741025797246987](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1267992776528625697](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1267992861354229760](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-012"></a>

### OM-012 — Null, All e DeHe

**Classificação:** CASO 2 — definição e retificação recuperadas. **Confiança:** ALTA na formulação; interpretação de Null ABERTA.

**Antes, descoberta, impacto e correção:** A tabela citava Null e ressalva literal, sem separar claramente supressão, detecção e fortalecimento. Livros descrevem Null/All; a palavra desativado gera ambiguidade conservada. Mestre distingue DeHe fortalecimento por reconstrução e a linha de regeneração. Complemento nos poderes; sem braço regenerado ou magia universal por memorização.

**Fonte/contexto:** [S023 · 1264755017882275860](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264755398020300892](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264756113216241755](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1265110015639814347](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1265822830906572912](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-013"></a>

### OM-013 — Livros da Casa Coratayne

**Classificação:** CASO 3 — informação histórica omitida. **Confiança:** ALTA no conteúdo dos livros; MEDIANA como história objetiva.

**Antes, descoberta, impacto e correção:** CONT-020 citava datas históricas sem os acontecimentos principais. Recuperados 507/Kerteós/portal/Polã, 610/sucessão de Draconia, 629/isolamento élfico, 635 e 680/influência/queda de Hebe. Tabela atribuída aos livros, sem fixar ano atual, conciliar versões ou aprovar eras adaptadas. Complemento na Bíblia e PS-037.

**Fonte/contexto:** [S023 · 1264729987290894417](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264733348517908571](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264733583650717737](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264735034259275869](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264742359690907708](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1264743912321454120](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

<a id="om-014"></a>

### OM-014 — Ymir e Beatriz: esposa e plano de casamento

**Classificação:** CASO 5 — cronologia conjugal insuficiente. **Confiança:** ALTA nas falas e informação autoral; cronologia ABERTA.

**Antes, descoberta, impacto e correção:** CONT-020 dizia categoricamente que Beatriz não era casada. S002 usa minha esposa e vontade de despertá-la; julho contém casamento futuro em diálogo/metajogo. A informação autoral de esposa é confirmada, mas não há cerimônia/data que concilie as cenas. Corrigida negação absoluta e mantida lacuna cronológica, sem retrocriar casamento.

**Fonte/contexto:** [S002 · 1246295509371457588](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002); [S002 · 1246644820898877471](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002); [S023 · 1265841931104026769](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023); [S023 · 1265842000763031623](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023). Intervalos e limites em [B002.2](26-Auditoria-B002-Continuidades-e-Varredura.md#checkpoint-b002-2).

**COR-E01 — revisão editorial, sem descoberta narrativa:** ARC-014 passa a “Yakkatsu e busca por sair do Inferno”; removida somente a cópia idêntica do bloco de evidências nessa seção. ID, links e ausência de saída consumada preservados.

**Reconciliação adicional de OM-003/004/007:** a base factual do documento 12 ainda atribuía pedido de ajuda/selo a Feuhs. Corrigida para a experiência com voz materna/divina e pedido de remoção dos próprios selos; execução não demonstrada. A referência a selo aplicado foi substituída por remoção. Não é nova cena/OM, mas propagação da correção antiga à proposta correspondente. [S003 · 1268024904721367103](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003).

<a id="registro-b002-3"></a>

## Registro adicional B002.3

<a id="om-015"></a>

### OM-015 — Agente da prisão de Ymir

**Impacto:** CORREÇÃO FACTUAL NECESSÁRIA. **Confiança:** alta nos resultados e nas falas como falas; insuficiente nas causas não recuperadas.

**Antes, descoberta e correção:** CONT-014 atribuía à Árvore a jaula e entrega aos Altruístas. A fonte descreve moradores em cidade nas árvores e homem que decreta escravidão; a Árvore Rainha posteriormente diz não conhecer Nefa/Altruístas. Corrigida atribuição, sem concluir que todas as cenas eram sonho.

**Fonte/contexto:** [S005 · 1229625869576962089](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1229626189757288509](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1229638202130960454](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1229638718202314802](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1229638997425524736](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1229937418921054249](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1232096882164236392](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1232099473002332160](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1232100505891639337](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005). [Intervalos e limites](27-Auditoria-B002-3-Fechamento-e-Qualidade.md).

<a id="om-016"></a>

### OM-016 — Nefa, Balenon e custos da caçada

**Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO. **Confiança:** alta nos resultados e nas falas como falas; insuficiente nas causas não recuperadas.

**Antes, descoberta e correção:** A Bíblia resumia traição/treino sem motivação e contraponto moral suficientes. Nefa justifica entregar Ymir para proteger aldeia; sua privacidade/recusas são demonstradas. Balenon questiona luta interminável; encontro com criança não é cura automática. Metade dos doze de Coleros morre; última pergunta sobre Nefa não tem resolução. Recuperados detalhes, sem destino inventado ou calendário universal.

**Fonte/contexto:** [S005 · 1230128027409584268](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1231394174729982062](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1231401197731184771](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239084143598370990](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239088690962235493](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239088709748391968](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239297436933947442](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239302970827341914](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239341038569652254](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005); [S005 · 1239342848562692169](../pesquisa/fase-3/Fontes-e-Evidencias.md#s005). [Intervalos e limites](27-Auditoria-B002-3-Fechamento-e-Qualidade.md).

<a id="om-017"></a>

### OM-017 — Limites da sombra adulta de Kian

**Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO. **Confiança:** alta nos resultados e nas falas como falas; insuficiente nas causas não recuperadas.

**Antes, descoberta e correção:** Perfil tratava poderes genericamente sem servidão versus união e retirada impossível de sombra viva. Sombra própria custa força; galinha morta submete-se e transporta Kian. Elemento ainda não definido; lapso Ymir não muda protagonista. Acrescentado complemento com espada persistente após despertar, sem fechar adulto–bebê.

**Fonte/contexto:** [S184 · 1235315352720642159](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1235337655672111174](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1235338598811697244](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1235751034643812483](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1236130301084831764](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1236832133784539236](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1236832690473271387](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1236838310249500773](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1237183069585145908](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1237183703915036723](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1237197270206779554](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1237198222175502386](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184); [S184 · 1237198913648328826](../pesquisa/fase-3/Fontes-e-Evidencias.md#s184). [Intervalos e limites](27-Auditoria-B002-3-Fechamento-e-Qualidade.md).

<a id="om-018"></a>

### OM-018 — Mulack, Driade e preparação delimitada

**Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO. **Confiança:** alta nos resultados e nas falas como falas; insuficiente nas causas não recuperadas.

**Antes, descoberta e correção:** Flor de Neve/armadura e expedição já constavam, mas faltavam homenagem ao frio de Mouran, espécie de Nyxis desconhecida, seleção de dez companheiros A+B e limite corporal/circulação. Driade Fistine é nome, não raça; negociar servidão não comprova selo. Elemento não repele mana. Complementados preparação e limites, sem nova solução da contradição.

**Fonte/contexto:** [S158 · 1199907745139273849](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1199910418072743986](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200267273198370856](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200273843000971356](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200508845991137352](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200585040766177381](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200586227448033401](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200678512223322132](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200678747788030032](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200679111094456350](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200680701712941186](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200949573078757537](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158); [S158 · 1200949796932956321](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158). [Intervalos e limites](27-Auditoria-B002-3-Fechamento-e-Qualidade.md).

<a id="om-019"></a>

### OM-019 — Ramos de Stark e Richard

**Impacto:** AJUSTE DE INTERPRETAÇÃO RECOMENDADO. **Confiança:** alta nos resultados e nas falas como falas; insuficiente nas causas não recuperadas.

**Antes, descoberta e correção:** Apoios eram apenas enumerados. Recuperado encontro de Stark com Emma e carona oferecida; sem unificar menina à filha de Lilith. Richard constrói, recebe aviso de Maya, mata lobo e encontra orbe; melhora física é narrada depois do gás, sem mecanismo completo. Maya morreu é OOC; Cot/Cop não unificado ao lobo. Último grunhido e projeto de arma continuam abertos.

**Fonte/contexto:** [S004 · 1264366352353984554](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004); [S004 · 1264366386701008967](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004); [S004 · 1264374090811052063](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004); [S004 · 1264374501576282245](../pesquisa/fase-3/Fontes-e-Evidencias.md#s004); [S010 · 1244446541968838778](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1244449778620694538](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1245912806469931051](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1245922295810228315](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246280393515208757](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246667764836470866](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246667765176078458](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246915249890656276](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246919793823453274](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246938115763998772](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1246996868161081395](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1247006701199167626](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010); [S010 · 1250963275642830868](../pesquisa/fase-3/Fontes-e-Evidencias.md#s010). [Intervalos e limites](27-Auditoria-B002-3-Fechamento-e-Qualidade.md).

**QA-E02:** Q10/S155479: corrigido rótulo amplo de contexto de ação/fala para mensagem auxiliar sem conteúdo ficcional. Ledger B001 preservado; correção aditiva em qualidade-B002.3.json, sem remover C/D ou mudar fato.
