# APOSTILA — TÓPICO 1: PROCESSO DE DESENVOLVIMENTO DE SOFTWARE
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Processo de Desenvolvimento de Software: Metodologias, métodos e processos de desenvolvimento ágil de software. Metodologias, métodos e processos de engenharia de requisitos. Metodologias, métodos e processos de engenharia de software.
>
> **Base de conhecimento:** `03.Engenharia de Software` (Aulas 00–05, 09, 10) e `04.Desenvolvimento de Software` (Aulas 14, 17) — Curso Regular TI 2020.2 + complemento (Scrum Guide 2020, manutenção).

---

# MÓDULO I — ENGENHARIA DE SOFTWARE E CICLOS DE VIDA

## 1. Conceitos

- **Engenharia de Software (IEEE)**: abordagem **sistemática, disciplinada e quantificável** para desenvolvimento, operação e manutenção de software. Princípios: formalidade, abstração, decomposição, generalização, flexibilização.
- **Ciclo de vida (Sommerville)**: Especificação → Desenvolvimento → Validação → Evolução. **(Pressman)**: Comunicação → Planejamento → Modelagem → Construção → Implantação. "Modelo de processo" = sinônimo de modelo de ciclo de vida em prova.

## 2. Modelos preditivos

- **Cascata** (Royce, 1970; sinônimos: waterfall, clássico, sequencial, linear, rígido): fases estritamente sequenciais; **atrasa** a redução de riscos; custo de correção depende do **momento da detecção** do erro. **Não facilita mudanças**.
- **Iterativo** (refaz versões) × **Incremental** (acrescenta builds). Exemplo da Monalisa: incremental = partes pintadas; iterativo = versões do quadro.
- **RAD**: 5 fases, ciclo de **60–90 dias**.
- **Prototipagem**: **Exploratória/Evolucionária** × **Throwaway/Descartável** — *quando o enunciado não especifica o tipo, a resposta é throwaway*.
- **Espiral** (Boehm, 1988): baseada em **análise de riscos**; evolucionário; ideal para sistemas **grandes** (Pressman: > 500 mil LOC).
- **Métodos formais** (Cleanroom), **CBSE/COTS** (2 fases de requisitos: especificação e modificação), **orientado a aspectos** (concern principal × crosscutting), **RUP** (fases Iniciação, Elaboração, Construção, Transição).

---

# MÓDULO II — MÉTODOS ÁGEIS

## 1. Manifesto Ágil (2001)

- 17 especialistas, Utah (Aliança Ágil). **4 valores**: indivíduos/interações **>** processos/ferramentas; software funcionando **>** documentação extensa; colaboração com o cliente **>** negociação de contrato; responder a mudanças **>** seguir um plano.
- *Pegadinha clássica*: valorizam-se **MAIS** os itens à esquerda, **não exclusivamente**. 12 princípios. **Agilidade ≠ velocidade**.

## 2. Scrum

- Framework leve; pilares **TIA** (Transparência, Inspeção, Adaptação). **Sprint** time-boxada **≤ 1 mês**.
- **Papéis**: **Product Owner** (único a priorizar o Product Backlog; garante ROI), **Development Team** (3–9, auto-organizado, multifuncional), **Scrum Master** (servo-líder, remove impedimentos — **jamais PO ao mesmo tempo**).
- **Artefatos**: **Product Backlog** (dinâmico; user stories), **Sprint Backlog** (tarefas, do DT; deve incluir ≥1 item de melhoria da retrospectiva), **Incremento** (**DoD obrigatório**; DoR opcional; Burndown opcional).
- **Eventos**: Planejamento (≤ 8h p/ sprint de 1 mês), Diária (≤ 15 min), Revisão (≤ 4h — foco no produto; PO valida), Retrospectiva (≤ 3h — foco no processo).
- **Scrum Guide 2020** *(complemento)*: 3 **accountabilities** (PO, SM, Scrum Master; "Developers"), **Product Goal** e **Sprint Goal** como compromissos (commitments), "self-managed".
- Story points / Planning Poker (Fibonacci: 1, 2, 3, 5, 8, 13...).

## 3. XP (Kent Beck)

- Práticas: Planejamento Incremental, **Pequenos Releases** (~2 sem), Projeto Simples (**KIS**), **Test-First (TDD)**, **Refactoring**, **Programação em Pares**, **Propriedade Coletiva**, **Integração Contínua**, Ritmo Sustentável (~40h/sem), Metáforas, Cliente On-site.
- **5 valores (CorSim ComFeRe)**: Coragem, Simplicidade, Comunicação, Feedback, Respeito.

## 4. Kanban (David J. Anderson; origem Toyota)

- **Visualizar o fluxo**; **limitar WIP** (sem número mágico); políticas explícitas; medir fluxo; feedback; melhoria contínua; "**comece com o que você tem hoje**".
- **Sem papéis e sem cerimônias prescritas**; **sem iterações por padrão** (Scrumban = Kanban + iterações). Não é metodologia de SDLC (mas bancas o tratam como método ágil).

## 5. Outros

- **FDD**: 5 processos (Modelo Abrangente; Lista de Funcionalidades; Planejar/ Detalhar/ Construir por Funcionalidade); feature em ≤ 2 semanas.
- **TDD**: abordagem de **desenvolvimento** (não de testes); ciclo **Vermelho → Verde → Refatorar**. **ATDD**: foco em aceitação/comunicação.
- **Escalagem (complemento)**: SAFe, LeSS, Nexus — ausentes no material local.

---

# MÓDULO III — ENGENHARIA DE REQUISITOS

## 1. Classificação de requisitos

| Critério | Tipos |
|---|---|
| Abstração | **Usuário** × **Sistema** (ambos podem ser funcionais ou não) |
| Funcionalidade | **Funcionais** ("o que") × **Não-funcionais** ("como"/restrições globais) × de domínio |
| Evolução | **Permanentes** × **Voláteis** (mutáveis, emergentes, consequentes, de compatibilidade) |
| Qualidade (QFD) | Normais, Esperados, **Fascinantes** |
| Origem dos RNF | Produto; **Organizacionais** (ambientais, operacionais, desenvolvimento); **Externos** (**interoperabilidade** é externa!) |

## 2. Fases (Sommerville)

**Viabilidade** (3 perguntas: contribui para os objetivos? é implementável com tecnologia/custo/prazo? integra-se?) → **Elicitação/Análise** → **Especificação** → **Validação** → **Gestão**.

## 3. Elicitação

- 4 atividades: obtenção, classificação, priorização/negociação, documentação.
- Técnicas: entrevistas (pirâmide/funil/diamante), etnografia, cenários, questionários, workshops, brainstorming, **JAD**, prototipação, **reúso (> 80%)**, **user stories** ("Como um \<papel\>, eu quero \<meta\> de modo que \<benefício\>"), **grupo focal (≤ 12)**, VORD.

## 4. Especificação e validação

- **Especificação** = contrato entre partes (requisitos de usuário + de sistema).
- **Validação**: revisão técnica (inspeções em 5 etapas; walkthroughs em 2), prototipação, geração de casos de teste. Atributos: validade, consistência, completude, verificabilidade, **rastreabilidade**.
- **Gestão**: rastreabilidade (origem → requisitos → projeto), matrizes, banco de dados de requisitos.

---

# MÓDULO IV — QUALIDADE E TESTES

## 1. Qualidade

- **QA** (processo, **prevenção**, início) × **QC** (produto, **detecção**, fim; engloba V&V).
- **V&V (Boehm)**: **Verificação** = "construindo o produto corretamente?" (comparação com a **especificação**; ambiente de dev) × **Validação** = "produto correto?" (**expectativas do usuário**; ambiente do usuário).
- **Verificação estática** (inspeção — não executa) × **dinâmica** (teste — executa).
- **Defeito → Erro → Falha (DEF)**: defeito (falta, universo físico) → erro (engano, universo da informação) → falha (comportamento observado diferente do esperado). *Nem todo defeito gera falha.* Pressman: erro = antes da liberação; defeito = depois.
- **ISO 9126**: Funcionalidade, Confiabilidade, Usabilidade, Eficiência, Manutenibilidade, Portabilidade ("EFI gênio fuma pouco"). Métricas: MTTF, MTBF, densidade de defeitos.

## 2. Testes

- **2 metas**: atender requisitos × descobrir defeitos. **Dijkstra**: "testes só mostram a **presença** de erros, não sua ausência".
- **7 princípios**: demonstram presença de defeitos; **exaustivos impossíveis**; testar cedo é mais barato; **Pareto 80/20**; paradoxo do pesticida; dependem do contexto; ausência de defeitos ≠ qualidade.
- **Processo**: Planejamento → Preparação → **Especificação (casos/roteiros)** → Execução → Entrega.
- **Níveis (QUANDO)**: **Unidade** (dev) → **Integração** (interfaces; big bang × incremental; ambiente de dev) → **Validação/Aceitação** (usuário) → **Sistema** (independente).
- **Técnicas (COMO)**: **Caixa-branca** (estrutural, caminhos, complexidade ciclomática) × **caixa-preta** (funcional, partição de equivalência, valor limite) × **caixa-cinza** (híbrida).
- **Tipos (O QUE)**: desempenho (**carga** = dentro dos limites; **estresse** = além, até ruptura), usabilidade, **regressão** (após mudanças), fumaça (showstopper), comparação (2 versões), **alfa** (ambiente do dev) × **beta** (ambiente real), recuperação (MTTR), compatibilidade, segurança.

## 3. Manutenção *(complemento — não detalhada no material)*

- **Corretiva** (defeitos) × **adaptativa** (mudanças de ambiente) × **evolutiva** (novas funcionalidades) × **preventiva** (evitar problemas futuros).

---

# RESUMO DE PEGADINHAS DE PROVA

1. Manifesto: "valorizam-se **MAIS** os itens à esquerda" — nunca "apenas".
2. **DoD obrigatório**; DoR e Burndown **opcionais**.
3. **Scrum Master jamais é PO** ao mesmo tempo; **somente o PO cancela a Sprint**.
4. Prototipagem sem tipo = **Throwaway**.
5. Cascata **não facilita** mudanças; custo de correção ↑ com a detecção tardia.
6. **Kanban**: sem iterações, sem papéis/cerimônias; **limite de WIP** é central.
7. **Verificação = especificação**; **Validação = usuário**.
8. Cadeia **Defeito → Erro → Falha** (DEF).
9. **QA** = prevenção/processo; **QC** = detecção/produto.
10. Estresse **vai além** dos limites; carga **fica dentro**.
11. **Alfa** = ambiente do desenvolvedor; **Beta** = ambiente real.
12. **Integração** ocorre no ambiente de **desenvolvimento**.
13. Teste exaustivo é **impossível**; testes **não provam** correção.
14. **TDD é abordagem de desenvolvimento** (Vermelho-Verde-Refatorar), não de testes.
15. **Interoperabilidade** (RNF) é **externa**, não organizacional.
16. Grupo focal **≤ 12**; reúso de requisitos **> 80%**; RAD **60–90 dias**.
17. Níveis ≠ técnicas ≠ tipos de teste (caixa-branca **não** é nível).
18. User story: "Como um **\<papel\>**, eu quero **\<meta\>** de modo que **\<benefício\>**".

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O Manifesto Ágil preconiza que apenas os itens do lado esquerdo de seus quatro valores devem ser valorizados, sendo vedado o uso de ferramentas, documentação e planos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O manifesto diz que se valorizam **mais** os itens à esquerda — os da direita também têm valor, em menor grau.

---

**Questão 2.** (FCC-style) No Scrum, o artefato que contém o conjunto de funcionalidades desejadas para o produto, priorizado exclusivamente pelo Product Owner, é:
a) Sprint Backlog.
b) Product Backlog.
c) Incremento.
d) Definition of Done.
e) Burndown Chart.

> **Resposta: b.** **Product Backlog** = visão do produto, priorizado pelo **PO**. Sprint Backlog é do DT; Burndown é opcional.

---

**Questão 3.** (CESPE-style) A verificação de software consiste em assegurar que o produto atende às expectativas e necessidades reais do usuário final.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é **validação**. **Verificação** = conformidade com a **especificação** ("construindo o produto corretamente").

---

**Questão 4.** (FCC-style) A sequência correta da cadeia de manifestação de defeitos em software é:
a) Falha → Erro → Defeito.
b) Erro → Defeito → Falha.
c) Defeito → Erro → Falha.
d) Defeito → Falha → Erro.
e) Erro → Falha → Defeito.

> **Resposta: c.** **Defeito → Erro → Falha** (mnemônico DEF). Nem todo defeito gera falha.

---

**Questão 5.** (CESPE-style) O teste de estresse tem por objetivo verificar o comportamento do sistema dentro dos limites de carga acordados com o cliente.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Dentro dos limites = teste de **carga**. **Estresse** vai **além** dos limites, até a degradação/ruptura.

---

**Questão 6.** (FCC-style) No TDD (Test-Driven Development), o ciclo de desenvolvimento é composto por:
a) Projetar, Codificar, Testar, Documentar.
b) Vermelho, Verde, Refatorar.
c) Planejar, Executar, Monitorar, Encerrar.
d) Especificar, Validar, Entregar, Manter.
e) Coletar, Transformar, Carregar, Consultar.

> **Resposta: b.** **Vermelho** (teste falha) → **Verde** (código mínimo) → **Refatorar**. O TDD é abordagem de **desenvolvimento**.

---

**Questão 7.** (CESPE-style) No Kanban, é recomendado o uso de iterações fixas (sprints) como prática central do método.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Kanban **não** adota iterações por padrão (limita WIP e trabalha em fluxo contínuo). A combinação com iterações é o **Scrumban**.

---

**Questão 8.** (FCC-style) Entre as técnicas de elicitação de requisitos, o grupo focal recomenda a participação de no máximo:
a) 5 pessoas.
b) 8 pessoas.
c) 12 pessoas.
d) 20 pessoas.
e) 30 pessoas.

> **Resposta: c.** Grupo focal: **até 12** participantes.

---

**Questão 9.** (CESPE-style) O requisito não funcional de interoperabilidade classifica-se como requisito de origem organizacional.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Interoperabilidade é RNF de origem **externa** (fatores fora do controle da organização). Organizacionais: ambientais, operacionais e de desenvolvimento.

---

**Questão 10.** (FCC-style) O nível de teste que verifica a interação entre componentes/módulos do sistema, antes da validação pelo usuário, é o teste de:
a) unidade.
b) integração.
c) aceitação.
d) desempenho.
e) regressão.

> **Resposta: b.** **Integração** testa interfaces entre componentes. Unidade = lógica interna; aceitação = visão do usuário.

---

**Questão 11.** (CESPE-style) Em testes de software, a técnica de caixa-preta baseia-se na estrutura interna do código e na análise de caminhos independentes.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Estrutura interna/caminhos = **caixa-branca**. **Caixa-preta** testa comportamento/funcionalidade, sem olhar o código (partição de equivalência, valor limite).

---

**Questão 12.** (FGV-style) Sobre o prototipação de software, é correto afirmar:
a) Quando o tipo não é especificado, entende-se o protótipo evolucionário.
b) O protótipo descartável (throwaway) é implementado para ser mantido e evoluído.
c) O protótipo descartável (throwaway) é utilizado para explorar requisitos e é descartado após a validação.
d) Protótipos servem apenas à fase de testes.
e) O protótipo evolucionário é sempre descartado após a especificação.

> **Resposta: c.** Sem tipo especificado = **throwaway** (descartável); o **evolucionário** é o que permanece e evolui.

---

**Questão 13.** (CESPE-style) O Scrum Master pode acumular a função de Product Owner em equipes pequenas, desde que haja autorização do cliente.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Os papéis são **incompatíveis** — o Scrum Master **jamais** é simultaneamente o PO.

---

**Questão 14.** (FCC-style) O modelo de processo de software baseado na análise e redução de riscos, com ciclos espirais de quatro a setores, é o modelo:
a) cascata.
b) RAD.
c) espiral.
d) incremental.
e) em V.

> **Resposta: c.** **Espiral** (Boehm) = análise de riscos; 4 setores por ciclo; indicado para sistemas grandes.

---

**Questão 15.** (CESPE-style) A qualidade de garantia (QA) foca na detecção de defeitos no produto final, ao passo que o controle de qualidade (QC) foca na prevenção por meio de processos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **QA** = prevenção/**processo**; **QC** = detecção/**produto** (engloba verificação e validação).

---

## Questões discursivas

**D1.** Diferencie verificação e validação de software e relacione-as com os ambientes de desenvolvimento e do usuário.

> **Modelo de resposta:** **Verificação** assegura que o software está sendo **construído corretamente**, comparando-o com a **especificação de requisitos** — tipicamente em ambiente de desenvolvimento. **Validação** assegura que foi construído o **produto correto**, atendendo às **expectativas do usuário** — tipicamente em ambiente do usuário (aceitação). A verificação é mais associada a inspeções/estática; a validação, a testes de aceitação.

**D2.** Explique os quatro valores do Manifesto Ágil e diferencie Scrum de Kanban.

> **Modelo de resposta:** Os valores do Manifesto valorizam **mais**: indivíduos e interações sobre processos e ferramentas; software funcionando sobre documentação extensa; colaboração com o cliente sobre negociação de contrato; e responder a mudanças sobre seguir um plano (sem excluir os itens da direita). **Scrum** é framework iterativo com **sprints** time-boxadas (≤ 1 mês), papéis (PO, SM, DT) e eventos fixos; **Kanban** é método de gestão de fluxo contínuo, **sem iterações nem papéis prescritos**, centrado em **visualizar o fluxo** e **limitar o WIP**, com melhoria evolutiva a partir do processo atual.

---

*Base: `03.Engenharia de Software` (Aulas 00–05, 09–10) e `04.Desenvolvimento de Software` (Aulas 14, 17). Complemento: Scrum Guide 2020 (product/sprint goal, commitments), tipos de manutenção e frameworks de escala (ausentes na base de 2020).*