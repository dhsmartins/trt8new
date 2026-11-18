# APOSTILA — TÓPICO 5: DESENVOLVIMENTO DE APLICAÇÕES WEB E MOBILE
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Desenvolvimento de aplicações web e mobile: linguagens de programação Java; linguagens de marcação de hipertexto (HTML); linguagens de folhas de estilo (CSS); web services; linguagens de programação JavaScript e TypeScript; linguagem de programação Python.
>
> **Base de conhecimento:** `04.Desenvolvimento de Software` (Aulas 02, 04, 07, 09, 18, 19) — Curso Regular TI 2020.2 + **complemento** (TypeScript, Python, design responsivo, frameworks modernos).

---

# MÓDULO I — HTML E CSS

## 1. HTML

- **HTML** = linguagem de **marcação** (não de programação), criada por Tim Berners-Lee. **Não case-sensitive** (XHTML é). `<!DOCTYPE>` é **instrução**, não tag. HTML5 exige `!DOCTYPE` e `<title>`.
- Papéis: **conteúdo = HTML**; **apresentação = CSS**; **comportamento = JavaScript** (regra W3C).
- Versões: 1991 → 2.0 (1995) → 3.2 (1997) → 4.01 (1999) → XHTML (2000) → **HTML5 (2014)**. `meta charset="utf-8"`.
- Tags **sem fechamento** (void): `img, br, hr, input, meta, link`. Títulos `h1`–`h6` (6 níveis). `th` = negrito + centralizado.
- **Formulários HTML5**: inputs `tel, search, url, email, date, number, range, color` (sem suporte viram text; **`tel` não é validado**); atributos `placeholder, required, pattern` (RegEx), `autofocus`. Validação client-side **não dispensa** a server-side.
- **Obsoletos**: `basefont, big, center, font, strike, tt`. **Removidos**: `frameset, frame, noframes` (acessibilidade); `acronym` → `abbr`; `applet` → `embed/object`; `dir` → `ul`.
- **Novos HTML5**: `article, aside, audio, canvas, datalist, details, figure, footer, header, main, nav, section, video, svg`; `sessionStorage`/`localStorage` (offline).

## 2. CSS

- **Cascading Style Sheets** (W3C). **Cascata** (prioridade decrescente): `!important` **usuário** > `!important` dev > dev (inline → interna → externa) > usuário > navegador. *Pegadinha: o `!important` do usuário vence o do dev.*
- Sintaxe `seletor { propriedade: valor; }`. Seletores: elemento (`p`), classe (`.x`), id (`#x` — **único**), atributo (`a[target="_blank"]`), agrupamento (vírgula). Conflito de classes: resolve pela **última regra**.
- Classificação: **inline** (`style`), **interna** (`<style>`), **externa** (`<link rel="stylesheet">`). `px` fixo × `em` relativo (bom para smartphones).
- **Tableless**: tabelas só para dados tabulares. **Position**: static (padrão), relative, absolute (relativa ao pai estático mais próximo), fixed (viewport), sticky.
- **CSS3**: transforms, animations, multicoluna (dispensa Flash/JS). *Complemento*: design responsivo com **media queries** (ausente no material).

---

# MÓDULO II — JAVASCRIPT, JSON E AJAX

## 1. JavaScript

- Criado por Netscape+Sun (1995); JScript = resposta da Microsoft. Linguagem **client-side**, **dinamicamente tipada**, baseada em **protótipos**, **escopo de função**, **não compilada**. **Case-SENSITIVE**. Padrão **ECMAScript** (ES6: `let/const`, classes, Map/Set).
- *Pegadinha clássica*: **"Java and JavaScript are as similar as Car and Carpet"** — Java é estático, classes, escopo de bloco, compilado; JS é dinâmico, protótipos, escopo de função, interpretado.
- 3 formas de inserção: **externa** (`.js` via `<script src>`), **incorporada** (`<head>`), **inline** (desaconselhável). Manipula o **DOM** (W3C) — `document.getElementById` + `innerHTML`.
- **JSON**: formato de intercâmbio — 2 estruturas (pares nome/valor e listas ordenadas). **Independente de linguagem**; sem DTD/XSD (o XML valida elementos; o JSON só a forma). Parsing = função JS (mais leve que XML).

## 2. AJAX

- **NÃO é uma tecnologia** — é um **conjunto**: XHTML+CSS (apresentação), DOM (exibição), XML+XSLT (dados), **XMLHttpRequest** (recuperação assíncrona), JavaScript (agrega). Elimina recarga total de página.
- `readyState` 0–4 (**4 = resposta pronta**); status 200 = OK, 404 = não encontrada; `responseXML` (DOM) × `responseText` (string). **Desvantagem**: sem JS, a aplicação quebra.
- **jQuery**: biblioteca cross-browser — `$(seletor).ação()`, `$(document).ready(...)`.

## 3. TypeScript *(complemento)*

- **JavaScript com tipagem estática** (superset da Microsoft): tipos, interfaces, enums, generics; **transpila** para JS; detecta erros de tipo **antes** da execução. Ver apostila T3.

---

# MÓDULO III — JAVA EE, SPRING E WEB SERVICES

## 1. Java EE / Jakarta EE

- Conjunto de **especificações** para aplicações distribuídas, robustas, escaláveis, **multicamadas**. Camadas: Cliente, Web, Negócio (EJB), EIS/Dados.
- Nomes: J2EE → Java EE → **Jakarta EE** (2018, Eclipse Foundation). **Perfis**: **Web Profile** (WAR; EJB Lite) × **Full Profile** (JAX-WS, JAX-RS, JMS, EAR). Módulos: **EAR** (aplicação completa), **WAR** (web: JSP/Servlets/HTML), **JAR** (EJB), **RAR** (resource adapter).
- APIs: **Servlets**, **JSF**, **JSP** (declarações/expressões/scriptlets/diretivas), **JSTL**, JPA, JMS, JTA, **JAX-WS (SOAP)**, **JAX-RS (REST)**, JAXB.

## 2. Spring

- Framework Java leve (~2MB), não-intrusivo, alternativa a EJB. **IoC** (Inversão de Controle) × **DI** (Injeção de Dependência — conceitos **independentes**; DI por construtor/setter/interface).
- Módulos: Core, AOP, DAO (abstrai JDBC), ORM (JPA/Hibernate), JMS, **MVC**, **Security** (autenticação × autorização; `<intercept-url>`), Boot, Data JPA.
- **Spring Boot**: autoconfiguração, servidor embarcado (ver apostila T8).

## 3. Web Services

- **SOAP**: **protocolo** (mensagens XML), WSDL descreve, UDDI registra. Envelope obrigatório; Header **opcional** (se presente, primeiro elemento); Body **obrigatório**; Fault opcional.
- **REST**: **estilo arquitetural** (Roy Fielding) — recursos via URI, métodos HTTP, **stateless**, JSON/XML. 6 restrições (cliente-servidor, stateless, camadas, cache, **interface uniforme**, código sob demanda — única opcional).
- *Comparação SOAP × REST: ver apostila T6.*

---

# MÓDULO IV — DESENVOLVIMENTO MOBILE

## 1. Abordagens

| Aspecto | Nativo | Web App (responsivo) | Híbrido |
|---|---|---|---|
| Linguagem | Plataforma (Swift/Kotlin/Java) | HTML+CSS+JS | Web envelopada em contêiner nativo |
| Distribuição | Loja de apps | Servidor/navegador | Loja de apps |
| Desempenho | Rápido | Dependente de rede | Intermediário |
| Hardware | Total (GPS, câmera...) | Parcial | Via framework |
| Custo | Mais caro | Mais barato | Intermediário |
| Atualização | Download/install | **Instantânea** (servidor) | Download/install |

- **Cross-platform** = Web/Responsivo + Híbrido. **Híbrido** = app web em **contêiner nativo** (Cordova, Ionic, Sencha Touch) — **não** acessa bibliotecas nativas diretamente (o contêiner faz); tem overhead de encapsulamento.
- **React Native** (Facebook): JS → código **nativo** (não é só webview); Hot Reloading; Flexbox. **Flutter** (Google): linguagem **Dart**; widgets; desenha em canvas (sem bridge).

## 2. Android e iOS

- **Android**: kernel **Linux**; **Dalvik/ART VM** (não JVM); componentes: **Activities** (telas), **Intents** ("cola" entre atividades), **Services** (2º plano, na thread principal), **Broadcast Receivers**, **Content Providers** (compartilham dados entre apps). `AndroidManifest.xml`; pastas `src`, `gen` (classe `R`), `res`.
- **iOS**: Objective-C/Swift, Cocoa Touch, Xcode.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **HTML não é linguagem de programação**; `!DOCTYPE` não é tag; HTML **não** case-sensitive (XHTML e JS sim).
2. **`img`/`br`/`hr`** não têm fechamento; **`tel` não é validado** pelos browsers.
3. Cascata CSS: **`!important` do usuário vence o do dev**; conflito de classes = **última regra**; **id é único**.
4. **Java ≠ JavaScript** ("Car and Carpet"); JS = **protótipos**, escopo de função, dinâmica.
5. **AJAX não é tecnologia**, é **conjunto**; `readyState=4` = resposta pronta; sem JS, a app quebra.
6. **JSON é independente de linguagem**; não tem DTD/XSD; identificadores entre aspas.
7. **Spring**: IoC e DI são conceitos **independentes**; injeção por interface **não** tem IoC.
8. **Android**: apps em Java mas em **Dalvik VM** (não JVM); **Services** na thread principal; **Content Provider** compartilha dados entre apps.
9. **Híbrido** = app **web envelopada** em contêiner nativo (não é mais leve).
10. HTML5: validação client-side **não dispensa** server-side; **frames removidos** por acessibilidade.
11. **Java EE**: Web Profile **não inclui** JAX-WS/JAX-RS/JMS/EAR (só WAR); EJB é **Lite**.
12. **Idempotentes**: GET/PUT/DELETE/HEAD/OPTIONS; **POST/PATCH não**. **Seguros** (sem efeitos): GET/HEAD/OPTIONS.
13. **SOAP = protocolo** (WSDL); **REST = estilo** (JSON comum).
14. **Nativo** = código por plataforma; **cross-platform** = um código, várias plataformas.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O HTML é uma linguagem de programação utilizada para definir a lógica e o comportamento das páginas web.
a) Certo. b) Errado.

> **Resposta: b (Errado).** HTML é linguagem de **marcação** (estrutura/conteúdo). A lógica/comportamento é do **JavaScript**; a apresentação, do **CSS**.

---

**Questão 2.** (FCC-style) Em CSS, a prioridade mais elevada na cascata de estilos é dada à declaração com:
a) estilos externos definidos em arquivo .css.
b) estilos internos definidos no head da página.
c) atributo style inline no elemento.
d) `!important` declarado pelo usuário no navegador.
e) `!important` declarado pelo desenvolvedor.

> **Resposta: d.** O `!important` do **usuário** supera até o `!important` do **desenvolvedor**.

---

**Questão 3.** (CESPE-style) Java e JavaScript são linguagens equivalentes, uma vez que ambas são compiladas, estaticamente tipadas e baseadas em classes.
a) Certo. b) Errado.

> **Resposta: b (Errado).** São linguagens **distintas**. Java = compilado, tipado estaticamente, classes. **JavaScript** = interpretado, dinâmico, **protótipos**.

---

**Questão 4.** (FCC-style) A tecnologia AJAX caracteriza-se por:
a) ser uma linguagem de programação substituta do JavaScript.
b) ser um conjunto de tecnologias que permite atualização assíncrona de partes de uma página, sem recarga total.
c) ser um padrão de banco de dados para aplicações web.
d) ser um framework Java para servidores de aplicação.
e) substituir o HTML na definição de estrutura de páginas.

> **Resposta: b.** AJAX = **conjunto** (XHTML/CSS + DOM + XMLHttpRequest + JS) com recuperação **assíncrona**. `readyState=4` indica resposta pronta.

---

**Questão 5.** (CESPE-style) O atributo `type="tel"` de formulários HTML5 garante validação automática do formato do número de telefone pelo navegador.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `tel` **não é validado** pelos navegadores (trata como text no fallback). Validação real exige `pattern`/JS.

---

**Questão 6.** (FCC-style) No desenvolvimento mobile, a abordagem híbrida caracteriza-se por:
a) usar apenas linguagens nativas da plataforma (Swift/Kotlin).
b) ser uma aplicação web distribuída pelo navegador, sem instalação.
c) envelopar uma aplicação web em um contêiner nativo, com acesso a hardware via framework.
d) dispensar completamente o uso de HTML e CSS.
e) ter desempenho superior ao nativo em todas as situações.

> **Resposta: c.** **Híbrido** = app **web** em contêiner nativo (Cordova/Ionic). O contêiner faz a ponte para o hardware.

---

**Questão 7.** (CESPE-style) No Android, a classe Service executa em um processo separado do sistema, dispensando cuidados com a thread principal.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Services rodam na **thread principal** (não são processo separado por padrão) — operações pesadas exigem threads próprias (IntentService/WorkManager).

---

**Questão 8.** (FCC-style) Em Java EE, o módulo WAR destina-se a:
a) aplicações enterprise completas (EAR).
b) componentes web (JSP, Servlets, HTML).
c) adapters de recursos (RAR).
d) clientes EJB (JAR).
e) bibliotecas de integração (JMS).

> **Resposta: b.** **WAR** = web (JSP/Servlets/HTML). EAR = aplicação completa; JAR = EJB; RAR = resource adapter.

---

**Questão 9.** (CESPE-style) O JSON baseia-se em XML e exige validação por esquemas DTD ou XSD para garantir a corretude dos elementos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** JSON **não** é baseado em XML nem tem DTD/XSD — é baseado em **pares chave/valor e listas** (sintaxe do JS, independente de linguagem); a aplicação valida o conteúdo.

---

**Questão 10.** (FCC-style) No Spring Framework, o conceito de Inversão de Controle (IoC) refere-se a:
a) a aplicação criar manualmente suas dependências com `new`.
b) o container gerenciar o ciclo de vida e a criação dos objetos (beans), invertendo o controle do código.
c) a substituição de SQL por ORM.
d) o uso obrigatório de EJB.
e) a autenticação de usuários.

> **Resposta: b.** **IoC** = o **container** cria/injeta os objetos (baixo acoplamento). **DI** é o padrão de injeção (por construtor/setter/interface).

---

**Questão 11.** (CESPE-style) A linguagem TypeScript é um superset do JavaScript que adiciona tipagem estática e é compilada (transpilada) para JavaScript antes da execução.
a) Certo. b) Errado.

> **Resposta: a (Certo).** TS = JS + tipos; **transpila** para JS; erros de tipo são detectados em compilação.

---

**Questão 12.** (FGV-style) Sobre métodos HTTP, é INCORRETO afirmar:
a) GET é idempotente e seguro (não altera o servidor).
b) POST é idempotente e pode ser repetido com o mesmo efeito.
c) PUT atualiza o recurso por substituição e é idempotente.
d) PATCH realiza atualização parcial do recurso.
e) DELETE remove o recurso e é idempotente.

> **Resposta: b.** **POST não é idempotente** (repetir cria múltiplos recursos) nem seguro.

---

**Questão 13.** (CESPE-style) No Android, o Content Provider tem como finalidade exclusiva a criação de interfaces gráficas com o usuário.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Content Provider** **compartilha dados** entre aplicativos (ex.: SQLite). Interface gráfica = **Activity/Views**.

---

**Questão 14.** (FCC-style) Em JavaScript, o método `document.write()` é recomendado para desenvolvimento de aplicações modernas por ser a forma padrão de atualizar o DOM.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `document.write()` **sobrescreve o documento** e serve só para testes. Atualização moderna: DOM API (`getElementById`, `innerHTML`, `querySelector`).

---

**Questão 15.** (CESPE-style) O Web Profile do Java EE inclui todas as APIs do Full Profile, como JAX-WS, JAX-RS, JMS e EAR.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Web Profile** é subconjunto (WAR + EJB **Lite**); **não inclui** JAX-WS/JAX-RS/JMS/EAR (do Full Profile).

---

## Questões discursivas

**D1.** Diferencie as abordagens nativa, web (responsivo) e híbrida no desenvolvimento mobile.

> **Modelo de resposta:** A **nativa** usa linguagens da plataforma (Swift/Kotlin/Java), oferece melhor desempenho e acesso total ao hardware, mas exige desenvolvimento por plataforma e atualização via loja. A **web responsiva** usa HTML+CSS+JS no navegador: atualização instantânea e baixo custo, porém depende de rede e tem acesso parcial ao hardware. A **híbrida** envolve uma app web em um **contêiner nativo** (Cordova/Ionic), acessando o hardware via framework, com custo intermediário e distribuição via loja — sem o desempenho do nativo.

**D2.** Explique a diferença entre SOAP e REST e entre IoC e DI no Spring.

> **Modelo de resposta:** **SOAP** é um **protocolo** de mensagens XML (envelope, WSDL, UDDI), mais rígido; **REST** é um **estilo arquitetural** com recursos identificados por URI, métodos HTTP, stateless e formatos leves como JSON. No Spring, **IoC** (Inversão de Controle) significa que o **container** gerencia a criação e o ciclo de vida dos objetos (beans), invertendo o controle do código; **DI** (Injeção de Dependência) é o **padrão** de fornecer essas dependências (por construtor, setter ou interface). São conceitos relacionados, porém independentes.

---

*Base: `04.Desenvolvimento de Software` (Aulas 02 — HTML/CSS; 04 — Java EE/Jakarta; 07 — JS/JSON/AJAX/jQuery/Spring; 09 e 19 — Mobile; 18 — monolítico×micro). Complemento: TypeScript, Python, design responsivo com media queries e frameworks modernos (React/Angular avançado) — ausentes na base de 2020. Web services (SOAP/REST/WSDL/UDDI): ver apostila T6.*