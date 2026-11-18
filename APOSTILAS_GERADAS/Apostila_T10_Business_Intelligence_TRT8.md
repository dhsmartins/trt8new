# APOSTILA — TÓPICO 10: BUSINESS INTELLIGENCE (BI)
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Business Intelligence (BI): Pipeline de dados; Fundamentos, orquestração, integração, ETL. Business Intelligence; Processo de coleta, organização, análise e compartilhamento de informações.
>
> **Base de conhecimento:** `11.Business Intelligence` (Aulas 00–11 — Curso Regular TI 2020.2, Prof. Thiago Rodrigues Cavalcanti) + **complemento** (orquestração moderna de pipelines, dashboards/KPIs, ELT).

---

# MÓDULO I — FUNDAMENTOS: DIKW E TIPOS DE DADOS

## 1. Hierarquia DIKW

- **Dado** → **Informação** → **Conhecimento** → **Inteligência** → (Experiência).
  - **Dado**: fatos brutos, não organizados/interpretados ("sinais que não foram processados, correlacionados, integrados, avaliados ou interpretados"). Matéria-prima da informação.
  - **Informação**: dado + contexto, relevância e propósito (ex.: "Idade de Thiago = 34"). Geração muito automatizável (formatação, tradução, fusão).
  - **Conhecimento**: informação contextual, relevante e acionável ("informação em ação" — Turban); inclui reflexão e síntese; frequentemente **tácito**, difícil de estruturar/capturar/transmitir. Resulta da avaliação da informação quanto a confiabilidade e relevância.
  - **Inteligência**: conhecimento que permite **agir com vantagem** no ambiente; síntese humana (julgamento + intuição). **Experiência** = efetividade da inteligência da organização.
- *Pegadinha CESPE (TCM-BA/2018)*: relatório de vendas por faixa/região = **informação** (ainda não avaliado quanto a confiabilidade/relevância — o gestor faz isso depois).

## 2. Tipos de dados

- **Estruturados** (tabelas/BD relacional), **semiestruturados** (XML, tags), **não estruturados** (texto, imagem, som).
- **Dados abertos**: 3 leis + 8 princípios (2007, Califórnia); **Instrução Normativa nº 4/2012 (INDA)**; publicados "na forma coletada na fonte, com a mais fina granularidade possível".

## 3. Sistemas de informação (SI)

- SI = componentes que **coletam, processam, armazenam e distribuem** informações para apoiar decisão, coordenação e controle. Atividades: entrada (coleta) → processamento → saída (distribuição). **Dimensões**: organização, gestão e tecnologia. Vantagem competitiva via modelo de forças de Porter.

---

# MÓDULO II — DATA WAREHOUSE, DATA MARTS E MODELAGEM MULTIDIMENSIONAL

## 1. Business Intelligence

- **BI**: técnicas, métodos e ferramentas de **análise de dados** para subsidiar processos de **decisão** (gabarito clássico de questão). Componentes (Turban); **Self-BI** (usuário final explora dados); governança de dados; **inteligência competitiva (CI)**.

## 2. Data Warehouse (DW)

- **DW**: repositório **orientado a assunto, integrado, histórico e não volátil** (Kimball/Inmon) para apoio à decisão.
- **Granularidade** (nível de sumarização) = **"o mais importante aspecto do projeto de um DW"** (Kimball). Granularidade alta (mais detalhe) ⇒ mais disco; granularidade baixa (sumarizado) ⇒ menos disco/índices, menos detalhe.
- **Kimball × Inmon**:
  - **Kimball**: **bottom-up** — **Data Marts** primeiro (por assunto/área), DW incremental; produção em 2–3 meses.
  - **Inmon**: **top-down** — **DW corporativo** primeiro; dele extraem-se dados/metadata para Data Marts, mais sumarizados.
- **Data Mart**: subconjunto do DW por **assunto/departamento**; também citado como área intermediária criada pelo ETL na transição OLTP→DW.

## 3. Modelagem multidimensional

- **Medidas**: **aditivas** (somam em qualquer dimensão — ex.: lucro líquido); **semiaditivas** (somáveis só em algumas dimensões — ex.: saldo em conta, que **não soma no tempo**); **não aditivas** (nunca somáveis — ex.: taxas/percentuais).
- **Esquema estrela**: 1 tabela **fato** central + **dimensões** em relação **1-N** (PK da fato composta pelas FKs das dimensões).
- **Floco de neve**: dimensões **normalizadas** em múltiplos níveis (3FN).
- **Constelação (galáxia)**: **várias tabelas fato** compartilhando dimensões.

---

# MÓDULO III — ETL (EXTRACT, TRANSFORM, LOAD) E PIPELINE DE DADOS

## 1. Definição e arquitetura

- **ETL**: conjunto de processos que traz dados de sistemas **OLTP** (e hoje websites, e-mails, redes sociais, planilhas) para um DW; **integra**, **transforma** para o formato desejado e **carrega** no destino. Funciona em lote ou tempo real, síncrono/assíncrono, físico/virtual.
- **Back room × front room** (analogia do restaurante): a "cozinha" (**staging**) é acessível só à equipe de ETL — **nenhum serviço de consulta** é fornecido na back room. O ETL consome **~70% dos recursos** de implementação/manutenção de um DW e **80% do tempo** de desenvolvimento (~1/3 do orçamento é ETL + limpeza).

## 2. As 4 etapas (Kimball)

1. **Extração**: dados brutos em disco, mínima reestruturação, restart fácil.
2. **Limpeza**: valores válidos, consistência, deduplicação, regras de negócio; pode exigir julgamento humano; **irreversível** (salvar resultados).
3. **Conformidade**: mesclar fontes (rótulos idênticos, medidas racionalizadas; acordo corporativo de domínios/medidas).
4. **Entrega**: estruturar em modelos dimensionais/estrela — base para cubos OLAP.

- **34 subsistemas Kimball** (agrupados): extração (1–3: data profiling, **CDC – Change Data Capture** com audit columns, timed extracts, full diff compare, database log scraping, message queue monitoring); limpeza/conformidade (4–8: limpeza, esquema de eventos de erro, dimensão de auditoria, deduplicação/sobrevivência, conformidade); entrega (9–21: **SCD**, **gerador de chave substituta** — mantém integridade referencial fato↔dimensão —, hierarquias, dimensões especiais); **gestão/orquestração** (22–34: agendamento por tempo/evento, captura de metadados, **logging para recuperação/reinicialização**, notificação sem intervenção humana, controle de versão, ambientes dev/teste/prod, backup, monitor de fluxo de trabalho com painel de status/desempenho).

## 3. ETL × ELT

| Critério | ETL | ELT |
|---|---|---|
| Ordem | Extrai → **transforma fora** → carrega | Extrai → **carrega** → transforma **no destino** |
| Onde transforma | Área de staging separada | Dentro do DW de destino (staging tables lá) |
| Papel do DW | Recebe dados já conformados | É **também** o motor de transformação |

*Gabarito FEPESE/JUCESC-2017: ELT transforma no DW de destino.*

## 4. Pipeline de dados e orquestração *(complemento)*

- **Pipeline** = fluxo contínuo de coleta → integração → transformação → carga → consumo. **Orquestração** = agendamento, dependências, reexecução e monitoramento dos fluxos (no material: subsistemas 22–34; na prática moderna: **Airflow, Luigi, Prefect, dbt** — ausentes da base).
- **Metadados**: dados sobre dados (linhagem, dicionário) — essenciais para governança e recuperação.
- Ciclo do edital: **coletar → organizar → analisar → compartilhar** informações (relaciona-se ao SI e ao BI).

---

# MÓDULO IV — OLAP E ANÁLISE

## 1. OLAP

- **OLAP** (On-Line Analytical Processing): processamento dedicado ao **suporte à decisão** via visualização de dados **agregados em múltiplas dimensões** (tempo, espaço, produto...) sobre DW/DM. **Não é banco de dados** e **não registra dados** (é ferramenta de manipulação/análise).

## 2. OLAP × OLTP

| | OLTP | OLAP |
|---|---|---|
| Função | **Atualização** de transações | **Análise** para decisão |
| Dados | Atualizados, atomizados | Sumarizados, **históricos** |
| Modelo | **Normalizado** | **Dimensional** (estrela/floco) |
| Volume | Poucos registros/consulta | Muitos registros |
| Consultas | Simples, < 1 s | Complexas, ad hoc |
| Ferramenta MS | SSMS | **SSAS** (Analysis Services) |

- *Outras ferramentas citadas na base: Cognos, Business Objects.*

## 3. Operações OLAP

- **Granularidade** (quanto mais detalhe, **menor** a granularidade); **roll-up** (drill-up: sobe a hierarquia, agrega); **drill-down** (desce a hierarquia ou adiciona dimensão); **slice** (seleciona **1** dimensão → subcubo) e **dice** (2+ dimensões); **pivot/rotate** (gira eixos).

## 4. Arquiteturas de servidor OLAP

- **MOLAP**: multidimensional proprietário (arrays/matriz esparsa), cubos **pré-calculados**, melhor desempenho; risco de **explosão de dados**; indicado a Data Marts.
- **ROLAP**: BD **relacional** (estrela/floco), SQL otimizado; escala mais dados; tecnologia madura.
- **HOLAP**: híbrido (relacional para menor granularidade + dimensional para agregados).
- **DOLAP** (desktop/portabilidade), **SOLAP** (espacial + SIG), WOLAP/MOLAP mobile.
- **12 regras de avaliação de produtos OLAP** (Codd): visão multidimensional, transparência, acessibilidade, desempenho consistente, cliente-servidor, dimensionalidade genérica, matriz esparsa dinâmica, multiusuário, cruzamento irrestrito, manipulação intuitiva, relatório flexível, dimensões/agregações ilimitadas.

## 5. Mineração de dados e Big Data

- **Mineração (data mining)**: descoberta (auto/semiautomática) de **padrões significativos** (previsões não triviais, vantagem econômica). Fases: seleção/coleta, avaliação de qualidade, preparação (coleta, limpeza, transformação, integração, formatação). Noções de aprendizado de máquina (ver tópico 9).
- **Big Data**: dimensões dos dados; **8 falácias** (ex.: "Big Data pode prever o futuro" — falsa). Tipos de análise.

## 6. Dashboards e KPIs *(complemento — esparsos na base)*

- **KPI** (Key Performance Indicator): indicador-chave de desempenho ligado a objetivo; **scorecard** = painel comparativo com metas. **Dashboard** = painel visual para monitoramento (no material, só "painel" no monitor de fluxo do ETL e menções a indicadores).
- **Compartilhamento**: relatórios, dashboards, portais de self-service BI.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **DIKW**: dado → informação → conhecimento → inteligência. Relatório pronto = **informação**, não conhecimento.
2. **Granularidade** é o aspecto **mais importante** do projeto de DW.
3. **ETL = ~70% dos recursos e 80% do tempo** de DW; **back room não serve consultas**.
4. **ELT transforma no DW de destino** (staging tables lá).
5. **Kimball = bottom-up** (Data Marts primeiro); **Inmon = top-down** (DW corporativo primeiro).
6. **Medidas semiaditivas** não somam em todas as dimensões (saldo × tempo).
7. **OLAP não é banco de dados** e **não registra dados**; MOLAP = cubos pré-calculados; ROLAP = relacional/estrela.
8. **Slice = 1 dimensão**; **dice = 2+**; roll-up sobe; drill-down desce.
9. **Limpeza (ETL) é irreversível** — salvar resultados.
10. **SCD** e **chave substituta** mantêm integridade referencial fato↔dimensão (subsistemas Kimball 9–21).
11. **Estrela** = fato + dimensões não normalizadas; **floco** = dimensões normalizadas (3FN); **constelação** = várias fatos.
12. **CDC** = Change Data Capture (captura de mudanças via audit columns/logs).
13. **SI coleta, processa, armazena e distribui** — dimensões: organização, gestão, tecnologia.
14. **Big Data**: "pode prever o futuro" = falácia clássica.
15. **Inmon** gera Data Marts **do DW**; **Kimball** constrói o DW **dos Data Marts**.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) Um relatório de vendas por faixa etária, região e modelo de produto constitui conhecimento organizacional, pois já está processado e formatado.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É **informação** (dado + contexto/formatação). **Conhecimento** exige avaliação quanto a confiabilidade/relevância e aplicação — tarefa do gestor.

---

**Questão 2.** (FCC-style) No projeto de um Data Warehouse, o aspecto considerado o mais importante por Kimball é:
a) a escolha do SGBD.
b) a granularidade dos dados.
c) o número de usuários.
d) o tipo de OLAP.
e) a localização física do servidor.

> **Resposta: b.** **Granularidade** = nível de sumarização — decisão que define volume, detalhe e desempenho de todo o DW.

---

**Questão 3.** (CESPE-style) O processo de ETL representa aproximadamente 70% dos recursos de implementação e manutenção de um Data Warehouse.
a) Certo. b) Errado.

> **Resposta: a (Certo).** ETL consome **~70% dos recursos** e **~80% do tempo** de desenvolvimento. A back room (staging) não atende consultas.

---

**Questão 4.** (FCC-style) Na abordagem ELT (Extract, Load, Transform), as transformações ocorrem:
a) em área de staging separada do DW.
b) dentro do próprio DW de destino, após o carregamento.
c) exclusivamente no sistema de origem (OLTP).
d) na estação do usuário final.
e) em servidor de aplicação web.

> **Resposta: b.** **ELT** carrega primeiro e transforma **no destino** (staging tables no DW). **ETL** transforma fora, antes de carregar.

---

**Questão 5.** (CESPE-style) O modelo proposto por Kimball para construção de Data Warehouse é top-down, partindo do DW corporativo para a criação de Data Marts.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **Kimball = bottom-up** (Data Marts → DW incremental); **Inmon = top-down** (DW corporativo → Data Marts).

---

**Questão 6.** (FCC-style) Em modelagem multidimensional, o saldo de uma conta bancária é exemplo de medida:
a) aditiva.
b) semiaditiva.
c) não aditiva.
d) derivada.
e) degenerada.

> **Resposta: b.** **Semiaditiva**: soma em algumas dimensões (ex.: agência), mas **não no tempo** (somar saldos mensais não faz sentido).

---

**Questão 7.** (CESPE-style) O OLAP é um tipo de banco de dados multidimensional que registra e armazena as transações do dia a dia da organização.
a) Certo. b) Errado.

> **Resposta: b (Errado).** OLAP **não é BD** nem registra dados — é ferramenta de **análise/agregação** sobre dados do DW. Quem registra transações é o **OLTP**.

---

**Questão 8.** (FCC-style) A operação OLAP que seleciona uma única dimensão de um cubo, gerando um subcubo, é:
a) roll-up.
b) drill-down.
c) slice.
d) dice.
e) pivot.

> **Resposta: c.** **Slice** = 1 dimensão; **dice** = 2+ dimensões; roll-up sobe hierarquia; drill-down desce; pivot gira eixos.

---

**Questão 9.** (CESPE-style) No esquema estrela, as dimensões são normalizadas em múltiplos níveis, conforme a Terceira Forma Normal.
a) Certo. b) Errado.

> **Resposta: b (Errado).** No **estrela**, dimensões são **desnormalizadas** (uma tabela por dimensão). A normalização (3FN) em múltiplos níveis é do **floco de neve**.

---

**Questão 10.** (FCC-style) O subsistema do ETL responsável por gerar chaves substitutas, garantindo a integridade referencial entre tabelas fato e dimensão, integra o grupo de:
a) extração.
b) limpeza.
c) entrega.
d) orquestração.
e) backup.

> **Resposta: c.** **Entrega** (subsistemas 9–21): SCD, **gerador de chave substituta**, hierarquias e dimensões especiais.

---

**Questão 11.** (CESPE-style) A arquitetura OLAP do tipo ROLAP utiliza banco de dados multidimensional proprietário com cubos pré-calculados em matrizes esparsas.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é **MOLAP**. **ROLAP** usa **BD relacional** (esquema estrela/floco) com SQL otimizado.

---

**Questão 12.** (FGV-style) Sobre a hierarquia DIKW, é correto afirmar:
a) dado é sinônimo de informação.
b) conhecimento é informação acrescida de contexto, relevância e acionabilidade, frequentemente tácito.
c) inteligência é gerada automaticamente por sistemas, sem julgamento humano.
d) experiência antecede dado na hierarquia.
e) informação exige avaliação de confiabilidade para existir.

> **Resposta: b.** **Conhecimento** = "informação em ação" (Turban), inclui reflexão/síntese e é tácito. **Inteligência** exige julgamento humano; **experiência** vem depois.

---

**Questão 13.** (CESPE-style) No modelo da arquitetura back room/front room de ETL, a área de staging (back room) é acessada diretamente pelos usuários finais para consultas analíticas.
a) Certo. b) Errado.

> **Resposta: b (Errado).** A **back room** (staging) é exclusiva da equipe de ETL — **nenhum serviço de consulta** é fornecido lá. As consultas usam o DW/DM (front room).

---

**Questão 14.** (FCC-style) O CDC (Change Data Capture) é um subsistema de extração do ETL que:
a) apaga dados antigos do DW.
b) captura apenas as mudanças ocorridas na origem (via audit columns, logs etc.).
c) cria cubos OLAP.
d) gera relatórios para a diretoria.
e) normaliza as dimensões.

> **Resposta: b.** **CDC** identifica e extrai só as **mudanças** (audit columns, database log scraping, message queue monitoring) — eficiência na extração.

---

**Questão 15.** (CESPE-style) Segundo as falácias do Big Data, o volume de dados garante, por si só, previsões precisas do futuro da organização.
a) Certo. b) Errado.

> **Resposta: b (Errado).** "Big Data pode prever o futuro" é uma das **8 falácias** — volume não substitui qualidade, contexto e método analítico.

---

## Questões discursivas

**D1.** Explique o pipeline de dados ETL, suas quatro etapas segundo Kimball e a diferença entre ETL e ELT.

> **Modelo de resposta:** O ETL é o conjunto de processos que **integra** dados de sistemas operacionais (OLTP e outras fontes) para o Data Warehouse: **Extração** (dados brutos com mínima reestruturação e restart fácil), **Limpeza** (consistência, deduplicação, regras de negócio — etapa irreversível), **Conformidade** (mesclar fontes e racionalizar medidas) e **Entrega** (estruturar em modelo dimensional/estrela). Consome ~70% dos recursos do DW. Em **ETL**, as transformações ocorrem **fora** do destino (staging); em **ELT**, os dados são carregados primeiro e transformados **dentro do DW de destino**.

**D2.** Diferencie OLTP de OLAP e explique os esquemas estrela, floco de neve e constelação.

> **Modelo de resposta:** **OLTP** suporta transações do dia a dia: dados atualizados, normalizados, consultas simples e rápidas. **OLAP** suporta **decisão**: dados sumarizados/históricos, modelo dimensional, consultas complexas multidimensionais (roll-up, drill-down, slice, dice, pivot) — e não registra dados. **Estrela**: uma tabela fato central com dimensões desnormalizadas (relação 1-N). **Floco de neve**: dimensões normalizadas em vários níveis (3FN). **Constelação**: várias tabelas fato compartilhando dimensões comuns.

---

*Base: `11.Business Intelligence` (Aulas 00–06: DIKW, SI, DW/Kimball-Inmon, ETL/34 subsistemas, OLAP, mineração, Big Data) do material local (2020). Complemento: dashboards/KPIs, orquestração moderna de pipelines (Airflow/dbt) e ELT como tópico próprio — ausentes ou esparsos na base.*