# Omissões, descobertas e correções — checkpoint B001

Auditoria independente de Dragons · 10/10/2026 · Etapa B iniciada, sem encerramento global.

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
