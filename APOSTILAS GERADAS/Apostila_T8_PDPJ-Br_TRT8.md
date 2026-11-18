# APOSTILA — TÓPICO 8: ARQUITETURA DE DESENVOLVIMENTO DA PLATAFORMA DIGITAL DO PODER JUDICIÁRIO (PDPJ-Br)
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Java; arquitetura de microsserviços; API RESTful; JSON; Spring (Spring Cloud, Spring Boot, Spring Eureka, Zuul); MapStruct; Swagger; Service Discovery; API Gateway; persistência (JPA 2.0, Hibernate 4.3+, Hibernate Envers, Flyway); PostgreSQL e H2; autenticação SSO, Keycloak, OAuth2 (RFC 6749), boas práticas RFC 9700; mensageria e webhooks (RabbitMQ, evento negocial, APIs reversas); Git; Docker, Kubernetes, Rancher; CI/CD.
>
> **Base de conhecimento:** conteúdo técnico complementar (o material-base local não cobre a PDPJ-Br). Foco no edital e na documentação oficial do CNJ.

---

# MÓDULO I — A PDPJ-Br E A ARQUITETURA DE MICROSERVIÇOS

## 1. PDPJ-Br (Plataforma Digital do Poder Judiciário)

- **Iniciativa do CNJ** para padronizar e compartilhar a **transformação digital** dos tribunais: componentes reutilizáveis (ex.: **PDPJ-Core**, sistemas processuais, autenticação unificada), interoperabilidade e **padrões técnicos** (Resolução CNJ nº 352/2020 e alterações; guias de arquitetura).
- Objetivos: reduzir retrabalho entre tribunais, garantir interoperabilidade (Base Nacional de Dados Processuais), acelerar a digitalização de serviços judiciais.
- Padrões técnicos relevantes: **API RESTful em JSON**, autenticação **SSO/OAuth2**, versionamento com **Git**, containers (**Docker/Kubernetes**), CI/CD.

## 2. Arquitetura de microsserviços

- **Microsserviços**: estilo arquitetural em que o sistema é um conjunto de **serviços pequenos, independentes e acoplados por contrato**, cada um com **própria base de dados** (database per service), deploy e escalabilidade independentes.
- **Monolito × microsserviços**: monolito = um único deploy, simples no início, difícil de escalar seletivamente; microsserviços = escalabilidade granular e times autônomos, mas complexidade de rede, consistência distribuída e operação.
- **Conceitos-chave**:
  - **Comunicação síncrona** (HTTP/REST, gRPC) × **assíncrona** (mensageria — RabbitMQ, Kafka).
  - **Service Discovery** (descoberta de serviços): serviços registam e localizam uns aos outros dinamicamente (**Spring Eureka** / Netflix Eureka).
  - **API Gateway** (ponto de entrada único: roteamento, autenticação, rate limit) — **Zuul** (Netflix) / Spring Cloud Gateway.
  - **Configuração centralizada** (Spring Cloud Config), **circuit breaker** (Resilience4j, Hystrix), **observabilidade** (logs, métricas, tracing — ELK, Prometheus, Jaeger).
  - **Padrão BFF** (Backend For Frontend), **saga** (consistência eventual entre serviços), **CQRS/Event Sourcing** (casos avançados).

---

# MÓDULO II — JAVA E O ECOSSISTEMA SPRING

## 1. Java (pontos de prova)

- Linguagem **orientada a objetos, compilada (bytecode JVM) e multiplataforma** ("write once, run anywhere").
- **JDK (Development Kit) × JRE (Runtime) × JVM (Virtual Machine)**.
- **POO**: encapsulamento, herança, polimorfismo, abstração; **interfaces × classes abstratas**; **exceptions** (checked × unchecked — `RuntimeException`); **generics**, **collections** (`List`, `Set`, `Map`), **streams** (Java 8+), **lambda**.
- **Gerenciamento de memória**: garbage collector (GC); sem ponteiros explícitos (diferente de C/C++).

## 2. Spring Boot

- Framework que **acelera** o desenvolvimento Spring com **autoconfiguração**, servidor embarcado (Tomcat), convenções sobre configuração, `application.properties`/`yml`, starters (dependências).
- **Anotações essenciais**: `@SpringBootApplication`, `@RestController`, `@Service`, `@Repository`, `@Component`, `@Autowired`, `@RequestMapping`/`@GetMapping` etc., `@Entity`, `@Configuration`, `@Bean`.
- **Injeção de dependência (IoC)**: o **container Spring** instancia e injeta dependências (não fazer `new` de serviços).

## 3. Spring Cloud

- Conjunto para **sistemas distribuídos**: **Spring Cloud Netflix Eureka** (service discovery — servidor de registro + clientes `@EnableEurekaClient`), **Zuul/Spring Cloud Gateway** (API Gateway), **Spring Cloud Config** (configuração central), **OpenFeign** (clientes HTTP declarativos), **Hystrix/Resilience4j** (circuit breaker), **Spring Cloud Stream** (mensageria).

## 4. MapStruct, Swagger

- **MapStruct**: biblioteca de **mapeamento objeto-objeto** (DTO ↔ entidade) por **geração de código em tempo de compilação** (rápido, sem reflexão — diferente do ModelMapper/BeanUtils em tempo de execução).
- **Swagger (OpenAPI)**: especificação e ferramentas para **documentar e testar APIs REST** — `springdoc-openapi`/`springfox` gera a UI interativa; o contrato OpenAPI é a **fonte do contrato da API** (padrão em microsserviços).

---

# MÓDULO III — API RESTFUL E JSON

## 1. REST

- **REST (Representational State Transfer)**: estilo arquitetural para APIs sobre HTTP com **recursos** identificados por **URIs**, operações pelos **métodos HTTP** e comunicação **stateless** (sem estado de sessão no servidor).
- **Métodos HTTP**: `GET` (ler — idempotente), `POST` (criar), `PUT` (atualizar por substituição — idempotente), `PATCH` (atualização parcial), `DELETE` (remover — idempotente).
- **Códigos de status**: `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized` (não autenticado), `403 Forbidden` (sem autorização), `404 Not Found`, `409 Conflict`, `500 Internal Server Error`.
- **Boas práticas**: versionamento da API (`/v1/...`), paginação, HATEOAS (opcional), autenticação OAuth2/JWT, tratamento de erros consistente.
- **SOAP × REST**: SOAP = protocolo, XML, WSDL, mais rígido; REST = estilo, JSON (comum), mais leve — pegadinha clássica.

## 2. JSON

- **JSON (JavaScript Object Notation)**: formato leve de troca de dados — **chave/valor** (`{}`), **arrays** (`[]`), tipos: string, number, boolean, null, object, array.
- Independente de linguagem; padrão de facto em APIs REST.
- **JSON × XML**: JSON é mais leve e nativo em JavaScript; XML é mais verboso, com esquemas (XSD) e namespaces.
- No Java: serialização/desserialização com **Jackson** (padrão do Spring Boot) ou Gson.

---

# MÓDULO IV — PERSISTÊNCIA: JPA, HIBERNATE, FLYWAY

## 1. JPA e Hibernate

- **JPA (Java Persistence API)**: **especificação** (padrão Jakarta/Java) de **ORM** (Object-Relational Mapping) — mapeia entidades Java para tabelas. **Hibernate** é a **implementação** mais usada (ou EclipseLink).
- **Anotações JPA**: `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`, `@JoinColumn`, `@Embedded`.
- **EntityManager** e **JPQL** (linguagem de consulta orientada a objetos — `SELECT e FROM Entidade e WHERE ...`).
- **Estados da entidade**: transient, managed, detached, removed.
- **Lazy × eager loading** (N+1 problem — pegadinha clássica de performance).
- Versão citada no edital: **JPA 2.0** e **Hibernate 4.3+** (conceitos de metamodelo, criteria API, cache de segundo nível).

## 2. Hibernate Envers

- **Envers**: módulo do Hibernate para **auditoria e versionamento de entidades** — mantém o **histórico de alterações** (tabelas `*_AUD`, revisões), permite consultas temporais ("como estava em D?"). Anotações: `@Audited`, `@NotAudited`.

## 3. Flyway

- **Flyway**: ferramenta de **migrations de banco de dados versionadas** (controle de versão do schema). Scripts `V1__create_table.sql`, `V2__add_column.sql` — aplicados em ordem, com histórico (`flyway_schema_history`). Reprodutibilidade entre ambientes (dev/test/prod).
- Alternativa: **Liquibase** (XML/YAML/SQL com changelogs).

## 4. PostgreSQL, H2, Oracle 19c, MySQL 8 (bancos do edital)

- **PostgreSQL**: SGBD relacional open source, robusto, ACID, JSON/JSONB, extensões (PostGIS). Versões do edital: **15, 16, 17 e 18**.
- **H2**: banco **em memória** (ou arquivo), leve, usado em **testes automatizados** e protótipos (compatibilidade JDBC).
- **Oracle 19c** e **MySQL 8**: outros SGBDs citados no edital (tópico 4).

---

# MÓDULO V — AUTENTICAÇÃO, SSO, KEYCLOAK E OAUTH2

## 1. SSO e Keycloak

- **SSO (Single Sign-On)**: o usuário autentica **uma vez** e acessa **vários sistemas** sem novo login.
- **Keycloak**: servidor de **identidade e acesso** open source (Red Hat) — SSO, usuários/papéis, **OIDC/OAuth2**, SAML, login social, MFA, federation LDAP/AD.

## 2. OAuth 2.0 (RFC 6749)

- **OAuth2**: framework de **autorização** (não de autenticação!) para **delegar acesso** — o usuário concede a um aplicativo acesso limitado aos seus recursos **sem compartilhar credenciais**.
- **Papéis**: **Resource Owner** (usuário), **Client** (app), **Authorization Server** (emite tokens), **Resource Server** (API protegida).
- **Fluxos (grant types)**:
  - **Authorization Code** (o mais seguro para apps com backend) — com **PKCE** obrigatório para SPAs e apps nativos.
  - **Client Credentials** (comunicação entre serviços, sem usuário).
  - **Implicit** (legado, desaconselhado) e **Password** (desaconselhado — RFC 9700).
- **Tokens**: **Access Token** (curta duração, acesso à API), **Refresh Token** (renova access token), **ID Token** (OIDC — identidade do usuário). **JWT (JSON Web Token)** = formato comum de token assinado (header.payload.signature).

## 3. Boas práticas de segurança — RFC 9700

*(Complementar — atualização de segurança do OAuth 2.0.)*
- Usar **PKCE** em todos os fluxos de authorization code; evitar o grant **password** e o **implicit**.
- **Access tokens de curta duração**; refresh tokens **rotativos** com detecção de reuso.
- **TLS obrigatório**; restrição rigorosa de **redirect URIs**; validar `state` (CSRF) e `nonce` (replay).
- Não expor tokens em URLs; limitar escopos (**least privilege**); monitorar e revogar tokens.
- OIDC (OpenID Connect): camada de **autenticação** sobre o OAuth2 (login + identidade).

---

# MÓDULO VI — MENSAGERIA E WEBHOOKS

## 1. Message Broker e RabbitMQ

- **Message broker**: intermediário assíncrono entre produtor e consumidor — **desacopla** serviços, absorve picos, garante entrega.
- **RabbitMQ**: broker open source baseado no protocolo **AMQP** — **exchanges**, **filas (queues)**, **bindings**, **produtores/consumidores**, confirmações (ack), dead-letter queues.
  - **Exchange types**: direct, topic, fanout, headers.
  - **Garantias**: at-most-once, at-least-once, **exactly-once** (mais caro).
- Alternativas: **Kafka** (log distribuído, streaming, retenção por tempo), ActiveMQ, SQS.

## 2. Evento negocial e webhooks

- **Evento negocial**: notificação de que **algo de negócio aconteceu** (ex.: processo movimentado, intimação publicada) — publicado para outros sistemas reagirem (padrão **event-driven architecture**).
- **Webhook**: **callback HTTP** — o provedor chama a **URL do assinante** quando o evento ocorre (push), em vez de o consumidor ficar consultando (polling). Exige: endpoint público, **assinatura do payload** (HMAC), reentrega idempotente, tratamento de falhas.
- **API reversa / integração inversa**: padrão em que um sistema interno expõe uma **API de callback** para receber notificações de sistemas externos (comum na integração do PDPJ com tribunais/órgãos externos).
- **Idempotência**: chave de idempotência em webhooks para evitar processamento duplicado.

---

# MÓDULO VII — GIT, DOCKER, KUBERNETES, RANCHER E CI/CD

## 1. Git

Ver apostila T7 (DevOps): controle de versão **distribuído**, branches, merge/rebase, pull requests, tags — usado em todos os projetos da PDPJ-Br.

## 2. Docker

- **Docker**: plataforma de **contêineres** — empacota aplicação + dependências em imagem leve (compartilha o kernel do SO; mais leve que VM).
- **Conceitos**: **Dockerfile** (instruções da imagem), **imagem** (template), **contêiner** (instância em execução), **registry** (Docker Hub), **volumes** (dados persistentes), **redes**.
- **Dockerfile** comum: `FROM` (imagem base), `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`/`ENTRYPOINT`.
- **docker-compose**: orquestra múltiplos contêineres em um host (dev local).

## 3. Kubernetes (K8s) e Rancher

- **Kubernetes**: **orquestrador de contêineres** (padrão de mercado) — escalabilidade automática, auto-recuperação, deploy sem downtime, service discovery e balanceamento nativos.
- **Conceitos**: **Pod** (menor unidade — 1+ contêineres), **Deployment** (replicação/rollouts), **Service** (exposição estável — ClusterIP/NodePort/LoadBalancer), **Ingress** (roteamento HTTP), **ConfigMap/Secret** (configuração/credenciais), **Namespace** (isolamento), **HPA** (autoscaling), **StatefulSet**, **DaemonSet**, **Helm** (pacotes/charts).
- **Rancher**: plataforma de **gestão de clusters Kubernetes** (multi-cluster, UI, RBAC, monitoramento, provisionamento).

## 4. CI/CD na PDPJ-Br

- Pipeline típico: commit Git → build (Maven) → testes → imagem Docker → push para registry → deploy no Kubernetes (Helm/manifests) → monitoramento.
- **Continuous Integration** (integração automática e testes a cada commit) × **Continuous Delivery** (artefato pronto para deploy manual) × **Continuous Deployment** (deploy automático) — ver apostila T7.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **OAuth2 é de AUTORIZAÇÃO**; **OIDC** é que adiciona autenticação/identidade (login).
2. **Grant password e implicit são desaconselhados** (RFC 9700); usar **authorization code + PKCE**.
3. **JPA é especificação; Hibernate é implementação**.
4. **MapStruct** mapeia em **tempo de compilação** (sem reflexão).
5. **Zuul/Eureka** = gateway/service discovery do Netflix OSS (Spring Cloud).
6. **Hibernate Envers** = **auditoria/versionamento** de entidades.
7. **Flyway** = migrations versionadas do **schema** do banco.
8. **H2** = banco em memória, típico de **testes**.
9. **Webhook** = push (o provedor chama sua URL); **polling** = consulta periódica.
10. **REST é um estilo; SOAP é um protocolo**. JSON é o formato comum do REST.
11. **Stateless** é requisito REST — sem estado de sessão no servidor.
12. **Pod** é a menor unidade do Kubernetes (não o contêiner isolado).
13. **401** = não autenticado; **403** = autenticado sem permissão.
14. **Microsserviços**: cada serviço com **própria base de dados**.
15. **JWT** = header.payload.signature (token assinado).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O protocolo OAuth 2.0 (RFC 6749) tem finalidade primordial de autenticação de usuários, sendo o OpenID Connect um complemento opcional de autorização.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **OAuth2 = autorização** (delegar acesso); **OpenID Connect = autenticação/identidade** sobre o OAuth2.

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

> **Resposta: b (Errado).** **401 Unauthorized** = não autenticado; **403** = autenticado, mas **sem permissão** (autorizado a estar logado, não a fazer isso).

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

> **Resposta: b (Errado).** **Flyway** gerencia **migrations versionadas do schema do banco de dados**. Imagens Docker vêm do **Dockerfile**.

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

> **Resposta: b (Errado).** A menor unidade é o **Pod**. O **Deployment** gerencia a **replicação e os rollouts** dos Pods.

---

**Questão 10.** (FCC-style) O padrão de comunicação em que um sistema notifica outro via HTTP callback, quando um evento negocial ocorre, chama-se:
a) polling.
b) webhook.
c) batch processing.
d) shared database.
e) ETL.

> **Resposta: b.** **Webhook** = push via callback HTTP. **Polling** = consulta periódica (o inverso).

---

**Questão 11.** (CESPE-style) A biblioteca MapStruct realiza o mapeamento entre objetos (DTOs e entidades) por reflexão em tempo de execução, semelhantemente ao BeanUtils.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O MapStruct **gera código em tempo de compilação** (anotações → implementações geradas) — mais rápido que as soluções de reflexão em runtime.

---

**Questão 12.** (FCC-style) No Docker, o arquivo que contém as instruções para a construção de uma imagem é denominado:
a) docker-compose.yml.
b) Dockerfile.
c) image.json.
d) container.conf.
e) registry.xml.

> **Resposta: b.** **Dockerfile** (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD). O **docker-compose.yml** orquestra múltiplos contêineres.

---

**Questão 13.** (CESPE-style) O Zuul, no ecossistema Spring Cloud, atua como API Gateway, concentrando o roteamento de requisições e funcionalidades transversais como autenticação e rate limiting.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Zuul (e o Spring Cloud Gateway) = **API Gateway**. Eureka = service discovery.

---

**Questão 14.** (FGV-style) Sobre JSON, é correto afirmar:
a) É um formato exclusivo do JavaScript, não podendo ser consumido por outras linguagens.
b) Baseia-se em XML e requer parsing via XSD.
c) É um formato leve de troca de dados baseado em pares chave/valor e arrays, amplamente usado em APIs REST.
d) Não suporta tipos primitivos como boolean e null.
e) É mais verboso que o XML e substitui o SOAP.

> **Resposta: c.** JSON é **independente de linguagem**, leve (chave/valor, arrays), padrão de APIs REST. Suporta string, number, boolean, null, object e array. **SOAP é protocolo** (não é substituído por JSON — REST é o estilo).

---

**Questão 15.** (CESPE-style) A arquitetura de microsserviços da PDPJ-Br preconiza que todos os serviços compartilhem uma única base de dados, para garantir consistência transacional ACID entre os serviços.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Padrão de microsserviços: **database per service** (base própria por serviço). A consistência entre serviços é tratada por **eventual consistency** (sagas, mensageria), não por transações ACID globais.

---

## Questões discursivas

**D1.** Explique os papéis do OAuth 2.0 e cite duas boas práticas de segurança da RFC 9700.

> **Modelo de resposta:** No OAuth 2.0 há quatro papéis: **Resource Owner** (usuário dono dos dados), **Client** (aplicação que solicita acesso), **Authorization Server** (emite os tokens após consentimento) e **Resource Server** (API que protege os recursos). Boas práticas da RFC 9700: usar **Authorization Code com PKCE** (evitar os grants password e implicit), manter **access tokens de curta duração** com **refresh tokens rotativos** e detecção de reuso, aplicar TLS, restrigir redirect URIs e validar `state`/`nonce`.

**D2.** Descreva o papel do Service Discovery (Eureka), do API Gateway (Zuul) e da mensageria (RabbitMQ) em uma arquitetura de microsserviços.

> **Modelo de resposta:** O **Service Discovery** (Eureka) mantém o registro das instâncias vivas dos serviços e permite a localização dinâmica, essencial com escalabilidade e recuperação automática. O **API Gateway** (Zuul) é o ponto único de entrada, fazendo roteamento, autenticação, rate limiting e agregação de respostas. O **RabbitMQ** (message broker) viabiliza comunicação **assíncrona** entre serviços (ex.: publicação de eventos negociais), absorvendo picos e desacoplando produtor e consumidor, com garantias de entrega e filas de reprocessamento.

---

*Conteúdo técnico complementar (o material-base local não cobre a PDPJ-Br). Referências: documentação CNJ/PDPJ-Br, Spring Cloud Netflix, RFC 6749 e RFC 9700 (OAuth 2.0 Security BCP), documentação Hibernate/JPA, Docker e Kubernetes.*