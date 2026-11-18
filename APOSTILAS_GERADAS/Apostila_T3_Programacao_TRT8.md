# APOSTILA — TÓPICO 3: PROGRAMAÇÃO
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Programação: linguagens de programação Python, Java, JavaScript e TypeScript. Fundamentos de programação: tipos de dados, variáveis, operadores, estruturas de controle, laços de repetição, funções, manipulação de strings, arranjos (arrays), estruturas de dados. Programação orientada a objetos (POO): classes, objetos, atributos, métodos, herança, polimorfismo, encapsulamento e abstração. Tratamento de exceções. Acesso a bancos de dados. Versionamento de código com Git.
>
> **Base de conhecimento:** `04.Desenvolvimento de Software` (Aula03 — POO/Java) + **complemento técnico** para Python, JavaScript e TypeScript (ausentes na base de 2020). Git e Maven/CI: ver apostilas T7/T8.

---

# MÓDULO I — FUNDAMENTOS DE PROGRAMAÇÃO

## 1. Conceitos básicos

- **Algoritmo**: sequência finita e ordenada de passos para resolver um problema. Linguagem de programação = formalismo para expressá-lo ao computador.
- **Tipos de dados**: **primitivos** (inteiros, reais/floating-point, caracteres, booleanos) × **compostos** (strings, arrays/listas, objetos, dicionários). **Tipagem estática** (Java, TypeScript) × **dinâmica** (Python, JavaScript): na estática, o tipo é declarado/verificado em **compilação**; na dinâmica, em **tempo de execução**.
- **Variáveis e constantes**: declaração, escopo (global/local/bloco), mutabilidade (`let`/`var` vs `const`, Python `PEP 8`).
- **Operadores**: aritméticos (`+ - * / % **`), relacionais (`== != > <`), lógicos (`&& || !` / `and or not`), atribuição, incremento; **precedência** e **curto-circuito**. **`=` × `==` × `===`** (em JS, `===` compara **valor e tipo** — pegadinha clássica).
- **Estruturas de controle**: `if/else`, `switch/case` (Java/JS) ou `match` (Python 3.10+), condicionais ternárias.
- **Laços de repetição**: `for` (contador), `while`, `do-while`; `for-each`/`for...of`; controle com `break`/`continue`. Evitar laços infinitos; complexidade de laços aninhados (O(n²)).
- **Funções/métodos**: parâmetros, retorno, **sobrecarga** (Java), valores padrão (Python/JS), **arrow functions** (JS/TS), recursão (caso base + passo recursivo), passagem por valor × por referência (em Java: primitivos por valor, objetos por referência).
- **Strings**: imutáveis em Java e Python; métodos comuns (concatenação, busca, substring, split/format, maiúsculas/minúsculas). **Interpolação** (f-strings Python, template literals JS/TS).
- **Arrays/listas/estruturas**: array (tamanho fixo em Java), lista dinâmica (`ArrayList`, `list` Python, `[]` JS), fila/pilha, dicionário/mapa (`Map`, `dict`, `Object`/`Map`), conjunto (`Set`). **Complexidade** básica: acesso por índice O(1), busca em lista O(n), busca em mapa O(1) amortizado.

## 2. Tratamento de exceções

- **Erro** (compilação) × **exceção** (tempo de execução) × **falha**.
- **Java**: `try/catch/finally`, `throw` (lança) × `throws` (declara); hierarquia: `Throwable → Error × Exception → RuntimeException` (**checked** × **unchecked**). `try-with-resources` (AutoCloseable).
- **Python**: `try/except/else/finally`, `raise`, exceções built-ins (`ValueError`, `TypeError`, `KeyError`, `ZeroDivisionError`), `Exception` como base comum.
- **JavaScript/TypeScript**: `try/catch/finally` (só catch de exceções em runtime; **não** distingue checked/unchecked); `throw` aceita qualquer valor; `Error` com `message`/`stack`. Promises: `.catch` e `async/await` com `try/catch`.

---

# MÓDULO II — PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)

## 1. Conceitos

- **POO**: paradigma que organiza o código em **objetos** (instâncias de **classes**) que combinam **estado** (atributos) e **comportamento** (métodos).
- **Os 4 pilares**:
  1. **Encapsulamento**: ocultar detalhes internos, expor interface controlada (`private/protected/public`; getters/setters).
  2. **Herança**: subclasse herda atributos/métodos de superclasse (`extends`); promove reuso (cuidado com acoplamento).
  3. **Polimorfismo**: mesma chamada, comportamentos diferentes — **sobrecarga** (compile-time) × **sobrescrita/override** (runtime; dinâmica).
  4. **Abstração**: modelar o essencial, esconder a complexidade (classes **abstratas** × **interfaces**).
- **Classe abstrata** (pode ter estado e métodos concretos; não é instanciável) × **interface** (contrato; em Java 8+, com métodos `default`/`static`; múltiplas implementações).
- **Outros conceitos**: **composição/agregação** ("tem-um" × "é-um"), **construtores**, `this`, `static`, `final`, **imutabilidade**, **acoplamento × coesão**, SOLID (complementar).

## 2. Java × Python × JavaScript × TypeScript (comparativo)

| Aspecto | Java | Python | JavaScript | TypeScript |
|---|---|---|---|---|
| Tipagem | Estática | Dinâmica | Dinâmica | **Estática (superset do JS)** |
| Compilação | Compilado (bytecode JVM) | Interpretado (CPython) | Interpretado (engine do browser/Node) | Compila p/ JS |
| POO | Classes (`class`) | Classes + múltipla herança | **Protótipos** + classes (ES6) | Classes (como Java moderno) |
| Sintaxe | `int x = 1;` | `x = 1` | `let x = 1;` | `let x: number = 1;` |
| Execução | JVM (multiplataforma) | Interpretador | Browser / Node.js | Node/browser (via JS) |
| Exceções | Checked + unchecked | `try/except` | `try/catch` (só runtime) | `try/catch` + tipagem |

- **Python**: indentação define blocos; `None`, list comprehensions, `PEP 8`; baterias incluídas (stdlib); usado em web (Django/Flask), dados e scripts.
- **JavaScript**: linguagem do navegador (ECMAScript); **dinâmica**, baseada em **protótipos**; assíncrono (event loop, callbacks, promises, `async/await`); **JSON** é subconjunto sintático; DOM.
- **TypeScript**: **JavaScript com tipos** (Microsoft); tipos opcionais, interfaces, enums, generics; **transpila** para JS; erros de tipo detectados **antes** da execução; usado em grandes aplicações (Angular).
- **Java**: POO estrita, JVM, forte em corporativo/Android; **JDBC** para banco; **Maven** para build (ver T7).

---

# MÓDULO III — ACESSO A BANCOS DE DADOS

## 1. Java (JDBC/JPA)

- **JDBC** (Java Database Connectivity): API padrão — `DriverManager`, `Connection`, `Statement`/`PreparedStatement`, `ResultSet`, `commit/rollback`.
- **PreparedStatement** evita **SQL injection** (parametrização); `Statement` concatena strings (perigoso).
- **JPA/Hibernate** (ORM): mapeia objetos ↔ tabelas; ver apostila T4/T8.

## 2. Python e JavaScript

- **Python**: **DB-API 2.0** (`psycopg2`/`psycopg` p/ PostgreSQL, `sqlite3`, `SQLAlchemy` como ORM).
- **JavaScript/TypeScript**: drivers (`pg`, `mysql2`), ORMs (**Sequelize**, **TypeORM**, **Prisma**); em Node.js, conexões assíncronas com pool.
- **Boas práticas**: parametrizar consultas (evitar injection), usar **pool de conexões**, transações explícitas, **migrations** para schema (Flyway — T8).

## 3. SQL

Ver apostila T4 (DDL/DML/DCL, JOIN, transações). O acesso programático sempre envolve **abrir conexão → executar SQL → tratar resultados → fechar** (ou usar ORM/pool).

---

# MÓDULO IV — VERSIONAMENTO DE CÓDIGO COM GIT

- **Git**: controle de versão **distribuído** (repositório completo em cada dev). Conceitos: **working tree → staging (add) → commit → push**; **branch** (ponteiro leve), **merge** (preserva história) × **rebase** (reescreve história), **revert** (novo commit que desfaz) × **reset** (move o ponteiro).
- Comandos essenciais: `git init/clone`, `status`, `add`, `commit -m`, `push/pull/fetch`, `branch`, `checkout/switch`, `merge`, `rebase`, `stash`, `log`, `tag`.
- **Fluxos**: **Git Flow** (main/develop/feature/release/hotfix) × **GitHub Flow/trunk-based** (main + PRs curtos). **PRs** para revisão; **semver** (major.minor.patch); `.gitignore`.
- *Detalhamento completo na apostila T7 (DevOps).*

---

# RESUMO DE PEGADINHAS DE PROVA

1. **`===` (JS)** compara **valor e tipo**; `==` faz coerção de tipos; `=` é atribuição.
2. **TypeScript** é **superset** do JS com **tipagem estática**; transpila para JavaScript.
3. **Java** é tipado estaticamente e compilado (JVM); **Python/JS** são dinâmicos.
4. **JS usa protótipos**; as classes ES6 são açúcar sintático sobre protótipos.
5. **Java**: exceções **checked** (obrigam `throws`/catch) × **unchecked** (`RuntimeException`). JS/Python **não** têm checked.
6. **PreparedStatement** previne **SQL injection**; concatenação de strings, não.
7. **Encapsulamento** = ocultar; **herança** = reuso ("é-um"); **polimorfismo** = mesmo método, comportamentos diferentes.
8. **Sobrecarga** = mesma assinatura-em-nome, parâmetros diferentes (compile-time); **sobrescrita** = mesma assinatura em subclasses (runtime).
9. **Classe abstrata** não é instanciável; **interface** define contrato (múltiplas em Java).
10. **Python** usa **indentação** como bloco (não chaves).
11. **`throw` (lança)** × **`throws` (declara)** em Java.
12. **Git merge** preserva história; **rebase** reescreve; **revert** cria commit novo que desfaz.
13. **`fetch`** só baixa; **`pull`** = fetch + merge.
14. **JSON** é independente de linguagem (embora a sintaxe venha do JS).
15. Java: **primitivos por valor, objetos por referência**.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) A linguagem TypeScript é uma linguagem distinta do JavaScript, executada diretamente pelo navegador sem transpilação.
a) Certo. b) Errado.

> **Resposta: b (Errado).** TypeScript é um **superset** do JavaScript que **transpila** para JS; o navegador executa o JavaScript gerado.

---

**Questão 2.** (FCC-style) Em JavaScript, a expressão `0 == "0"` retorna true, enquanto `0 === "0"` retorna false porque:
a) `===` compara apenas o tipo dos operandos.
b) `==` compara valor e tipo; `===` apenas valor.
c) `===` compara valor e tipo; `==` compara apenas o valor, com coerção de tipos.
d) ambos comparam igualmente, a diferença é apenas de performance.
e) `===` não é suportado em JavaScript.

> **Resposta: c.** `==` faz **coerção** (compara o valor após conversão); `===` exige **valor e tipo** iguais (comparação estrita).

---

**Questão 3.** (CESPE-style) Em Java, uma exceção do tipo RuntimeException exige que o método a declare na cláusula throws ou a capture em bloco try-catch.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `RuntimeException` é **unchecked** (não verificada) — **não** obriga `throws`/catch. As **checked** (ex.: `IOException`) é que obrigam.

---

**Questão 4.** (FCC-style) O pilar da POO que consiste em ocultar os detalhes internos de um objeto, expondo apenas uma interface controlada de acesso, é:
a) herança.
b) polimorfismo.
c) encapsulamento.
d) abstração.
e) sobrecarga.

> **Resposta: c.** **Encapsulamento** (modifiers private/protected/public, getters/setters).

---

**Questão 5.** (CESPE-style) No Python, os blocos de código são delimitados por chaves { }, semelhantemente ao Java.
a) Certo. b) Errado.

> **Resposta: b (Errado).** No Python, os blocos são definidos por **indentação** (espaços/tabulações), não por chaves.

---

**Questão 6.** (FCC-style) Em acesso a banco de dados via JDBC, a classe que permite executar consultas SQL parametrizadas, prevenindo SQL injection, é:
a) Statement.
b) PreparedStatement.
c) DriverManager.
d) ResultSet.
e) Connection.

> **Resposta: b.** **PreparedStatement** parametriza (`?`) e previne **SQL injection**; `Statement` concatena strings.

---

**Questão 7.** (CESPE-style) O polimorfismo de sobrecarga (overloading) ocorre em tempo de execução, quando subclasses fornecem implementações diferentes de um mesmo método.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Sobrecarga** = compile-time (mesmo nome, parâmetros diferentes). A **sobrescrita (override)** em subclasses é que ocorre em **runtime** (polimorfismo dinâmico).

---

**Questão 8.** (FCC-style) Em TypeScript, a principal vantagem em relação ao JavaScript puro é:
a) execução nativa sem compilação.
b) verificação de tipos em tempo de compilação, reduzindo erros em tempo de execução.
c) ausência de suporte a orientação a objetos.
d) substituição completa do JavaScript no navegador.
e) menor tamanho dos artefatos finais.

> **Resposta: b.** **Tipagem estática** detectada antes da execução (transpila para JS).

---

**Questão 9.** (CESPE-style) Em Git, o comando `git rebase` reaplica commits sobre outra base, preservando integralmente o histórico original do branch.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `rebase` **reescreve o histórico** (cria novos commits). Quem preserva é o `merge`. Rebase é perigoso em branches compartilhados.

---

**Questão 10.** (FCC-style) A estrutura de dados que armazena pares chave-valor, com acesso médio O(1), é:
a) array.
b) lista encadeada.
c) pilha.
d) dicionário (mapa/tabela hash).
e) fila.

> **Resposta: d.** **Dicionário/mapa (hash)** = chave-valor, O(1) médio. Array = acesso O(1) por índice, mas busca O(n); lista encadeada = O(n).

---

**Questão 11.** (CESPE-style) Em Python, a palavra-chave `None` representa um objeto vazio equivalente a zero ou à string vazia.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `None` é o **absence de valor** (singleton `NoneType`) — diferente de `0`, `""` ou `False` (embora todos sejam falsy em contexto booleano).

---

**Questão 12.** (FGV-style) Sobre tratamento de exceções, é correto afirmar:
a) Java e Python possuem exceções verificadas (checked) que obrigam o uso de throws.
b) Em JavaScript, o bloco catch trata apenas exceções de tempo de execução, sem distinção checked/unchecked.
c) Em Java, `throw` declara que um método pode lançar exceção.
d) Em Python, o bloco `finally` só executa se ocorrer exceção.
e) Exceções devem ser usadas para controle normal de fluxo do programa.

> **Resposta: b.** JS só trata exceções de runtime. Em Java, **`throws`** declara; **`throw`** lança. `finally` **sempre** executa (Python/Java). Exceções não são para fluxo normal.

---

**Questão 13.** (CESPE-style) A composição, em POO, representa uma relação do tipo "é-um", típica da herança entre classes.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Composição/agregação** = "**tem-um**" (objeto contém outro). **Herança** = "**é-um**".

---

**Questão 14.** (FCC-style) Em JavaScript moderno, a construção `async/await` é usada para:
a) declarar variáveis imutáveis.
b) simplificar o consumo de Promises, escrevendo código assíncrono com sintaxe síncrona.
c) criar classes abstratas.
d) tipar variáveis estaticamente.
e) compilar TypeScript.

> **Resposta: b.** `async/await` é açúcar sintático sobre **Promises** para código assíncrono legível.

---

**Questão 15.** (CESPE-style) No Git, o comando `git fetch` atualiza as referências remotas no repositório local e já integra automaticamente as mudanças ao branch de trabalho.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `fetch` **só baixa** (atualiza referências remotas); **`pull`** = fetch + **merge** (integra).

---

## Questões discursivas

**D1.** Explique os quatro pilares da POO e diferencie sobrecarga de sobrescrita de métodos.

> **Modelo de resposta:** Os pilares são: **encapsulamento** (ocultar detalhes e expor interface controlada), **herança** (subclasse reutiliza atributos/métodos de superclasse — relação "é-um"), **polimorfismo** (mesma chamada com comportamentos distintos) e **abstração** (modelar o essencial via classes abstratas/interfaces). **Sobrecarga** (overloading) ocorre em **tempo de compilação**: mesmo nome, diferentes listas de parâmetros no mesmo escopo. **Sobrescrita** (overriding) ocorre em **tempo de execução**: subclasses redefinem um método herdado com a mesma assinatura, e a versão executada depende do objeto concreto (polimorfismo dinâmico).

**D2.** Compare Java, Python, JavaScript e TypeScript quanto a tipagem, compilação e modelo de POO, e cite uma medida de segurança no acesso a banco de dados.

> **Modelo de resposta:** **Java** é estaticamente tipado, compilado para bytecode da JVM, com POO por classes e exceções checked/unchecked. **Python** é dinamicamente tipado e interpretado, com blocos por indentação e POO por classes (herança múltipla). **JavaScript** é dinâmico, interpretado (browser/Node), baseado em **protótipos** (classes ES6 como sintaxe), com assincronia via event loop/promises. **TypeScript** é JavaScript com **tipagem estática** (superset), compilado (transpilado) para JS, muito usado em aplicações grandes. No acesso a banco, deve-se usar consultas **parametrizadas** (ex.: `PreparedStatement` no JDBC) para prevenir **SQL injection**, além de pool de conexões e transações explícitas.

---

*Base: `04.Desenvolvimento de Software` (Aula03 — POO/Java; Aula05 — JDBC/JPA). Complemento: Python, JavaScript e TypeScript não têm aula dedicada no material local de 2020 — conteúdo técnico complementar. Git: ver apostila T7 (DevOps).*