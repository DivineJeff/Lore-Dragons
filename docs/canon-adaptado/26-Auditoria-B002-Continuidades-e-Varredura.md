# Auditoria B002 — continuidades e varredura sistemática

<a id="checkpoint-b002-2"></a>

## Checkpoint B002.2 — confronto concluído nos intervalos, B002 ainda parcial

Base verificada: main `9973184d9770e3add3acea04e02563b7dbad6649`, PR #16 mesclado; branch própria `lore/auditoria-b002-2-confronto`. Esta seção é o estado atual; o relatório B002.1 abaixo é histórico e conserva seus contadores/pendências da época. A/B concluídas, C/D do corpus parciais. Nenhuma decisão DD, adaptação definitiva ou B003 executado.

### Cobertura e denominadores

| Métrica | B002.1 | B002.2 atual |
| --- | --- | --- |
| Corpus principal + poderes | 89.155 + 158 | 89.155 + 158 = 89.313 |
| C acumulada por união de IDs | 4.542 | 10,431 |
| D acumulada por união de IDs | 3.973 | 10,431 |
| C sem D | 569 | 0 |
| Principais ainda sem C | 84.771 | 78,882 |
| Trajetórias integralmente revistas | 0 | 0 |

Nesta rodada: **5,889 novas C**, **574 revisitas distintas**, **6,458 novas D** (incluem as 569 antigas C sem D). Total efetivamente lido/confrontado: 6,463 IDs distintas. Os 41 acessos repetidos de S023 205–245 recuperaram uma saída truncada, sem acréscimo; validação posterior de citações também não acrescenta cobertura. **Zero mensagens com conteúdo parcialmente lido nos intervalos declarados**, após recuperação; isto não elimina lacunas ficcionais ou partes de fontes não examinadas. C/D atual 11.679151% do total; principal 11.522629%. 158 poderes continuam cobertos por B001, sem reinício.

[Ledger adicional: todas as IDs, hashes, índices, disposições e D](auditoria-fontes/triagem-B002.2.json). B001, B002.1 e respectivas validações preservados byte a byte. [Acumulado](auditoria-fontes/cobertura-acumulada.json), [plano](auditoria-fontes/plano-varredura.json), [matrizes](auditoria-fontes/matrizes-revisao.json), [validação](auditoria-fontes/validacao-B002.2.json).

### Intervalos realmente examinados

Índices base zero, extremos inclusivos. J01–J06 identificam precisamente as 569 antigas C sem D; J07 é fronteira já revisada. Os demais são novas leituras. A avaliação contextual de cada intervalo explicita acontecimentos, tentativas, NPCs, retificações, metajogo e disposição documental. Não houve releitura de S008 ou reinício dos trechos concluídos.

| Intervalo | Fonte | Índices inclusivos | IDs lidas | Frente | Documentos confrontados |
| --- | --- | --- | --- | --- | --- |
| J01 | [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | 176–260 | 85 | revisita C sem D | CONT-019, Henry, Michael, PS-023 |
| J02 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 148–230 | 83 | revisita C sem D | CONT-017, Kian, ARC-015 |
| J03 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 820–862 | 43 | revisita C sem D | CONT-020, Ymir, OM-014 |
| J04 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 904–1020 | 117 | revisita C sem D | CONT-020, Henry, Ymir |
| J05 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 1070–1249 | 180 | revisita C sem D | CONT-020, PS-026, PS-036, OM-008 |
| J06 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 1339–1399 | 61 | revisita C sem D | CONT-020, PS-001, PS-026 |
| J07 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 236–240 | 5 | contexto de fronteira | CONT-018, CRIT-033 |
| J08 | [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | 261–405 | 145 | dirigida | CONT-019, PS-001, PS-023, Henry, Ymir |
| J09 | [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | 406–580 | 175 | dirigida | CONT-019, Henry, Michael |
| J10 | [S161](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161) | 1500–1715 | 216 | dirigida | Harry, CRIT-005, PS-022, CONT-016 |
| J11 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 0–170 | 171 | dirigida | CONT-020, Ymir, Beatriz |
| J12 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 171–340 | 170 | dirigida | CONT-020, NPCs, OM-009 |
| J13 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 341–480 | 140 | dirigida | CONT-020, CRIT-027, OM-010 |
| J14 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 481–650 | 170 | dirigida | CONT-020, CRIT-027, PS-037, OM-012, OM-013 |
| J15 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 651–819 | 169 | dirigida | CONT-020, Ymir, Beatriz, OM-012, OM-014 |
| J16 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 241–450 | 210 | sistemática | CONT-018, Ymir, NPCs |
| J17 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 451–690 | 240 | sistemática | CONT-018, Ymir, CRIT-027 |
| J18 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 691–850 | 160 | sistemática | CONT-018, CRIT-027, CRIT-031, OM-010 |
| J19 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 851–1039 | 189 | sistemática | CONT-018, Ymir, Beatriz |
| J20 | [S182](../pesquisa/fase-3/Fontes-e-Evidencias.md#s182) | 0–210 | 211 | dirigida | Kian, CONT-016, PS-021 |
| J21 | [S182](../pesquisa/fase-3/Fontes-e-Evidencias.md#s182) | 211–393 | 183 | dirigida | Kian, CONT-016, PS-021 |
| J22 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 1700–1940 | 241 | dirigida | Kian, Henry, CONT-016, PS-021 |
| J23 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 2405–2465 | 61 | dirigida | Kian, PS-021, CONT-016 |
| J24 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 231–450 | 220 | dirigida | CONT-017, Kian, ARC-015 |
| J25 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 451–750 | 300 | dirigida | CONT-017, Yalia, Kian |
| J26 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 751–1050 | 300 | dirigida | CONT-017, Kian, organizações |
| J27 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 1051–1350 | 300 | dirigida | CONT-017, Kian, poderes |
| J28 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 1351–1650 | 300 | dirigida | CONT-017, Kian, Emília |
| J29 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 1651–1950 | 300 | dirigida | CONT-017, Kian, OM-011 |
| J30 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 1951–2250 | 300 | dirigida | CONT-017, Kian, NPCs, facções |
| J31 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 2251–2485 | 235 | dirigida | CONT-017, CRIT-026, ARC-015, OM-011 |
| J32 | [S002](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002) | 0–240 | 241 | sistemática | CONT-018, Lilith, Ymir, CRIT-032 |
| J33 | [S002](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002) | 241–500 | 260 | sistemática | CONT-018, Lilith, Ymir, CRIT-032 |
| J34 | [S002](../pesquisa/fase-3/Fontes-e-Evidencias.md#s002) | 501–782 | 282 | sistemática | CONT-018, Lilith, Ymir, PS-039, OM-014 |

### Disposição editorial por intervalo

**J01 — S016 176–260:** Ataque ao acampamento: campo/trapas de Michael são tentativas. Bola de Henry atinge árvore, não aniquila tropas; Michael derruba troncos e o salva. Narração, ações propostas e comentários auxiliares separados. CASO 1: sequência geral documentada; resultado de Henry não ampliado. Limites/IDs de início e fim no ledger.

**J02 — S013 148–230:** Floresta, sombra limitada, ferramentas e lobo: ferimentos e sobrevivência confirmados; caminhada continua. Piadas de Henry/entidades não são intervenção divina. CASO 1, identidade preservada, transição não explicada. Limites/IDs de início e fim no ledger.

**J03 — S023 820–862:** Diálogo conjugal e condição de princesa: casamento tratado como plano neste contexto, sem revogar informação autoral de esposa. Nenhuma cerimônia recuperada. Falas e metajogo não estabelecem cronologia global. Limites/IDs de início e fim no ledger.

**J04 — S023 904–1020:** Henry presente e caminhada ao quarto de Garius. Relato de retorno não explica mecanismo nem nomeia salvador. CASO 1; encontro não realiza resgate da irmã. Limites/IDs de início e fim no ledger.

**J05 — S023 1070–1249:** Morte/luto de Garius e Berthold: Disare e missão diplomática são relatos situados. Rumores sobre órgãos não viram poder adquirido. Colapso usa alma como tijolos de ponte segundo NPC, não ação realizada; Quimera/Deus Demônio não fundidos. OM-008 detalha custo e limites omitidos. Limites/IDs de início e fim no ledger.

**J06 — S023 1339–1399:** Henry chamado rei demônio não comprova soberania. Identificação de Surgência e idade de guitarra são falas locais; piada de 60 mil anos de Rans não entra no calendário. Flauta não convoca Nines neste uso. CASO 1, resultado negativo preservado. Limites/IDs de início e fim no ledger.

**J07 — S001 236–240:** Revisita de cinco IDs da entrada na torre para interpretar a fuga posterior; abrigo narrado, sem morte do atirador. Não aumenta C ou D. Limites/IDs de início e fim no ledger.

**J08 — S016 261–405:** Batalha termina localmente. Michael cogita usurpar liderança; não obtém reino. Mestre retifica Lucas: chega separadamente, não acompanhou Ymir. Vermund descreve Surgência como filhos da terra e maldição; testemunho NPC sem mecanismo universal. Espada luminosa de Lucas falha; falta de memória anterior ao despertar não é memória completa. Limites/IDs de início e fim no ledger.

**J09 — S016 406–580:** Henry fere Lucas e depois o cura; chuva de formigas/perda de consciência são narradas, agente não identificado. Prisioneiros e convite de Henry à ferraria; aprendizagem não concluída. Michael abandona plano de armadilhas; atacantes ainda chegam e partida não se conclui. Piadas Dani/dez anos/evento canônico não criam NPC, calendário ou causa divina. Limites/IDs de início e fim no ledger.

**J10 — S161 1500–1715:** Harry nominal ajuda cura e coordena Zex/civis; mestre considera ações feitas. Flecha abdominal retirada por Zex e limite de cura com mana específico. Sem Astro ou ponte de corpo neste recorte final. Henry inconsciente e efeito do vento não são transformação nova. Personalidade/nominalidade confirmadas aqui; vínculo pessoal Harry–Astro provável por S008 anterior, memória e ponte corporal insuficientes. Limites/IDs de início e fim no ledger.

**J11 — S023 0–170:** Vermund revela projeto Solus de bombardear Piferme, sem execução. Ferimento das asas de Kral e tentativa de cura excessiva de Ymir não demonstram restauração completa. Fala de exterminar fadas e relatos de morte de pelotões são ações/relatos, não regra universal ou fusão da floresta com Myria pessoa. Limites/IDs de início e fim no ledger.

**J12 — S023 171–340:** Floresta, prisioneiro STWART LITTLE e execução de pescoço pelo mestre; nenhuma ponte com Stwart do Inferno de Yakkatsu. Infiltração da fortaleza e disparos: pedidos de cura total e matar todos não substituem resultados. CASO 5 por homônimo que exige documentação separada. Limites/IDs de início e fim no ledger.

**J13 — S023 341–480:** Ymir mata adversários da sala e foge do bombardeio, permanece ferido. Scroll Froid/rei dos mares não concede todas técnicas. Mestre confirma Sexto Sentido 10 m com gasto de energia. Tentar criar ar da água falha; desmaio antecede despertar enfaixado na Casa Coratayne. Rans aparece no jardim. Recuperação não restaura braço. Limites/IDs de início e fim no ledger.

**J14 — S023 481–650:** Limia atribui resgate a Garius, administrador da casa/ministro de Polã. Livros registram datas/eventos históricos com perspectiva da fonte, não ano atual. Magias 9–0 e custos/anos não significam aprendizado pleno. Null/All e fortalecimento DeHe requerem explicação literal. Beatriz reencontra Ymir, relata despertar na Árvore da Vida e procura por ele. Objetivos pessoais e memória parcial preservados. Limites/IDs de início e fim no ledger.

**J15 — S023 651–819:** Pernas de Beatriz perfeitas; braço de Ymir ausente. Ela diz ontem enquanto ele conta semanas, sem calendário conciliado. Mestre retifica DeHe como fortalecimento por reconstruir fibras; regeneração é outra linha. Nove livros memorizados, não biblioteca inteira. Afeto/beijo e casamento oferecido em metajogo não são cerimônia ou conjunção cronológica demonstrada. Limites/IDs de início e fim no ledger.

**J16 — S001 241–450:** Fuga da torre e cartazes de missões; gangue retirada por mal-entendido, sem missão concluída. Quémero nomeado sem posto de comandante confirmado. Cidade de animais, Powl/Froid, combate com canguru e compra de manoplas. Plano de desmontar organização e hipérbole de meio universo não são vitórias realizadas. Resgate iniciado no ataque de aves. Limites/IDs de início e fim no ledger.

**J17 — S001 451–690:** Resgate da menina aceito e Ceifador lançado por golpe, não decapitado por ação unilateral. Cura alivia mulher, mas ela depois morre; Tamura e treino com Froid seguem. MUTON 31; nove técnicas de água descritas não são todas adquiridas. Conversão mana/água tem demonstrações locais e desgaste. Limites/IDs de início e fim no ledger.

**J18 — S001 691–850:** Treino produz doze litros e fadiga; não supera Froid por afirmação do jogador. Tengetsu nomeado, notícias de governador e assassinatos permanecem relatos. Myria é pessoa, distinta de região. Sexto Sentido desperta em seis metros e exige energia, com hemorragia. Pedidos de cura/controle coletivo não executam automaticamente. Limites/IDs de início e fim no ledger.

**J19 — S001 851–1039:** Ajuda de Powl/Froid e raízes de Myria; cura de Ymir falha antes de posterior extração de bala e auxílio Tamura. Beatriz impostora pede amputação que Ymir não executa; demoníaca revelação/morte não atinge a verdadeira Beatriz em coma. Retorno corrigido de três horas para quarenta minutos, sem regra global. Nostalgia final OOC não continua história. Limites/IDs de início e fim no ledger.

**J20 — S182 0–210:** Lúcifer estuda e adapta energia, marca abdominal; pedidos de dominar armas não concedem tudo. Encontra God/Michael, estuda energia inversa, testa esfera e sofre exaustão. Ruínas/sobreviventes de Mouran; elevador atinge carro de Henry. Não é viagem dimensional nem novo rei estabelecido. Limites/IDs de início e fim no ledger.

**J21 — S182 211–393:** Relatos de fome e inflação em Mouran. Gwierlan usa rei do inferno ironicamente, e cidade infernal como metáfora. Cura de terra falha. Mestre alterna Kian/Lúcifer na mesma sequência ao chegar à Árvore, receber equipamento e lutar. Armas simples autorizadas, armas complexas recusadas. Velho não identificado como Edward por hipótese OOC. Retorno final é intenção. Limites/IDs de início e fim no ledger.

**J22 — S187 1700–1940:** Kian aparece adulto no palácio com Henry/Michael/Lilith; galinha de sombras tem alcance de 30 m e retorna ao usuário. Cura Travessa cancelada antes da cura de Henry. Transporte no pássaro coletivo e proximidade do castelo destruído narrados. Recordação fragmentária de castelo no céu não é memória total. Incidentes de Bytes/Nai e exageros auxiliares não encerram seus arcos. Limites/IDs de início e fim no ledger.

**J23 — S187 2405–2465:** Contexto de luta com Edward e comentários de jogador sobre morrer/flecha de fogo: metajogo não demonstra morte corporal de Kian nem explica adulto–bebê. Comparação com morte de Henry no trecho já auditado não funde resultados. CASO 1: lacuna conservada. Limites/IDs de início e fim no ledger.

**J24 — S013 231–450:** Azazel deixa floresta, nomeia-se, chega com Galius ao subterrâneo de Tékia. Flecha é descrita como mana; Galius morto e absorção involuntária do cérebro são narrados, não todo poder controlado. Desmaio, sangue e choro não recuperam todas memórias anteriores. Abismo do Paraíso é designação da cidade subterrânea, sem plano Inferno confirmado. Limites/IDs de início e fim no ledger.

**J25 — S013 451–750:** Yalia acolhe; agressores batidos fogem. Cura Travessa apodrece carne e restaura com limitações; flashback da absorção não é nova morte. Trabalho/feira e engano por velho de cinco dracos; salto e agressor ainda gemendo não são morte neste primeiro golpe. Vulnerabilidade não equivale a divindade. Limites/IDs de início e fim no ledger.

**J26 — S013 751–1050:** Morte do agressor por esmagamento e energia esgotada. Brown oferece trabalho; servidor confunde Kian e pede desculpas. Contrato dos Magnatas não unifica todas facções. Miliart impõe ordens locais. Mortos erguidos por sombras após falhas, corpos ficam e sombras somem por limite energético. Tentativa de comer cadáver provoca vômito; impulso não define terceira alma. Limites/IDs de início e fim no ledger.

**J27 — S013 1051–1350:** Yalia ajuda. Trevas/Sombras e níveis locais distintos; absorção tipo buraco negro tem alcance cinco metros, falhas e explosão. Armazena espadas na sombra; tentativa de espada antiga falha neste ponto. Confronto, sombras, dano ao braço e alteração muscular: não conferem corpo adulto permanente. Captura começa com arqueiro e correntes. Limites/IDs de início e fim no ledger.

**J28 — S013 1351–1650:** Cativeiro e violência contra ambos tratados sem reproduzir material privado explícito. Emília liberta Azazel e participa ativamente da fuga; curas falham/perigo de morte. Ele mata torturador e guarda; energia interrompe transformação. Hotel cobra dracos. Cena da menina curada como criada é sonho, ela segue desacordada ao despertar. Limites/IDs de início e fim no ledger.

**J29 — S013 1651–1950:** Demonificação contextual com custo zero não zera efeitos de toda magia. Rith relata três dias locais; Emília nomeia-se. Hotel invadido, camuflagem e fuga; atropelamento de slime é corrigido e entrada dele no corpo negada OOC, sem Astro/Kian fundidos. Yalia acolhe Emília. Mestre diz que a mente ainda é Kian, com pouco conhecimento de Trevas/Sombras. Sombra própria emerge; integração e controle ainda observados em etapas. Limites/IDs de início e fim no ledger.

**J30 — S013 1951–2250:** Yalia vê sombra, Azazel a recolhe; não apenas sonho. Emília aparece viva no café. Pedido condicional de anunciar morte não é morte. Casa de Rith destruída e bilhete não confirmam seu destino. Westia humana; Rezi/raizel são nomes usados no diálogo. Bombas, cultistas e portal; demonização do cultista não identifica culto com Quimera/Deus Dragão. Monarca é adversário distinto de Kian. Limites/IDs de início e fim no ledger.

**J31 — S013 2251–2485:** Braços negros e espada recuperada; aparente morte de Azazel desfeita pela ilusão de Westia. Ela permanece ferida, não morreu ilusoriamente. Colapso de metade do teto subterrâneo e abalo na cidade não destroem todo reino. Destinos de aliados/Monarca não concluídos. Terras roxas, ave, absorção involuntária por contato sem núcleo explicitado, queda e entrada na cabana. Velha dorme na cadeira; Azazel observa casa com poções. Não demonstrar que ele dormiu ou que anfitriã é Ellen. Limites/IDs de início e fim no ledger.

**J32 — S002 0–240:** Lilith desperta e encontra Ymir. Sete dias e reconstrução por mago Terra/orbe confirmados localmente. Custo militar na primeira recuperação e relato de ave/orbe não significam quest realizada aqui. Ymir lembra Mouran/Ellen sem transporte demonstrado. Montanha/sombras: Yoran atribui orbe e Fierch está vivo, sem impostor comprovado. Limites/IDs de início e fim no ledger.

**J33 — S002 241–500:** Fierch nega vínculo do orbe à montanha, contradizendo Yoran; normalidade de corpo tem explicação metafísica do NPC, não prova impostor. Desgaste neural e drenagem contrapõem ausência de efeitos mencionada. Beliart retifica quem o usou; quatro o obtiveram. Sonho de tábua termina ao despertar, sem apagar batalha de S001. Quinto mago é forma de tratamento; autonomia/refusa de NPC explícita. Limites/IDs de início e fim no ledger.

**J34 — S002 501–782:** Nomes/elementos dos quatro magos recuperados. Ymir diz esposa e prioriza despertá-la; plano dos cinco/orbe para braço não executado. Neyfor/Lilith tornam-se amigos, sem romance consumado. Coiote alvo de intenção. Mestre esquece e depois retoma Emma, não apaga existência. Raízes e despertar da menina coincidem sem causalidade/poder atribuído. Yoran chega ao fim, ataque não narrado. Limites/IDs de início e fim no ledger.

### Continuidade de Henry

**Comprovado:** morte narrada em S187 e tratamento do corpo/alma já confrontados em B002.1; retorno vivo em S016, continuidade da batalha e cura de Lucas. A causa anterior à morte não é o soco cerebral tentado e recusado como golpe conclusivo. **Relato:** Henry diz ter sido salvo por um conhecido, sem nome ou método. **Provável:** alguma intervenção intermediária segundo ele; não identificada independentemente. **Desconhecido:** como corpo/alma voltaram e quem executou o retorno. Velho de maio e conhecido de junho não foram fundidos. A leitura integral de S016 encerra o intervalo, não a biografia de Henry.

### Harry–Astro: cinco condições separadas

| Condição | Resultado documental | Limite |
| --- | --- | --- |
| Continuidade pessoal | Provável pela associação OOC de S008 anteriormente examinada. | S161 final confirma Harry, sem ponte explícita a Astro. |
| Continuidade de memória | Insuficiente; versões locais discordam. | Não garantir memória íntegra do Harry anterior. |
| Continuidade corporal | Insuficiente entre Harry nominal e hospedeira. | Entrada na mulher não recuperada; ela sobrevive após saída. |
| Mudança de manifestação | Astro sai da mulher e ocupa homem prestes a morrer em S008. | Não demonstrar que novo homem já era cadáver, ou que mulher vira Harry. |
| Identidade nominal | Harry nomeado pelo mestre/Zex em S161; Astro apresenta-se em S008. | Dois nomes não provam ou negam automaticamente pessoa única. |

Lyone é procurado e há fotografia; parentesco não é confirmado. S008 foi usado como confronto documental já realizado, sem nova contagem. [S161 · 1212959525368238090](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161); [S161 · 1212960389114105856](../pesquisa/fase-3/Fontes-e-Evidencias.md#s161). Transição e antecedentes continuam pendentes em S161 0–1499 e outras fontes pertinentes.

### Kian / Lúcifer / Azazel: matriz de manifestações

| Aparição/nome | Corpo, memória e controle | Capacidade/personalidade observada | Afirmação do jogador versus resultado do mestre | Lacuna |
| --- | --- | --- | --- | --- |
| S187 1700–1940, Kian | Adulto no palácio e transporte; recordação fragmentária de castelo. | Sombra com alcance 30 m; pouca agressividade não vira essência moral fixa. | Cura Travessa é cancelada; cura de Henry não creditada a Kian. Transporte coletivo confirmado. | Outras aparições adultas S187 ainda não revistas. |
| S182 0–393, Lúcifer/Kian | Adulto, estudo prolongado local, adaptação energética e marca abdominal. | Curiosidade, estudo, conversa e testes que esgotam. | Mestre usa ambos nomes na mesma sequência; cura do chão falha, armas complexas recusadas. Rei do inferno é ironia, sem soberania. | Não demonstra mecanismo de chegada ao bebê. |
| S187 2405–2465, morte comentada | Corpo de Kian não recebe resolução conclusiva nesse comentário. | Falas informais e OOC. | Morri/flecha de fogo do jogador não substitui morte narrada. | Causa/transição ainda desconhecidas. |
| S013 integral, Azazel | Bebê chamado Azazel; crescimento pessoal até doze anos. Mestre afirma mente ainda Kian, com pouco conhecimento de Trevas/Sombras. | Curiosidade, sobrevivência, absorções involuntárias, violência e limites de energia. | Propostas de controlar todas sombras, recuperar espada ou curar Emília têm falhas e resoluções próprias. Sonho de cura não realiza cura. | Memória/repertório completos não demonstrados; identidade pessoal autoral confirmada. |
| Final S013 | Vivo e ferido, entra na cabana; velha dorme. | Observa poções/alquimia, sem repouso próprio confirmado. | Absorção da ave por contato não nomeia núcleo; ilusão desfaz aparente morte de Azazel, não Westia. | Identidade da velha e destinos de aliados continuam abertos. |

[S013 · 1253899431401492600](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1256055535262765096](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1256055716578590780](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1264741025797246987](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1267992776528625697](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013); [S013 · 1267992861354229760](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013). Não são três personagens independentes; não há integração completa, terceira alma ou mecanismo adulto–bebê inventado.

### Ymir, Beatriz e antecedentes

Projeto Solus de Vermund permanece intenção de bombardeio de Piferme; não fundido ao bombardeio da fortaleza. Ferimentos, tentativa de criar ar fracassada e desmaio antecedem Casa Coratayne; resgate atribuído por Limia a Garius. Ele administra a casa e é ministro de Polã, sem posse/soberania universal. Beatriz relata despertar na Árvore da Vida, casa reconhecida e procura por Ymir; reencontro afetuoso e pernas perfeitas narrados, braço de Ymir ausente. Seu ontem versus semanas dele não resolve o calendário. Família, missão diplomática e sequestro da irmã são relatos; ela quer perguntar, escolher e buscar a irmã, não mero instrumento de Ymir. Garius morto, luto e viagem dos dois culminam na chegada à cidade élfica; missão e Milena não realizados.

**Beatriz esposa por informação autoral confirmada; cronologia do casamento aberta.** S002 usa esposa, julho contém plano, sem cerimônia recuperada. **Supremacia futura D/B e Trajetória I de Ymir mantidas** no adaptado; sem feito retroativo. Livros, títulos, custos e limites são documentados com atribuição e escala local.

### Reconciliação e correções

Rans: pedido de remover selos à voz materna/divina; experiência narrada, identidade objetiva/remoção/recuperação de Hermione incertas. Perfil, relações, ARC-016, PS-038, CRIT-040, índice e propostas foram reconciliados com OM-003/004/007; corrigida a premissa residual do pedido no documento 12. Mulack: Philip Glorian/pesquisa racial incorporados; natureza das criaturas e desfecho original contraditórios; sobrevivência adaptada aprovada. Rechecadas relações/arcos/índices/propostas, sem novo destino ou alteração desnecessária. Reconciliação no [documento 23](23-Auditoria-de-Compatibilidade-dos-12-Protagonistas.md).

Novas OM-008–014 no [registro 25](25-Omissoes-Descobertas-e-Correcoes-Checkpoint.md#registro-adicional-b0022): Colapso/custo; homônimo Stwart; Sexto seis/dez metros; quatro erros de Azazel; Null/All/DeHe; história dos livros; cronologia conjugal. COR-E01 é editorial: ARC-014 explicita busca por sair, com duplicata idêntica removida, resultado preservado. Correções de Kian propagadas apenas às bases factuais dos documentos adaptados 02/15/19; DD-01–43 intactos. CONT-018/019 e demais sequências corroboradas não foram reconstruídas do zero.

### Matrizes proporcionais

**PS (40 entradas):** 17 parcialmente revisado; 22 não iniciado; 1 em investigação.

**CRIT (40 entradas):** 25 não iniciado; 15 parcialmente revisado.

**ARC (19 entradas):** 11 não iniciado; 8 parcialmente revisado.

**protagonists (12 entradas):** 8 parcialmente revisado; 4 não iniciado.

S002 trouxe exame incidental de Lilith como varredura; sua frente dirigida de B003 permanece por executar. PS-030 está em investigação somente pela ressalva do homônimo; ARC-014 recebe ajuste editorial, sem revisão contextual do ramo de Yakkatsu. Nenhuma entrada ou trajetória foi elevada a revisão concluída.

### Fontes concluídas e trabalho restante

**Integrais em C/D (não biografias):** S001, S002, S003, S008, S013, S016, S023, S174, S182, S198, PWR001, PWR002, PWR003, PWR004, PWR005, PWR006, PWR007, PWR008, PWR009, PWR010, PWR011, PWR012 — 22 fontes não vazias. **Parciais:** S025, S028, S037, S068, S106, S118, S123, S146, S155, S158, S161, S166, S178, S187 — 14. **Sem exame semântico independente:** 162 fontes não vazias; lista completa por fonte no acumulado. As 16 vazias não são leitura narrativa. Novas fontes completas nesta rodada: S001, S002, S013, S016, S023, S182.

**B002 ainda em andamento.** Falta confrontar o restante adulto de S187: 0–1699, 1941–2404, 2466–2649; trechos 2650–2961 já auditados em B002.1 não devem ser reiniciados. Antecedentes Kian em S184 0–577, S051 0–8, S052 0–233 e S070 (tamanho/partes já C no manifesto/ledger) precisam de revisão contextual proporcional. Harry: S161 0–1499 e pontes pessoais/memória/corpo ainda não demonstradas. Mulack: S158 0–1279 e fontes anteriores continuam pendentes. Henry/Ymir/Rans têm outras fontes ainda parciais; ausência de explicação nos arquivos completos não autoriza fechá-las globalmente. Próxima varredura: S004 0–57, depois S005 em núcleos de até 200 com contexto; nenhuma dessas leituras foi contada aqui.

B003 permanece **não executado**, condicionado ao fechamento verificável das investigações B002; futuros focos já planejados (Bytes/Nairóbi, Yakkatsu/Bardock/Stwart, God/Gotter/Árvore, EREN/Ana, Lilith/Hads/Emma, Michael, Rans, Henry) não são progresso narrativo. Não há parecer de prontidão para criar grandes acontecimentos nem nova era/cronologia adaptada.

---

## Relatório histórico B002.1 — preservado


**Checkpoint B002.1 finalizado; lote B002 EM ANDAMENTO.** Base: main `0be4f883d1bbcf206d28fc838fcc7f82f794bc04`, PR #15 mesclado. Não reinicia A, processamento ou B001. Nenhuma construção histórica definitiva autorizada.

## Cobertura independente

4.122 IDs distintas lidas neste checkpoint: **4.105 novas** e **17 revisitas de B001**; mais 56 acessos repetidos internos a S187 para recuperar uma saída truncada, sem progresso adicional. Índices abaixo são base zero, inclusive. C acumulada: **4.542 / 89.313 (5.085486%)**; principal **4.384 / 89.155 (4.917279%)**, mais todas as 158 PWR já triadas em B001. Restam **84.771** principais sem C independente. D acumulada: **3.973 / 89.313 (4.448401%)**; trechos lidos que ainda aguardam confronto detalhado não foram contados em D. A/B concluídas; C/D parciais.

[Ledger com todas as IDs/hashes e avaliações](auditoria-fontes/triagem-B002.json), [união acumulada por fonte](auditoria-fontes/cobertura-acumulada.json), [plano de varredura](auditoria-fontes/plano-varredura.json), [matrizes completas](auditoria-fontes/matrizes-revisao.json). B001 e seu manifesto/validação permanecem históricos, intactos.

## Intervalos realmente examinados

| Intervalo | Fonte | Índices inclusivos | C | D | Frente |
| --- | --- | --- | --- | --- | --- |
| I01 | [S187](../pesquisa/fase-3/Fontes-e-Evidencias.md#s187) | 2650–2961 | 312 | 312 | dirigida |
| I02 | [S016](../pesquisa/fase-3/Fontes-e-Evidencias.md#s016) | 0–260 | 261 | 176 | dirigida |
| I03 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 1280–1550 | 271 | 271 | dirigida |
| I04 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 1551–1820 | 270 | 270 | dirigida |
| I05 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 1821–1899 | 79 | 79 | dirigida |
| I06 | [S158](../pesquisa/fase-3/Fontes-e-Evidencias.md#s158) | 1900–2115 | 216 | 216 | dirigida |
| I07 | [S198](../pesquisa/fase-3/Fontes-e-Evidencias.md#s198) | 0–16 | 17 | 17 | revisita |
| I08 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 0–176 | 177 | 177 | dirigida |
| I09 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 177–549 | 373 | 373 | dirigida |
| I10 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 550–790 | 241 | 241 | dirigida |
| I11 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 791–946 | 156 | 156 | dirigida |
| I12 | [S003](../pesquisa/fase-3/Fontes-e-Evidencias.md#s003) | 947–1015 | 69 | 69 | dirigida |
| I13 | [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | 0–240 | 241 | 241 | dirigida |
| I14 | [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | 241–376 | 136 | 136 | dirigida |
| I15 | [S008](../pesquisa/fase-3/Fontes-e-Evidencias.md#s008) | 377–470 | 94 | 94 | dirigida |
| I16 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 0–147 | 148 | 148 | dirigida |
| I17 | [S013](../pesquisa/fase-3/Fontes-e-Evidencias.md#s013) | 148–230 | 83 | 0 | dirigida |
| I18 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 820–1020 | 201 | 41 | dirigida |
| I19 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 1021–1210 | 190 | 49 | dirigida |
| I20 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 1211–1399 | 189 | 89 | dirigida |
| I21 | [S023](../pesquisa/fase-3/Fontes-e-Evidencias.md#s023) | 1400–1556 | 157 | 157 | dirigida |
| I22 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 0–204 | 205 | 205 | sistemática |
| I23 | [S001](../pesquisa/fase-3/Fontes-e-Evidencias.md#s001) | 205–240 | 36 | 36 | sistemática |

S003 e S008 foram lidos integralmente; S198 foi revisitado integralmente. Em S158, a sequência relevante da dungeon, desde preparação/entrada até retificação/recusa e conversa posterior, está em 1280–2115; 0–1279 não recebe leitura integral. S001 0–240 inicia a frente sistemática e registra encerramento parcial na entrada da torre, cuja conversa segue pendente. S023 820–1556 cobre casamento, família e chegada final; os antecedentes 0–819 ainda faltam. S016 0–260 e S013 0–230 são parciais. Não declarar estes arquivos completos.

## Avaliação contextual de cada intervalo

### I01 — S187

Morte de Henry: esmagamento, cura tentada, morte do mestre, alma-orbe, velho desconhecido, transporte e corpo deixado em Mouran. O soco cerebral é tentativa do jogador; não mata a criatura por resolução. Sete horas são viagem interna. Não há nome confirmado do velho nem ligação demonstrada entre ele e o salvador de junho. CONT-016/CRIT-003 já preservavam alma e morte: CASO 1.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, correção ou retificação, metajogo relevante, mensagens auxiliares, material ambíguo.

### I02 — S016

Michael conversa sobre Mouran, mercadorias e guerra; conquistar Piferme é intenção. Henry reaparece no índice 153; afirma retorno e salvamento por conhecido, sem nome/método. Quase purgatório é relato pessoal. A batalha posterior ao retorno continua além de 260: não se encerra a campanha nem se certifica a fonte inteira. CONT-019/PS-023 mantidos.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I03 — S158

Preparação, equipamento, Nyxis deixada com Driade, entrada no templo e combate coletivo. Mortes de carregadores e baixas reduzem suprimentos; Philip Glorian coordena apoio. Sala de pesquisa racial encontrada. Resultado de união de raças não é demonstrado; explicações são do pesquisador NPC. OM-005.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de NPC, diálogo de personagem, definição de habilidade, correção ou retificação, metajogo relevante, mensagens auxiliares.

### I04 — S158

Pesquisa incompleta, experimento descrito, nome parcialmente apagado e passagem secreta. Não identificar monstro pelo palpite OOC. Evacuação confirmada, Mulack sozinho, gasto de mana rompe vasos; rei goblin encontrado já morto. Reforços pedidos não chegam. Notificação de oito exclusões e comentário de que ação foi apagada: lacuna local, sem reconstruir conteúdo.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de NPC, diálogo de personagem, definição de habilidade, correção ou retificação, metajogo relevante, notificações de sistema, mensagens auxiliares, material ambíguo.

### I05 — S158

Emboscada, falha de detecção, armadura, ataque e pulmão perfurado em texto editado. Mestre lembra armadura e manda refazer; jogador insiste na morte e recusa continuar. Segunda notificação de dez exclusões. A sequência não escolhe destino único: CRIT-004/PS-020 contraditórios. Edição visível não fornece versões anteriores completas.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, correção ou retificação, metajogo relevante, notificações de sistema, mensagens auxiliares, material ambíguo.

### I06 — S158

Discussão e convivência fora de personagem após a interrupção; não há nova resolução ficcional da retificação da armadura ou retorno de Mulack. Resultado negativo limitado a este fim do canal; metajogo não vira morte adicional.

Categorias não exclusivas: metajogo relevante, metajogo sem consequência canônica, mensagens auxiliares.

### I07 — S198

Memorial e comentário retrospectivo de maio já lidos em B001. Confronto com fim da dungeon reforça contradição; nenhuma ID é progresso novo. OM-002 preservada.

Categorias não exclusivas: metajogo relevante, material ambíguo, mensagens auxiliares.

### I08 — S003

Reencontro afetuoso de Rans e Hermione, relato dela de luz/tempo decorrido, treino conjunto e lago Phegor. Ela está ativa no início; a passagem à inconsciência posterior não recebe causa nesse arquivo. Abraço e carinho não provam casamento.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I09 — S003

Metajogo de personalidade, aparência, idade e ficha de Hermione. Vento é discutido/definido, mas não se atribui cada proposta de aparência como metamorfose realizada. Menção OOC a esposa não demonstra cerimônia. Chamada, reação e mensagens sem texto permanecem auxiliares.

Categorias não exclusivas: metajogo relevante, metajogo sem consequência canônica, definição de habilidade, mensagens auxiliares, material ambíguo.

### I10 — S003

Conversa sobre desenhos, agenda e convivência dos participantes, sem consequência ficcional estabelecida. O intervalo foi lido; não se publica sua transcrição nem se incorpora assunto pessoal ao canon.

Categorias não exclusivas: metajogo sem consequência canônica, mensagens auxiliares.

### I11 — S003

Voo, desgaste neural e dezesseis horas até sul de Piferme/Terceira Paróquia. Hermione desacordada aparece na ação editada do jogador, sem causa ou recuperação demonstrada. Multidão interpreta aparência como divina; mestre narra sensações e mudança das asas. Feuhs é humano. Não conferir autoridade divina universal pelas crenças dos cidadãos.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, definição de habilidade, metajogo relevante, mensagens auxiliares, material ambíguo.

### I12 — S003

Pena, experiência de luz/clamores, pressão sobre alma, auréola e voz que se identifica como deusa/mãe. Rans pede remoção de seus selos à voz; não pede receber um selo de Feuhs. Orientação branca/amarela não prova concessão de poderes ilimitados. Mestre termina com despertar em cama, sem resolução para Hermione nem remoção narrada. OM-003/004/007; CRIT-040.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I13 — S008

Astro em corpo feminino busca Lyone, chega a Olta e desce ao mercado negro subterrâneo. Saída da hospedeira e sobrevivência dela são narradas. Memória de Abismo e calendário aparecem em diálogos incompatíveis, sem unificar meses ou fazer salto global. A entrada nesse corpo não é mostrada.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I14 — S008

Comentário OOC associa o corpo a Harry; Astro se apresenta e relata meses no corpo, mas isto não demonstra transição nominal inequívoca. Hospedeira desperta e sai; sua continuidade posterior falta. Relatos de memória discordam. Manter CRIT-005 provável, dossiês e versões separados.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I15 — S008

Novo homem prestes a morrer, ainda não cadáver confirmado; ocupar/curar é ação de Astro. Fotografia de Lyone não confirma parentesco. Retificação sobre objetos disponíveis; depois tiros, crescimento e destruição do mercado local. Não é destruição de todo Olta nem de um plano Inferno. Absorver todos os cérebros é pedido, não concessão de todo conhecimento. Caverna vazia narrada ao fim. OM-006.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, correção ou retificação, metajogo relevante, mensagens auxiliares, material ambíguo.

### I16 — S013

Despertar infantil; mãe chama Azazel e mestre nomeia Kian na mente/berço. Saltos pessoais, aprendizagem da fala, cura após tentativa de magia, treinamento e abandono pelo pai. Ária é invocada com cura contextual, não aparição comprovada. Continuidade externa preservada, mecanismo adulto–bebê não aparece neste começo. CONT-017/CRIT-006 já cobrem identidade e crescimento.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, definição de habilidade, metajogo relevante, mensagens auxiliares, material ambíguo.

### I17 — S013

Caminho da floresta, sombra com limite explícito, ferramentas tentadas, ataque do lobo e ferimentos resolvidos. A aparição cômica de Henry e pergunta sobre entidades cósmicas não provam interferência divina histórica. Caminhada/frutas continuam após 230; confronto amplo de poderes e destino pendente.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, metajogo relevante, mensagens auxiliares, material ambíguo.

### I18 — S023

Contexto anterior na banheira; revelação da segunda princesa, irmã ausente, casamento ainda não consumado e vontade de Beatriz expressa. Transformação em pássaro é narrada, não confirmação de impostor atual. Henry vivo entra na cena; Ymir relata morte/retorno sem explicar o mecanismo. Caminhada e jardim conduzem ao quarto de Garius; continuação lida em I19.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I19 — S023

Corpo de Garius, corte e petrificação narrados, luto de Beatriz e cuidado de Ymir. Berthold explica Disare e neutralização: testemunho NPC, sem demonstrar regra cósmica universal. Relata missão diplomática, emboscadas e amnésia. Rumores sobre órgãos élficos permanecem rumores. Edward/Deward discutidos sem fundir nomes. Novo confronto detalhado dessas informações ainda pendente, salvo luto/causa atribuída já representados em CONT-020.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, material ambíguo.

### I20 — S023

Altruístas, Belphegor, Colapso e guerra de cem anos segundo Berthold: não demonstrar uso/ponte efetuada. Proibição jocosa de sogro não anula informação autoral futura de esposa. Mensagem sobre irmã mandada ignorar pelo mestre, seguida de informação nova específica sobre Quimera e equipe. Beatriz escolhe perguntar e usar as próprias pernas. Tentativa de chamar Nines pela flauta falha: ninguém vem. Item flauta aparece, sem conceder todos os comandos.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, correção ou retificação, metajogo relevante, mensagens auxiliares, material ambíguo.

### I21 — S023

Berthold relata Rans caçador; isto não narra caça realizada. Henry tenta ir à biblioteca e mestre redireciona canal. Beatriz escolhe mostrar cidade, conta irmã/mediações e limita própria memória da emboscada. Ymir manifesta preferência por paz; chegada à cidade dos elfos narrada, sem cerimônia ou resgate. Conversas posteriores ao fim da sessão não são novas cenas. CONT-020/ARC-018 confirmados no trecho final.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, correção ou retificação, metajogo relevante, metajogo sem consequência canônica, mensagens auxiliares, material ambíguo.

### I22 — S001

Início ordenado do corpus: quarto e sombras formam montanha/orbe, tentativa de interação falha. Treino sensorial reconhecido possível, ainda não adquirido. Powl se apresenta, Froid usa duas espadas e fala do estilo rei da água; vila proposta ainda não visitada neste recorte. Aparente derrota fatal por tiro é retificada por Previsão: meio segundo, desvio confirmado e esgotamento neural. CRIT-032/033 e perfil de Ymir já representam esses núcleos; não atribuir causa do orbe sem outra fonte.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, correção ou retificação, definição de habilidade, metajogo relevante, mensagens auxiliares, conteúdo repetido, notificações de sistema, material ambíguo.

### I23 — S001

Extensão até entrada na torre para não parar no tiro: reflexo revela atirador, pedras e desvios permitem fuga, vigia oferece abrigo e mestre confirma entrada na torre. Identidade/motivo do atirador e diálogo do vigia continuam além de 240, explicitamente pendentes. Rolagens/fichas repetidas são auxiliares mecânicos, não outro evento ou novo poder.

Categorias não exclusivas: narração do mestre, resolução de ações, ação tentada pelo jogador, diálogo de personagem, diálogo de NPC, metajogo relevante, mensagens auxiliares, notificações de sistema.

## Descobertas e correções rastreáveis

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

## Resultados mantidos e limites

Henry: morte, saída da alma e reaparição já estavam corretamente documentadas (CASO 1); o conhecido não nomeado do relato de junho não é automaticamente o velho de maio. Harry/Astro: S008 integral fortalece a associação contextual, sem confirmar ponte nominal (CASO 5). Kian/Azazel: narração usa ambos os nomes na infância; a confirmação externa continua válida e o mecanismo permanece aberto, com investigação adulta ainda pendente. Mulack: dungeon integral relevante confirma que a retificação não foi resolvida pela recusa; memorial/comentário de maio não apagam versões (CASO 1/5). Ymir/Beatriz: vontade dela e afeto, condição de princesa, irmã e chegada estão representados; diálogo admite chamar de esposa antes do casamento naquela cena. Informação autoral de esposa não é revogada, cerimônia/cronologia não inventadas. Rans: correção de premissa não resolve remoção, natureza da voz ou condição de Hermione.

Notificações de exclusão em S158 (índices 1755 e 1869, oito/dez mensagens) e comentário sobre ação apagada comprovam perda local, sem fornecer IDs/conteúdo nem garantir que havia explicação definitiva. Não somar as duas notificações como 18 mensagens distintas recuperadas. Calendário em S008 (janeiro versus referência a 25 de julho), mensagem de Berthold sobre irmã seguida de pedido do mestre para ignorar e relatos sobre Edward/Deward exigem confronto ampliado; não corrigir calendário global por inferência.

## Matriz das quarenta pendências

Todas as 40 entradas possuem registro de situação anterior, fontes/IDs conhecidas, fontes adicionais, intervalos lidos, evidência/resultado, confiança, classificação e impacto no JSON. Fontes anteriores não reexaminadas são marcadas como herdadas. Dez entradas recebem investigação parcial; trinta ficam INVESTIGAÇÃO PENDENTE. Nenhuma é declarada irrecuperável por esta rodada.

| PS | Título | Estado independente | Intervalos | Resultado atual |
| --- | --- | --- | --- | --- |
| [PS-001](../canon-original/19-Matriz-Canon-Critico.md#ps-001) | Origem da Surgência | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-002](../canon-original/19-Matriz-Canon-Critico.md#ps-002) | Saída física versus marca | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-003](../canon-original/19-Matriz-Canon-Critico.md#ps-003) | Rio e conclusão do ramo de minhocas | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-004](../canon-original/19-Matriz-Canon-Critico.md#ps-004) | Prisão inicial ou minas de Mouran | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-005](../canon-original/19-Matriz-Canon-Critico.md#ps-005) | Resultado do primeiro altar | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-006](../canon-original/19-Matriz-Canon-Critico.md#ps-006) | Núcleo, lembranças e cristal da força | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-007](../canon-original/19-Matriz-Canon-Critico.md#ps-007) | Ellen e prefeito | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-008](../canon-original/19-Matriz-Canon-Critico.md#ps-008) | Trevor e Patrick supostamente traidores | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-009](../canon-original/19-Matriz-Canon-Critico.md#ps-009) | Cristal ou Veneno de Ymir | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-010](../canon-original/19-Matriz-Canon-Critico.md#ps-010) | Noah desaparecido | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-011](../canon-original/19-Matriz-Canon-Critico.md#ps-011) | Figura negra, laboratório e sombras | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-012](../canon-original/19-Matriz-Canon-Critico.md#ps-012) | Título e coroa de EREN | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-013](../canon-original/19-Matriz-Canon-Critico.md#ps-013) | Morte de Rans no segundo altar | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-014](../canon-original/19-Matriz-Canon-Critico.md#ps-014) | Lilith e Hads | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-015](../canon-original/19-Matriz-Canon-Critico.md#ps-015) | Gás azul | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-016](../canon-original/19-Matriz-Canon-Critico.md#ps-016) | Quatro altares e desfecho de Mouran | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-017](../canon-original/19-Matriz-Canon-Critico.md#ps-017) | Harry, God-Zilla e entradas pouco documentadas | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-018](../canon-original/19-Matriz-Canon-Critico.md#ps-018) | Note: nome, máscara e anonimato | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-019](../canon-original/19-Matriz-Canon-Critico.md#ps-019) | Ponte à Guilda/Piferme/Olta e fim da campanha | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-020](../canon-original/19-Matriz-Canon-Critico.md#ps-020) | Final de Mulack | PARCIALMENTE REVISADO | I03, I04, I05, I06, I07 | CONTRADIÇÃO PRESERVADA |
| [PS-021](../canon-original/19-Matriz-Canon-Critico.md#ps-021) | Adulto Kian → bebê Azazel | PARCIALMENTE REVISADO | I16, I17 | PARCIALMENTE ESCLARECIDA; INVESTIGAÇÃO PENDENTE |
| [PS-022](../canon-original/19-Matriz-Canon-Critico.md#ps-022) | Harry → Astro e hospedeira | PARCIALMENTE REVISADO | I13, I14, I15 | PROVÁVEL; INVESTIGAÇÃO PENDENTE |
| [PS-023](../canon-original/19-Matriz-Canon-Critico.md#ps-023) | Henry volta à vida | PARCIALMENTE REVISADO | I01, I02, I18, I21 | PARCIALMENTE ESCLARECIDA; INVESTIGAÇÃO PENDENTE |
| [PS-024](../canon-original/19-Matriz-Canon-Critico.md#ps-024) | Beatriz: coma e memória | PARCIALMENTE REVISADO | I18, I19, I20, I21 | PARCIALMENTE ESCLARECIDA; INVESTIGAÇÃO PENDENTE |
| [PS-025](../canon-original/19-Matriz-Canon-Critico.md#ps-025) | Irmã de Beatriz / Quimera / Milena | PARCIALMENTE REVISADO | I18, I19, I20, I21 | ABERTA; PARCIALMENTE REVISADA |
| [PS-026](../canon-original/19-Matriz-Canon-Critico.md#ps-026) | Nefa e Altruístas | PARCIALMENTE REVISADO | I20 | INVESTIGAÇÃO PENDENTE |
| [PS-027](../canon-original/19-Matriz-Canon-Critico.md#ps-027) | Líder Pantera | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-028](../canon-original/19-Matriz-Canon-Critico.md#ps-028) | Emma e pai alegado | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-029](../canon-original/19-Matriz-Canon-Critico.md#ps-029) | God depois da caça | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-030](../canon-original/19-Matriz-Canon-Critico.md#ps-030) | Yakkatsu sai do Inferno | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-031](../canon-original/19-Matriz-Canon-Critico.md#ps-031) | Bytes: favor e Nairóbi | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-032](../canon-original/19-Matriz-Canon-Critico.md#ps-032) | Exclusões e tópicos privados | PARCIALMENTE REVISADO | I04, I05 | PARCIALMENTE ESCLARECIDA; INVESTIGAÇÃO PENDENTE |
| [PS-033](../canon-original/19-Matriz-Canon-Critico.md#ps-033) | Golems roubados no Inferno | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-034](../canon-original/19-Matriz-Canon-Critico.md#ps-034) | Gwierlan morto segundo Edward | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-035](../canon-original/19-Matriz-Canon-Critico.md#ps-035) | Wilbur e Hermest | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-036](../canon-original/19-Matriz-Canon-Critico.md#ps-036) | Culto do Deus Dragão / Deus Demônio | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-037](../canon-original/19-Matriz-Canon-Critico.md#ps-037) | Escalas e calendários | PARCIALMENTE REVISADO | I16, I17, I18, I19, I20, I21 | INVESTIGAÇÃO PENDENTE |
| [PS-038](../canon-original/19-Matriz-Canon-Critico.md#ps-038) | Rans, Hermione e selo | PARCIALMENTE REVISADO | I08, I09, I10, I11, I12 | PREMISSA CORRIGIDA; DESFECHOS ABERTOS |
| [PS-039](../canon-original/19-Matriz-Canon-Critico.md#ps-039) | Coiote e governo de Piferme | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |
| [PS-040](../canon-original/19-Matriz-Canon-Critico.md#ps-040) | Michael, Mytria e conquista | NÃO INICIADO | — | INVESTIGAÇÃO PENDENTE |

## Pontos críticos e arcos

Onze dos 39 CRIT anteriores e sete dos 19 ARC receberam confronto parcial; os demais NÃO INICIADOS no novo exame factual. CRIT-040 é adicional, sem apagar/renumerar os 39. Nenhum arco recebe fechamento inventado. Começo, resultados, decisões e últimos estados anteriores estão preservados em `previous_text`; intervalos e limites novos estão separados. Revisão detalhada de todos os campos continua pendente.

| CRIT | Título | Estado independente | Intervalos |
| --- | --- | --- | --- |
| [CRIT-001](../canon-original/19-Matriz-Canon-Critico.md#crit-001) | Rans sobrevive e retorna publicamente | NÃO INICIADO | — |
| [CRIT-002](../canon-original/19-Matriz-Canon-Critico.md#crit-002) | Lilith → Hads → Lilith | NÃO INICIADO | — |
| [CRIT-003](../canon-original/19-Matriz-Canon-Critico.md#crit-003) | Henry morre em maio e reaparece em junho | PARCIALMENTE REVISADO | I01, I02, I18 |
| [CRIT-004](../canon-original/19-Matriz-Canon-Critico.md#crit-004) | Mulack: morte / armadura intacta / memorial | PARCIALMENTE REVISADO | I03, I04, I05, I06, I07 |
| [CRIT-005](../canon-original/19-Matriz-Canon-Critico.md#crit-005) | Astro associado a Harry | PARCIALMENTE REVISADO | I13, I14, I15 |
| [CRIT-006](../canon-original/19-Matriz-Canon-Critico.md#crit-006) | Kian/Lúcifer/Azazel é continuidade confirmada externamente | PARCIALMENTE REVISADO | I16 |
| [CRIT-007](../canon-original/19-Matriz-Canon-Critico.md#crit-007) | Note é Ymir, antes da máscara | NÃO INICIADO | — |
| [CRIT-008](../canon-original/19-Matriz-Canon-Critico.md#crit-008) | Ellen resgatada viva | NÃO INICIADO | — |
| [CRIT-009](../canon-original/19-Matriz-Canon-Critico.md#crit-009) | Gwierlan vivo; Michael rei | NÃO INICIADO | — |
| [CRIT-010](../canon-original/19-Matriz-Canon-Critico.md#crit-010) | Quarto altar destruído pela besta | NÃO INICIADO | — |
| [CRIT-011](../canon-original/19-Matriz-Canon-Critico.md#crit-011) | Terceiro altar e contagem global | NÃO INICIADO | — |
| [CRIT-012](../canon-original/19-Matriz-Canon-Critico.md#crit-012) | Ritual e Patrick | NÃO INICIADO | — |
| [CRIT-013](../canon-original/19-Matriz-Canon-Critico.md#crit-013) | Karl morto; Edward foge | NÃO INICIADO | — |
| [CRIT-014](../canon-original/19-Matriz-Canon-Critico.md#crit-014) | Marca: permanência confirmada e última referência de Henry | NÃO INICIADO | — |
| [CRIT-015](../canon-original/19-Matriz-Canon-Critico.md#crit-015) | Garold morre e Lilith governa | NÃO INICIADO | — |
| [CRIT-016](../canon-original/19-Matriz-Canon-Critico.md#crit-016) | Wilbur e Dimitri | NÃO INICIADO | — |
| [CRIT-017](../canon-original/19-Matriz-Canon-Critico.md#crit-017) | God: auxílio à Árvore e última caçada | NÃO INICIADO | — |
| [CRIT-018](../canon-original/19-Matriz-Canon-Critico.md#crit-018) | Henry recusa Fogo Demoníaco | NÃO INICIADO | — |
| [CRIT-019](../canon-original/19-Matriz-Canon-Critico.md#crit-019) | Yakkatsu: Linhas, Bardock e Inferno | NÃO INICIADO | — |
| [CRIT-020](../canon-original/19-Matriz-Canon-Critico.md#crit-020) | Bytes: favor e esfera | NÃO INICIADO | — |
| [CRIT-021](../canon-original/19-Matriz-Canon-Critico.md#crit-021) | Bytes e Nairóbi | NÃO INICIADO | — |
| [CRIT-022](../canon-original/19-Matriz-Canon-Critico.md#crit-022) | Beatriz viva, princesa e recuperada | PARCIALMENTE REVISADO | I18, I19, I20, I21 |
| [CRIT-023](../canon-original/19-Matriz-Canon-Critico.md#crit-023) | Emma e raízes | NÃO INICIADO | — |
| [CRIT-024](../canon-original/19-Matriz-Canon-Critico.md#crit-024) | Pantera e Quimera | NÃO INICIADO | — |
| [CRIT-025](../canon-original/19-Matriz-Canon-Critico.md#crit-025) | Deus Dragão e Deus Demônio | PARCIALMENTE REVISADO | I19 |
| [CRIT-026](../canon-original/19-Matriz-Canon-Critico.md#crit-026) | Westia e velho de maio | PARCIALMENTE REVISADO | I01 |
| [CRIT-027](../canon-original/19-Matriz-Canon-Critico.md#crit-027) | MUTON, Sexto Sentido e livros | NÃO INICIADO | — |
| [CRIT-028](../canon-original/19-Matriz-Canon-Critico.md#crit-028) | Henry em canal vazio | PARCIALMENTE REVISADO | I21 |
| [CRIT-029](../canon-original/19-Matriz-Canon-Critico.md#crit-029) | Fim recuperável | PARCIALMENTE REVISADO | I21 |
| [CRIT-030](../canon-original/19-Matriz-Canon-Critico.md#crit-030) | Natureza de Kian: concessão e contestação | NÃO INICIADO | — |
| [CRIT-031](../canon-original/19-Matriz-Canon-Critico.md#crit-031) | Ceifador, Froid e Tengetsu | NÃO INICIADO | — |
| [CRIT-032](../canon-original/19-Matriz-Canon-Critico.md#crit-032) | Sombras do orbe de Piferme | PARCIALMENTE REVISADO | I22 |
| [CRIT-033](../canon-original/19-Matriz-Canon-Critico.md#crit-033) | Previsão de Ymir | PARCIALMENTE REVISADO | I22, I23 |
| [CRIT-034](../canon-original/19-Matriz-Canon-Critico.md#crit-034) | Henry/Harry no núcleo inicial | NÃO INICIADO | — |
| [CRIT-035](../canon-original/19-Matriz-Canon-Critico.md#crit-035) | Crescimento lunar de Henry | NÃO INICIADO | — |
| [CRIT-036](../canon-original/19-Matriz-Canon-Critico.md#crit-036) | Controle Magnético de Lilith | NÃO INICIADO | — |
| [CRIT-037](../canon-original/19-Matriz-Canon-Critico.md#crit-037) | Mortes e controles alheios no final de S046 | NÃO INICIADO | — |
| [CRIT-038](../canon-original/19-Matriz-Canon-Critico.md#crit-038) | Ária, Draconia e sugadores de alma | NÃO INICIADO | — |
| [CRIT-039](../canon-original/19-Matriz-Canon-Critico.md#crit-039) | Primeira alegação de morte de Mulack versus dungeon final | NÃO INICIADO | — |
| [CRIT-040](../canon-original/19-Matriz-Canon-Critico.md#crit-040) | Rans: pedido de remoção e voz materna/divina | PARCIALMENTE REVISADO | I11, I12 |

| ARC | Título | Estado independente | Intervalos |
| --- | --- | --- | --- |
| [ARC-001](../canon-original/17-Biblia-Canon-Original.md#arc-001) | Surgência, aparente resgate e escravização | NÃO INICIADO | — |
| [ARC-002](../canon-original/17-Biblia-Canon-Original.md#arc-002) | Exploração do ramo de minhocas e retorno ao rio | NÃO INICIADO | — |
| [ARC-003](../canon-original/17-Biblia-Canon-Original.md#arc-003) | Controle de energia lunar e proteção dos companheiros | PARCIALMENTE REVISADO | I01, I02, I18, I21 |
| [ARC-004](../canon-original/17-Biblia-Canon-Original.md#arc-004) | Descoberta de capacidade e vínculo de EREN | NÃO INICIADO | — |
| [ARC-005](../canon-original/17-Biblia-Canon-Original.md#arc-005) | Briga da rua B e crescimento involuntário | NÃO INICIADO | — |
| [ARC-006](../canon-original/17-Biblia-Canon-Original.md#arc-006) | Busca de saída de Mulack e integração de Yakkatsu | NÃO INICIADO | — |
| [ARC-007](../canon-original/17-Biblia-Canon-Original.md#arc-007) | Anonimato e consolidação de Note | PARCIALMENTE REVISADO | I22, I23 |
| [ARC-008](../canon-original/17-Biblia-Canon-Original.md#arc-008) | Busca de renda, serpente e novo cativeiro de Lilith | NÃO INICIADO | — |
| [ARC-009](../canon-original/17-Biblia-Canon-Original.md#arc-009) | Preparação e missão contra os altares de Mouran | NÃO INICIADO | — |
| [ARC-010](../canon-original/17-Biblia-Canon-Original.md#arc-010) | Culto e crise política entre Mouran, Olta e Piferme | NÃO INICIADO | — |
| [ARC-011](../canon-original/17-Biblia-Canon-Original.md#arc-011) | Guerra, treino e golems do Inferno | NÃO INICIADO | — |
| [ARC-012](../canon-original/17-Biblia-Canon-Original.md#arc-012) | Lilith rainha e proteção de Emma | NÃO INICIADO | — |
| [ARC-013](../canon-original/17-Biblia-Canon-Original.md#arc-013) | Bytes e Nairóbi | NÃO INICIADO | — |
| [ARC-014](../canon-original/17-Biblia-Canon-Original.md#arc-014) | Yakkatsu e saída do Inferno | NÃO INICIADO | — |
| [ARC-015](../canon-original/17-Biblia-Canon-Original.md#arc-015) | Kian, Lúcifer e infância de Azazel | PARCIALMENTE REVISADO | I16, I17 |
| [ARC-016](../canon-original/17-Biblia-Canon-Original.md#arc-016) | Rans, sobrevivência e Hermione | PARCIALMENTE REVISADO | I08, I09, I10, I11, I12 |
| [ARC-017](../canon-original/17-Biblia-Canon-Original.md#arc-017) | Harry e ramo Astro | PARCIALMENTE REVISADO | I13, I14, I15 |
| [ARC-018](../canon-original/17-Biblia-Canon-Original.md#arc-018) | Beatriz, família real e Quimera | PARCIALMENTE REVISADO | I18, I19, I20, I21 |
| [ARC-019](../canon-original/17-Biblia-Canon-Original.md#arc-019) | Michael e campanha de Mytria | PARCIALMENTE REVISADO | I02 |

## Protagonistas

Sete perfis parcialmente revisados e cinco não iniciados na nova revisão factual. PWR de B001 permanece verificado separadamente; nenhum protagonista está concluído.

| Protagonista | Estado | Ainda falta |
| --- | --- | --- |
| Michael Uchiyama | PARCIALMENTE REVISADO | S016 261–580, governos/expansão e trajetória anterior; B003 |
| Rans | PARCIALMENTE REVISADO | Antecedentes do Abismo, causa do estado de Hermione, falsa morte e vínculos anteriores; B003 |
| Henry Chambers | PARCIALMENTE REVISADO | S016 261–580, passagens intermediárias, construções e relações anteriores; #mar vazio não prova desfecho |
| God-Zilla | NÃO INICIADO | Gotter/Árvore, caça e fontes anteriores; B003 |
| Harry | PARCIALMENTE REVISADO | S161 última cena nominal, antecedentes de Astro/Lyone e transição corporal |
| Kian / Lúcifer / Azazel | PARCIALMENTE REVISADO | S187 adulto/relatos OOC de morte; S182 Lúcifer; S013 231–2485 e poderes em contexto |
| Mulack | PARCIALMENTE REVISADO | S158 0–1279 e percurso anterior; o trecho relevante da dungeon foi lido, perfil inteiro não |
| Bytes Sky | NÃO INICIADO | Nairóbi/favor/esfera, demais trajetórias; B003 |
| EREN | NÃO INICIADO | Ana, títulos, arma e últimos estados; B003 |
| Lilith Chipper | NÃO INICIADO | Hads, Emma, governos e últimos estados; B003 |
| Ymir / Note | PARCIALMENTE REVISADO | S023 0–819, antecedentes de Bia/cidade; S001 241–1039; percurso anterior |
| Yakkatsu Tenshin | NÃO INICIADO | Bardock/Stwart/Inferno e últimos estados; B003 |

## NPCs e mundo recuperados neste checkpoint

| Elemento | Registro e estatuto | Continuidade/limite |
| --- | --- | --- |
| Hermione / Feuhs / voz materna | S003 integral: afeto/treino, estado descrito pelo jogador, sacerdote humano e experiência extraordinária | Sem identificar voz ou curar Hermione; OM-003/004/007. |
| Philip Glorian / pesquisador sem nome | S158: coordenação rank A e explicações de laboratório | NPC/pesquisa recuperados em OM-005; não provam biologia universal. |
| Nyxis / Driade | Preparação S158: familiar deixado com Driade | Sem escolher destino final; torneio proposto não realizado no trecho. |
| Hospedeira / homem moribundo / Lyone | S008: saída da mulher viva, novo corpo em homem ainda vivo e fotografia | Não identificar parentesco ou transformar relatos de Astro em todos os resultados. |
| Beatriz / Berthold / Garius / irmã | S023 820–1556: autonomia, família, luto e objetivos | Quimera/Disare/aliança relatadas por NPC; antecedentes e resgate não concluídos. |
| Velho desconhecido / Vermund / Gwierlan | S187 e S016: intervenção no fim de Henry e campanha | Sem identidade do salvador ou conquista de Piferme. |
| Powl / Froid / vigia | S001 0–240: apresentações e abrigo | Já citados na Bíblia; fala sobre vila/estilo não confirma todos os poderes. |
| Terceira Paróquia / Santo Templo da Luz | S003: local de chegada e episódio de Rans | Crença pública não define hierarquia divina universal. |
| Mercado Submundo de Olta | S008: alçapão, comércio e devastação local | OM-006: sem equação com plano Inferno. |
| Disare / cultos / Altruístas / Belphegor / Colapso | S023: explicações de Berthold e relatos históricos | Não criar eras, executar Colapso ou fundir Deus Dragão/Deus Demônio; confronto detalhado restante. |

Ana, Stwart, Bardock, Emma, Ellen, Gotter, Nairóbi, Árvore, Nefa e demais NPCs conservam investigação futura; menções não equivalem a revisão integral de suas trajetórias.

## Continuação específica e prontidão

**Antes de encerrar B002:** S016 261–580; S161 última sequência nominal de Harry (localizar trecho e ler seu contexto integral); S187 passagem adulta de Kian e relatos de flecha de fogo, S182 Lúcifer e confronto com S013; S023 0–819 para salvamento/despertar/memória e antecedentes da família. Ampliar busca de pontes sem atribuir triagem aos resultados de pesquisa textual. Confrontar também os intervalos já lidos que ainda não receberam D; o JSON separa seus contadores.

**Frente sistemática:** continuar S001 241–399 com contexto 236–404; depois blocos de 200 até 1039, preservando fechamento de cenas, e seguir S002 em ordem. Plano inclui todos os 202 S, fontes vazias e contadores acumulados.

**B003, após B002:** Bytes/Nairóbi/favor (S173; esfera S174 já B001 e busca final S014), Yakkatsu/Bardock/Stwart/Inferno (localizadores do perfil, intervalos completos a delimitar), God/Gotter/Árvore (S133/S135/S178), EREN/Ana (S159/S166), Lilith/Hads/Emma (S166/S173/S002), Michael/expansão (S016 e antecedentes), Rans/falsa morte (S165/S166/S167), Henry/construções (S178 e ramos anteriores). A lista é plano, não leitura executada.

**NÃO APTO provisório para encerrar a auditoria e liberar a construção histórica global:** cobertura e investigações ainda insuficientes. Não é reprovação de integridade dos arquivos nem exigência de resolver todo mistério. DD-01–43, supremacia futura D/B e Trajetória I de Ymir, Beatriz esposa com cronologia aberta e sobrevivência adaptada de Mulack permanecem intactos. Nenhuma Fase 6, era ou acontecimento definitivo iniciado.
