# APOSTILA — TÓPICO 2: GESTÃO DE PROJETOS E GOVERNANÇA DE TI
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Gestão de Projetos e Governança de TI: PMBOK 8ª Edição; ITIL Version 5; COBIT 2019.
>
> **Base de conhecimento:** `05.Governança de TI` (Curso Regular TI 2020.2 — PMBOK 6ª, ITIL v3/v4, COBIT 5 e 2019) + **complemento** para as versões que o edital exige (PMBOK 8ª; ITIL atual).

---

# MÓDULO I — GOVERNANÇA DE TI

## 1. Conceito

- **TI (ISO/IEC 38500)**: recursos para **adquirir, processar, armazenar e disseminar informações** — o cerne é a **informação**, não a tecnologia.
- **Governança de TI (Forrester)**: processo de tomada de decisões sobre a TI. **(ITGI)**: responsabilidade da **alta administração**, garantindo que a TI sustente e estenda as estratégias do negócio.
- **Níveis de planejamento**: **estratégico → tático → operacional**. Alinhamento **negócio ↔ TI**.
- Frameworks de referência: **COBIT**, **ITIL**, **CMMI**, **PMBOK**.

## 2. Governança × Gestão (COBIT)

| | Governança | Gestão |
|---|---|---|
| Verbos | **Avaliar**, **Dirigir**, **Monitorar** | **Planejar**, **Construir**, **Executar**, Monitorar |
| Domínio | EDM | APO + BAI + DSS + MEA |
| Responsável | Conselho de administração | Diretoria executiva (CEO) |
| Foco | Necessidades das partes interessadas, direção, conformidade | Executar conforme a direção |

---

# MÓDULO II — COBIT 2019

## 1. Fundamentos

- Framework de **governança e gestão de I&T empresarial** (Enterprise I&T — não só o departamento de TI); sucessor do COBIT 5.
- **3 resultados da EGIT**: realização de **benefícios**; otimização de **risco** (preservar valor); otimização de **recursos**.
- **6 princípios do sistema de governança**: (1) toda empresa precisa de um sistema de governança (equilíbrio benefícios–riscos–recursos); (2) construído por **componentes** que atuam holísticamente; (3) **dinâmico**; (4) **distingue governança de gestão**; (5) **adaptado** (design factors); (6) **ponta a ponta** (não só TI). **3 princípios do framework**: baseado em modelo conceitual; aberto e flexível; alinhado a padrões/regulamentos.
- **7 componentes**: processos; estruturas organizacionais; princípios/políticas/procedimentos; informações; cultura, ética e comportamento; pessoas/habilidades; serviços, infraestrutura e aplicativos. Podem ser **genéricos** ou **variantes**.
- **Design factors** (11) e **áreas de foco (focus areas)**: estratégia empresarial, metas, perfil de risco, cenário de ameaças, requisitos de conformidade, papel do TI, sourcing, métodos de implementação, adoção de tecnologia, porte da empresa etc.
- **Goals Cascade**: necessidades das partes interessadas → **metas empresariais (13)** → **metas de alinhamento** → priorização dos objetivos de gestão.
- **5 domínios** (verbos = propósito):
  - **EDM** — Avaliar, Dirigir e Monitorar (**governança**, conselho)
  - **APO** — Alinhar, Planejar e Organizar
  - **BAI** — Construir, Adquirir e Implementar
  - **DSS** — Entrega, Serviço e Suporte
  - **MEA** — Monitorar, Avaliar e Analisar
- **CPM (COBIT Performance Management)** + **níveis de capacidade 0 a 5** (baseados no **CMMI**): **capacidade** associa-se a **processos**; **maturidade**, a **áreas de foco**.
- **O que o COBIT NÃO é** (clássico de CESPE): não é descrição completa do ambiente de TI; não é estrutura para processos de negócio; não é framework técnico de toda tecnologia; **não prescreve decisões** (define **quais** decisões tomar, **como** e **por quem**).
- Publicações COBIT 2019: Introduction and Methodology; Governance and Management Objectives; Design Guide; Implementation Guide.

## 2. COBIT 5 (base histórica)

- **5 princípios**: atender necessidades das partes interessadas (cascata de objetivos); cobrir a organização **ponta a ponta**; modelo único integrado; abordagem holística (**habilitadores**); distinguir governança de gestão.
- **37 processos** em 5 domínios (5 EDM + 32 de gestão).
- *COBIT 5 × 2019*: "habilitadores" → "**componentes**"; novos **design factors** e focus areas; mesmos 5 domínios.

---

# MÓDULO III — ITIL

## 1. ITIL 4 (versão atual — edital "ITIL Version 5")

> O material local cobre **ITIL v3 e ITIL 4**; o edital menciona "ITIL Version 5" — na prática, a família ITIL publicada é a **ITIL 4** (com atualizações posteriores do Axelos). Estude ITIL 4 como base e trate o nome do edital como sinônimo da versão corrente.

- **História**: CCTA (governo britânico, anos 1980) → v2 (2001) → v3 (2007, ciclo de vida) → 2011 → **ITIL 4 (2019)**.
- **Valor**: **co-criação** entre provedor, consumidor e terceiros (percebido). **Utilidade** = "o que o serviço faz" (fit for purpose) × **Garantia/warranty** = "como performa" (disponibilidade, capacidade, segurança, continuidade — fit for use).
- **7 princípios norteadores**: 1) Foco no valor; 2) **Começar de onde você está** (não começar do zero); 3) Progredir iterativamente com feedback; 4) Colaborar e promover visibilidade (**colaboração ≠ consenso**); 5) Pensar e trabalhar holísticamente; 6) Manter simples e prático; 7) **Otimizar e automatizar**.
- **4 dimensões do gerenciamento de serviço**: 1) Organizações e pessoas; 2) Tecnologia e informação; 3) Parceiros e fornecedores; 4) Fluxos de valor e processos.
- **SVS (Sistema de Valor do Serviço)** — 5 componentes: Princípios norteadores; Governança; Cadeia de valor de serviço; Práticas; Melhoria contínua. Entradas = oportunidade e demanda; saídas = valor. Inimigo: silos organizacionais.
- **Cadeia de valor (6 atividades)**: **Planejar, Melhorar, Engajar, Desenho e transição, Obter/Construir, Entrega e suporte**. Todas as interações externas passam por **Engajar**; novos recursos, por **Obter/Construir**. *Produtos, serviços, demanda e valor NÃO são atividades* (são componentes do SVS — pegadinha).
- **34 práticas**: **13 gerais** (melhoria contínua, segurança da informação, conhecimento, risco, portfólio, relacionamento, financeiro de serviço, estratégia, fornecedor, força de trabalho...), **17 de serviço** (incidente, problema, mudança, catálogo, nível de serviço, configuração, disponibilidade, capacidade, continuidade, liberação, central de serviço...), **3 técnicas** (implantação; infraestrutura e plataforma; desenvolvimento de software).
- Conceitos: **incidente** = interrupção imprevista (restaurar rápido) ≠ **problema** = causa raiz (prevenir recorrência) ≠ **requisição** = solicitação normal. **ICs** (itens de configuração) = configuração de serviço.

## 2. ITIL v3 (ainda cobrado)

- **5 estágios do ciclo de vida**: **Estratégia de Serviço** (núcleo) → **Desenho** → **Transição** → **Operação** → **Melhoria Contínua** (7 passos, baseado no **PDCA**).
- **Funções só na Operação**: Central de Service Desk (local/centralizada/virtual/**Follow the Sun**), Gerenciamento Técnico, Operações de TI, Aplicações.
- **SLA** (acordo com o **cliente**) × **OLA** (acordo **interno**) × **UC** (contrato com **terceiros**). 3 formas de SLA: por serviço, por cliente, multinível.
- **Catálogo de serviços**: visão de **negócio** × visão **técnica**. Portfólio = funil + catálogo + obsoletos.
- **4 Ps do Desenho**: Pessoas, Parceiros, Processos, Produtos.
- *ITIL v3 × 4*: processos/funções → **práticas**; entrega de valor → **co-criação**; 5 livros → **SVS + cadeia de valor**.

---

# MÓDULO IV — PMBOK (GESTÃO DE PROJETOS)

> O edital pede **PMBOK 8ª Edição**; o material local é **6ª (2017)**. Os fundamentos (projeto, ciclo de vida, áreas de conhecimento, restrições) permanecem; a 7ª (2021) substituiu "49 processos/10 áreas" por **12 princípios + 8 domínios de performance**; a 8ª é continuação dessa abordagem. Abaixo, a base clássica + o complemento da 7ª/8ª.

## 1. Fundamentos (clássicos, válidos em qualquer edição)

- **Projeto** = esforço **temporário** para criar um produto, serviço ou resultado **exclusivo**. **Operação** = contínua e repetitiva (não é projeto). Projeto **pode gerar** uma nova operação.
- **Gerenciamento de projetos** = equilibrar restrições conflitantes: **escopo, qualidade, cronograma (tempo), orçamento (custo), recursos e riscos**.
- **Ciclo de vida**: preditivo (cascata), **adaptativo (ágil)**, iterativo, incremental, híbrido. Influência das partes interessadas e risco altos no **início**; custo de mudança cresce com o tempo.
- **5 grupos de processos** (≠ fases do ciclo de vida): **Iniciação, Planejamento, Execução, Monitoramento e Controle, Encerramento**. PMBOK 6: **49 processos × 10 áreas**.
- **Iniciação**: **Termo de Abertura (Project Charter)** + registro das partes interessadas.
- **10 áreas (PMBOK 6)**: Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos, Aquisições, Partes Interessadas.
- **Escopo**: escopo do **projeto** (trabalho) × escopo do **produto** (características). **EAP/WBS** = decomposição **orientada a entregas**; menor nível = **pacote de trabalho**. **Scope creep** = aumento não controlado. **Validar escopo** (aceitação do cliente) ≠ **Controlar qualidade** (cumprimento de requisitos).
- **Cronograma**: **CPM** (caminho crítico = atividades **sem folga**; define a duração total) × tarefas com folga.
- **Custos**: **PERT** — estimativa de 3 pontos: **triangular tE = (tO + tM + tP)/3**; **beta tE = (tO + 4tM + tP)/6**.
- **Riscos**: identificar; análise **qualitativa** (matriz probabilidade × impacto) × **quantitativa** (efeito numérico); planejar e **implementar respostas**; monitorar.
- **Mudanças PMBOK 5 → 6**: **+3 processos** (Gerenciar o Conhecimento do Projeto; Controlar os Recursos; Implementar Respostas aos Riscos), **−1** (Encerrar Aquisições) = **49**. **Tempo → Cronograma**; **RH → Recursos** (inclui materiais).

## 2. PMBOK 7ª/8ª — complemento (domínios de performance)

*(A 7ª edição (2021) reestruturou o guia; a 8ª dá continuidade.)*
- **12 princípios**: ser um administrador diligente, respeitar e cuidar das pessoas, engajar as partes interessadas, focar no valor, pensar sistemicamente, **liderar**, **adaptar baseado no contexto**, **construir qualidade**, **navegar na complexidade**, otimizar respostas a riscos, **adotar adaptabilidade e resiliência**, permitir a mudança.
- **8 domínios de performance** (substituem o foco em "áreas"): **Partes Interessadas; Equipe; Abordagem de Desenvolvimento e Ciclo de Vida (preditivo/ágil/híbrido); Planejamento; Trabalho do Projeto; Entrega; Medida; Incerteza**.
- Ênfase: **resultados e performance** (não só processos), tailoring (adaptação ao contexto), governança do projeto, métricas de valor entregue.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **Governança** (conselho, EDM: avaliar/dirigir/monitorar) ≠ **gestão** (CEO: planejar/construir/executar).
2. **COBIT não prescreve decisões** — define quais, como e por quem decidir.
3. Cascata COBIT: stakeholders → **13 metas empresariais** → metas de alinhamento → objetivos de gestão.
4. **Capacidade** (processos, 0–5, CMMI) × **maturidade** (áreas de foco).
5. **COBIT 5: habilitadores** → **COBIT 2019: componentes**; domínios **EDM/APO/BAI/DSS/MEA** mantidos.
6. ITIL: **incidente** ≠ **problema** ≠ **requisição**.
7. **SLA** (cliente) × **OLA** (interno) × **UC** (terceiro).
8. ITIL 4: **utilidade** (o que faz) × **garantia** (como performa); **valor é co-criado**.
9. **Cadeia de valor tem 6 atividades** — produtos/serviços/demanda/valor **não** são atividades.
10. **Colaboração ≠ consenso** (ITIL 4).
11. **4 Ps** (v3) ≠ **4 dimensões** (ITIL 4).
12. **Grupos de processos ≠ fases do ciclo de vida** (PMBOK).
13. **Projeto** = temporário + exclusivo; "contínuo e repetitivo" = **operação**.
14. PMBOK 6: **49 processos / 10 áreas / 5 grupos**; **caminho crítico não é área** de conhecimento.
15. **EAP**: decomposição por **entregas**; menor nível = **pacote de trabalho**.
16. **PERT beta = (O + 4M + P)/6**; triangular = (O + M + P)/3.
17. **Validar escopo** = aceitação (cliente); **controlar qualidade** = requisitos.
18. PMBOK 7ª/8ª: **princípios + domínios de performance** (não "49 processos" — mantenha o dual para o edital).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) No COBIT 2019, a função da governança de TI é planejar, construir, executar e monitorar as atividades de TI, conforme a direção definida pelo conselho de administração.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Essas são as atividades da **gestão** (APO/BAI/DSS/MEA). A **governança** (EDM) **avalia necessidades, define a direção e monitora** desempenho e conformidade — responsabilidade do **conselho**.

---

**Questão 2.** (FCC-style) O domínio do COBIT 2019 exclusivamente dedicado à governança, e de responsabilidade do conselho de administração, é:
a) APO.
b) BAI.
c) DSS.
d) EDM.
e) MEA.

> **Resposta: d.** **EDM** (Evaluate, Direct and Monitor) = governança. APO/BAI/DSS/MEA = gestão.

---

**Questão 3.** (CESPE-style) O COBIT 2019 tem como característica prescrever as melhores decisões de TI para cada organização, indicando a estratégia, a arquitetura e o orçamento ideais.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O COBIT **não prescreve** decisões — define **quais** decisões devem ser tomadas, **como** e **por quem**.

---

**Questão 4.** (FCC-style) Na cadeia de valor do serviço (ITIL 4), a atividade por onde passam todas as interações externas com clientes, usuários e fornecedores é:
a) Planejar.
b) Engajar.
c) Melhorar.
d) Obter/Construir.
e) Entrega e suporte.

> **Resposta: b.** **Engajar** = todas as interações externas. Novos recursos passam por **Obter/Construir**.

---

**Questão 5.** (CESPE-style) Na ITIL 4, o conceito de garantia (warranty) refere-se ao que o serviço faz para atender à necessidade do cliente, enquanto utilidade refere-se ao seu desempenho.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **utilidade** = o que o serviço faz (adequado à finalidade); **garantia** = como performa (disponibilidade, capacidade, segurança, continuidade — adequado ao uso).

---

**Questão 6.** (FCC-style) No ITIL, a causa raiz de um ou mais incidentes, cuja análise visa prevenir a recorrência, é registrada como:
a) incidente.
b) requisição de serviço.
c) problema.
d) mudança.
e) evento.

> **Resposta: c.** **Problema** = causa raiz. **Incidente** = interrupção imprevista (restaurar o serviço). **Requisição** = solicitação padrão.

---

**Questão 7.** (CESPE-style) O SLA (Service Level Agreement) é o acordo de nível de serviço firmado entre a área de TI e um fornecedor externo.
a) Certo. b) Errado.

> **Resposta: b (Errado).** SLA é com o **cliente**. Com **terceiros/fornecedores** é o **UC (Underpinning Contract)**; acordos **internos** são **OLAs**.

---

**Questão 8.** (FCC-style) No PMBOK, o documento que formalmente autoriza a existência de um projeto e confere autoridade ao gerente para aplicar recursos é:
a) Termo de Abertura do Projeto (Project Charter).
b) Plano de Gerenciamento do Projeto.
c) EAP (WBS).
d) Termo de Referência.
e) Matriz de partes interessadas.

> **Resposta: a.** **Project Charter** autoriza o projeto na **Iniciação** e nomeia o gerente.

---

**Questão 9.** (CESPE-style) Os cinco grupos de processos do PMBOK (Iniciação, Planejamento, Execução, Monitoramento e Controle e Encerramento) equivalem às fases do ciclo de vida do projeto.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Grupos de processos ≠ fases**. Os grupos são agrupamentos lógicos de processos e podem ocorrer em qualquer fase; as fases dependem do ciclo de vida (preditivo, ágil...).

---

**Questão 10.** (FCC-style) Pela estimativa PERT beta, considerando os tempos otimista (tO = 10), provável (tM = 12) e pessimista (tP = 20), a duração esperada é:
a) 12.
b) 13.
c) 14.
d) 15.
e) 16.

> **Resposta: c.** tE = (tO + 4tM + tP)/6 = (10 + 48 + 20)/6 = 78/6 = **13**. (Fórmula beta; a triangular daria 14.)

---

**Questão 11.** (CESPE-style) A EAP (Estrutura Analítica do Projeto) é uma decomposição hierárquica do escopo orientada a entregas, cujo nível mais baixo é o pacote de trabalho.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **EAP/WBS** decompõe o escopo por **entregas**; o menor nível é o **pacote de trabalho** (produto/entrega, não atividade).

---

**Questão 12.** (FGV-style) Sobre os princípios norteadores da ITIL 4, é correto afirmar:
a) "Começar de onde você está" recomenda descartar os processos existentes e reiniciar.
b) Colaborar e promover visibilidade significa que todas as decisões exigem consenso unânime.
c) Otimizar e automatizar deve vir antes de simplificar o trabalho.
d) Progredir iterativamente com feedback permite melhorias incrementais e validação contínua.
e) Pensar e trabalhar holísticamente significa atuar em silos por especialidade.

> **Resposta: d.** "Começar de onde você está" = **não** começar do zero; colaboração **não** é consenso; primeiro **manter simples e prático**, depois otimizar/automatizar; holístico = **anti-silo**.

---

**Questão 13.** (CESPE-style) No PMBOK 6ª edição, foram acrescentados os processos "Gerenciar o Conhecimento do Projeto", "Controlar os Recursos" e "Implementar Respostas aos Riscos", totalizando 49 processos.
a) Certo. b) Errado.

> **Resposta: a (Certo).** +3 (Conhecimento, Controlar Recursos, Implementar Respostas aos Riscos) e −1 (Encerrar Aquisições) → **49 processos**.

---

**Questão 14.** (FCC-style) O caminho crítico de um projeto corresponde:
a) à maior sequência de atividades com folga, que permite folga no cronograma.
b) à sequência de atividades sem folga, que determina a duração total do projeto.
c) à soma dos custos das atividades do projeto.
d) ao grupo de processos de Monitoramento e Controle.
e) à fase de maior risco do ciclo de vida.

> **Resposta: b.** Caminho crítico = atividades **sem folga** (float zero); define a **duração total**. Atraso em qualquer uma atrasa o projeto.

---

**Questão 15.** (CESPE-style) Segundo o COBIT 2019, a capacidade de um processo está associada às áreas de foco (focus areas), enquanto a maturidade está associada aos processos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **capacidade** ↔ **processos** (níveis 0–5, base CMMI); **maturidade** ↔ **áreas de foco**.

---

## Questões discursivas

**D1.** Diferencie governança e gestão de TI segundo o COBIT 2019 e cite os três resultados esperados da EGIT.

> **Modelo de resposta:** A **governança** (domínio EDM) cabe ao **conselho de administração**: **avalia** as necessidades das partes interessadas, **define a direção** (priorização e decisões) e **monitora** desempenho e conformidade. A **gestão** (APO, BAI, DSS, MEA) cabe à **diretoria executiva**: **planeja, constrói, executa e monitora** em alinhamento à direção. Os três resultados da EGIT são: **realização de benefícios**, **otimização de risco** (preservar/atentar valor) e **otimização de recursos**.

**D2.** Descreva a cadeia de valor do serviço da ITIL 4 e explique a diferença entre utilidade e garantia de um serviço.

> **Modelo de resposta:** A cadeia de valor tem **6 atividades**: Planejar, Melhorar, Engajar, Desenho e transição, Obter/Construir e Entrega e suporte — todas as interações externas passam por **Engajar**. **Utilidade** (fit for purpose) = **o que o serviço faz** para atender à necessidade do cliente; **Garantia** (warranty, fit for use) = **como o serviço performa**: disponibilidade, capacidade, segurança e continuidade. O **valor** é **co-criado** entre provedor, consumidor e terceiros.

---

*Base: `05.Governança de TI` (Aulas 00–08 e material extra de ITIL v4, COBIT 2019) do material local (2020). Complemento: atualizações PMBOK 7ª/8ª (princípios e domínios de performance) — o material local cobre o PMBOK 6ª; ITIL 4 como versão corrente do edital ("ITIL Version 5").*