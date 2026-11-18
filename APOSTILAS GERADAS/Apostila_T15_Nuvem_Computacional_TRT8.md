# APOSTILA — TÓPICO 15: NUVEM COMPUTACIONAL
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Nuvem computacional: arquitetura; nuvem pública e privada; modelos de serviço IaaS, PaaS e SaaS; implantação e operação em nuvem e contêineres; Kubernetes, Docker, Serverless Framework.
>
> **Base de conhecimento:** `01.Sistemas Operacionais e Arquitetura` (Aula11 — nuvem; Aula12 — virtualização/Docker/Kubernetes/OpenShift; Aula14 — data center/modelos) — Curso Regular TI 2020.2 + **complemento** (Serverless/FaaS, NIST, cloud native).

---

# MÓDULO I — FUNDAMENTOS E ARQUITETURA DE NUVEM

## 1. Conceito e benefícios

- **Computação em nuvem**: conjunto de recursos **virtuais** de fácil utilização e acesso (hardware, software, plataformas, serviços), **dinamicamente reconfiguráveis** para se ajustar à carga variável, otimizando o uso de recursos.
- **Elasticidade** (benefício-chave): evita sub/superutilização. Ex.: site com média de 1.000 vendas/dia que faz promoção e salta para 50.000 adquire mais processamento/memória/banda **apenas pelo período da promoção** (pague-por-uso).
- **Origem**: modelo **IDC (Internet Data Center)** — data center operado por provedor, infraestrutura compartilhada por várias organizações (exige grande segurança) — deu origem à nuvem. Nuvem privada **on-premises** é possível (ex.: Azure Stack) — "ainda não há tecnologia para implantar própria nuvem" está **ERRADA**.
- **Tecnologias envolvidas**: **virtualização** (essencial), containers, automação, redes definidas por software.
- **Arquitetura**: **multi-inquilino (multi-tenant)**, hipervisor na nuvem, APIs de provisionamento, orquestração, medição/medição de consumo, SLA.
- *Complemento (NIST SP 800-145)*: 5 características essenciais — **autoatendimento sob demanda, acesso amplo por rede, pool de recursos, elasticidade rápida, serviço medido**.

## 2. Modelos de serviço ("X como Serviço")

| Aspecto | IaaS | PaaS | SaaS |
|---|---|---|---|
| O que oferece | **Infraestrutura** (processamento/armazenamento virtualizados) | **Plataforma** p/ **desenvolvedor** (computação, armazenamento, comunicação) | **Aplicação completa** hospedada, via browser |
| Controle do usuário | SO, armazenamento, aplicações, rede (**não** a infra física); pode escolher o SO | Código/aplicações sobre a plataforma | Só usa o software ("nada embaixo") |
| Exemplos | Máquinas virtuais | Frameworks de desenvolvimento | Gmail/Drive, SalesForce |
| Posição na pilha | Base | Meio | Topo |

- Regra: quanto mais "alto" (**SaaS**), **menos** o usuário controla; quanto mais "baixo" (**IaaS**), mais controle.
- **SaaS** é o modelo **mais maduro** (e com mais provedores). **PaaS** = mais indicado para **desenvolvimento**; **não** obriga o cliente a gerenciar SO (quem gerencia SO é **IaaS**).
- *Pegadinha clássica (CESPE/BNB-2018)*: "IaaS é modelo de **implementação** no qual aplicações são virtualizadas em contêineres" — **ERRADA**: IaaS é modelo de **serviço**; **modelos de implantação** são privada/pública/híbrida/comunitária.

## 3. Modelos de implantação ("quem enxerga o serviço")

- **Privada**: uso interno (pela organização ou terceiros); segurança/controle rigorosos; equipe de TI própria decide permissões; pode ser **on-premises**.
- **Pública**: disponibilizada publicamente; modelo **"pague-por-uso"**; provedor cuida de software, infraestrutura, provisionamento e manutenção; qualquer usuário da Internet.
- **Híbrida**: duas ou mais nuvens (privadas/públicas/comunitárias) que permanecem entidades únicas, conectadas por tecnologia que propicia **portabilidade de dados e aplicações**.
- **Comunitária**: compartilhada por organizações com **interesses comuns** (missão, segurança, política, jurisdição, economia); administrada **pelas próprias organizações ou por terceiros**.

---

# MÓDULO II — VIRTUALIZAÇÃO

## 1. Conceito

- Três partes: **sistema hospedeiro (host)**; **camada de virtualização / hypervisor / VMM** (disponibiliza interfaces virtuais às VMs); **sistema convidado (guest)**. Pode-se ter n VMs (ex.: Ubuntu + Windows XP sobre Windows Server).
- Aplicável a: computadores (servidores/desktops), redes, armazenamento e aplicações — **NÃO a periféricos** (questão IF-RS-2018: "EXCETO" = virtualização de periféricos).
- **Níveis**: hardware (direto sobre o hardware, sem SO), SO, linguagem de programação.

## 2. Técnicas (x86)

1. **Virtualização total** (translação binária + execução direta): abstração completa; **NÃO exige modificação** do SO convidado; facilita migração de VMs; desvantagem = emulação de hardware genérico degrada desempenho.
2. **Paravirtualização** (assistida pelo SO): melhor desempenho, mas **REQUER modificação do SO convidado** (chamadas privilegiadas passam pelo hypervisor); ex.: **Xen** (não possui drivers de dispositivo — apenas gerencia E/S).
3. **Assistida por hardware**: extensões **Intel VT/AMD-V**; hypervisor em anel abaixo do ring 0; melhor desempenho; praticamente eliminou a necessidade de modificar o SO.

- **Hypervisor bare-metal** (Type 1, roda direto no hardware — ex.: **VMware ESXi**) × **hosted** (Type 2, sobre um SO — ex.: VirtualBox). *Pegadinha*: ESXi = **bare-metal**; hosted é o inverso.
- Associações: VirtualBox = criar VMs; OneDrive/Dropbox = armazenamento em nuvem; Nessus = verificação de vulnerabilidades; Ossim = segurança.

---

# MÓDULO III — CONTÊINERES: DOCKER, KUBERNETES, OPENSHIFT

## 1. Docker

- Software de **contêiner** da Docker, Inc.; camada de abstração/automação para **virtualização de SO** (Windows/Linux). Emprega **isolamento de recursos do kernel Linux (namespaces)** e sistema de arquivos com união (**OverlayFS**), criando contêineres independentes em **uma única instância do SO**.
- O **kernel é compartilhado** com a hospedeira → menos sobrecarga que VMs de hardware completo; empacota app + dependências; portável (on-premises, nuvem). **Alternativa à virtualização de servidor completo**.
- *Contêiner ≠ VM*: contêiner compartilha o kernel; VM tem SO próprio e hypervisor.

## 2. Kubernetes

- Sistema **open source** (Google) para **gerenciamento/orquestração de aplicativos em containers** em múltiplos hosts de um cluster; foco em microsserviços; adaptado ao Docker.
- Recursos: **balanceamento de carga** e **migração de containers sem perda de dados** (questão PUC-PR/TJ-MS-2017). Não prende à API do Docker (problema do Docker Swarm); pode rodar com outros runtimes (ex.: Rocket/CoreOS).
- Conceitos (complemento): pods, deployments, services, namespaces, self-healing, escalonamento horizontal.

## 3. OpenShift

- Produto da **Red Hat** para implantação/gerenciamento de software baseado em container; distribuição suportada do **Kubernetes** usando Docker e ferramentas DevOps.

## 4. Serverless / FaaS *(complemento — ausente na base de 2020)*

- **Serverless**: o provedor gerencia infraestrutura; o desenvolvedor escreve **funções** executadas sob demanda (**FaaS** — Function as a Service). Ex.: **AWS Lambda**, Azure Functions, Google Cloud Functions.
- **Serverless Framework**: ferramenta open source para implantar aplicações serverless (configuração por `serverless.yml`, provisionamento em nuvem, integração com API Gateway). Vantagens: sem gerenciar servidores, escala automática, cobrança por execução; limites: cold start, tempo de execução, dependência do provedor.

---

# MÓDULO IV — IMPLANTAÇÃO E OPERAÇÃO EM NUVEM

- **Provisionamento**: autoatendimento via painel/API; IaC (Infrastructure as Code — complemento: Terraform/CloudFormation).
- **Operação**: monitoramento, escalonamento (auto scaling), backup, segurança (compartimentação de responsabilidades entre provedor e cliente — modelo **responsabilidade compartilhada**), custos (FinOps).
- **Portabilidade/híbrida**: containers facilitam mover workloads entre nuvens; Kubernetes como camada de orquestração.
- **Alta disponibilidade**: múltiplas zonas/regiões, réplicas, balanceamento, failover.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **IaaS/PaaS/SaaS = modelos de SERVIÇO**; **privada/pública/híbrida/comunitária = modelos de IMPLANTAÇÃO** (confundi-los é erro clássico).
2. **PaaS = desenvolvimento**; **SaaS = software pronto (mais maduro)**; **IaaS = controle de SO/rede**.
3. **Nuvem privada pode ser on-premises** (não exige terceiros).
4. **Virtualização total NÃO modifica o guest**; **paravirtualização MODIFICA** (Xen). **Não virtualiza periféricos**.
5. **ESXi = hypervisor bare-metal**; hosted roda sobre SO.
6. **Docker = contêiner** (kernel compartilhado, namespaces, OverlayFS); **Kubernetes = orquestração** (balanceamento, migração sem perda); **OpenShift = Red Hat sobre Kubernetes**.
7. **Contêiner ≠ VM** (contêiner compartilha kernel).
8. **SaaS é o mais maduro** e com mais provedores.
9. **Elasticidade** = adicionar/recursos conforme carga (ex.: promoção 1.000→50.000).
10. **Híbrida** = portabilidade de dados/aplicações entre nuvens; **comunitária** = interesses comuns (pode ser administrada por terceiros).
11. **Serverless/FaaS** = funções sob demanda, sem gerenciar servidores (complemento).
12. **Virtualização NÃO se aplica a periféricos** (IF-RS-2018).
13. **PaaS não obriga gerenciar SO** (IaaS é que dá controle de SO).
14. **IDC** = origem histórica da nuvem (data center compartilhado).
15. **Assistida por hardware** = Intel VT/AMD-V (praticamente dispensa modificar o guest).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O IaaS é um modelo de implementação de nuvem no qual aplicações são virtualizadas em contêineres.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **IaaS** é modelo de **serviço** (infraestrutura). Modelos de **implantação** são privada/pública/híbrida/comunitária. Contêineres são outra tecnologia.

---

**Questão 2.** (FCC-style) O modelo de serviço em nuvem mais indicado para desenvolvedores que desejam criar aplicações sem gerenciar a infraestrutura e o sistema operacional é:
a) IaaS.
b) PaaS.
c) SaaS.
d) DaaS.
e) CaaS.

> **Resposta: b.** **PaaS** = plataforma para **desenvolvimento**. IaaS dá controle de SO; SaaS é software pronto.

---

**Questão 3.** (CESPE-style) A virtualização total exige que o sistema operacional convidado seja modificado para se comunicar com o hypervisor.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Virtualização total** NÃO exige modificação. A **paravirtualização** é que **requer** modificação do guest (ex.: Xen).

---

**Questão 4.** (FCC-style) O Docker caracteriza-se por:
a) criar máquinas virtuais com SO completo.
b) isolar aplicações em contêineres que compartilham o kernel da hospedeira, com menor sobrecarga que VMs.
c) ser um hypervisor bare-metal.
d) substituir o Kubernetes.
e) exigir virtualização de hardware.

> **Resposta: b.** **Docker** = contêiner (namespaces, OverlayFS, **kernel compartilhado**). Não é hypervisor nem VM.

---

**Questão 5.** (CESPE-style) O Kubernetes é uma ferramenta da Red Hat para virtualização de servidores, sendo incompatível com Docker.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Kubernetes** = orquestração de **containers** (Google, open source), **adaptado ao Docker** (e outros runtimes). **OpenShift** é da Red Hat (sobre Kubernetes).

---

**Questão 6.** (FCC-style) A principal vantagem da nuvem híbrida em relação às demais é:
a) ser exclusivamente pública.
b) permitir portabilidade de dados e aplicações entre nuvens.
c) dispensar virtualização.
d) ser gratuita.
e) eliminar a necessidade de segurança.

> **Resposta: b.** **Híbrida** = duas ou mais nuvens com **portabilidade** de dados/aplicações (privadas+públicas).

---

**Questão 7.** (CESPE-style) A nuvem privada implica, necessariamente, a contratação de um provedor externo, não podendo ser implantada no próprio data center da organização.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Nuvem privada **pode ser on-premises** (no próprio data center — ex.: Azure Stack) ou por terceiros.

---

**Questão 8.** (FCC-style) O SaaS é o modelo de serviço de nuvem considerado o mais maduro, no qual o usuário acessa aplicações completas via navegador, sem gerenciar infraestrutura.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **SaaS** = aplicação completa via browser (multi-tenant); é o **mais maduro** e com mais provedores.

---

**Questão 9.** (CESPE-style) A virtualização aplica-se a computadores, redes, armazenamento e aplicações, mas não a periféricos.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Não** se virtualiza **periféricos** (questão IF-RS-2018 — "EXCETO": periféricos).

---

**Questão 10.** (FCC-style) O hypervisor VMware ESXi classifica-se como:
a) hosted (roda sobre um SO hospedeiro).
b) bare-metal (roda direto sobre o hardware).
c) contêiner.
d) sistema de arquivos.
e) protocolo de rede.

> **Resposta: b.** **ESXi = bare-metal** (Type 1). Ex.: hosted = VirtualBox (Type 2, sobre SO).

---

**Questão 11.** (CESPE-style) A elasticidade em nuvem refere-se à capacidade de ajustar dinamicamente os recursos conforme a carga de trabalho, evitando sub e superutilização.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Elasticidade = provisionar/recursos conforme demanda (ex.: promoção 1.000→50.000 vendas/dia, pagando só pelo período).

---

**Questão 12.** (FGV-style) Sobre a nuvem comunitária, é correto afirmar:
a) é exclusivamente administrada pela organização cliente.
b) é compartilhada por organizações com interesses comuns, podendo ser administrada por elas ou por terceiros.
c) equivale à nuvem pública.
d) dispensa qualquer requisito de segurança.
e) é um modelo de serviço (IaaS/PaaS/SaaS).

> **Resposta: b.** **Comunitária** = interesses comuns (missão, segurança, jurisdição); administrada pelas próprias organizações **ou por terceiros**. É modelo de **implantação**.

---

**Questão 13.** (CESPE-style) O OpenShift é um orquestrador de containers open source criado pelo Google, independente da Red Hat.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **OpenShift** é da **Red Hat** (distribuição do **Kubernetes** com Docker e DevOps). O Kubernetes (Google) é que é o orquestrador open source.

---

**Questão 14.** (FCC-style) A diferença fundamental entre contêiner (Docker) e máquina virtual é que:
a) o contêiner inclui um SO completo; a VM, não.
b) o contêiner compartilha o kernel da hospedeira; a VM tem SO próprio via hypervisor.
c) ambos são idênticos.
d) a VM é mais leve que o contêiner.
e) contêineres exigem hypervisor bare-metal.

> **Resposta: b.** **Contêiner** = kernel **compartilhado** (namespaces/OverlayFS); **VM** = SO próprio + hypervisor.

---

**Questão 15.** (CESPE-style) No modelo Serverless (FaaS), o desenvolvedor provisiona e administra os servidores que executam suas funções.
a) Certo. b) Errado.

> **Resposta: b (Errado).** No **serverless**, o **provedor** gerencia a infraestrutura; o desenvolvedor só escreve **funções** executadas sob demanda (ex.: AWS Lambda). Cobrança por execução.

---

## Questões discursivas

**D1.** Diferencie os modelos de serviço IaaS, PaaS e SaaS e os modelos de implantação privada, pública, híbrida e comunitária.

> **Modelo de resposta:** **IaaS** oferece infraestrutura virtualizada (o usuário controla SO, rede e aplicações); **PaaS** oferece plataforma para desenvolvimento (sem gerenciar SO); **SaaS** oferece aplicação completa via navegador (mais maduro; usuário só consome). São modelos de **serviço**. Os modelos de **implantação** definem quem acessa: **privada** (uso interno, pode ser on-premises), **pública** (pague-por-uso, acesso geral), **híbrida** (duas ou mais nuvens com portabilidade) e **comunitária** (organizações com interesses comuns, administrada por elas ou terceiros).

**D2.** Compare virtualização e contêineres, explicando Docker, Kubernetes e Serverless.

> **Modelo de resposta:** A **virtualização** cria máquinas virtuais com SO próprio, mediadas por um hypervisor (total, paravirtualizada ou assistida por hardware); há maior isolamento, mas mais sobrecarga. Os **contêineres** (Docker) empacotam a aplicação e dependências compartilhando o **kernel** da hospedeira (namespaces, OverlayFS), sendo mais leves e portáveis. O **Kubernetes** orquestra contêineres em cluster (balanceamento, escalonamento, migração sem perda de dados); o **OpenShift** (Red Hat) é uma distribuição suportada dele. No **Serverless (FaaS)**, o provedor executa funções sob demanda sem gerenciamento de servidores (ex.: AWS Lambda, Serverless Framework).

---

*Base: `01.Sistemas Operacionais e Arquitetura` (Aula11 — nuvem/elasticidade; Aula12 — virtualização/Docker/Kubernetes/OpenShift; Aula14 — IDC e modelos de implantação). Complemento: Serverless/FaaS e Serverless Framework (ausentes na base de 2020), características NIST, responsabilidade compartilhada e IaC.*