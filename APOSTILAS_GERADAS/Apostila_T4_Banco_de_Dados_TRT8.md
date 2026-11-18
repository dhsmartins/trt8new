# APOSTILA — TÓPICO 4: BANCO DE DADOS
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Conceito de Banco de dados. Projeto de bancos de dados: conceitos, modelagem, normalização e linguagem SQL. Operações de banco de dados: extração, filtragem, classificação e combinação de dados. Transações e controle de concorrência. Tuning de banco de dados. Programação em PL/pgSQL e PL/SQL. Ferramentas e linguagens para banco de dados: PostgreSQL (versões 15, 16, 17 e 18); Oracle (versão 19c); MySQL (versão 8); NoSQL.
>
> **Base de conhecimento:** `07.Banco de Dados` e `08.SGBDs` (Curso Regular TI 2020.2) + complemento técnico para as versões atuais dos SGBDs.

---

# MÓDULO I — CONCEITOS E PROJETO DE BANCO DE DADOS

## 1. Conceitos fundamentais

- **Banco de dados (BD)**: coleção de dados **relacionados e persistentes**, organizados para atender múltiplos usuários e aplicações. **SGBD** (DBMS): software que gerencia o BD (ex.: PostgreSQL, Oracle, MySQL) — oferece definição, manipulação, controle de acesso, concorrência, recuperação e integridade.
- **Arquitetura em 3 esquemas** (ANSI/SPARC): **esquema externo** (visões dos usuários), **esquema conceitual** (modelo lógico global), **esquema interno** (armazenamento físico). **Independência lógica e física de dados**.
- **Modelo relacional** (Codd, 1970): dados em **relações** (tuplas × atributos). Conceitos: **grau** (nº de colunas) × **cardinalidade** (nº de linhas); restrições de integridade (PK, FK, CHECK, UNIQUE, NOT NULL); **integridade de entidade** (PK não nula) e **referencial** (FK).
- **NoSQL × relacional**: NoSQL = "Not Only SQL" — **chave-valor, documentos, colunas (wide column) e grafos**; modelo **BASE** (Basically Available, Soft state, Eventually consistent) em vez de **ACID**; escala horizontal; usados em Big Data / alta disponibilidade. ACID × BASE: o relacional garante consistência imediata; o NoSQL prioriza disponibilidade/partição (ver tópico 9 — CAP/BASE).

## 2. Modelo Entidade-Relacionamento (MER)

- **MER (Peter Chen, 1976)**: **entidades** (retângulos), **relacionamentos** (losangos), **atributos** (elipses). Notações: Chen, Barker, **pé-de-galinha (crow's foot)**, IDEF1X.
- **Atributos**: monovalorados × multivalorados; armazenados × derivados; simples × compostos (aninháveis → **complexos**).
- **Cardinalidade**: 1:1, 1:N, N:1, M:N; mínima/máxima entre parênteses (min=0 → opcional; min≥1 → obrigatório).
- **Entidade forte** (tem PK própria) × **entidade fraca** (depende de forte; **relacionamento identificador**; atributo da forte faz parte da PK da fraca).
- **Auto-relacionamento** (ex.: CASAMENTO entre PESSOA e PESSOA em papéis diferentes).
- **Especialização** (top-down: superclasse → subclasses) × **generalização** (bottom-up: subclasses → superclasse) — inversas. **Disjunção** ("d": instância pertence a no máximo uma subclasse) × **sobreposição** ("o": pode pertencer a várias). **Participação total** (linhas duplas) × parcial.
- **Agregação**: trata um relacionamento como entidade de nível superior (relação entre relacionamentos).
- **Mapeamento ER → relacional**: entidades → tabelas; relacionamentos 1:N → FK no lado N; M:N → tabela de junção; atributos multivalorados → tabela nova; entidade fraca → PK composta (FK da forte + discriminador).

## 3. Normalização (Codd, 1972)

- **Objetivo**: eliminar **redundância** e **anomalias** (inserção, atualização, exclusão) por **decomposição**.
- **Dependência funcional (DF)**: X → Y (no máximo um Y por X). X = **determinante**; DF **trivial** se X contém Y. **Superchave** × **chave** (superchave mínima) × **chave candidata** × **chave primária**; atributos **primários** (membro de alguma candidata) × **não primários**.

| FN | Requisito | Problema eliminado |
|---|---|---|
| **1FN** | Domínios **atômicos** | Atributos compostos/multivalorados |
| **2FN** | 1FN + dependência **total** da chave candidata | Dependência **parcial** |
| **3FN** | 2FN + sem dependência **transitiva** de não primários | Dependência transitiva |
| **FNBC** | **Todo determinante é chave candidata** | Determinante não candidato |
| **4FN** | Eliminar **dependências multivaloradas** independentes | DMVs |
| **5FN** | Decomposição **sem perdas na junção** | Join dependency |

- **Cumulatividade**: 2FN exige 1FN; 3FN exige 2FN; FNBC exige 3FN. **FNBC é mais rígida que 3FN** (se está na FNBC, está na 3FN; o inverso não vale).
- Soluções: atributo **composto** → separar em colunas; **multivalorado** → nova tabela com chave composta.
- **UNIQUE com NULL não é determinante** (logo, não é chave candidata — pegadinha da FNBC).

---

# MÓDULO II — SQL E OPERAÇÕES SOBRE DADOS

## 1. Sublinguagens

SQL é **declarativa** (declara-se o *quem*, o SGBD decide o *como*).

| Sublinguagem | Comandos | Função |
|---|---|---|
| **DDL** | CREATE, ALTER, DROP, TRUNCATE | Definir/modificar objetos |
| **DML** | SELECT, INSERT, UPDATE, DELETE | Manipular dados |
| **DQL** | SELECT | Consultar (subconjunto da DML) |
| **DTL** | COMMIT, ROLLBACK, SAVEPOINT | Transações |
| **DCL** | GRANT, REVOKE | Permissões |

## 2. Consultas (extração, filtragem, classificação e combinação)

- **Ordem lógica de avaliação**: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`.
- **Filtragem**: `WHERE` (=, >, <, BETWEEN, LIKE, IN, IS NULL); **linhas** antes do agrupamento.
- **Agrupamento**: `GROUP BY` + funções agregadas (`COUNT, SUM, AVG, MAX, MIN`); **`HAVING`** filtra **grupos** depois do agrupamento (pegadinha: HAVING × WHERE).
- **Classificação**: `ORDER BY` (ASC/DESC).
- **Combinação**: **JOIN** — INNER, LEFT/RIGHT/FULL OUTER, CROSS; **UNION/INTERSECT/EXCEPT** (combinar consultas); **subconsultas** (IN, EXISTS, ALL, ANY/SOME).
- **VIEW**: consulta nomeada — **comum não é materializada** (executa a cada acesso); visões com JOIN/agregação **não são atualizáveis**. **Visão materializada** **armazena o resultado** (PostgreSQL 9.3+; REFRESH).
- **DELETE** (DML: remove linhas, transacional) × **TRUNCATE** (DDL: remove todas as linhas, rápido, sem log por linha) × **DROP** (DDL: remove o objeto e os dados).
- **GRANT/REVOKE** (DCL): privilégios, roles, `WITH GRANT OPTION`. **INFORMATION_SCHEMA**: catálogo de metadados.

---

# MÓDULO III — TRANSAÇÕES E CONCORRÊNCIA

## 1. ACID e transação

- **Transação**: unidade lógica de trabalho; inicia com BEGIN/START TRANSACTION, termina com **COMMIT** ou **ROLLBACK**; **SAVEPOINT** = rollback parcial.
- **ACID**: **A**tomicidade (tudo ou nada), **C**onsistência (estado válido), **I**solamento (transações não se interferem), **D**urabilidade (persiste após commit).

## 2. Níveis de isolamento (ANSI)

| Nível | Dirty Read | Non-Repeatable | Phantom |
|---|---|---|---|
| READ UNCOMMITTED | Sim | Sim | Sim |
| READ COMMITTED | Não | Sim | Sim |
| REPEATABLE READ | Não | Não | Sim |
| SERIALIZABLE | Não | Não | Não |

- **Dirty read** = ler dado não commitado (que pode ser desfeito); **non-repeatable read** = reler o mesmo dado e ver valor diferente; **phantom** = nova linha que satisfaz o filtro aparece entre leituras.

## 3. Controle de concorrência

- Problemas: atualização perdida, dirty read, non-repeatable, phantom.
- **Locks**: binário (uma transação por item) × múltiplo (**read lock** compartilhado + **write lock** exclusivo). **Protocolo 2PL** (duas fases: crescimento de locks → redução de unlocks). Alternativas: ordenação por **timestamp**, protocolo baseado em grafos.
- **Serializabilidade**: plano serializável ⇔ **grafo de precedência sem ciclos**.
- **Recuperação**: log (WAL — write-ahead log), **checkpoints**, redo/undo.
- **MVCC** (PostgreSQL/Oracle/MySQL-InnoDB): cada transação lê um *snapshot* — leituras não bloqueiam escritas.

---

# MÓDULO IV — ÍNDICES E TUNING

## 1. Índices

- **Primário** (chave de ordenação, esparso), **clustering** (campo de agrupamento, esparso), **secundário** (não chave, **denso**). **Denso** (entrada por valor) × **esparso** (entrada por bloco/valor distinto). **Multinível** (B-tree).
- **B-tree/B+tree** (padrão); **hash** (busca por igualdade); no PostgreSQL: **GiST, GIN, BRIN** (complementar).

## 2. Tuning

- **Full table scan × uso de índices**; otimização baseada em **custo**; formatação de consultas; estatísticas atualizadas (`ANALYZE`).
- **Alta disponibilidade**: cluster, **replicação**, **failover**, **balanceamento de carga**, backup online.
- Ferramentas: `EXPLAIN ANALYZE` (PostgreSQL), execution plans (Oracle), slow query log (MySQL) — *complementar*.

---

# MÓDULO V — PL/pgSQL E PL/SQL

## 1. PL/SQL (Oracle)

- Linguagem **procedural extensão do SQL** da Oracle, executada no servidor.
- **Blocos**: `DECLARE` (declarações) → `BEGIN` (executáveis) → `EXCEPTION` (tratamento de erros).
- **Estruturas**: IF/THEN/ELSE, CASE, loops (FOR, WHILE); **cursores** (implícitos/explícitos); **exceções** (nativas/usuário).
- **Procedures** (parâmetros IN/OUT) × **functions** (retornam valor) × **packages** (agrupamento). **Triggers**: BEFORE/AFTER/INSTEAD OF; row/statement.

## 2. PL/pgSQL (PostgreSQL)

- Linguagem procedural do PostgreSQL: `CREATE FUNCTION ... LANGUAGE plpgsql` com blocos `DECLARE/BEGIN/EXCEPTION`, estruturas de controle, cursores e **triggers**. Suporta visões atualizáveis, **MVCC** e transações completas.

---

# MÓDULO VI — SGBDDS DO EDITAL

| SGBD | Versões do edital | Destaques examináveis |
|---|---|---|
| **PostgreSQL** | **15, 16, 17 e 18** | Open source, ACID, JSON/JSONB, PL/pgSQL, MVCC, visões materializadas, lógica de replicação. *Complemento (pós-11)*: MERGE (15), incremental sorting, multirange, SQL/JSON, `NULLS NOT DISTINCT`, melhorias de VACUUM/paralelismo |
| **Oracle** | **19c** | SGBD líder empresarial; **19c = release de longo prazo (LTS)**; multitenant (CDB/PDB), **Automatic Indexing**, RAC, PL/SQL, dicionário de dados. *Base local cobre 11g* |
| **MySQL** | **8** | InnoDB (padrão, ACID, FK) × MyISAM; **8.0**: window functions, CTEs recursivas, utf8mb4 padrão, roles, CHECK constraints, invisible/descending indexes |
| **NoSQL** | — | Chave-valor (Redis), documentos (MongoDB), colunas (Cassandra), grafos (Neo4j); BASE; uso em Big Data |

- **H2** (citado no tópico 8): banco **em memória** para testes.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **DELETE** é DML (transacional); **TRUNCATE** e **DROP** são DDL.
2. **WHERE** filtra **linhas** antes do GROUP BY; **HAVING** filtra **grupos** depois.
3. **3FN × FNBC**: FNBC exige **todo determinante = chave candidata**; é mais rígida.
4. **UNIQUE com NULL** não é determinante → não qualifica a FNBC.
5. **View comum não é materializada**; **materializada** guarda o resultado fisicamente.
6. **Atributo composto** → separar colunas; **multivalorado** → nova tabela (ambos violam a 1FN).
7. **Grau** = nº de colunas; **cardinalidade** = nº de linhas.
8. **SQL é declarativa**, não procedural.
9. **READ COMMITTED** resolve dirty read; **REPEATABLE READ** ainda tem **phantom**; só **SERIALIZABLE** resolve tudo.
10. **ACID** (relacional) × **BASE** (NoSQL) não são equivalentes.
11. **Especialização** = top-down; **generalização** = bottom-up.
12. **Disjunção** = exclusividade de subclasse; **sobreposição** = múltiplas.
13. **Índice secundário** é **denso**; primário/clustering são **esparso**s.
14. **PG 15–18 / Oracle 19c / MySQL 8** = versões do edital (base local: PG 11, Oracle 11g — complementar as novidades).
15. **MVCC**: leituras não bloqueiam escritas (PostgreSQL).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) No modelo relacional, o comando TRUNCATE, que remove todas as linhas de uma tabela, pertence à sublinguagem DML.
a) Certo. b) Errado.

> **Resposta: b (Errado).** TRUNCATE é **DDL** (define/altera objetos — remove o conteúdo da tabela de forma rápida). O comando DML que remove linhas é o **DELETE** (transacional, linha a linha).

---

**Questão 2.** (FCC-style) A cláusula SQL utilizada para filtrar grupos resultantes da operação GROUP BY é:
a) WHERE.
b) HAVING.
c) ORDER BY.
d) DISTINCT.
e) INTO.

> **Resposta: b.** **HAVING** filtra **grupos** após o agrupamento; **WHERE** filtra **linhas** antes. Ordem lógica: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

---

**Questão 3.** (CESPE-style) Uma tabela encontra-se na Terceira Forma Normal (3FN) quando todos os seus atributos não primários são totalmente dependentes da chave candidata.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Essa é a definição da **2FN** (dependência total, sem parcial). A **3FN** exige ainda que **não haja dependência transitiva** de atributos não primários em relação à chave.

---

**Questão 4.** (FCC-style) Entre as formas normais apresentadas, aquela que exige que todo determinante de uma dependência funcional seja também chave candidata é:
a) 1FN.
b) 2FN.
c) 3FN.
d) FNBC (Boyce-Codd).
e) 4FN.

> **Resposta: d.** A **FNBC** é mais rígida que a 3FN: **todo determinante deve ser chave candidata**. Se está na FNBC, está na 3FN (o inverso não é verdadeiro).

---

**Questão 5.** (CESPE-style) O nível de isolamento READ COMMITTED elimina os fenômenos de dirty read e de leitura não repetível.
a) Certo. b) Errado.

> **Resposta: b (Errado).** READ COMMITTED elimina **dirty read** apenas. A **leitura não repetível** persiste até o REPEATABLE READ, e o **phantom** até o SERIALIZABLE.

---

**Questão 6.** (FCC-style) No modelo Entidade-Relacionamento, uma entidade que não possui atributos suficientes para definir sua chave primária, dependendo de outra entidade para tanto, denomina-se:
a) entidade forte.
b) entidade fraca.
c) entidade associativa.
d) generalização.
e) agregação.

> **Resposta: b.** **Entidade fraca** não tem PK própria; o **relacionamento identificador** e atributos da entidade **forte** completam sua chave.

---

**Questão 7.** (CESPE-style) Uma view criada a partir de um JOIN entre duas tabelas pode ser atualizada normalmente por meio de comandos INSERT e UPDATE.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Visões com **JOIN, agrupamento ou agregação não são atualizáveis**. Além disso, a view comum **não é materializada** — é uma consulta executada a cada acesso.

---

**Questão 8.** (FCC-style) A propriedade ACID que garante que uma transação será executada por inteiro ou não produzirá nenhum efeito denomina-se:
a) Atomicidade.
b) Consistência.
c) Isolamento.
d) Durabilidade.
e) Serializabilidade.

> **Resposta: a.** **Atomicidade** = tudo ou nada. Consistência = estado válido; Isolamento = transações independentes; Durabilidade = persistência pós-commit.

---

**Questão 9.** (CESPE-style) A especialização, no modelo EER, corresponde ao processo bottom-up de agrupamento de subclasses em uma superclasse comum.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Especialização** é top-down (superclasse → subclasses). O processo **bottom-up** (subclasses → superclasse) é a **generalização**.

---

**Questão 10.** (FCC-style) Sobre índices em banco de dados, é correto afirmar:
a) O índice secundário é esparso, com uma entrada por bloco.
b) O índice primário é denso, com entrada para cada registro.
c) O índice secundário é denso, com entrada para cada valor dos campos indexados.
d) O índice clustering exige a chave primária como campo de ordenação.
e) Índices eliminam a necessidade de tuning de consultas.

> **Resposta: c.** **Secundário = denso**; primário e clustering = **esparso**. Índices ajudam, mas não substituem o tuning.

---

**Questão 11.** (CESPE-style) O MySQL 8 utiliza, por padrão, o mecanismo de armazenamento MyISAM, que oferece suporte completo a transações ACID e chaves estrangeiras.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O mecanismo padrão do MySQL 8 é o **InnoDB** (ACID, FK, MVCC). O **MyISAM** não suporta transações nem chaves estrangeiras.

---

**Questão 12.** (FCC-style) A linguagem procedural padrão do PostgreSQL para a criação de funções, triggers e blocos de programação no servidor é:
a) PL/SQL.
b) T-SQL.
c) PL/pgSQL.
d) PSM.
e) Java Stored Procedures.

> **Resposta: c.** **PL/pgSQL** é do PostgreSQL; **PL/SQL** é do Oracle; T-SQL, do SQL Server.

---

**Questão 13.** (CESPE-style) No modelo relacional, atributos multivalorados violam a Primeira Forma Normal e devem ser remanejados para uma nova tabela, com chave composta.
a) Certo. b) Errado.

> **Resposta: a (Certo).** 1FN exige domínios atômicos. **Multivalorado** (ex.: telefones) → **nova tabela**; **composto** (ex.: endereço) → separar em colunas.

---

**Questão 14.** (FCC-style) Em controle de concorrência, o protocolo de bloqueio em duas fases (2PL) caracteriza-se por:
a) Liberar locks progressivamente à medida que novos locks são adquiridos.
b) Uma fase de crescimento (aquisição de locks) seguida de uma fase de redução (liberação), sem nova aquisição após o primeiro unlock.
c) Uso exclusivo de timestamps para serialização, sem bloqueios.
d) Permissão de dirty reads para aumentar a concorrência.
e) Bloqueio binário exclusivo de leitura e escrita.

> **Resposta: b.** **2PL**: fase de **crescimento** (só adquire) e fase de **redução** (só libera). Garante serializabilidade.

---

**Questão 15.** (CESPE-style) Os bancos de dados NoSQL adotam obrigatoriamente o modelo ACID, dispensando o conceito de consistência eventual.
a) Certo. b) Errado.

> **Resposta: b (Errado).** NoSQL adota tipicamente **BASE** (Basically Available, Soft state, Eventually consistent) — consistência **eventual**, foco em disponibilidade/partição. ACID é o modelo do relacional.

---

## Questões discursivas

**D1.** Diferencie as formas normais 3FN e FNBC e explique a diferença entre dependência funcional parcial e transitiva.

> **Modelo de resposta:** A **3FN** exige que a tabela esteja na 2FN e que nenhum atributo não primário dependa **transitivamente** da chave candidata (A→B→C, com B e C não chave). A **FNBC** é mais rígida: exige que **todo determinante** de qualquer dependência funcional seja **chave candidata** — resolvendo casos em que um atributo primário é determinado por um não primário (permitido na 3FN). **Dependência parcial** (eliminada pela 2FN): o atributo não chave depende de **parte** de uma chave composta. **Dependência transitiva** (eliminada pela 3FN): o atributo depende de outro atributo não chave, que por sua vez depende da chave.

**D2.** Explique os fenômenos dirty read, non-repeatable read e phantom e relate-os aos níveis de isolamento SQL.

> **Modelo de resposta:** **Dirty read** = ler dados ainda não commitados (que podem ser revertidos); **non-repeatable read** = duas leituras do mesmo registro retornam valores diferentes por interferência de outra transação; **phantom** = linhas novas que satisfazem a consulta aparecem entre leituras. **READ UNCOMMITTED** sofre os três; **READ COMMITTED** elimina o dirty read; **REPEATABLE READ** elimina também o non-repeatable; apenas **SERIALIZABLE** elimina o phantom, equivalendo à execução em série.

---

*Base: `07.Banco de Dados` (Aulas 00–10) e `08.SGBDs` (Aulas 00–07) do material local; complemento técnico para PostgreSQL 15–18, Oracle 19c, MySQL 8 e PL/pgSQL (ausentes ou desatualizados na base de 2020).*