# APOSTILA — TÓPICO 9: CIÊNCIA DE DADOS E INTELIGÊNCIA ARTIFICIAL
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Fundamentos de estatística e análise de dados; Big Data: ferramentas e arquiteturas; Algoritmos de machine learning: supervisionado e não supervisionado; Avaliação de modelos; IA Generativa, ética e governança de modelos; Processos e práticas: DataOps, MLOps.
>
> **Base de conhecimento:** apostilas Estratégia 2020.2 (Business Intelligence Aula02–Aula06 e Aula10; Banco de Dados Aula08) + complementos atuais (IA generativa, MLOps, métricas de avaliação — conteúdos pós-2020, sinalizados no texto).

---

# MÓDULO I — FUNDAMENTOS DE ESTATÍSTICA E ANÁLISE DE DADOS

## 1. Conceitos fundamentais

- **Estatística**: conjunto de técnicas para organizar, descrever, analisar e interpretar dados. Divide-se em três áreas: **estatística descritiva**, **probabilidade** e **inferência estatística**.
- **População**: conjunto de todos os elementos que possuem ao menos uma característica em comum. **Amostra**: subconjunto **próprio** (menor) e **representativo** da população. **Amostragem**: processo de seleção da amostra.
- **Parâmetro** × **Estimador** (pegadinha clássica):
  - **Parâmetro**: medida da **população**; é **constante**; símbolos θ, μ (média), σ² (variância), σ (desvio padrão), ρ.
  - **Estimador**: fórmula/função aplicada à **amostra**; símbolos θ̂, x̅, s², s, r.
  - **Erro amostral**: ε = θ̂ − θ.

## 2. Estatística descritiva e Análise Exploratória de Dados (AED)

- **AED**: resumir as características principais dos dados, geralmente com métodos **visuais**, **sem impor um modelo** (diferente da Estatística Clássica e da Bayesiana). Promovida por **John Tukey**.
- **Medidas de tendência central**:
  - **Moda**: valor mais frequente. Ex.: {3,4,5,6,7,7,7,8,8,9} → moda = 7. **Única medida válida para escala nominal.**
  - **Mediana**: valor central da série **ordenada**; com número par de elementos, é a **média dos dois centrais**.
  - **Média**: soma/n; só faz sentido para escala **intervalar** ou **de razão**.
- **Medidas de dispersão**: amplitude, amplitude interquartílica (IIQ = Q3 − Q1), **variância** (soma dos desvios da média elevados ao quadrado — *a soma dos desvios sem elevar é sempre 0*), **desvio padrão** (raiz da variância; volta à unidade original), coeficiente de variação.
- **Assimetria** (distribuição inclinada) e **curtose** (grau de achatamento/pontude).

## 3. Escalas de mensuração (assunto recorrente em prova)

| Escala | Natureza | O que permite | Exemplo |
|---|---|---|---|
| **Nominal** | Qualitativa | Só igualdade/diferença, **sem ordem** | sexo, cor, estado civil |
| **Ordinal** | Qualitativa | Igualdade + **ordem** (diferenças não quantificáveis) | classe social, faixa etária, likert |
| **Intervalar** | Quantitativa | Diferenças significativas; **zero relativo/convenção** (0°C ≠ ausência de calor) | temperatura Celsius, ano, IQ |
| **Razão** | Quantitativa | Diferenças **e razões** significativas; **zero absoluto** | peso, altura, renda, distância |

**Pegadinha CESPE (TCE-PB 2018):** não confundir **nível de mensuração** (quanto de informação a variável apresenta) com **nível de manipulação** (como ela se relaciona no experimento):
- **Independente**: manipulada pelo pesquisador.
- **Dependente**: medida/registrada (resposta).
- **De controle**: mantida fixa para isolar efeito.

## 4. Variáveis

- **Qualitativas**: nominal e ordinal. **Quantitativas**: **discreta** (nº de filhos — contagem) e **contínua** (peso, altura — medição).

## 5. Visualização de dados

- **Barras**: qualitativas ordinais/discretas. **Pizza**: categorias nominais.
- **Histograma**: retângulos **contíguos**; a **área** = frequência relativa; informa centralidade, amplitude e simetria.
- **Boxplot (diagrama de caixa)**: Q1, mediana (Q2), Q3. **Outliers/discrepantes**: valores > Q3 + 1,5·(Q3−Q1) ou < Q1 − 1,5·(Q3−Q1). Informa posição, dispersão, assimetria, caudas e discrepantes.
- **Série temporal** (linha): evolução no tempo. **Polígono de frequências**: liga os pontos médios do histograma. **Dispersão (scatterplot)**: relação entre **duas** variáveis quantitativas. **Curvas de nível**: mapas de contorno.

## 6. Amostragem

| Tipo | Modalidade | Descrição |
|---|---|---|
| Aleatória simples | Probabilística | Cada elemento com a **mesma chance** de ser escolhido |
| Por estratificação | Probabilística | Divide a população em ≥2 **estratos** homogêneos e amostra cada um |
| Por conglomerados | Probabilística | Divide a área em **seções** (agrupamentos), sorteia seções e analisa **todos** os elementos delas |
| Sistemática | Probabilística | Escolhe cada elemento de ordem *k* |
| Conveniência | **Não** probabilística | Elementos de fácil acesso |
| Julgamento | **Não** probabilística | Escolha do pesquisador/entrevistador |
| Por cotas | **Não** probabilística | Cotas proporcionais, sem critério probabilístico |

**Regra prática de prova:** se o sorteio/probabilidade participa → probabilística; se há subjetividade ou conveniência → não probabilística. **Estratificação** = homogeneidade **dentro** dos grupos, heterogeneidade **entre** eles; **conglomerados** = o inverso.

## 7. Estatística inferencial (complemento — não está no material 2020)

- **Inferência estatística**: generalizar resultados da amostra para a população, quantificando a incerteza.
- **Intervalo de confiança (IC)**: faixa de valores plausíveis para o parâmetro, com nível de confiança (ex.: 95%). IC 95% para a média: x̅ ± z·(s/√n).
- **Teste de hipóteses**: H₀ (hipótese nula — "não há efeito/diferença") × H₁ (alternativa). O **p-valor** é a probabilidade de observar o resultado (ou mais extremo) assumindo H₀ verdadeira. **p < α (usualmente 0,05) → rejeita-se H₀.**
  - **Erro tipo I**: rejeitar H₀ verdadeira (falso positivo). **Erro tipo II**: não rejeitar H₀ falsa (falso negativo).
- **Correlação × causalidade**: correlação (ex.: coeficiente de Pearson r ∈ [−1,1]) **não** implica causalidade — pegadinha universal.
- **Regressão linear**: Y = β₀ + β₁X₁ + … + βₙXₙ + ε (previsão de valor **numérico**). **Regressão logística**: prevê **probabilidade** de classe (classificação binária).

---

# MÓDULO II — BIG DATA: FERRAMENTAS E ARQUITETURAS

## 1. Conceito e os Vs

- **Big Data**: captura, gerenciamento e análise de dados **para além dos estruturados** (vídeo, imagens, logs, sensores, redes sociais). ~85% dos dados corporativos são **não estruturados**; IBM (2013): 2,5 exabytes gerados por dia.
- **3Vs originais** — propostos por **Doug Laney** (Meta Group, 2001; depois Gartner): **Volume, Velocidade, Variedade**.
- **Vs adicionais**: **Veracidade** (4º V, IBM — confiabilidade; ex.: sentimentos em redes sociais são incertos), **Valor** (Oracle — o valor por byte é baixo; dados devem gerar retorno), **Visibilidade**, **Variabilidade/Complexidade** (SAS — picos de fluxo, múltiplas fontes), **Visualização**.
- IBM cita **7 dimensões**: volume, variedade, velocidade, veracidade, valor + **governança** (propriedade/legalidade — ex.: dados de pacientes) e **pessoas** (modelagem, estatística).

## 2. Big Data Analytics e os tipos de análise

- **BI × Big Data Analytics** (pergunta clássica): o **BI responde perguntas que já existem** (explica o **passado**); o **Big Data Analytics encontra perguntas que nem sabíamos que existiam** (tendências/padrões para o futuro).
- **Tipos de análise**:
  - **Descritiva**: fotografia do presente (ex.: a pessoa **é** má pagadora hoje).
  - **Diagnóstica**: as causas (ex.: **virou** má pagadora porque ficou viúva).
  - **Preditiva**: prever comportamento (ex.: valor do dólar no ano que vem).
  - **Prescritiva**: prever **consequências** de um acontecimento (ex.: impacto do dólar nas importações).

## 3. As 8 falácias do Big Data (cuidado em prova)

1. Big Data engloba **apenas** dados estruturados — **FALSO**.
2. Só existe em escala de petabytes — **FALSO**.
3. Só vale para a Vale do Silício — **FALSO**.
4. Só grandes organizações se beneficiam — **FALSO**.
5. Requer dados externos — **FALSO** (comece pelos internos).
6. **Big Data prevê o futuro** — **FALSO**: os dados vêm do passado; só projeta tendências sob circunstâncias semelhantes.
7. Substitui valores/ética — **FALSO**.
8. Resolve qualquer problema — **FALSO** (não resolve problemas não quantificáveis, como comportamento individual).

**Fato de prova (CESPE TJ/SE 2014):** em Big Data, a análise exige **transformar dados não estruturados em estruturados**; consultas ad hoc são **diferentes** das de bancos tradicionais (fontes/formatos não fixos).

## 4. NoSQL

- **Origem**: termo cunhado em reunião de 11/06/2009 (São Francisco — Johan Oskarsson) sobre bancos **não relacionais, distribuídos e open source**. Inspirado em **BigTable (Google)** e **Dynamo (Amazon)**. Lê-se "**Not only SQL**".
- **Características**: não usa modelo relacional; bom em clusters; código aberto; **schema free**; resultado: **persistência poliglota** (mistura de tecnologias conforme a necessidade).
- **Agregado**: conjunto de objetos tratado como unidade de manipulação/consistência. **Orientação por agregados** em chave-valor, documento e família de colunas (grafos têm modelo próprio).

| Modelo | Característica | Exemplos |
|---|---|---|
| **Chave-valor** | Agregado **opaco**; pesquisa só pela chave (get/set); sem consultas complexas | DynamoDB, Redis, Riak |
| **Documento** | Agregado **transparente** (JSON/XML); consultas parciais; sem esquema rígido | MongoDB, CouchDB |
| **Colunar (família de colunas)** | Trilha = (linha, coluna, **timestamp**); leitura/escrita atômicas por linha; **column family** | BigTable, Cassandra, HBase |
| **Grafos** | Nós, **arestas** (relacionamentos) e propriedades; multigrafo rotulado/direcionado | Neo4J, InfoGrid |

- **Distribuição**: **fragmentação** (distribui dados **diferentes** entre servidores) × **replicação** (copia os mesmos dados). Replicação **mestre-escravo** (mestre grava, escravos leem — menos conflitos) × **ponto a ponto** (qualquer nó grava — sem SPOF).
- **Teorema CAP** (Eric Brewer, 2000; provado por Gilbert e Lynch): em sistema distribuído, entre **Consistência, Disponibilidade e Tolerância a partições**, escolhe-se **apenas duas**.
  - Consistência = toda leitura retorna o valor mais recente; Disponibilidade = toda requisição recebe resposta; Tolerância a partições = o sistema sobrevive a "split brain" (rede dividida).
- **ACID × BASE**:
  - **ACID** (Atomicidade, Consistência, Isolamento, Durabilidade): pessimista, bloqueios, consistência **imediata**; relacionais priorizam **C+A**.
  - **BASE** (Basically Available, Soft State, Eventual consistency): otimista, consistência **eventual**; favorece **A+P**. *Pegadinha: sistemas bancários não podem relaxar a consistência.*
- **MapReduce**: padrão de computação em cluster. `Map(k1,v1) → lista(k2,v2)`; `Reduce(k2, lista(v2)) → lista(v3)`. Exemplo clássico: **censo romano** (contagem paralela por região).

## 5. Hadoop e ecossistema

- **Hadoop**: framework **open source** para armazenamento/processamento em larga escala em hardware **commodity**, tolerante a falhas. = **HDFS** (armazenamento distribuído) + **MapReduce** (processamento paralelo).
  - **HDFS**: daemons **NameNode** (metadados), **DataNode** (blocos), BackupNode, Checkpoint NameNode.
- **Camada de programação sobre MapReduce**:
  - **Hive**: interface SQL (**HiveQL**), criado no Facebook; **HiveQL NÃO é compatível com SQL92**; suporta UDFs.
  - **Pig**: script **Pig Latin** (Yahoo); dados semiestruturados.
  - **Spark**: **até 100× mais rápido que MapReduce em memória** (10× em disco); processamento em **streaming/tempo real**; suportado pelo YARN.
- **HBase**: NoSQL colunar sobre HDFS (inspirado no BigTable); baixa latência, forte consistência, esquema flexível.
- **Ingestão de dados**:
  - **Flume**: eventos/logs → HDFS. Agente: **Source → Channel → Sink**.
  - **Sqoop**: Hadoop ↔ bancos relacionais/DW (import/export via MapReduce + driver JDBC).
  - **NiFi**: fluxo automatizado entre sistemas (FlowFile, Conteúdo, Proveniência; ZooKeeper elege o coordenador).
  - **Kafka**: plataforma de **streaming** distribuída (tópicos, partições, brokers, líder/réplica, produtores/consumidores).
  - **Storm**: processamento de streaming em tempo real.
- **Gestão e apoio**:
  - **YARN** (Yet Another Resource Negotiator): gerencia recursos do Hadoop 2.x (suporta MapReduce, Spark, Storm, Tez).
  - **ZooKeeper**: coordenação/sincronização distribuída. **Oozie**: agendamento de workflows.
  - **Mahout**: biblioteca de **machine learning** (recomendação, clustering, classificação).
  - **Ambari**: administração/monitoramento de clusters (APIs RESTful).

## 6. Data Warehouse, ETL e OLAP (complemento de contexto — coberto no Tópico 10, mas cai junto)

- **Granularidade** = nível de detalhe/sumarização; é o **aspecto mais importante do projeto de DW**. *Granularidade alta = menos detalhe.*
- **Medidas em tabela fato**: **aditivas** (somam em qualquer dimensão — ex.: lucro), **semiaditivas** (somam só em algumas — ex.: saldo não soma no tempo), **não aditivas** (nunca somam — ex.: percentuais/taxas).
- **ETL (Extract-Transform-Load)**: consome ~**70–80%** dos recursos/tempo de um projeto de DW. 4 etapas (Kimball): **Extração** (com *data profiling* e **CDC** — change data capture), **Limpeza**, **Conformidade**, **Entrega** + **Gestão**. *Staging area* = área temporária ("cozinha" do restaurante).
- **OLAP** (E.F. Codd): análise **multidimensional**, consultas **ad hoc**; **não armazena dados** (é ferramenta de análise).
  - **Operações**: **roll-up/drill-up** (agregar), **drill-down** (detalhar), **slice** (corta 1 dimensão), **dice** (≥2 dimensões), **pivot/rotate** (gira eixos), **drill-across** (**mais de uma tabela fato** — visão Kimball), **drill-through** (vai às **tabelas relacionais** de back-end).
  - **Arquiteturas**: **MOLAP** (cubos multidimensionais; Data Marts; "explosão de dados"), **ROLAP** (relacional + middleware; grandes volumes/DW), **HOLAP** (híbrido), **DOLAP** (desktop), **SOLAP** (SIG/geográfico), WOLAP (web).
  - **OLTP × OLAP**: OLTP atualiza registros atômicos, dados correntes, resposta <1s, consultas pré-definidas; OLAP analisa dados sumarizados/históricos, arrays/cubos, resposta de segundos a **horas**, consultas ad hoc, armazenamento **maior**.

---

# MÓDULO III — ALGORITMOS DE MACHINE LEARNING

## 1. Conceitos

- **Machine Learning (ML)**: área da **Inteligência Artificial** em que sistemas **aprendem com experiência** (dados), melhorando desempenho em tarefas sem serem programados explicitamente.
- **Teorema NFL (No Free Lunch)**: **não existe algoritmo melhor para todos os problemas** — a escolha depende dos dados e da tarefa.

## 2. Paradigmas de aprendizado

| Paradigma | Dados | Objetivo | Exemplos de tarefa |
|---|---|---|---|
| **Supervisionado** | Entradas **com** rótulos/saídas conhecidas ("professor") | Aprender f: entradas → saída | Classificação (classe) e Regressão (valor numérico) |
| **Não supervisionado** | **Sem** rótulos | Descobrir estrutura oculta | Clustering, redução de dimensionalidade, regras de associação |
| **Por reforço** | Agente + ambiente; **recompensas/punições** | Maximizar recompensa | Ajuste dinâmico de preços, robótica, jogos |
| **Semissupervisionado** | Poucos rótulos + muitos não rotulados | Combinar | Semi-supervised learning |
| **Por transferência** | Conhecimento de uma tarefa/domínio para outro | Reaproveitar | Fine-tuning de LLMs |

## 3. Algoritmos — supervisionado

- **Árvores de decisão** (paradigma **simbólico**, TDIDT): nós de decisão, folhas = classe; induzem regras IF-THEN; ex.: ID3, C4.5, CART. Vantagem: **interpretável**.
- **Naive Bayes** (paradigma **estatístico**): teorema de Bayes com suposição de **independência condicional** entre atributos; rápido, bom para texto/spam.
- **KNN — K vizinhos mais próximos** (paradigma **baseado em exemplos**): classifica pelo **voto majoritário** dos K vizinhos mais próximos (distância); exige normalização; "preguiçoso" (lazy).
- **Redes neurais artificiais** (paradigma **conexista**): camadas de **entrada → escondidas → saída**; **pesos** ajustados por **regra delta/backpropagation**. **Deep learning** = redes com muitas camadas (CNN para imagens, RNN/LSTM para sequências, Transformers para texto).
- **Regressão linear/logística** (paradigma estatístico): previsão de valores (linear) ou probabilidades de classe (logística).
- **SVM (máquinas de vetores de suporte)**: hiperplano de separação com **margem máxima**; eficaz em espaços de alta dimensão.
- **Ensembles**:
  - **Bagging** (ex.: Random Forest): treina em **subamostras** (bootstrap) e combina por votação/média → reduz **variância**.
  - **Boosting** (ex.: AdaBoost, Gradient Boosting, XGBoost): sequencial, ajusta **pesos** aos erros anteriores → reduz **viés**.
  - **Stacking**: as **saídas** de vários modelos viram **entrada** de um meta-modelo.

## 4. Algoritmos — não supervisionado

- **Clustering/agrupamento** (descritivo; "classificação" para estatísticos, "segmentação" para marketing):
  - **K-means** (particional): K centróides, minimiza intra-cluster; sensível a outliers e à inicialização.
  - **Hierárquico**: dendrograma; aglomerativo (bottom-up) ou divisivo (top-down).
  - **DBSCAN** (densidade): encontra formas arbitrárias e detecta ruído.
  - Medidas de **distância**: D(A,B)=D(B,A) (simetria); D(A,A)=0; positividade; desigualdade triangular.
- **Redução de dimensionalidade**: **PCA** (análise de componentes principais), seleção de atributos, autoencoders.
- **Regras de associação** (mercado — "quem compra pão compra leite"): padrão X → Y.
  - **Suporte** = % de transações em que a regra ocorre (frequência).
  - **Confiança** = grau de certeza da regra = **P(Y|X)**.
  - *Pegadinha FGV: "confiança = quantas vezes a regra se verifica" está ERRADO — isso é o **suporte**.*
  - Itemsets grandes: algoritmo Apriori (fechamento por baixo + **antimonotonicidade** — se um itemset é infrequente, todos os seus superconjuntos também são).

## 5. Pré-processamento de dados (KDD e CRISP-DM)

- **Processo KDD** (Knowledge Discovery in Databases): limpeza → integração → seleção → transformação → **mineração**.
- **CRISP-DM** (1996 — 6 fases, sequência **não obrigatória**/iterativa): 1. Entendimento do negócio; 2. Compreensão dos dados; 3. **Preparação (>50% do trabalho)**; 4. Modelagem; 5. Avaliação; 6. Entrega/Deployment.
- **Problemas de qualidade**: **incompletude** (valor/atributo/objeto ausente), **inconsistência** (fora do domínio), **ruído** (outliers/variações).
- **Tarefas de pré-processamento**: limpeza, integração, **transformação** (padronização/normalização — ex.: z-score, min-max), **redução** (seleção de atributos, compressão, discretização).

---

# MÓDULO IV — AVALIAÇÃO DE MODELOS

## 1. Matriz de confusão (classificação binária)

|  | Previsto **Positivo** | Previsto **Negativo** |
|---|---|---|
| **Real Positivo** | VP (verdadeiro positivo) | FN (falso negativo — erro tipo II) |
| **Real Negativo** | FP (falso positivo — erro tipo I) | VN (verdadeiro negativo) |

## 2. Métricas essenciais

- **Acurácia** = (VP + VN) / total. *Enganosa em bases desbalanceadas (ex.: fraude 1% — "prever sempre não-fraude" dá 99% de acurácia e zero utilidade).*
- **Precisão** = VP / (VP + FP) — "dos que o modelo disse serem positivos, quantos realmente são?" (custo alto de falso positivo, ex.: spam).
- **Recall (sensibilidade/revocação)** = VP / (VP + FN) — "dos positivos reais, quantos o modelo capturou?" (custo alto de falso negativo, ex.: câncer, fraude).
- **F1-score** = média harmônica de precisão e recall: 2·P·R/(P+R). Equilibra os dois.
- **Especificidade** = VN / (VN + FP).
- **Curva ROC e AUC**: ROC plota TPR (recall) × FPR (1−especificidade) variando o limiar; **AUC** = área sob a curva (1 = perfeito; 0,5 = aleatório).
- **Métricas de regressão**: **MAE** (erro absoluto médio), **MSE** (erro quadrático médio — penaliza erros grandes), **RMSE** (raiz do MSE — unidade original), **R²** (proporção da variância explicada).

## 3. Validação e generalização

- **Holdout**: separa **treino** (ex.: 70–80%) e **teste** (20–30%). Pode haver terceiro conjunto de **validação** para ajuste de hiperparâmetros.
- **Validação cruzada (k-fold)**: divide em *k* partes; treina em *k*−1 e testa em 1, rotacionando; resultado = média das *k* rodadas. Mais robusta que holdout simples.
- **Underfitting × Overfitting** (viés × variância):
  - **Viés (bias) alto → underfitting**: modelo simples demais, erra até nos dados de treino.
  - **Variância alta → overfitting**: modelo complexo demais, "decora" o treino (inclusive o **ruído**) e falha no teste.
  - **Trade-off**: buscar o ponto de equilíbrio. Técnicas anti-overfitting: regularização (L1/L2), poda, dropout, mais dados, validação cruzada, early stopping.

---

# MÓDULO V — IA GENERATIVA

*(Conteúdo pós-2020 — não está na base Estratégia; cobrir bem, é tendência de banca.)*

## 1. Conceito

- **IA Generativa**: modelos que **geram conteúdo novo** (texto, imagem, áudio, código, vídeo) a partir de padrões aprendidos em grandes volumes de dados — em contraste com IA **discriminativa**, que **classifica/prediz** rótulos.
- **Fundamento**: **redes neurais profundas**; para texto, a arquitetura dominante é o **Transformer** (artigo "Attention Is All You Need", 2017), baseado no mecanismo de **atenção**.

## 2. Modelos de linguagem (LLMs)

- **LLM (Large Language Model)**: modelo treinado em enormes corpora para **prever o próximo token**. Ex.: famílias GPT, Claude, Llama, Gemini.
- **Fases de desenvolvimento**:
  1. **Pré-treinamento (self-supervised)**: previsão de tokens em texto bruto.
  2. **Fine-tuning supervisionado (SFT)**: exemplos instrução→resposta.
  3. **Alinhamento (ex.: RLHF** — reinforcement learning from human feedback): preferências humanas para segurança/utilidade.
- **Token**: unidade de texto (palavra ou pedaço) processada pelo modelo; define custo e limite de contexto (**janela de contexto**).
- **Prompt engineering**: técnicas de instrução (zero-shot, few-shot com exemplos, chain-of-thought — "pense passo a passo", personas, restrições de formato).
- **Embeddings**: vetores numéricos que representam significado semântico — base de busca semântica e **RAG**.

## 3. Técnicas e aplicações

- **RAG (Retrieval-Augmented Generation)**: recupera documentos relevantes em uma base (busca vetorial) e os injeta no contexto do LLM — **reduz alucinações** e atualiza o conhecimento sem retreinar.
- **Agentes de IA**: LLM + ferramentas (busca, código, APIs) com ciclo de raciocínio-ação-observação.
- **Geração de imagem**: modelos de **difusão** (ex.: Stable Diffusion) e GANs.
- **Alucinação**: o modelo gera informação **plausível, mas falsa** — risco central dos LLMs.

## 4. Limitações

- Corte de conhecimento (dados de treino têm data final); sem memória permanente entre conversas (sem mecanismos externos); alucinações; custo computacional elevado; vieses herdados dos dados; sensibilidade a prompts.

---

# MÓDULO VI — ÉTICA E GOVERNANÇA DE MODELOS DE IA

## 1. Ética e vieses algorítmicos

- **Viés algorítmico**: modelo reproduz/amplia desigualdades dos dados históricos (ex.: sistemas de recrutamento que discriminam gênero; reconhecimento facial com maior erro em peles escuras).
- **Princípios de IA responsável** (OCDE, UNESCO, NIST AI RMF): **transparência/explicabilidade**, **justiça/não discriminação**, **accountability (responsabilização)**, **segurança/robustez**, **privacidade**, **supervisão humana**, **beneficência e não maleficência**.
- **Explicabilidade (XAI)**: capacidade de explicar decisões do modelo (ex.: SHAP, LIME). Modelos "caixa-preta" (deep learning) × modelos interpretáveis (árvore de decisão).

## 2. Governança de modelos

- **AI Model Governance**: framework de políticas, papéis e controles sobre o ciclo de vida do modelo — inventário de modelos, documentação (model cards), aprovação para produção, auditorias, monitoramento, aposentadoria.
- **Model card / datasheet for datasets**: documentação padronizada de uso pretendido, métricas por subgrupo, limitações.
- **Avaliação de impacto algorítmico**: analisar riscos antes do deploy (similar a DPIA/LAIA — relatório de impacto).

## 3. LGPD (Lei 13.709/2018) aplicada a IA

- **Bases legais** para tratamento de dados em IA (consentimento, legítimo interesse, execução de contrato, etc.).
- **Direitos do titular**: acesso, correção, eliminação, revisão de decisões automatizadas (**art. 20 — direito à revisão de decisão tomada unicamente com base em tratamento automatizado**).
- **Dados pessoais sensíveis** (raça, saúde, biometria): proteção reforçada contra discriminação algorítmica.
- **Princípios**: finalidade, adequação, necessidade, transparência, segurança, prevenção, não discriminação, responsabilização.
- **Encarregado (DPO)** e **privacidade desde a concepção (privacy by design)**.

## 4. Regulação em evolução

- **EU AI Act** (União Europeia, 2024): abordagem por **risco** (inaceitável / alto / limitado / mínimo); IA de uso geral (GPAI) com obrigações de transparência; proibição de usos (ex.: pontuação social).
- No Brasil: **PL 2338/2023** (Marco Legal da IA) — princípios, direitos dos titulares, governança baseada em risco, sanções.

---

# MÓDULO VII — DATAOPS E MLOPS

*(Conteúdo pós-2020 — complementar.)*

## 1. DataOps

- **DataOps**: aplicação de práticas **DevOps/ágil** ao **ciclo de vida de dados** — integração, qualidade, orquestração e entrega contínua de dados.
- **Objetivos**: dados **confiáveis, rápidos e reutilizáveis**; automação de pipelines de dados; colaboração entre times de dados; **monitoramento de qualidade** (testes de dados — ex.: Great Expectations), observabilidade de dados, versionamento de dados.
- **Diferença para MLOps**: DataOps cuida do **dado** (da fonte ao consumo); MLOps cuida do **modelo** (do treino à produção).

## 2. MLOps

- **MLOps**: união de **Machine Learning + DevOps + Engenharia de Dados**; práticas para levar modelos à produção de forma **reprodutível, automatizada e monitorada**.
- **Ciclo**: coleta/preparação de dados → treinamento → avaliação → deployment → **monitoramento** → retreinamento.
- **Pilares/práticas**:
  - **CI/CD/CT** para ML: integração contínua, entrega contínua e **treinamento contínuo** (retraining).
  - **Versionamento**: código, **dados** (ex.: DVC), modelos e experimentos (ex.: MLflow).
  - **Feature store**: repositório compartilhado de features (consistência treino × produção).
  - **Registro de modelos (model registry)** e controle de linhagem (lineage).
  - **Deployment**: shadow, canary, A/B testing, blue-green, batch × online (real-time inference).
  - **Monitoramento em produção**: **data drift** (distribuição dos dados muda) e **concept drift** (relação entrada-saída muda); alertas de degradação de métricas; retreinamento automático.
- **Níveis de maturidade MLOps** (Google): Nível 0 (manual), Nível 1 (pipeline automatizado de treino), Nível 2 (CI/CD/CT completo com monitoramento e retreinamento).
- **Ferramentas típicas**: MLflow, Kubeflow, Airflow/Prefect (orquestração), DVC, TFX, Evidently (drift).

---

# RESUMO DE PEGADINHAS DE PROVA

1. **Suporte ≠ confiança** (FGV): confiança = P(Y|X); suporte = frequência da regra.
2. **Classificação = supervisionado; clustering = não supervisionado.**
3. **OLAP não armazena dados**; operações OLAP podem levar **horas**; OLAP usa **mais** armazenamento que OLTP.
4. **Granularidade alta = menos detalhe.**
5. **Big Data não prevê o futuro**; não se resume a estruturados/petabytes/grandes empresas.
6. **BI explica o passado; Big Data Analytics encontra perguntas novas.**
7. **Drill-across** = várias tabelas fato (Kimball); **drill-through** = detalhe nas tabelas relacionais. *A FCC usa definições equivocadas — atenção à banca.*
8. **CAP**: só 2 de 3. **ACID** prioriza C+A; **BASE** prioriza A+P.
9. **CRISP-DM**: 6 fases, sequência **não obrigatória**; preparação = **>50%** do esforço.
10. **ETL ≈ 70–80%** do projeto de DW; 4 etapas (extração, limpeza, conformidade, entrega) + gestão.
11. **Moda** = única medida de tendência central para escala **nominal**.
12. **HiveQL não é SQL92**; **Spark** é até 100× mais rápido que MapReduce em memória.
13. **NoSQL = "Not only SQL"**; schema free; persistência poliglota.
14. **Parâmetro** (constante, população) ≠ **estimador** (função, amostra).
15. **Acurácia engana em bases desbalanceadas** — use precisão/recall/F1.
16. **Overfitting = variância alta; underfitting = viés alto.**
17. **NFL**: não existe melhor algoritmo universal.
18. **CAP de Brewer**; prova de Gilbert e Lynch.
19. **MapReduce**: `Map(k1,v1)→lista(k2,v2)`; `Reduce(k2,lista(v2))→lista(v3)`.
20. **LGPD art. 20**: direito à **revisão de decisões automatizadas**.

---

# CADERNO DE QUESTÕES COMENTADAS (15 questões)

**Questão 1.** (CESPE-style) Em estatística, considere a afirmação: "O estimador é uma medida calculada sobre a população, cujo valor é sempre constante."
Assinale a opção correta:
a) Certo.
b) Errado. O estimador é calculado sobre a **amostra**, enquanto a medida constante da população é o **parâmetro**.

> **Resposta: b.** Parâmetro = medida da população (constante: μ, σ, ρ). Estimador = função amostral (x̅, s², r). O erro amostral ε = θ̂ − θ.

---

**Questão 2.** (FCC-style) Sobre escalas de mensuração, é correto afirmar:
a) A escala nominal permite ordenar as categorias.
b) A escala ordinal possui zero absoluto.
c) A temperatura medida em Celsius é exemplo de escala de razão.
d) A escala de razão possui zero absoluto e permite razões entre valores.
e) A escala intervalar é qualitativa.

> **Resposta: d.** (a) nominal **não** ordena; (b) ordinal não tem zero absoluto (nem é quantitativa); (c) Celsius tem **zero relativo** → intervalar; (e) intervalar é **quantitativa**.

---

**Questão 3.** (CESPE-style) A moda é a única medida de tendência central aplicável a variáveis em escala nominal.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Média e mediana exigem quantificação (ordinal para mediana em casos de ordenação, mas nominal → só moda).

---

**Questão 4.** (FGV-style) Um analista encontra a regra de associação "X → Y" em 8% das transações, e observa que em 75% das transações em que X ocorre, Y também ocorre. Nesse contexto, 8% corresponde ao ______ e 75% corresponde ao ______.
a) suporte; confiança.
b) confiança; suporte.
c) lift; suporte.
d) confiança; lift.
e) suporte; lift.

> **Resposta: a.** Suporte = frequência da regra na base (8%); confiança = P(Y|X) = 75%. *Pegadinha clássica: confiança NÃO é "quantas vezes a regra se verifica na base inteira".*

---

**Questão 5.** (CESPE-style) O teorema CAP estabelece que um sistema distribuído pode garantir simultaneamente consistência, disponibilidade e tolerância a partições de rede.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Brewer (2000): escolhem-se **duas** das três propriedades. Bancos relacionais priorizam C+A; NoSQL BASE prioriza A+P.

---

**Questão 6.** (FCC-style) No ecossistema Hadoop, o componente responsável por gerenciar os recursos do cluster no Hadoop 2.x, permitindo que outros paradigmas além do MapReduce sejam executados, é:
a) HDFS.
b) Hive.
c) YARN.
d) ZooKeeper.
e) Sqoop.

> **Resposta: c.** **YARN** (Yet Another Resource Negotiator) gerencia recursos e suporta MapReduce, Spark, Storm e Tez. HDFS armazena; Hive consulta (HiveQL); ZooKeeper coordena; Sqoop integra com RDBMS.

---

**Questão 7.** (CESPE-style) O Apache Hive utiliza a linguagem HiveQL, cuja sintaxe é totalmente compatível com o padrão SQL92.
a) Certo. b) Errado.

> **Resposta: b (Errado).** HiveQL **não** é compatível com SQL92 — é semelhante ao SQL, mas com diferenças e extensões (UDFs).

---

**Questão 8.** (FCC-style) Sobre OLAP, assinale a alternativa correta:
a) A operação drill-down agrega dados, subindo na hierarquia dimensional.
b) Slice corta o cubo em duas ou mais dimensões.
c) Drill-across consulta mais de uma tabela fato com dimensões em comum.
d) O MOLAP armazena dados em tabelas relacionais normalizadas.
e) OLAP é um banco de dados que armazena os dados analisados.

> **Resposta: c.** (a) agregação é **roll-up** (drill-down **detalha**); (b) slice = **1** dimensão; dice = ≥2; (d) MOLAP usa **cubos/arrays multidimensionais** (ROLAP usa relacional); (e) OLAP **não armazena** — é ferramenta de análise.

---

**Questão 9.** (CESPE-style) Em machine learning, um modelo que apresenta alto desempenho nos dados de treinamento e desempenho significativamente inferior em dados novos está sob o fenômeno denominado underfitting.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Esse cenário é **overfitting** (variância alta — decorou o treino, inclusive ruído). Underfitting = viés alto: erro alto **também no treino**.

---

**Questão 10.** (FGV-style) Em um problema de detecção de fraude (1% dos casos positivos), um modelo que classifica todas as transações como "não fraude" apresenta 99% de acurácia. A métrica mais adequada para avaliar esse modelo seria:
a) acurácia.
b) precisão combinada com recall (F1-score).
c) erro quadrático médio (MSE).
d) R².
e) suporte.

> **Resposta: b.** Acurácia engana em bases **desbalanceadas**. Precisão, recall e o F1-score capturam o desempenho sobre a classe minoritária. MSE e R² são de **regressão**; suporte é de regras de associação.

---

**Questão 11.** (CESPE-style) O K-means é um algoritmo de aprendizado supervisionado, pois requer rótulos de classe para formar os grupos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** K-means é **não supervisionado** (clustering): agrupa por similaridade **sem rótulos**. Classificação (com rótulos) é supervisionada.

---

**Questão 12.** (FCC-style) O modelo de IA generativa baseado na arquitetura Transformer, que utiliza mecanismo de atenção e é treinado para prever o próximo token do texto, é exemplo de:
a) sistema especialista simbólico.
b) Large Language Model (LLM).
c) algoritmo de clustering hierárquico.
d) banco NoSQL orientado a documentos.
e) técnica de ETL.

> **Resposta: b.** LLMs (GPT, Claude, Llama etc.) são modelos de linguagem baseados em Transformers. O mecanismo de **atenção** (artigo "Attention Is All You Need", 2017) é o fundamento.

---

**Questão 13.** (CESPE-style) A técnica de RAG (Retrieval-Augmented Generation) tem como principal característica recuperar documentos relevantes em uma base externa e incorporá-los ao contexto do modelo, contribuindo para reduzir alucinações.
a) Certo. b) Errado.

> **Resposta: a (Certo).** RAG = recuperação + geração: busca semântica (embeddings) + injeção no contexto. Reduz alucinações e permite atualizar conhecimento sem retreinar o modelo.

---

**Questão 14.** (FGV-style) No âmbito da LGPD, o direito do titular de solicitar a revisão de decisão tomada unicamente com base em tratamento automatizado de dados está previsto:
a) no art. 7º, inciso IX.
b) no art. 20.
c) no art. 33.
d) no art. 46.
e) no art. 65.

> **Resposta: b.** O **art. 20** da Lei 13.709/2018 assegura a revisão de decisões automatizadas, com direito a solicitar a intervenção humana — pilar da governança de IA no Brasil.

---

**Questão 15.** (CESPE-style) Sobre MLOps e DataOps, assinale a opção correta:
a) DataOps trata exclusivamente do deploy de modelos de machine learning.
b) O data drift refere-se à mudança na distribuição dos dados de entrada ao longo do tempo, podendo degradar modelos em produção.
c) Feature store é um repositório de modelos aposentados.
d) MLOps dispensa versionamento de dados, pois apenas o código precisa ser versionado.
e) Retreinamento contínuo (CT) é prática exclusiva de DataOps.

> **Resposta: b.** (a) DataOps cuida do **ciclo de dados**; deploy de modelos é MLOps; (c) feature store guarda **features** (consistência treino/produção); (d) MLOps versiona **dados, código e modelos** (ex.: DVC); (e) CT (continuous training) é do **MLOps**.

---

## Questões discursivas (para treino de prova discursiva)

**D1.** Explique a diferença entre aprendizado supervisionado e não supervisionado, citando dois algoritmos de cada e uma aplicação típica.

> **Modelo de resposta:** No supervisionado, o algoritmo aprende a partir de exemplos **com rótulos** (pares entrada-saída), tarefa típica de **classificação** (ex.: árvores de decisão, Naive Bayes — detecção de spam) e **regressão** (ex.: regressão linear — previsão de demanda). No não supervisionado, **não há rótulos**; o objetivo é descobrir estrutura oculta nos dados, como em **clustering** (ex.: K-means — segmentação de clientes) e **regras de associação** (ex.: Apriori — análise de mercado). Há ainda o aprendizado **por reforço**, no qual um agente aprende por recompensas e punições.

**D2.** Cite os Vs do Big Data e explique por que a afirmação "Big Data prevê o futuro" é considerada uma falácia.

> **Modelo de resposta:** Os 3Vs originais (Doug Laney, 2001) são **Volume, Velocidade e Variedade**; acrescentam-se **Veracidade, Valor, Visibilidade, Variabilidade**, entre outros (IBM cita 7 dimensões, incluindo governança e pessoas). A afirmação é falsa porque os dados coletados referem-se sempre ao **passado**; o Big Data identifica **padrões, correlações e tendências** que, sob circunstâncias semelhantes, podem indicar cenários futuros — mas sem previsão determinística, especialmente para comportamentos individuais ou eventos sem precedentes.

---

## Referências de estudo na base local (trt8 new)

- `APOSTILAS ESTRATEGIA MD\01.Curso.Regular.TI.2020.2\11.Business Intelligence\Aula10.md` — Estatística e AED.
- `...\11.Business Intelligence\Aula06.md` — Big Data, NoSQL, Hadoop, MapReduce.
- `...\11.Business Intelligence\Aula05.md` — Mineração de dados, CRISP-DM, ML clássico.
- `...\11.Business Intelligence\Aula04.md` — OLAP.
- `...\11.Business Intelligence\Aula02.md` — DW e granularidade. `Aula03.md` — ETL.
- `...\07.Banco de Dados\Aula08.md` — Bancos paralelos e distribuídos (CAP, fragmentação).
- Complementos pós-2020 (IA generativa, métricas modernas, MLOps/DataOps, LGPD/IA): redigidos com base em conhecimento técnico atual.
