# APOSTILA — TÓPICO 7: DEVOPS E DEVSECOPS
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Maven; Git; CI/CD; Testes Automatizados.
>
> **Base de conhecimento:** conteúdo técnico complementar (o material-base local de 2020 não cobre DevOps de forma sistemática) — a apostila segue o estado da prática, com foco no que banca cobra.

---

# MÓDULO I — CULTURA DEVOPS

## 1. Conceito

- **DevOps**: união de **Dev**elopment e **Op**erations — cultura, práticas e ferramentas que visam **entregar software de forma rápida, frequente e confiável**, com colaboração entre desenvolvimento, operações e segurança.
- **Objetivos (DORA)**: frequência de deploy alta, lead time baixo, **MTTR** (tempo médio de recuperação) baixo, taxa de falha de mudança baixa.
- **Os Três Caminhos** (Gene Kim, *The Phoenix Project* / *DevOps Handbook*):
  1. **Fluxo** (sistemas thinking): acelerar o fluxo do trabalho da esquerda para a direita (dev → operações).
  2. **Feedback**: criar laços de feedback à direita para a esquerda (operacoes → dev), o mais cedo possível.
  3. **Aprendizado e experimentação**: cultura de aprendizado contínuo, experimentação e coragem para assumir riscos calculados.
- **CALMS**: **C**ultura, **A**utomação, **L**ean, **M**ensuração (métricas), **S**haring (compartilhamento).
- **Lean/Kanban no DevOps**: limitar WIP, eliminar desperdício, fluxo contínuo.

## 2. DevOps × ITIL × Agile (pegadinha)

- **Agile** acelera o **desenvolvimento**; **DevOps** estende a agilidade até **operações/produção**; **ITIL** estrutura o **serviço** (processos de incidente, mudança, configuração). Complementares, não antagônicos.

---

# MÓDULO II — GIT E VERSIONAMENTO DE CÓDIGO

## 1. Fundamentos

- **Git**: sistema de controle de versão **distribuído** (cada dev tem o repositório completo — diferente do SVN/CVS, centralizados).
- **Conceitos-chave**:
  - **Repositório local** × **remoto** (origin); **working tree** × **staging area (index)** × **repositório local**.
  - **Commit**: snapshot imutável identificado por **hash SHA-1** (chave criptográfica do conteúdo + metadados).
  - **Branch**: ponteiro leve para um commit; **HEAD** aponta para o branch atual.
  - **Merge** × **rebase**: merge preserva a história (commit de merge); **rebase reescreve a história** (aplica commits sobre a base nova — não usar em branches compartilhados).
  - **Fast-forward** × **3-way merge** (com commit de merge quando há divergência).

## 2. Comandos essenciais

| Comando | Função |
|---|---|
| `git init` / `git clone <url>` | Cria / copia repositório |
| `git status` / `git log --oneline` | Estado / histórico |
| `git add <arquivo>` (staging) / `git commit -m "msg"` | Prepara / registra |
| `git push` / `git pull` / `git fetch` | Envia / baixa+integra / só baixa |
| `git branch <nome>` / `git checkout -b <nome>` / `git switch` | Cria/alterna branch |
| `git merge <branch>` / `git rebase <branch>` | Integra commits |
| `git revert <commit>` | **Cria commit novo desfazendo** o anterior (seguro — preserva história) |
| `git reset --soft/--mixed/--hard` | Move o ponteiro (hard descarta mudanças — perigoso) |
| `git stash` / `git stash pop` | Guarda/restaura mudanças temporárias |
| `git cherry-pick <commit>` | Aplica um commit específico em outro branch |

## 3. Fluxos de trabalho

- **Git Flow** (Vincent Driessen): `main` (produção), `develop`, `feature/*`, `release/*`, `hotfix/*` — mais formal, bom para releases versionados.
- **GitHub Flow / Trunk-based**: `main` sempre deployável + branches de feature curtos + **PRs (pull requests)**; integração frequente.
- **Convenções**: mensagens de commit claras (imperativo); tags para versões (`v1.2.0` — semver: major.minor.patch); `.gitignore` para artefatos.

*Pegadinhas*: **revert** desfaz **preservando** a história; **reset** reescreve/remonta. **fetch** só baixa; **pull** = fetch + merge. Rebase **não** deve ser usado em branches já publicados.

---

# MÓDULO III — MAVEN

## 1. Conceito

- **Maven**: ferramenta de **automação de build e gerência de dependências** para projetos **Java** (Apache). Filosofia: **convenção sobre configuração** (estrutura de pastas padrão: `src/main/java`, `src/test/java`).
- **POM (Project Object Model)** — `pom.xml`: coração do projeto. Declara groupId, artifactId, version (**GAV** — coordenadas), dependências, plugins, propriedades, módulos (multi-módulo).
- **Repositórios**: **local** (`~/.m2/repository`), **central** (Maven Central) e **privado/corporativo** (Nexus, Artifactory). Ordem de resolução: local → remoto configurado → central.

## 2. Ciclo de vida (lifecycle) e fases

- **Default lifecycle**: `validate → compile → test → package → verify → install → deploy`.
  - `mvn compile` compila; `mvn test` roda testes (Surefire); `mvn package` gera o artefato (**jar/war**); `mvn install` instala no repositório local; `mvn deploy` publica no remoto.
- **Clean lifecycle**: `mvn clean` remove o `target/` (build anterior).
- **Site lifecycle**: gera documentação.
- **Plugins**: cada fase executa **goals** de plugins (ex.: maven-compiler-plugin, maven-surefire-plugin).
- **Dependências**: `scope` define o alcance — `compile` (padrão), `provided` (ex.: servlet-api), `runtime`, `test` (ex.: JUnit), `system`, `import`.
- **Resolução transitiva**: dependências de dependências são baixadas automaticamente; **conflitos** resolvidos pela versão **mais próxima** da raiz (e dependencyManagement para controlar).

## 3. Comandos usuais

```bash
mvn clean install        # limpa, compila, testa e instala
mvn clean package -DskipTests   # gera artefato sem testes
mvn dependency:tree      # árvore de dependências (conflitos)
mvn test -Dtest=MinhaClasseTest  # roda teste específico
```

*Pegadinhas*: Maven é **declarativo** (pom.xml) × Ant (**imperativo** — build.xml). `install` publica no repositório **local**; `deploy`, no **remoto**. Escopo `test` **não** vai para produção.

---

# MÓDULO IV — CI/CD

## 1. Conceitos

- **CI (Integração Contínua)**: prática de **integrar código no repositório central várias vezes ao dia**, com build e testes **automáticos** a cada commit. Objetivo: detectar erros cedo (feedback rápido).
- **CD**: **Continuous Delivery** (entrega contínua — artefato **sempre pronto** para deploy, que é manual) × **Continuous Deployment** (implantação contínua — **todo** build aprovado vai **automaticamente** para produção).
- **Pipeline típico de CI/CD**: checkout → build (Maven/npm) → testes unitários → análise estática → testes de integração → empacotamento → deploy em staging → testes E2E → aprovação → deploy em produção → monitoramento.

## 2. Ferramentas

- **Jenkins** (open source, master/agents, Jenkinsfile — pipelines como código), **GitLab CI/CD** (.gitlab-ci.yml), **GitHub Actions** (workflows YAML), **Azure DevOps Pipelines**, **CircleCI**, **Travis CI**, **Argo CD** (GitOps), **SonarQube** (qualidade de código).

## 3. Estratégias de deploy

| Estratégia | Descrição | Risco |
|---|---|---|
| **Recreate** (big bang) | Derruba a versão antiga e sobe a nova | Janela de indisponibilidade |
| **Rolling update** | Substitui instâncias aos poucos | Médio (Kubernetes padrão) |
| **Blue-green** | Dois ambientes idênticos; troca o tráfego de uma vez | Baixo; rollback = trocar de volta |
| **Canary** | Encaminha pequena % do tráfego à versão nova e aumenta gradualmente | Baixo; detecta problemas cedo |
| **Shadow (dark launch)** | Tráfego real espelhado na nova versão sem retornar ao usuário | Sem impacto; exige infra dobrada |
| **Feature flags (toggles)** | Liga/desliga funcionalidades em produção sem deploy | Desacopla deploy de release |

## 4. Infraestrutura como código e GitOps

- **IaC** (Terraform, CloudFormation, Ansible): infraestrutura versionada como código.
- **GitOps**: o repositório Git é a **fonte única de verdade**; mudanças de infra/deploy via PR; o orquestrador (ex.: Argo CD) converge o estado real para o declarado.

---

# MÓDULO V — TESTES AUTOMATIZADOS

## 1. Pirâmide de testes (Mike Cohn)

```
       /  E2E  \          poucos, lentos, caros
      / Integração \      meio-termo
     / Unitários     \    muitos, rápidos, baratos
```

- **Testes unitários**: testam **unidade isolada** (método/classe), com **mocks/stubs** para dependências; rápidos; executam a cada build. Ferramentas: **JUnit** (Java), **pytest** (Python), **Jest/JUnit** (JS/TS).
- **Testes de integração**: verificam a **interação entre componentes** (API + banco, serviços). Ferramentas: Testcontainers, Postman/Newman, RestAssured.
- **Testes E2E (ponta a ponta)**: simulam o **usuário real** no sistema completo. Ferramentas: **Selenium**, **Cypress**, **Playwright**.
- **Testes de regressão**: garantem que mudanças não quebraram o que funcionava (suíte automatizada re-executada).
- **Testes de carga/desempenho**: JMeter, Gatling, k6.

## 2. TDD e BDD

- **TDD (Test-Driven Development)**: ciclo **Red** (escrever teste que falha) → **Green** (código mínimo para passar) → **Refactor** (melhorar mantendo testes verdes). Teste vem **antes** do código.
- **BDD (Behavior-Driven Development)**: testes em linguagem natural (Given/When/Then — ex.: Cucumber/Gherkin), comunicação dev × negócio.

## 3. Métricas e conceitos

- **Cobertura de código** (% de linhas/ramos executados pelos testes) — alta cobertura **não** garante qualidade (falta a **asserção** correta).
- **Mock × stub × fake**: mock = expectativas verificáveis; stub = respostas pré-programadas; fake = implementação simplificada real (ex.: in-memory DB).
- **Testes determinísticos**: sempre o mesmo resultado; flaky tests (intermitentes) corroem a confiança no pipeline.

---

# MÓDULO VI — DEVSECOPS

## 1. Conceito

- **DevSecOps**: integra a **segurança** ao ciclo DevOps desde o início (**shift-left security** — "empurrar a segurança para a esquerda"), em vez de inspecionar apenas no fim.
- **Princípios**: segurança como código; automação de controles; monitoramento contínuo em produção; **least privilege**; segurança compartilhada por todos os times.

## 2. Práticas e ferramentas

| Prática | O que faz | Exemplos |
|---|---|---|
| **SAST** (análise estática) | Examina o **código-fonte** sem executar (bugs, vulnerabilidades) | SonarQube, Checkmarx, Semgrep |
| **DAST** (análise dinâmica) | Testa a aplicação **em execução** (ataques simulados, sem ver o código) | OWASP ZAP, Burp Suite |
| **SCA** (análise de componentes) | Varre **dependências de terceiros** por vulnerabilidades conhecidas (CVE) | Dependabot, Snyk, OWASP Dependency-Check |
| **Secrets scanning** | Impede credenciais/chaves commitadas no repositório | git-secrets, truffleHog |
| **IaC scanning** | Analisa templates de infraestrutura | tfsec, Checkov |
| **Container scanning** | Varre imagens de contêiner | Trivy, Clair |

## 3. Outros pontos

- **Gerenciamento de vulnerabilidades**: triagem por severidade (CVSS), SLA de correção, remediação contínua.
- **Supply chain de software**: SBOM (lista de materiais do software), verificação de artefatos assinados (ex.: Sigstore), princípios do **SLSA**.
- **OWASP Top 10**: ranking das vulnerabilidades web mais críticas (injeção, broken access control, XSS etc.) — referência clássica de banca.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **Continuous Delivery ≠ Continuous Deployment**: delivery = pronto para deploy (manual); deployment = vai automático para produção.
2. **Git revert** desfaz preservando a história; **reset** reescreve. **fetch** só baixa; **pull** = fetch + merge.
3. **Rebase reescreve a história** — evitar em branches compartilhados.
4. Maven: **install** → repositório **local**; **deploy** → **remoto**. Escopo **test** não vai para produção.
5. Maven é **declarativo**; Ant é **imperativo**.
6. **Cobertura alta ≠ qualidade** — o teste precisa asserir o comportamento certo.
7. **TDD**: teste **antes** do código (Red → Green → Refactor).
8. **Blue-green** troca o tráfego de uma vez; **canary** libera gradualmente.
9. **SAST** = código parado; **DAST** = aplicação rodando; **SCA** = dependências.
10. DevOps **Três Caminhos**: fluxo, feedback, aprendizado. **CALMS**: cultura, automação, lean, mensuração, sharing.
11. **Git Flow** tem `develop` + `release` + `hotfix`; **GitHub Flow** tem só `main` + features.
12. **Feature flag** desacopla deploy de release.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) No Git, o comando `git revert` apaga o commit do histórico do repositório, reescrevendo a linha do tempo.
a) Certo. b) Errado.

> **Resposta: b (Errado).** `git revert` **cria um novo commit** que desfaz as mudanças do anterior — **preserva** a história. Quem reescreve história é `git reset` / `rebase`.

---

**Questão 2.** (FCC-style) No Maven, o comando que compila, executa os testes, empacota o projeto e o instala no repositório local do desenvolvedor é:
a) mvn deploy.
b) mvn verify.
c) mvn clean install.
d) mvn package.
e) mvn compile.

> **Resposta: c.** O ciclo default executa `validate → compile → test → package → verify → install` — `install` deposita o artefato no repositório **local** (`~/.m2`). `deploy` publica no **remoto**.

---

**Questão 3.** (CESPE-style) Continuous Deployment consiste em manter o código sempre em condições de ser implantado, cabendo à equipe a decisão manual do momento do deploy em produção.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Essa é a definição de **Continuous Delivery** (deploy manual). No **Continuous Deployment**, todo build aprovado pelos testes vai **automaticamente** para produção.

---

**Questão 4.** (FCC-style) A prática de TDD (Test-Driven Development) é caracterizada pelo ciclo:
a) Escrever o código, depois o teste, e por fim a documentação.
b) Red, Green, Refactor.
c) Planejar, Projetar, Codificar, Testar, Manter.
d) Testar em produção com usuários reais.
e) Escrever todos os testes de integração no fim do sprint.

> **Resposta: b.** TDD = **Red** (teste que falha) → **Green** (código mínimo) → **Refactor**. O teste é escrito **antes** do código.

---

**Questão 5.** (CESPE-style) Um teste automatizado que verifica a integração entre a aplicação e o banco de dados, sem isolar dependências, é classificado como teste unitário.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Teste **unitário** isola a unidade (com mocks). A verificação da interação entre componentes é teste de **integração**.

---

**Questão 6.** (FCC-style) Na pirâmide de testes de Mike Cohn, a base é composta por:
a) testes E2E, em maior quantidade.
b) testes de aceitação.
c) testes unitários, rápidos e em grande quantidade.
d) testes manuais exploratórios.
e) testes de performance.

> **Resposta: c.** Base = **unitários** (muitos, rápidos, baratos); meio = integração; topo = **E2E** (poucos, lentos, caros).

---

**Questão 7.** (CESPE-style) No Git Flow, os branches `release/*` destinam-se exclusivamente à correção de falhas críticas detectadas em produção.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Correções em produção são dos branches **`hotfix/*`**. Os `release/*` preparam uma **versão para release** (acertos finais, versão, changelog).

---

**Questão 8.** (FCC-style) A análise de segurança de aplicações que examina o código-fonte estaticamente, sem executar o programa, é denominada:
a) DAST.
b) SCA.
c) SAST.
d) Pentest.
e) Fuzzing.

> **Resposta: c.** **SAST** = análise **estática** (código parado). **DAST** = dinâmica (app rodando). **SCA** = componentes/dependências.

---

**Questão 9.** (CESPE-style) A estratégia de deploy canary consiste em substituir integralmente o ambiente de produção pela nova versão, com retorno imediato à versão anterior em caso de falha.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Essa é a **blue-green** (dois ambientes, troca total do tráfego). **Canary** libera a versão nova para **pequena fatia do tráfego** e aumenta gradativamente.

---

**Questão 10.** (FCC-style) No Maven, a dependência declarada com o escopo `test`:
a) é incluída no artefato final para uso em produção.
b) está disponível apenas na fase de compilação.
c) é usada apenas pelos testes e não acompanha o artefato final.
d) substitui as dependências `compile` em tempo de execução.
e) é ignorada pelo ciclo de build.

> **Resposta: c.** Escopo `test` (ex.: JUnit) vale só para a compilação/execução de testes — **não** vai para o jar/war de produção.

---

**Questão 11.** (CESPE-style) Os Três Caminhos do DevOps são: fluxo, feedback e aprendizado/ experimentação.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Gene Kim: **Fluxo** (dev→ops), **Feedback** (ops→dev, cedo) e **Aprendizado e experimentação** (cultura de melhoria contínua).

---

**Questão 12.** (FGV-style) Sobre Git, é INCORRETO afirmar:
a) `git fetch` atualiza as referências remotas locais sem integrar ao branch de trabalho.
b) `git pull` equivale a `git fetch` seguido de `merge`.
c) `git rebase` reaplica commits sobre outra base, reescrevendo o histórico.
d) `git merge` sempre reescreve o histórico do branch de destino.
e) Branches no Git são ponteiros leves para commits.

> **Resposta: d.** `git merge` **preserva** a história (pode criar um commit de merge); quem reescreve é o `rebase`.

---

**Questão 13.** (CESPE-style) O GitOps tem como princípio central que o estado desejado da infraestrutura e dos deploys é declarado em um repositório Git, que serve como fonte única de verdade, com convergência automática do ambiente real.
a) Certo. b) Errado.

> **Resposta: a (Certo).** GitOps: tudo declarado no Git (PRs como mudança), e ferramentas (ex.: Argo CD) convergem o ambiente para o estado declarado.

---

**Questão 14.** (FCC-style) Entre as métricas do relatório DORA de desempenho de equipes de software, NÃO se inclui:
a) frequência de deploy.
b) lead time para mudanças.
c) tempo médio de recuperação (MTTR).
d) taxa de falha de mudança.
e) número de linhas de código produzidas por desenvolvedor.

> **Resposta: e.** As 4 métricas DORA são as letras a-d. "Linhas de código por dev" **não** é métrica de desempenho (e é um antipadrão clássico).

---

**Questão 15.** (CESPE-style) A ferramenta Maven executa seus builds com base em um arquivo de configuração imperativo chamado build.xml.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O Maven é **declarativo**: seu descritor é o **`pom.xml`** (Project Object Model). O `build.xml` é do **Ant**, que é imperativo.

---

## Questões discursivas

**D1.** Explique a diferença entre Continuous Delivery e Continuous Deployment e cite duas estratégias de deploy de baixo risco.

> **Modelo de resposta:** No **Continuous Delivery**, o pipeline mantém o software sempre pronto para produção, mas a implantação depende de **aprovação manual**; no **Continuous Deployment**, todo artefato que passa nos testes é implantado **automaticamente** em produção. Estratégias de baixo risco: **blue-green** (dois ambientes idênticos, troca do tráfego e retorno imediato) e **canary** (liberação gradual para uma fração dos usuários), além de **feature flags** e **rolling updates**.

**D2.** Diferencie SAST, DAST e SCA no contexto de DevSecOps.

> **Modelo de resposta:** **SAST** (Static Application Security Testing) analisa o **código-fonte estaticamente**, sem executar o programa, identificando vulnerabilidades na implementação. **DAST** (Dynamic Application Security Testing) testa a aplicação **em execução**, simulando ataques, sem acesso ao código. **SCA** (Software Composition Analysis) varre as **dependências de terceiros** do projeto procurando vulnerabilidades conhecidas (CVEs). Todos integram o pipeline desde cedo (shift-left security).

---

*Conteúdo técnico complementar (o material-base local não cobre DevOps de forma sistemática). Referências: Phoenix Project/DevOps Handbook (Três Caminhos), Scrum Guide, Maven Documentation, Git Documentation, DORA State of DevOps, OWASP.*
