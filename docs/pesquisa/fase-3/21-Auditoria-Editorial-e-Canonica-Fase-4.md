# Auditoria editorial e canônica da Fase 4

09/10/2026 · Edição auditada: Revisão 1 · Correções propostas: Revisão 2

## Parecer

A edição publicada precisava de correções antes de servir como fundamento editorial do novo jogo. A estrutura geral, os 12 protagonistas, os 19 arcos, as 40 pendências e a separação entre cânone original e adaptação estavam presentes. Entretanto, havia sínteses excessivamente curtas, referências sem contexto suficiente, datas incompletas, contradições omitidas e uma atribuição não demonstrada de função a God.

A Revisão 2 corrige esses problemas nos documentos existentes. Com essas correções, a Bíblia oferece uma entrada suficiente para compreender a história **recuperável**: origem do grupo, conflitos, dispersão, percursos individuais e últimos estados conhecidos. Ela permanece acompanhada do índice, da matriz e das fontes para consultas e decisões controversas. Não representa uma história integral com todos os mecanismos explicados ou um final recuperado. Sua aprovação editorial não transforma lacunas em respostas.

Este parecer se refere à Revisão 2 proposta em branch própria. A edição em `main` só incorpora essas correções quando o novo PR for revisado e mesclado. A auditoria não iniciou adaptação, continuação ou Fase 5.

## Base, método e limites

- O [PR #1](https://github.com/DivineJeff/Lore-Dragons/pull/1) estava fechado e **mesclado**, com merge em 09/10/2026 às 18:49:48 UTC. A base auditada de `main` é o commit `96398a99da1f5781c1c7e1e4d1dc02990d3eafae`, árvore `461d9a1d3182d6bbae91f2b31a99f94af1209d7c`.
- A árvore do merge coincide com a árvore publicada da Fase 4. Antes das correções, os 15 arquivos da cópia local conferiam com seus blobs remotos: sete documentos Markdown e oito ZIPs originais.
- Foram examinados os documentos publicados, os requisitos do pedido original e suas correções posteriores, e a consolidação final da Fase 3: cronologia, eventos, perfis, últimos estados, arcos, pendências, poderes e fontes. As instruções posteriores que definem a Bíblia como entrega da Fase 4 prevalecem sobre a numeração inicial das fases.
- Na edição recebida, 478 IDs únicos citados foram conferidos quanto à existência e correspondência de fonte. Essa verificação técnica não é validação automática da interpretação. Afirmações críticas, discrepâncias e complementos foram confrontados com as mensagens originais e seu contexto, distinguindo ação do jogador, resultado do mestre, diálogo, mecânica, OOC e confirmação externa.
- Os 214 localizadores de fonte foram conferidos diretamente nos ZIPs: 202 exportações narrativas e 12 fontes de poderes. Cada entrada foi vinculada ao ordinal e ao SHA-256 do HTML. A base narrativa conserva 89.155 mensagens; a base de poderes, 158. Das exportações narrativas, 16 estão vazias.
- Esta auditoria **não refez uma leitura sequencial das 89.155 mensagens**. Ela revisou a síntese integral e a consolidação, com retorno dirigido às evidências. Não é possível garantir recuperação de conteúdo apagado, canais não exportados ou uma informação que não tenha sido incorporada à investigação. Não foi descoberto material externo que complete esses limites.

## Resultado dos oito critérios

| Critério | Situação da edição recebida | Resultado da revisão |
| --- | --- | --- |
| 1. Doze protagonistas | Todos presentes, mas vários percursos posteriores ficavam dispersos; God ainda tinha frase de checkpoint. | Todos conservados e ampliados com desenvolvimento, consequências, limites e evidências. A profundidade acompanha a disponibilidade de material. |
| 2. Cronologia, causas e arcos | Espinha dorsal preservada; ramos sobrepostos podiam parecer uma sequência única; alguns intervalos terminavam antes dos eventos descritos. | Guia de causalidade, distinção dos ramos paralelos, datas corrigidas e consequências concretas nos arcos posteriores. |
| 3. NPCs, mundo, organizações, poderes e itens | Categorias existentes, com omissões relevantes e enquadramentos ambíguos. | Apoios e antagonistas complementados; regiões e organizações distinguidas; capacidades e objetos contextualizados. |
| 4. Informação da Fase 3 omitida | Cura leve de Yakkatsu, Previsão de Ymir, disputa de Natureza de Kian e contextos pessoais estavam insuficientes. | Informação recuperada inserida nas seções existentes, sem substituir a investigação nem criar episódios. |
| 5. Hipótese promovida a fato | Função de God, força probatória da marca de Henry e autoria do abate da besta precisavam de correção. | Afirmações delimitadas pela natureza da fonte; autoria exclusiva do abate permanece provável. |
| 6. Contradições e lacunas | As 40 pendências existiam, mas divergências importantes não estavam igualmente visíveis. | Pendências preservadas; dez novos pontos críticos acrescentados. Nomes diferentes de cultos deixam de ser tratados, por si só, como contradição comprovada. |
| 7. Referências e acesso | IDs e metadados existiam; faltava um procedimento público preciso para encontrar cada HTML original. | Ligações aos ZIPs, ordinal da entrada, hash e instrução de busca do ID no HTML. Âncoras de continuidade adicionadas ao índice. |
| 8. Compreensão sem ler a transcrição | Visão geral possível, com lacunas editoriais nos percursos e transições. | Aprovada para compreender a história recuperável com Bíblia, índice e matriz. Não aprovada como explicação completa da cosmologia ou encerramento da campanha. |

## Avaliação dos protagonistas

Os perfis mantêm identidade, comportamento demonstrado, percurso, relações, poderes, conflitos, último estado e questões abertas. As diferenças de extensão refletem a evidência disponível; personagens com interrupção documental não receberam acontecimentos inventados para equilibrar o tamanho.

| Protagonista | Complemento e avaliação | Limite preservado |
| --- | --- | --- |
| [Michael Uchiyama](../../canon-original/17-Biblia-Canon-Original.md#personagem-01) | Reconstrução, diplomacia, aprendizado e campanha de Mytria articulados ao percurso coletivo. | Campanha em andamento; último estado não é destino final. |
| [Rans](../../canon-original/17-Biblia-Canon-Original.md#personagem-02) | Sobrevivência individual separada do reencontro público; desenvolvimento com Akai e Hermione conectado. | Local final depende de continuidade local; não transportar acompanhantes sem evidência. |
| [Henry Chambers](../../canon-original/17-Biblia-Canon-Original.md#personagem-03) | Crises lunares, altares, morte e reaparição distinguem evento de causa desconhecida. | Retorno à vida e trecho de canal vazio sem mecanismo recuperado; marca sem remoção comprovada. |
| [God-Zilla](../../canon-original/17-Biblia-Canon-Original.md#personagem-04) | Teleporte, combate, reencontro com Lúcifer, auxílio à Árvore, colar e caça reunidos; checkpoint removido. | Nenhuma nomeação formal como guardião; presença posterior escassa não prova abandono ou morte. |
| [Harry Phils](../../canon-original/17-Biblia-Canon-Original.md#personagem-05) | Bytes, hospital, ascensão política, pacto, Zaraph, Zex e combate final dão profundidade além do ramo Astro. | Astro permanece associação provável; corpo usado e personalidade não recebem mecanismo inventado. |
| [Kian / Lúcifer / Azazel](../../canon-original/17-Biblia-Canon-Original.md#personagem-06) | Estudo, marca, mana invertida, limitações, Natureza e infância de Azazel ligados à confirmação externa de continuidade. | Continuidade pessoal confirmada externamente; transformação adulto–bebê e divergência de elemento não resolvidas. |
| [Lilith Chipper](../../canon-original/17-Biblia-Canon-Original.md#personagem-07) | Culto inicial, Hads, restauração, coroação e Emma organizados como percurso. | Relações entre cultos e destino após a última cena permanecem abertos. |
| [Bytes Sky](../../canon-original/17-Biblia-Canon-Original.md#personagem-08) | Aprendizado, vínculos com Yakkatsu e Nairóbi, deslocamentos e encontro com Gut explicitados. | Toque na esfera e busca pretendida não são resultado concluído. |
| [EREN](../../canon-original/17-Biblia-Canon-Original.md#personagem-09) | Crise corporal, alegação de príncipe, deslocamentos e último passeio recebem continuidade. | Declaração de título não estabelece legitimidade universal nem cosmologia da Natureza. |
| [Mulack / Jin Mu-Won](../../canon-original/17-Biblia-Canon-Original.md#personagem-10) | Integração, treinamento, dungeon e conflitos do registro descritos sem antecipar a origem relatada. | Morte/memorial versus retificação do último combate permanecem contraditórios. |
| [Yakkatsu](../../canon-original/17-Biblia-Canon-Original.md#personagem-11) | Claws, cura leve, correção de elemento, Bardock, Stwart e culpa no Inferno acrescentados. | Cura leve não é regeneração de membros; saída do Inferno não recuperada. |
| [Ymir Realmheart / Note](../../canon-original/17-Biblia-Canon-Original.md#personagem-12) | Note anterior à máscara preservado; Beatriz, captura, missão e Previsão articulados. | Persona não é transformação mágica; resgate da irmã e chegada a Milena não concluídos. |

## Problemas encontrados e correções

### A01 — Atribuição indevida de função a God

A fala de apresentação identifica **a Árvore** como guardiã de Mouran. O pedido a God é ajuda a um amigo, seguido de transporte pelo galho. Outro pedido coletivo de proteção aparece em diálogo com Henry e Gwierlan. A síntese misturava essas cenas. Foram corrigidos cronologia, perfil, relações e CRIT-017. Ver [contexto de apoio](../../canon-original/17-Biblia-Canon-Original.md#relacoes) e [CRIT-017](../../canon-original/19-Matriz-Canon-Critico.md#crit-017--god-auxílio-à-árvore-e-última-caçada).

### A02 — Força da evidência: marca, besta e terceiro altar

A marca tem confirmação narrada em 3 de janeiro; a referência de 20 de janeiro é fala de Henry. A besta sofre corte na cabeça narrado pelo mestre, mas o reconhecimento explícito de morte usado anteriormente vinha de comentário OOC. A morte reconhecida na continuidade não confirma, com a mesma força, autoria exclusiva de Henry. O terceiro altar é atribuído no planejamento; a referência usada como execução não demonstra destruição. Foram delimitadas as afirmações em cronologia, objetos, arcos e matriz. Ver CRIT-010, CRIT-011, CRIT-014, PS-002 e PS-016 na [matriz](../../canon-original/19-Matriz-Canon-Critico.md).

### A03 — Datas e ordem causal

CONT-002 passa a abranger 20–21 de janeiro e a correção posterior do nome Nyxis. CONT-013 inclui 15 de abril na chegada à Paróquia e 16 de abril na explosão. CONT-014 chega a 23 de abril; CONT-015, a 5 de maio. CONT-018 explicita o antecedente de Balenon de 12 de maio; CONT-019 começa em 7 de junho. A coroa quebrada antecede a recitação do ritual de Patrick. O guia inicial explica que os ramos não compõem um calendário ficcional global conciliado. Ver [cronologia](../../canon-original/17-Biblia-Canon-Original.md#historia).

### A04 — Profundidade editorial e resíduos de checkpoint

Foram retiradas orientações obsoletas de leitura futura, e não evidências. Os 12 perfis ganharam desenvolvimento posterior contextualizado. ARC-010 a ARC-019 passaram a explicitar participantes, conflito e consequências em lugar de remissões genéricas. PS-020 a PS-040 receberam perguntas e envolvidos efetivos, evitando repetir o título como conteúdo. Identificadores e limites históricos foram conservados.

### A05 — Omissões de apoio, poderes, crenças e objetos

Entraram contextos de Ana, Karl/Elra/Ellen, Redner, Claws, Doutor, Zaraph, Valmount, Jakaw, Caeman, Froid, Powl, Tamura, Myria, Tengetsu, Ceifador, Mont e Ground. Organizações Magnatas e Miliart foram distinguidas de regiões; cidades dos lagartos, animais e Cloudgate não foram fundidas automaticamente. Draconia continua relato situado; invocação de Ária com cura não prova aparição divina. O velho do laboratório não recebeu a identidade não demonstrada de “Niin”.

Previsão de Ymir, cura leve de Yakkatsu e disputa de Natureza de Kian ganharam tratamento explícito sem alterar as 18 entradas oriundas das fichas de poderes. A retirada de Gravidade de Yakkatsu agora é sustentada pela correção direta, distinguindo crença do personagem de concessão de elemento. Orbe de linhas, reconstrução por Terra, sombras atribuídas por Yoran e negadas por Fierch, anel de Ana e papel ZEYROC foram contextualizados sem funções novas.

### A06 — Contradições insuficientemente visíveis

A matriz passou de 29 para 39 pontos críticos. CRIT-030 a CRIT-039 registram: Natureza de Kian; relatos de Ceifador/Tengetsu; sombras do orbe; Previsão; troca Henry/Harry em enunciado; ajuste de crescimento lunar; comentário de outro RPG associado a Lilith; intervenção inválida no personagem de Harry; Ária/Draconia e natureza de seus relatos; falsa morte antiga de Mulack corrigida para braço quebrado, separada da ruptura posterior.

As 40 pendências permanecem. PS-036 foi refinada: nomes distintos de cultos não provam relação nem contradição. Não houve escolha arbitrária de uma versão para fechar Natureza de Kian, Ceifador, Mulack, altares, Fallhebe ou o orbe. Ver [matriz crítica](../../canon-original/19-Matriz-Canon-Critico.md).

### A07 — Referências localizáveis

Os IDs existentes eram corretos como identificadores, mas sua localização exigia conhecer a investigação local. O [registro de fontes](Fontes-e-Evidencias.md) agora aponta ZIP, ordinal da entrada e hash de cada HTML, com instruções para localizar a mensagem e ler contexto. O [índice](../../canon-original/18-Indice-Rapido-Canon.md) inclui os 20 blocos de continuidade. Nenhuma transcrição adicional foi publicada.

## Integridade e controle de mudanças

A auditoria preserva os oito ZIPs originais e os arquivos de investigação da Fase 3. O diff proposto altera seis Markdown existentes e acrescenta este relatório; os três documentos principais são revisados no lugar. Os IDs de protagonistas, poderes, arcos e pendências continuam utilizáveis. O espaço do cânone adaptado permanece sem alteração.

As verificações de entrega incluem destinos de links e âncoras, existência e correspondência das mensagens citadas, ordinais e hashes dos 214 HTMLs, igualdade dos blobs dos ZIPs com a base, preservação dos identificadores e ausência de caminhos locais ou contatos nos documentos publicados. O commit remoto, a árvore resultante, o estado do novo PR e a permanência de `main` na base são conferidos após publicação. O recibo de entrega registra essa conferência posterior separadamente deste parecer.

## Pendências e uso autorizado desta edição

Permanecem sem resolução documental o mecanismo do retorno de Henry, a transformação Kian–Azazel, o conflito sobre Mulack, a associação completa Harry–Astro, execução individual dos altares, relação entre cultos, causas integrais de curas e ilusões, reparo de Zex, efeito da esfera de Bytes, resgate da irmã de Beatriz e vários destinos após as últimas cenas. A saída de Henry para exportação vazia e a ausência de encerramento da campanha continuam limites explícitos.

A última cena recuperável é Ymir e Beatriz na cidade dos elfos, em 31/07/2024, seguida de fim da sessão. Não é o final ficcional dos demais personagens. A Bíblia revisada pode fundamentar decisões futuras sobre a história original, desde que cada questão controvertida continue vinculada à matriz e que qualquer solução criada futuramente seja identificada como adaptação. Esta auditoria não produziu essas soluções.
