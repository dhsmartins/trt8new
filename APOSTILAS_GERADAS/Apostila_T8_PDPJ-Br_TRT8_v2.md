# APOSTILA — TÓPICO 8 (V2): ARQUITETURA DE DESENVOLVIMENTO DA PLATAFORMA DIGITAL DO PODER JUDICIÁRIO (PDPJ-Br)
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Java; arquitetura de microsserviços; API RESTful; JSON; Spring (Spring Cloud, Spring Boot, Spring Eureka, Zuul); MapStruct; Swagger; Service Discovery; API Gateway; persistência (JPA 2.0, Hibernate 4.3+, Hibernate Envers, Flyway); PostgreSQL e H2; autenticação SSO, Keycloak, OAuth2 (RFC 6749), boas práticas RFC 9700; mensageria e webhooks (RabbitMQ, evento negocial, APIs reversas); Git; Docker, Kubernetes, Rancher; CI/CD.
>
> **Base de conhecimento:** conteúdo técnico complementar (o material-base local não cobre a PDPJ-Br). **V2 ampliada**: conceitos explicados com mais profundidade e **quadros comparativos entre tecnologias similares** (o que a banca usa para confundir alternativas).

---

# MÓDULO I — A PDPJ-Br E A ARQUITETURA DE MICROSERVIÇOS

## 1. PDPJ-Br (Plataforma Digital do Poder Judiciário)

- **Iniciativa do CNJ** para padronizar e compartilhar a **transformação digital** dos tribunais: componentes reutilizáveis (ex.: **PDPJ-Core**, sistemas processuais, autenticação unificada), interoperabilidade e **padrões técnicos** (Resolução CNJ nº 352/2020 e alterações; guias de arquitetura — ver também o Tópico 17, sobre os normativos).
- Objetivos: reduzir retrabalho entre tribunais, garantir interoperabilidade (Base Nacional de Dados Processuais), acelerar a digitalização de serviços judiciais.
- Padrões técnicos relevantes: **API RESTful em JSON**, autenticação **SSO/OAuth2**, versionamento com **Git**, containers (**Docker/Kubernetes**), CI/CD.

## 2. Arquitetura de microsserviços (conceito aprofundado)

- **Microsserviços**: estilo arquitetural em que o sistema é decomposto em **serviços pequenos, independentes e acoplados por contrato** (API), cada um com **própria base de dados** (*database per service*), deploy e escalabilidade independentes, organizados por **domínio de negócio** (ex.: serviço de intimações, de petições, de autenticação).
- **Por que existe**: em um monolito, qualquer mudança exige rebuild/redeploy de tudo; um único bug derruba o sistema inteiro; times grandes trabalham no mesmo código e conflitam. Microsserviços separam **responsabilidade, escala e falha** por serviço.
- **Conceitos-chave**:
  - **Comunicação síncrona** (HTTP/REST, gRPC — o chamador espera a resposta) × **assíncrona** (mensageria — RabbitMQ, Kafka — o chamador publica e segue; o consumidor processa quando puder).
  - **Service Discovery** (descoberta de serviços): em vez de endereços fixos, os serviços **registam** instâncias vivas em um servidor de registro e **localizam** uns aos outros dinamicamente (**Spring Eureka** / Netflix Eureka) — essencial quando instâncias sobem/descem (escala automática).
  - **API Gateway** (ponto de entrada único do exterior: roteamento, autenticação, rate limit, agregação) — **Zuul** (Netflix) / Spring Cloud Gateway.
  - **Configuração centralizada** (Spring Cloud Config), **circuit breaker** (Resilience4j, Hystrix — "disjuntor" que corta chamadas a serviço falho para não propagar indisponibilidade), **observabilidade** (logs, métricas, tracing — ELK, Prometheus, Jaeger).
  - **Padrão BFF** (Backend For Frontend), **saga** (consistência eventual entre serviços por eventos), **CQRS/Event Sourcing** (casos avançados).

## 3. Comparação: estilos arquiteturais similares

| Critério | **Monolito** | **Microsserviços** | **SOA** | **Serverless (FaaS)** |
|---|---|---|---|---|
| Unidade | um único deploy | vários serviços pequenos | serviços "grandes" (ESB) | funções por evento |
| Base de dados | compartilhada | **própria por serviço** | compartilhada/central | gerenciada pelo provedor |
| Escala | do sistema inteiro | **por serviço** | por serviço (menos granular) | por invocação |
| Deploy | tudo junto | **independente** | acoplado ao ESB | por função |
| Complexidade | baixa no início, alta no crescimento | alta (rede, consistência distribuída) | alta (ESB, XML) | baixa operação, lock-in do provedor |
| Falha | derruba o sistema | **isolada por serviço** | propaga pelo ESB | isolada por função |
| Quando usar | sistemas pequenos/médios | sistemas grandes, times autônomos | integração corporativa legada | cargas esparsas/eventos |

- **SOA × microsserviços**: SOA usa ESB (barramento) e XML/WS-*; microsserviços usam APIs leves (REST/JSON) e inteligência nas pontas, **sem barramento central**.
- **Monolito modular** (monólito bem separado internamente) é etapa intermediária: muitos projetos migram de monolito modular → microsserviços.

## 4. Comparação: comunicação síncrona × assíncrona

| Critério | **Síncrona** (REST/gRPC) | **Assíncrona** (mensageria/webhook) |
|---|---|---|
| Acoplamento | tempo (ambos vivos no mesmo instante) | **desacoplada no tempo** |
| Resposta | imediata (o chamador espera) | posterior (fila/evento) |
| Picos de carga | derruba o chamado | **fila absorve** o pico |
| Falha do receptor | a chamada falha | mensagem fica na fila (retry) |
| Exemplo PDPJ | consultar dados de processo | notificar "movimentação processual" |

---

# MÓDULO II — JAVA E O ECOSSISTEMA SPRING

## 1. Java (pontos de prova)

- Linguagem **orientada a objetos, compilada (bytecode JVM) e multiplataforma** ("write once, run anywhere"): o código compila para **bytecode**, que roda em qualquer **JVM** — o mesmo .jar roda em Windows/Linux sem recompilar.
- **JDK (Development Kit)** = ferramentas de desenvolvimento (compilador `javac`, JVM, bibliotecas) × **JRE (Runtime)** = apenas o que roda aplicações (JVM + bibliotecas) × **JVM (Virtual Machine)** = executa o bytecode e gerencia memória. *Analogia: JDK = oficina completa; JRE = só o motor; JVM = o motor.*
- **POO**: encapsulamento (esconder detalhes internos), herança (reuso por especialização), polimorfismo (mesma chamada, comportamentos diferentes), abstração (modelar o essencial); **interfaces** (contrato, múltipla implementação) × **classes abstratas** (reuso + contrato, herança única); **exceptions** (checked × unchecked — `RuntimeException`); **generics** (tipagem segura em collections), **collections** (`List` ordenada/duplica, `Set` sem duplicatas, `Map` chave→valor), **streams** (Java 8+, processamento declarativo de coleções), **lambda** (funções anônimas).
- **Gerenciamento de memória**: garbage collector (GC) libera memória automaticamente; sem ponteiros explícitos (diferente de C/C++).

## 2. Spring Boot

- Framework que **acelera** o desenvolvimento Spring com **autoconfiguração** (deduz configuração a partir das dependências — "opinionated defaults"), servidor embarcado (Tomcat — não precisa instalar servidor de aplicação), convenções sobre configuração, `application.properties`/`yml`, **starters** (pacotes de dependências prontos, ex.: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`).
- **Anotações essenciais**: `@SpringBootApplication`, `@RestController` (REST + serialização JSON), `@Service` (regra de negócio), `@Repository` (acesso a dados), `@Component`, `@Autowired` (injeção), `@RequestMapping`/`@GetMapping` etc., `@Entity` (JPA), `@Configuration`, `@Bean`.
- **Injeção de dependência (IoC)**: o **container Spring** instancia e injeta dependências (o programador **não** faz `new` de serviços) — desacopla classes e facilita testes (mock de dependências).

## 3. Spring Cloud

- Conjunto de projetos para **sistemas distribuídos**: **Spring Cloud Netflix Eureka** (service discovery — servidor de registro + clientes `@EnableEurekaClient`), **Zuul/Spring Cloud Gateway** (API Gateway), **Spring Cloud Config** (configuração central versionada, ex.: no Git), **OpenFeign** (clientes HTTP declarativos — "interface Java vira chamada REST"), **Hystrix/Resilience4j** (circuit breaker), **Spring Cloud Stream** (mensageria sobre RabbitMQ/Kafka).

## 4. MapStruct, Swagger

- **MapStruct**: biblioteca de **mapeamento objeto-objeto** (DTO ↔ entidade) que **gera código em tempo de compilação** (o compilador escreve o mapper; rápido, sem reflexão, erros de mapeamento pegos no build).
- **Swagger (OpenAPI)**: especificação + ferramentas para **documentar e testar APIs REST** — `springdoc-openapi`/`springfox` gera a **UI interativa** (Swagger UI, com botão "Try it out"); o contrato **OpenAPI** (YAML/JSON) é a **fonte do contrato da API** — base para testes e integração em microsserviços.

## 5. Comparação: tecnologias similares do ecossistema Java

| Critério | **MapStruct** | **ModelMapper / BeanUtils** | **Dozer** |
|---|---|---|---|
| Quando mapeia | **compilação** (código gerado) | **execução** (reflexão) | execução (reflexão) |
| Performance | alta | média/baixa | baixa |
| Erros de mapeamento | pego no **build** | só em **runtime** | só em runtime |
| Uso típico | DTO↔entidade em alta escala | casos simples | legado |

| Critério | **Swagger/OpenAPI** | **WSDL (SOAP)** | **Javadoc** |
|---|---|---|---|
| O que documenta | **API REST** (contrato executável) | serviço SOAP | código Java |
| Formato | OpenAPI (YAML/JSON) | XML | HTML |
| Testável | sim (UI interativa) | via cliente SOAP | não |
| Papel em microsserviços | **contrato entre serviços** | legado corporativo | documentação interna |

- **Spring Boot × Spring Framework "puro"**: Boot = autoconfiguração + servidor embarcado + starters (projeto sobe com uma classe); o Framework puro exige configuração XML/Java extensa e servidor de aplicação externo (Tomcat/WildFly instalado à parte).

---

# MÓDULO III — API RESTFUL, JSON E FORMATOS DE DADOS

## 1. REST (conceito aprofundado)

- **REST (Representational State Transfer)**: **estilo arquitetural** (não protocolo!) para APIs sobre HTTP em que tudo é um **recurso** identificado por **URI**, manipulado por **métodos HTTP** com **representações** (JSON/XML) — comunicação **stateless** (cada requisição carrega tudo o que é necessário; o servidor **não guarda sessão**).
- **Restrições de REST** (o que faz uma API ser "RESTful"): cliente-servidor, **stateless**, cacheável, interface uniforme (URI + métodos + representações), sistema em camadas.
- **Métodos HTTP**: `GET` (ler — idempotente e cacheável), `POST` (criar — não idempotente), `PUT` (atualizar por **substituição completa** — idempotente), `PATCH` (atualização **parcial**), `DELETE` (remover — idempotente).
- **Códigos de status**: `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request` (requisição inválida), `401 Unauthorized` (**não autenticado**), `403 Forbidden` (autenticado **sem permissão**), `404 Not Found`, `409 Conflict`, `500 Internal Server Error`.
- **Boas práticas**: versionamento da API (`/v1/...`), paginação, HATEOAS (links de navegação — nível mais "puro" de REST, raramente exigido), autenticação OAuth2/JWT, tratamento de erros consistente.

## 2. Comparação: estilos de API similares

| Critério | **REST** | **SOAP** | **GraphQL** | **gRPC** |
|---|---|---|---|---|
| Natureza | **estilo** arquitetural | **protocolo** (WSDL, XML) | linguagem de consultas | framework RPC (Google) |
| Formato | **JSON** (comum) | XML | JSON | **binário (protobuf)** |
| Contrato | OpenAPI (opcional) | **WSDL (obrigatório)** | Schema (SDL) | `.proto` (obrigatório) |
| Transporte | HTTP | HTTP/SMTP etc. | HTTP | HTTP/2 |
| Peso | leve | verboso | leve (só o pedido) | **muito leve/rápido** |
| Caso típico | APIs web públicas/internas | sistemas corporativos legados, WS-Security | clientes com necessidades variadas (mobile) | microsserviço↔microsserviço de alta performance |

- **Pegadinha clássica**: "REST substitui SOAP" é simplificação — REST é **estilo**, SOAP é **protocolo**; JSON não "substitui" SOAP (REST é que é o estilo leve que se popularizou no lugar de WS-*).

## 3. JSON (conceito aprofundado)

- **JSON (JavaScript Object Notation)**: formato **leve, texto puro** de troca de dados — **objetos** (`{ "chave": valor }`), **arrays** (`[...]`), tipos: string, number (inteiros e decimais), boolean, null, object, array.
- **Independente de linguagem** (nasceu do JavaScript, mas todo idioma tem parser); padrão de facto de APIs REST por ser legível, leve e nativo em navegadores.
- No Java: serialização/desserialização com **Jackson** (padrão do Spring Boot) ou Gson.

## 4. Comparação: formatos de dados similares

| Critério | **JSON** | **XML** | **YAML** |
|---|---|---|---|
| Sintaxe | `{"chave": valor}` | `<tag>valor</tag>` | indentação (chave: valor) |
| Verbosidade | **baixa** | alta | baixa |
| Schema | JSON Schema (opcional) | XSD (formal) | limitado |
| Comentários | não | sim (`<!-- -->`) | sim (`#`) |
| Uso típico | **APIs REST** | SOAP, documentos, legado | **arquivos de configuração** (K8s, docker-compose) |
| Parser em JS | nativo (`JSON.parse`) | via DOM | via biblioteca |

- **JSON × XML** em prova: JSON é mais leve e nativo em JavaScript; XML é mais verboso, com esquemas (XSD), namespaces e suporte a comentários/atributos.

---

# MÓDULO IV — PERSISTÊNCIA: JPA, HIBERNATE, FLYWAY

## 1. JPA e Hibernate (conceito aprofundado)

- **ORM (Object-Relational Mapping)**: técnica que **mapeia objetos Java ↔ tabelas relacionais** — o programador trabalha com entidades/objetos; o ORM traduz para SQL (INSERT/UPDATE/SELECT). Elimina SQL manual repetitivo, mas exige entender o que o ORM gera (pegadinhas de performance).
- **JPA (Java Persistence API)**: **especificação** (padrão Jakarta/Java — um conjunto de interfaces/anotações: `@Entity`, `EntityManager`, JPQL). **Hibernate** é a **implementação** mais usada (outra: EclipseLink). *Regra de prova: JPA define as regras; Hibernate as executa.*
- **Anotações JPA**: `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`, `@JoinColumn`, `@Embedded`.
- **EntityManager** (ciclo de vida/persistência) e **JPQL** (consulta orientada a objetos: `SELECT e FROM Entidade e WHERE ...` — consulta a **entidades**, não a tabelas).
- **Estados da entidade**: *transient* (nunca persistida), *managed* (controlada pelo EntityManager), *detached* (foi persistida, mas saiu do contexto), *removed* (marcada para exclusão).
- **Lazy × eager loading**: *eager* carrega o relacionamento junto; *lazy* carrega só quando acessado. Acessar lazy fora da sessão → `LazyInitializationException`; consultas com lazy mal planejadas → **problema N+1** (1 consulta + N consultas de relacionamento — pegadinha clássica de performance).
- Versões citadas no edital: **JPA 2.0** e **Hibernate 4.3+** (metamodelo, criteria API, cache de segundo nível).

## 2. Comparação: formas de acesso a dados similares

| Critério | **JPA/Hibernate (ORM)** | **JDBC puro** | **jOOQ / MyBatis** |
|---|---|---|---|
| Nível | alto (objetos) | baixo (SQL manual) | intermediário |
| SQL | gerado pelo ORM | escrito à mão | escrito/referenciado |
| Produtividade | alta | baixa | média |
| Controle do SQL | indireto (JPQL/SQL nativo) | **total** | alto |
| Risco típico | N+1, consultas ineficientes | boilerplate, SQL injection | menor abstração |

- **JPA × Hibernate**: JPA = **especificação** (API de anotações); Hibernate = **implementação** (ferramenta que dá vida à especificação, com recursos extras como Envers).

## 3. Hibernate Envers

- **Envers**: módulo do Hibernate para **auditoria e versionamento de entidades** — mantém o **histórico de alterações** em tabelas `*_AUD` + tabela de revisões; permite consultas temporais ("como estava este processo em D?"). Anotações: `@Audited`, `@NotAudited`. *Não confundir: Envers audita **dados**; Git versiona **código**.*

## 4. Flyway × Liquibase (migrations)

- **Migrations de banco**: scripts versionados que evoluem o **schema** do banco de forma controlada e reprodutível entre ambientes (dev/test/prod) — sem "aquele campo que alguém criou à mão em produção".
- **Flyway**: scripts **SQL puro** nomeados `V1__create_table.sql`, `V2__add_column.sql` — aplicados **em ordem**, com histórico registrado em `flyway_schema_history`. Simples e direto.
- **Liquibase**: **changelogs** em XML/YAML/SQL com **changesets** — abstrai diferenças entre SGBDs (um changelog para Oracle e PostgreSQL), permite rollback lógico.

| Critério | **Flyway** | **Liquibase** |
|---|---|---|
| Formato do script | **SQL** (V1__desc.sql) | XML/YAML/SQL (changesets) |
| Aprendizado | simples | mais estruturado |
| Multi-SGBD | um script por banco | **um changeset, vários bancos** |
| Rollback | limitado (SQL manual) | suportado (lógico) |
| Uso típico | projetos Java/Spring | ambientes heterogêneos |

## 5. Bancos de dados do edital

| Critério | **PostgreSQL** | **H2** | **Oracle 19c** | **MySQL 8** |
|---|---|---|---|---|
| Tipo | relacional open source | **em memória/arquivo**, leve | relacional comercial | relacional open source |
| Uso típico | **produção** (PDPJ) | **testes automatizados/protótipos** | corporativo/legado | web |
| Diferenciais | ACID, JSON/JSONB, PostGIS | sobe com a aplicação, JDBC | robustez, recursos avançados | simplicidade, ecossistema web |
| Versões no edital | 15, 16, 17, 18 | — | 19c | 8 |

- **H2**: por ser em memória, o banco "nasce" a cada execução dos testes — ideal para testes rápidos; **não** é banco de produção.

# MÓDULO V — AUTENTICAÇÃO, SSO, KEYCLOAK E OAUTH2

## 1. SSO e Keycloak (conceito aprofundado)

- **SSO (Single Sign-On)**: o usuário autentica **uma vez** e acessa **vários sistemas** sem novo login (ex.: login único do PDPJ para sistemas de tribunais). Ganho: menos senhas; risco: a sessão única deve ser bem protegida (se cai, cai tudo).
- **Keycloak**: servidor de **identidade e acesso** open source (Red Hat) — SSO, gestão de usuários/papéis/realm, **OIDC/OAuth2**, SAML, login social, **MFA**, federation LDAP/AD. É a peça de identidade da arquitetura PDPJ.

## 2. Autenticação × autorização (não confundir!)

- **Autenticação** = **quem é você** (login, credenciais, token de identidade). **Autorização** = **o que você pode fazer** (permissões, papéis, escopos). *Análogo: passaporte (autenticação) × visto (autorização).*

## 3. OAuth 2.0 (RFC 6749) — conceito aprofundado

- **OAuth2**: framework de **autorização** (**não** de autenticação!) para **delegar acesso**: o usuário concede a um aplicativo acesso **limitado** aos seus recursos **sem compartilhar a senha** (ex.: "este app pode ler seus processos, mas não peticionar").
- **Papéis**: **Resource Owner** (usuário dono dos dados), **Client** (app que pede acesso), **Authorization Server** (emite tokens após consentimento), **Resource Server** (API protegida que valida o token).
- **Fluxos (grant types)**:
  - **Authorization Code** (o mais seguro para apps com backend) — com **PKCE** (code verifier/challenge) obrigatório para SPAs e apps nativos.
  - **Client Credentials** (comunicação serviço↔serviço, **sem usuário** — ex.: microsserviços da PDPJ chamando uns aos outros).
  - **Implicit** (legado, desaconselhado — token exposto no navegador) e **Password** (desaconselhado — a senha vai ao client; RFC 9700).
- **Tokens**: **Access Token** (curta duração, autoriza chamadas à API), **Refresh Token** (renova o access token sem novo login), **ID Token** (OIDC — diz **quem é** o usuário). **JWT (JSON Web Token)** = formato comum de token assinado (**header.payload.signature**) — o servidor da API valida a assinatura sem consultar o emissor a cada chamada.

## 4. Comparação: protocolos de identidade similares

| Critério | **OAuth 2.0** | **OpenID Connect (OIDC)** | **SAML 2.0** |
|---|---|---|---|
| Finalidade | **autorização** (delegar acesso) | **autenticação/identidade** sobre OAuth2 | autenticação federada (SSO corporativo) |
| Token | access token (JSON/JWT) | **ID token** + access token | assertion XML |
| Formato | JSON | JSON | **XML** |
| Uso típico | APIs, delegação de acesso | **login SSO moderno** (Keycloak) | SSO corporativo legado (AD/empresas) |
| Mobile/SPA | bom (com PKCE) | **o recomendado** | ruim (XML pesado) |

- **Pegadinha rei**: **OAuth2 = autorização; OIDC = autenticação**. Dizer "OAuth2 autentica o usuário" é errado — quem autentica é o OIDC (ou SAML) por cima do OAuth2.

## 5. Comparação: tipos de token

| Critério | **JWT (token opaco/assinado)** | **Token opaco (reference)** |
|---|---|---|
| Conteúdo | **payload legível** (claims) — só assinado, não cifrado | string sem sentido; o servidor guarda o estado |
| Validação | local (verificar assinatura/exp) | **chamar o servidor** a cada requisição |
| Revogação | difícil (válido até expirar) | **fácil (apagar no servidor)** |
| Performance | alta | menor (round-trip) |
| Uso típico | microsserviços (validação local) | sessões centralizadas |

## 6. Boas práticas de segurança — RFC 9700 (OAuth 2.0 Security BCP)

*(Complementar — atualização de segurança do OAuth 2.0.)*
- Usar **PKCE** em todos os fluxos de authorization code; **evitar** os grants **password** e **implicit**.
- **Access tokens de curta duração**; refresh tokens **rotativos** com **detecção de reuso** (se um refresh roubado for reusado, revoga-se a família inteira).
- **TLS obrigatório**; restrição rigorosa de **redirect URIs** (lista exata, sem curingas perigosos); validar `state` (anti-CSRF) e `nonce` (anti-replay).
- Não expor tokens em URLs (nem logs); limitar escopos (**least privilege**); monitorar e revogar tokens.
- **OIDC**: camada de **autenticação** sobre o OAuth2 (login + identidade do usuário).

---

# MÓDULO VI — MENSAGERIA E WEBHOOKS

## 1. Message Broker e RabbitMQ (conceito aprofundado)

- **Message broker**: intermediário **assíncrono** entre **produtor** (publica) e **consumidor** (assina) — **desacopla** serviços (não precisam se conhecer nem estar vivos ao mesmo tempo), **absorve picos** de carga (a fila cresce) e **garante entrega** (retry, dead-letter).
- **RabbitMQ**: broker open source baseado no protocolo **AMQP** — o produtor envia a uma **exchange**; a exchange roteia para **filas (queues)** segundo **bindings**; consumidores pegam das filas com **confirmação (ack)** — se o consumidor cair, a mensagem volta/reprocessa; **dead-letter queues** guardam mensagens que falharam repetidamente.
  - **Exchange types**: **direct** (chave exata), **topic** (padrões com curinga `*`/`#`), **fanout** (broadcast para todas as filas), **headers** (por cabeçalhos).
  - **Garantias de entrega**: **at-most-once** (pode perder — sem confirmação), **at-least-once** (pode duplicar — confirma + retry; exige **idempotência** no consumidor), **exactly-once** (exatamente uma vez — mais caro/complexo).
- **Padrão**: usar **at-least-once + consumidor idempotente** (chave de idempotência) — combinação mais cobrada em prova.

## 2. Comparação: brokers e padrões de integração similares

| Critério | **RabbitMQ** | **Kafka** | **ActiveMQ / SQS** |
|---|---|---|---|
| Modelo | **fila** (broker tradicional, AMQP) | **log distribuído** (append-only, tópicos com retenção) | filas (JPA/JMS / nuvem) |
| Mensagem | consumida e (em geral) removida | **retida por tempo** — vários consumidores relêem | consumida e removida |
| Ponto forte | roteamento flexível (exchanges), ack | **streaming**, alto throughput, replay | simplicidade / managed |
| Uso típico | **eventos negociais, filas de trabalho** | telemetria, eventos em escala | filas simples |

| Critério | **Webhook (push)** | **Polling (pull)** | **WebSocket / SSE** |
|---|---|---|---|
| Quem inicia | o **provedor chama** sua URL | você **consulta** periodicamente | canal persistente |
| Latência | baixa (imediata) | alta (intervalo do polling) | baixa (tempo real) |
| Custo | baixo (só quando há evento) | alto (consultas em vão) | conexão mantida |
| Riscos | endpoint público, reentrega duplicada | atraso + carga | infra mais complexa |
| Exemplo PDPJ | "processo movimentado → callback" | "a cada 5 min, houve movimento?" | painéis em tempo real |

## 3. Evento negocial, webhooks e API reversa

- **Evento negocial**: notificação de que **algo de negócio aconteceu** (ex.: processo movimentado, intimação publicada) — publicado para outros sistemas reagirem (padrão **event-driven architecture**). É o coração da integração da PDPJ com sistemas de tribunais.
- **Webhook**: **callback HTTP** — quando o evento ocorre, o provedor faz uma requisição HTTP para a **URL registrada do assinante** (push), em vez de o consumidor ficar consultando (polling). Exige: endpoint público, **assinatura do payload** (HMAC — prova autenticidade), **reentrega idempotente** (o consumidor não pode duplicar efeitos), tratamento de falhas e timeouts.
- **API reversa / integração inversa**: padrão em que um sistema interno expõe uma **API de callback** para receber notificações de sistemas externos (comum na integração do PDPJ com tribunais/órgãos externos).
- **Idempotência**: chave única por evento — processar duas vezes o mesmo evento produz o **mesmo efeito** que processar uma (essencial com at-least-once e reentregas de webhook).

---

# MÓDULO VII — GIT, DOCKER, KUBERNETES, RANCHER E CI/CD

## 1. Git

Ver apostila T7 (DevOps): controle de versão **distribuído** (cada dev tem o repositório completo), branches, merge/rebase, pull requests, tags — usado em todos os projetos da PDPJ-Br. **Distribuído × centralizado (SVN)**: em SVN o histórico vive no servidor central; em Git cada clone é um repositório completo (trabalho offline, branches baratos).

## 2. Docker (conceito aprofundado)

- **Docker**: plataforma de **contêineres** — empacota aplicação + dependências (runtime, bibliotecas) em **imagem** leve e portável. O contêiner **compartilha o kernel do SO hospedeiro** (diferente de VM, que tem SO próprio) — sobe em segundos e roda igual em dev/test/prod.
- **Conceitos**: **Dockerfile** (receita/instruções da imagem), **imagem** (template somente-leitura), **contêiner** (instância em execução da imagem), **registry** (Docker Hub/privado — onde imagens ficam), **volumes** (dados persistentes fora do contêiner), **redes**.
- **Dockerfile** comum: `FROM` (imagem base), `WORKDIR`, `COPY`, `RUN` (compila/instala), `EXPOSE` (porta), `CMD`/`ENTRYPOINT` (o que roda ao iniciar).
- **docker-compose**: orquestra múltiplos contêineres em um host (típico de **dev local**: app + banco + fila com um comando).

## 3. Comparação: virtualização × contêineres

| Critério | **VM (ex.: VMware, VirtualBox)** | **Contêiner (Docker)** |
|---|---|---|
| O que inclui | SO completo + app | só app + dependências |
| Kernel | **próprio** por VM | **compartilhado** com o hospedeiro |
| Tamanho | GBs | MBs |
| Inicialização | minutos | **segundos** |
| Isolamento | mais forte (hardware) | mais leve (namespaces/cgroups) |
| Portabilidade | média | **alta** ("roda igual em todo lugar") |

## 4. Kubernetes (K8s) e Rancher (conceito aprofundado)

- **Kubernetes**: **orquestrador de contêineres** (padrão de mercado, nascido no Google) — automatiza deploy, **escalabilidade automática**, **auto-recuperação** (reinicia/reagenda contêiner morto), deploy sem downtime (rollouts/rollbacks), service discovery e balanceamento nativos. Responde: "como rodar **milhares** de contêineres em produção com confiança".
- **Conceitos**: **Pod** (menor unidade de deploy — 1+ contêineres que compartilham rede/volumes; **não** é o contêiner isolado!), **Deployment** (replicação/rollouts/rollbacks de Pods), **Service** (exposição estável com IP — ClusterIP interno / NodePort / LoadBalancer externo), **Ingress** (roteamento HTTP/domínios/SSL), **ConfigMap/Secret** (configuração/credenciais — **nunca** senha em imagem), **Namespace** (isolamento lógico), **HPA** (autoscaling por CPU/métricas), **StatefulSet** (aplicações com estado, ex.: banco), **DaemonSet** (um Pod por nó), **Helm** (gerenciador de pacotes/charts).
- **Rancher**: plataforma de **gestão de clusters Kubernetes** (multi-cluster, UI gráfica, RBAC, monitoramento, provisionamento) — **gerencia** o K8s; **não** é um orquestrador concorrente.

## 5. Comparação: orquestradores e ferramentas similares

| Critério | **Kubernetes** | **Docker Swarm** | **Rancher** |
|---|---|---|---|
| O que é | **orquestrador** de contêineres | orquestrador simples do Docker | **gestor** de clusters K8s |
| Escala/complexidade | alta (padrão de mercado) | baixa (fácil, menos recursos) | UI multi-cluster, RBAC |
| Autoscaling/self-heal | **sim (HPA)** | limitado | provê gestão sobre K8s |
| Uso típico | **produção PDPJ** | protótipos/micro deploys | operar vários clusters K8s |

| Critério | **Docker** | **Kubernetes** | **Docker Compose** |
|---|---|---|---|
| Papel | criar/rodar contêineres | **orquestrar** contêineres em cluster | orquestrar contêineres **em 1 host** |
| Escopo | um contêiner/imagem | cluster de produção | dev local |

## 6. CI/CD (conceito aprofundado)

- **Pipeline típico**: commit Git → build (Maven) → testes → imagem Docker → push para registry → deploy no Kubernetes (Helm/manifests) → monitoramento.
- **Continuous Integration** (integração automática + testes a cada commit, detectando quebra cedo) × **Continuous Delivery** (artefato **pronto** para deploy, mas o **disparo é manual**) × **Continuous Deployment** (deploy **automático** em produção sem aprovação humana) — ver apostila T7. *Deliver = pode deployar a qualquer momento; Deployment = deploya mesmo.*
- Ferramentas comuns: **Jenkins**, **GitLab CI/CD**, **GitHub Actions**, ArgoCD (GitOps).

---

# RESUMO DE PEGADINHAS DE PROVA

1. **OAuth2 é de AUTORIZAÇÃO**; **OIDC** é que adiciona autenticação/identidade (login). SAML = SSO legado (XML).
2. **Grant password e implicit são desaconselhados** (RFC 9700); usar **authorization code + PKCE**; **Client Credentials** é serviço↔serviço (sem usuário).
3. **Autenticação** (quem é) × **autorização** (o que pode) — nunca são sinônimos.
4. **JPA é especificação; Hibernate é implementação**.
5. **MapStruct** mapeia em **tempo de compilação** (sem reflexão); ModelMapper/BeanUtils = reflexão em runtime.
6. **Zuul/Spring Cloud Gateway = API Gateway** (entrada única); **Eureka = Service Discovery** (registro/localização de instâncias) — não confundir os papéis.
7. **Hibernate Envers** = **auditoria/versionamento de dados** (tabelas `*_AUD`); **Git** versiona **código**.
8. **Flyway** = migrations versionadas do **schema** (scripts SQL `V1__`); **Liquibase** = changesets multi-SGBD.
9. **H2** = banco **em memória**, típico de **testes**; PostgreSQL = produção.
10. **Webhook** = push (o provedor chama sua URL); **polling** = consulta periódica (pull).
11. **REST é um estilo; SOAP é um protocolo**. JSON é o formato comum do REST; XML é o do SOAP.
12. **Stateless** é restrição REST — sem estado de sessão no servidor.
13. **Pod** é a menor unidade do Kubernetes (1+ contêineres) — **não** é o Deployment (que gerencia réplicas/rollouts).
14. **Microsserviços**: **database per service** (base própria por serviço); consistência entre serviços = **eventual** (sagas/eventos), não ACID global.
15. **JWT** = header.payload.signature (token **assinado**, não cifrado); validação local × token opaco (validação no servidor).
16. **401** = não autenticado; **403** = autenticado sem permissão.
17. **PUT** = substituição completa (idempotente); **PATCH** = atualização parcial.
18. **Container compartilha o kernel** do hospedeiro; **VM tem SO próprio** (mais pesada, mais isolada).
19. **Rancher gerencia clusters K8s** — não é orquestrador alternativo.
20. **Continuous Delivery** = pronto para deploy (manual); **Continuous Deployment** = deploy automático.
21. **Garantias de entrega**: at-least-once pode **duplicar** — exige **idempotência** no consumidor.
22. **RabbitMQ** = filas/AMQP (roteamento por exchanges); **Kafka** = log distribuído (streaming/replay).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O protocolo OAuth 2.0 (RFC 6749) tem finalidade primordial de autenticação de usuários, sendo o OpenID Connect um complemento opcional de autorização.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **OAuth2 = autorização** (delegar acesso); **OpenID Connect = autenticação/identidade** sobre o OAuth2. Autenticação × autorização são conceitos distintos.

---

**Questão 2.** (FCC-style) Na arquitetura de microsserviços da PDPJ-Br, o componente responsável por registrar as instâncias dos serviços e permitir que se localizem dinamicamente é:
a) Zuul.
b) Spring Eureka (Service Discovery).
c) MapStruct.
d) Flyway.
e) Hibernate Envers.

> **Resposta: b.** **Eureka** = service discovery (registro + localização). **Zuul** é o **API Gateway** (roteamento/entrada única); MapStruct mapeia objetos; Flyway versiona schema; Envers audita entidades.

---

**Questão 3.** (CESPE-style) O Hibernate Envers é utilizado para versionar o código-fonte das entidades JPA no repositório Git.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O Envers faz **auditoria/versionamento de dados** (histórico de alterações das entidades no banco — tabelas `*_AUD`). Versionamento de código é o **Git**.

---

**Questão 4.** (FCC-style) No padrão REST, a operação de atualização parcial de um recurso é tipicamente realizada com o método HTTP:
a) GET.
b) POST.
c) PUT.
d) PATCH.
e) DELETE.

> **Resposta: d.** **PATCH** = atualização **parcial**; **PUT** = substituição completa (idempotente); GET lê; POST cria; DELETE remove.

---

**Questão 5.** (CESPE-style) O status HTTP 403 (Forbidden) indica que o cliente não se autenticou junto ao servidor.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **401 Unauthorized** = não autenticado; **403** = autenticado, mas **sem permissão** (logado, mas não autorizado a essa operação).

---

**Questão 6.** (FCC-style) A abordagem de persistência da PDPJ-Br que usa JPA com Hibernate para mapear entidades Java a tabelas de banco de dados exemplifica:
a) programação funcional.
b) ORM (Object-Relational Mapping).
c) serialização de objetos em JSON.
d) cache distribuído.
e) virtualização de banco de dados.

> **Resposta: b.** ORM converte objetos ↔ registros relacionais. **JPA especifica**; **Hibernate implementa**.

---

**Questão 7.** (CESPE-style) A ferramenta Flyway tem como finalidade gerar imagens Docker a partir do código Java do projeto.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Flyway** gerencia **migrations versionadas do schema do banco de dados** (scripts `V1__...`). Imagens Docker vêm do **Dockerfile**.

---

**Questão 8.** (FCC-style) O fluxo (grant type) do OAuth 2.0 recomendado para aplicações web com backend próprio, e que com PKCE torna-se o padrão também para SPAs e apps nativos, é:
a) Resource Owner Password Credentials.
b) Implicit.
c) Client Credentials.
d) Authorization Code.
e) Device Code.

> **Resposta: d.** **Authorization Code** (com **PKCE**). Password e implicit são **desaconselhados** (RFC 9700); Client Credentials é para comunicação entre serviços (sem usuário).

---

**Questão 9.** (CESPE-style) No Kubernetes, a menor unidade de deploy que pode conter um ou mais contêineres é o Deployment.
a) Certo. b) Errado.

> **Resposta: b (Errado).** A menor unidade é o **Pod** (1+ contêineres). O **Deployment** gerencia a **replicação e os rollouts** dos Pods.

---

**Questão 10.** (FCC-style) O padrão de comunicação em que um sistema notifica outro via HTTP callback, quando um evento negocial ocorre, chama-se:
a) polling.
b) webhook.
c) batch processing.
d) shared database.
e) ETL.

> **Resposta: b.** **Webhook** = push via callback HTTP (o provedor chama a URL do assinante). **Polling** = consulta periódica (o inverso).

---

**Questão 11.** (CESPE-style) A biblioteca MapStruct realiza o mapeamento entre objetos (DTOs e entidades) por reflexão em tempo de execução, semelhantemente ao BeanUtils.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O MapStruct **gera código em tempo de compilação** (anotações → implementações geradas) — mais rápido que as soluções de reflexão em runtime (ModelMapper/BeanUtils).

---

**Questão 12.** (FCC-style) No Docker, o arquivo que contém as instruções para a construção de uma imagem é denominado:
a) docker-compose.yml.
b) Dockerfile.
c) image.json.
d) container.conf.
e) registry.xml.

> **Resposta: b.** **Dockerfile** (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD). O **docker-compose.yml** orquestra múltiplos contêineres em um host.

---

**Questão 13.** (CESPE-style) O Zuul, no ecossistema Spring Cloud, atua como API Gateway, concentrando o roteamento de requisições e funcionalidades transversais como autenticação e rate limiting.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Zuul (e o Spring Cloud Gateway) = **API Gateway** (entrada única). **Eureka** = service discovery (registro/localização).

---

**Questão 14.** (FGV-style) Sobre JSON, é correto afirmar:
a) É um formato exclusivo do JavaScript, não podendo ser consumido por outras linguagens.
b) Baseia-se em XML e requer parsing via XSD.
c) É um formato leve de troca de dados baseado em pares chave/valor e arrays, amplamente usado em APIs REST.
d) Não suporta tipos primitivos como boolean e null.
e) É mais verboso que o XML e substitui o SOAP.

> **Resposta: c.** JSON é **independente de linguagem**, leve (chave/valor, arrays), padrão de APIs REST. Suporta string, number, boolean, null, object e array. **SOAP é protocolo** (REST é o estilo; JSON não "substitui" SOAP).

---

**Questão 15.** (CESPE-style) A arquitetura de microsserviços da PDPJ-Br preconiza que todos os serviços compartilhem uma única base de dados, para garantir consistência transacional ACID entre os serviços.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Padrão de microsserviços: **database per service** (base própria por serviço). A consistência entre serviços é tratada por **consistência eventual** (sagas, mensageria), não por transações ACID globais.

---

## Questões discursivas

**D1.** Explique os papéis do OAuth 2.0 e cite duas boas práticas de segurança da RFC 9700.

> **Modelo de resposta:** O OAuth 2.0 é um framework de **autorização** (delegação de acesso sem compartilhar credenciais) com quatro papéis: **Resource Owner** (usuário dono dos dados), **Client** (aplicação que solicita acesso), **Authorization Server** (emite os tokens após consentimento) e **Resource Server** (API que protege os recursos). A autenticação/identidade fica a cargo do **OpenID Connect** (camada sobre o OAuth2). Boas práticas da RFC 9700: usar **Authorization Code com PKCE** (evitar os grants password e implicit) e manter **access tokens de curta duração** com **refresh tokens rotativos** e detecção de reuso (também válidos: TLS obrigatório, restrição rigorosa de redirect URIs e validação de `state`/`nonce`).

**D2.** Descreva o papel do Service Discovery (Eureka), do API Gateway (Zuul) e da mensageria (RabbitMQ) em uma arquitetura de microsserviços, explicando quando usar comunicação síncrona e assíncrona.

> **Modelo de resposta:** O **Service Discovery** (Eureka) mantém o registro das instâncias vivas dos serviços e permite a **localização dinâmica**, essencial quando instâncias sobem/descem por escala automática. O **API Gateway** (Zuul) é o **ponto único de entrada**, fazendo roteamento, autenticação, rate limiting e agregação de respostas, de modo que os clientes não precisam conhecer cada serviço. O **RabbitMQ** (message broker) viabiliza comunicação **assíncrona** (filas/exchanges, confirmações, dead-letter queues), desacoplando produtor e consumidor e absorvendo picos. Em geral, usa-se **comunicação síncrona** (REST) para consultas que precisam de resposta imediata e **assíncrona** (eventos negociais, webhooks) para notificações e processamento posterior — com garantias at-least-once e **idempotência** no consumidor.

---

*V2 de `Apostila_T8_PDPJ-Br_TRT8.md` (original mantido). Conteúdo técnico complementar (o material-base local não cobre a PDPJ-Br). Referências: documentação CNJ/PDPJ-Br, Spring Cloud Netflix, RFC 6749 e RFC 9700 (OAuth 2.0 Security BCP), documentação Hibernate/JPA, Docker e Kubernetes.*
