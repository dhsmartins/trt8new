# APOSTILA — TÓPICO 6: ARQUITETURAS DE SISTEMAS
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Arquiteturas de Sistemas: arquiteturas de sistemas multicamadas; arquiteturas cliente-servidor; arquiteturas de objetos distribuídos.
>
> **Base de conhecimento:** `01.Sistemas Operacionais e Arquitetura` e `04.Desenvolvimento de Software` (Aulas 11 — camadas/MVC/RMI; 12 — SOA; 13 — web services SOAP/REST; 18 — monolítico×micro) — Curso Regular TI 2020.2 + **complemento** (microsserviços, containers, mensageria).

---

# MÓDULO I — CLIENTE-SERVIDOR, P2P, CLUSTER E GRID

## 1. Arquitetura cliente-servidor (C/S)

- **Cliente** solicita serviços/recursos; **servidor** fornece. Comunicação via **rede**, com protocolos. Modelo de **duas camadas** (tradicional): cliente (apresentação + lógica) + servidor (dados).
- **Cliente gordo (fat client)**: grande parte da lógica de negócio roda no cliente — mais autônomo, mas manutenção difícil (atualizar todos os clientes). **Cliente magro (thin client)**: lógica no servidor; cliente só apresenta — atualização centralizada, clientes baratos.
- **Fila de mensagens** entre cliente e servidor para requisições; servidor atende em ordem/por prioridade.
- **Vantagens**: compartilhamento de recursos, escalabilidade vertical/horizontal, segurança centralizada, gerenciamento central. **Desvantagens**: ponto único de falha no servidor, congestionamento (tráfego), custo de servidor/infra, dependência de rede.
- **C/S × Peer-to-Peer (P2P)**: no P2P **não há servidor central** — cada nó é cliente e servidor ao mesmo tempo. P2P **puro** (Napster inicial, Gnutella) × **híbrido** (índice central + compartilhamento entre pares). Vantagens P2P: escalabilidade, resiliência; desvantagens: segurança/gerenciamento difíceis.

## 2. Cluster × Grid

- **Cluster**: conjunto de servidores **locais** conectados que se comportam como **um único servidor** — foco em **alta disponibilidade (HA)** e tolerância a falhas (failover). Tipos: **balanceado**, **HA**, **HPC** (alta performance).
- **Grid computing**: recursos geograficamente distribuídos, de domínios administrativos diferentes, para problemas de **alto desempenho computacional (HPC)** — "computação em grade". Cluster = mesma sala/domínio; grid = disperso.

---

# MÓDULO II — SISTEMAS MULTICAMADAS

## 1. Camadas × Tiers

- **Camada (layer)** = divisão **lógica** do software (mesma máquina). **Tier** = divisão **física/distribuída** (máquinas diferentes). Uma aplicação em 3 **camadas** pode rodar em 1 **tier** (tudo em um servidor) ou em 3 tiers (separados por rede).
- **1 camada/tier**: aplicação monolítica standalone (tudo junto: UI, negócio, dados) — simples, sem rede, pouco escalável.
- **2 camadas (C/S clássico)**: cliente (UI + parte do negócio) + servidor de banco. Problemas: "cliente gordo", manutenção distribuída.
- **3 camadas/tiers**: **apresentação** (UI) / **negócio** (regras, app server) / **dados** (SGBD). Benefícios: reuso das regras, escalabilidade independente por camada, segurança (usuário não acessa o BD diretamente), manutenção centralizada das regras.
- **4 camadas/tiers**: acrescenta camada de **integração/EIS** (sistemas legados, ERP, serviços externos) — ou: apresentação / web / aplicação / dados.
- *Pegadinha*: **3 tiers ⇒ 3 camadas; 3 camadas ⇏ 3 tiers** (podem estar na mesma máquina).

## 2. Coesão × Acoplamento

- **Acoplamento**: dependência entre módulos. **Alto acoplamento = ruim** (mudança em um afeta outro). **Baixo acoplamento = bom**.
- **Coesão**: quanto um módulo faz coisas relacionadas ao seu objetivo. **Alta coesão = bom**; baixa coesão = módulo "faz tudo".
- Objetivo: **alta coesão + baixo acoplamento**.

## 3. MVC (Model-View-Controller)

- Separa **modelo** (dados + regras), **visão** (apresentação) e **controlador** (entrada/fluxo do usuário). Relações no "triângulo MVC": o **modelo** notifica views e controllers (padrão Observador); a **view** exibe o modelo; o **controlador** manipula o modelo. O usuário interage com o controller (e com a view).
- *Pegadinha*: **o usuário interage com o Controller**, não com o modelo. Uma view pode observar vários modelos; um modelo ser exibido em várias views.

---

# MÓDULO III — OBJETOS DISTRIBUÍDOS E MIDDLEWARE

## 1. Middleware

- Camada de **software intermediário** que permite comunicação e troca de dados entre sistemas heterogêneos (plataformas, linguagens, BDs diferentes). Tipos: **RPC**, **MOM** (message-oriented middleware — filas), **TP monitors**, **object request brokers (ORB)**.

## 2. RMI (Remote Method Invocation) — Java

- Permite invocar métodos de objetos em **outra JVM** (outra máquina) como se fosse local. Funciona **apenas com Java**.
- Componentes: **stub/proxy** (lado do cliente, simula o objeto remoto), **skeleton** (lado do servidor, recebe a chamada e delega ao objeto real) e o **RMI Registry (binder)** — serviço de **nomes** que localiza o objeto remoto (lookup/bind).
- Fluxo: cliente → stub → rede (JRMP) → skeleton → objeto real (e retorno no sentido inverso).

## 3. CORBA (Common Object Request Broker Architecture) — OMG

- Padrão **independente de linguagem e plataforma**: **ORB** (Object Request Broker) faz a intermediação; **IDL** (Interface Definition Language) define as interfaces (neutra à linguagem); **IIOP** é o protocolo de rede. Permite interoperabilidade entre objetos de fornecedores diferentes.

## 4. DCOM / COM+ — Microsoft

- **DCOM** = extensão do COM para objetos distribuídos (Microsoft), com "suporte DCOM" para comunicação entre componentes em máquinas diferentes. Alternativa do ecossistema Windows ao CORBA/RMI.

## 5. Interoperabilidade

- Capacidade de sistemas diferentes trocarem informações/utilizarem recursos mutuamente. Requer **contratos comuns** (interfaces, protocolos, formatos). *Princípio-chave da SOA e dos web services.*

---

# MÓDULO IV — SOA, WEB SERVICES E MICROSSERVIÇOS

## 1. SOA (Service-Oriented Architecture)

- Arquitetura baseada em **serviços** autocontidos, com **contrato** publicado (interface), **baixo acoplamento** e **reusabilidade** entre sistemas.
- **8 princípios**: contrato padronizado; baixo acoplamento; abstração (o serviço esconde a lógica); reusabilidade; autonomia; **statelessness** (quando possível); descobribilidade (publicação em registro); composibilidade (serviços compõem outros).
- **ESB (Enterprise Service Bus)**: barramento corporativo que media mensagens entre serviços (roteamento, transformação, orquestração). O ESB **evita acoplamento ponto a ponto** (n×n) entre sistemas.
- **Orquestração × Coreografia**:
  - **Orquestração**: um **orquestrador central** (ex.: BPEL) controla a ordem e o fluxo dos serviços — o processo é visto como um todo.
  - **Coreografia**: **sem controlador central** — cada participante conhece apenas sua parte e reage a eventos dos demais (mais acoplado/distribuído).
- Composição: **composição** (reúne serviços para novo serviço) × **orquestração** (fluxo controlado) × **coreografia** (fluxo distribuído).

## 2. Web Services — SOAP

- **SOAP** = **protocolo** de mensagens **XML** (independente de plataforma). Estrutura: **Envelope** (obrigatório, raiz) → **Header** (**opcional**; se presente, é o primeiro elemento filho) → **Body** (**obrigatório**) → **Fault** (opcional, erros).
- **WSDL** (Web Services Description Language): **descreve** o serviço (operações, mensagens, endpoints) — o "contrato" XML.
- **UDDI** (Universal Description, Discovery and Integration): **registro/diretório** de serviços (páginas branca/amarela/verde) — permite descoberta.
- **WS-Security**: extensões de segurança para SOAP (assinatura, criptografia, tokens) — não confundir com HTTPS.
- Fluxo típico: provedor **publica** no UDDI (descreve via WSDL) → consumidor **descobre** → **liga** (bind) e consome.

## 3. Web Services — REST

- **REST** (Representational State Transfer) = **estilo arquitetural** (Roy Fielding), não protocolo. **6 restrições**: (1) cliente-servidor; (2) **stateless**; (3) cacheável; (4) **interface uniforme** (identificação de recursos por URI, manipulação por representações, mensagens autodescritivas, HATEOAS); (5) sistema em camadas; (6) código sob demanda (**única opcional**).
- Recursos identificados por **URI**; operações pelos **métodos HTTP** (GET/POST/PUT/PATCH/DELETE); formatos leves (**JSON**, XML).
- **SOAP × REST**: SOAP = protocolo rígido (XML, WSDL, WS-*); REST = estilo leve (JSON, stateless, cacheável), mais simples para web/mobile.

| | SOAP | REST |
|---|---|---|
| Natureza | Protocolo | Estilo arquitetural |
| Formato | XML (envelope) | JSON/XML (qualquer) |
| Contrato | WSDL | Interface uniforme (URI + HTTP) |
| Estado | Pode manter | **Stateless** |
| Complexidade | Maior (WS-*) | Menor |

## 4. Monolítico × Microsserviços *(complemento)*

- **Monolítico**: aplicação única e acoplada (todas as camadas em um deploy). Simples de começar; escala como um todo.
- **Microsserviços**: serviços pequenos, independentes, cada um com seu dado e deploy (comunicação por API/mensageria). Escalam por serviço, tecnologias heterogêneas; exigem DevOps, observabilidade e integração (API Gateway, service discovery — ver apostila T8).
- *Pegadinha*: microsserviço **não** é "SOA com outro nome" — é uma evolução com granularidade mais fina, containers e DevOps.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **Cliente-servidor × P2P**: no P2P **não há servidor central**; cada nó é cliente e servidor.
2. **Camada (layer) = lógica**; **tier = físico**. 3 camadas podem rodar em 1 tier.
3. **Cliente gordo** = lógica no cliente (manutenção difícil); **magro** = lógica no servidor.
4. **Alta coesão + baixo acoplamento** é o ideal (o inverso cai como alternativa falsa).
5. **MVC**: usuário interage com o **Controller**; o **modelo** notifica as views (Observador).
6. **RMI = Java-only**; **CORBA = independente** de linguagem (IDL, ORB, IIOP); **DCOM = Microsoft**.
7. **RMI Registry = binder** (localiza o objeto remoto); **stub** (cliente) × **skeleton** (servidor).
8. **SOAP = protocolo** (WSDL descreve, UDDI registra); **REST = estilo** (JSON, stateless).
9. **SOAP**: envelope obrigatório; **header opcional** (se presente, primeiro filho); body obrigatório.
10. **REST: 6 restrições**; "código sob demanda" é a **única opcional**.
11. **Orquestração** = controlador central (BPEL); **coreografia** = sem central, reação a eventos.
12. **ESB** evita acoplamento ponto a ponto (n×n) entre sistemas.
13. **Cluster = HA/locais**; **grid = HPC/disperso**.
14. **3 tiers ⇒ 3 camadas**; o inverso **não** é verdadeiro.
15. **WS-Security ≠ HTTPS** (é extensão SOAP: assinatura/criptografia/tokens).
16. Microsserviços: serviços independentes com **próprio dado e deploy** (não é só "SOA menor").

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) Em uma arquitetura cliente-servidor tradicional, o cliente gordo (fat client) concentra no servidor a maior parte da lógica de negócio, simplificando a manutenção das estações de trabalho.
a) Certo. b) Errado.

> **Resposta: b (Errado).** No **fat client**, a lógica fica **no cliente** — a manutenção é difícil (atualizar todas as estações). No **thin client**, a lógica fica no servidor (manutenção centralizada).

---

**Questão 2.** (FCC-style) A principal diferença entre uma arquitetura em 3 camadas (layers) e uma arquitetura em 3 tiers é que:
a) layers separam conceitualmente o software; tiers separam fisicamente os componentes em máquinas distintas.
b) layers exigem 3 servidores; tiers podem rodar em uma máquina só.
c) layers e tiers são sinônimos absolutos.
d) tiers separam apenas banco e aplicação.
e) layers refere-se exclusivamente a hardware.

> **Resposta: a.** **Layer = lógico**; **tier = físico/distribuído**. 3 camadas podem rodar em 1 tier.

---

**Questão 3.** (CESPE-style) No padrão de projeto MVC, o usuário final interage diretamente com o modelo (Model), que por sua vez atualiza a visão (View) sem intervenção do controlador.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O usuário interage com o **Controller**. O **Model** notifica as **Views** (padrão Observador); o Controller manipula o Model.

---

**Questão 4.** (FCC-style) Em sistemas distribuídos baseados em objetos, o componente do RMI responsável por localizar o objeto remoto (serviço de nomes) é:
a) stub (proxy).
b) skeleton.
c) RMI Registry (binder).
d) ORB.
e) IDL.

> **Resposta: c.** **RMI Registry** = serviço de nomes (**binder**). **Stub** simula o objeto no cliente; **skeleton** recebe a chamada no servidor.

---

**Questão 5.** (CESPE-style) A tecnologia CORBA tem como característica exigir que os objetos distribuídos sejam implementados em linguagem Java.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **CORBA** é **independente de linguagem** (interface definida em **IDL**; intermediação pelo **ORB**; protocolo **IIOP**). Quem é Java-only é o **RMI**.

---

**Questão 6.** (FCC-style) No padrão SOAP, o elemento opcional que pode conter informações de autenticação, transação e roteamento é:
a) Envelope.
b) Header.
c) Body.
d) Fault.
e) WSDL.

> **Resposta: b.** **Header** é **opcional**; se presente, é o **primeiro** filho do Envelope. **Body** é obrigatório; Fault (erros) é opcional.

---

**Questão 7.** (CESPE-style) O UDDI tem a função de descrever as operações e mensagens de um web service, servindo como seu contrato de interface.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **UDDI = registro/descoberta** de serviços. Quem **descreve** (contrato) é o **WSDL**.

---

**Questão 8.** (FCC-style) Entre as seis restrições da arquitetura REST, a única considerada opcional é:
a) cliente-servidor.
b) stateless.
c) cacheabilidade.
d) interface uniforme.
e) código sob demanda (code-on-demand).

> **Resposta: e.** As cinco primeiras são obrigatórias; **code-on-demand** é a única **opcional**.

---

**Questão 9.** (CESPE-style) Em SOA, a coreografia (choreography) caracteriza-se por um orquestrador central que controla a execução sequencial dos serviços, como em BPEL.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é **orquestração** (BPEL, controlador central). **Coreografia** = sem central; cada participante reage a eventos (padrão distribuído).

---

**Questão 10.** (FCC-style) Qual o objetivo principal do ESB (Enterprise Service Bus) em uma SOA?
a) armazenar dados dos serviços.
b) intermediar mensagens entre sistemas (roteamento, transformação), evitando acoplamento ponto a ponto.
c) substituir o banco de dados.
d) compilar os serviços.
e) autenticar usuários finais.

> **Resposta: b.** **ESB** media a integração (roteia, transforma, orquestra), evitando o acoplamento n×n entre sistemas.

---

**Questão 11.** (CESPE-style) Em uma arquitetura multicamadas, o objetivo do bom design é obter baixa coesão dentro dos módulos e alto acoplamento entre eles.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **alta coesão** (módulo focado) e **baixo acoplamento** (pouca dependência).

---

**Questão 12.** (FGV-style) Sobre arquiteturas cliente-servidor e P2P, é correto afirmar:
a) No P2P, um servidor central é obrigatório para a troca de arquivos.
b) No cliente-servidor, o servidor fornece recursos e o cliente os solicita.
c) Cluster e grid são sinônimos.
d) No P2P puro, não há nó que atue como cliente.
e) Cliente-servidor não permite escalabilidade.

> **Resposta: b.** No P2P **não** há servidor central (cada nó é cliente e servidor); **cluster** (HA, locais) ≠ **grid** (HPC, disperso). C/S permite escalabilidade vertical/horizontal.

---

**Questão 13.** (CESPE-style) No RMI, o stub é instalado no servidor e tem por função receber as requisições remotas e despachá-las ao objeto real.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Stub** fica no **cliente** (simula o objeto remoto). Quem recebe e despacha no servidor é o **skeleton**.

---

**Questão 14.** (FCC-style) A afirmação "3 tiers implica 3 camadas, mas 3 camadas não implica necessariamente 3 tiers" está:
a) correta, pois camadas podem coexistir em uma mesma máquina.
b) incorreta, pois os termos são sinônimos.
c) correta apenas em sistemas mainframe.
d) incorreta, pois tiers são lógicos e camadas físicas.
e) correta apenas em arquiteturas P2P.

> **Resposta: a.** **Camadas = lógicas** (podem estar em 1 máquina); **tiers = físicas** (máquinas distintas).

---

**Questão 15.** (CESPE-style) O WS-Security é dispensado em ambientes que utilizam exclusivamente comunicação HTTPS.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **WS-Security** trata segurança **no nível da mensagem SOAP** (assinatura, criptografia, tokens) — complementar e independente do transporte (HTTPS assegura o canal, não a mensagem ponta a ponta em intermediários).

---

## Questões discursivas

**D1.** Diferencie camadas (layers) de tiers e explique as vantagens da arquitetura de três camadas.

> **Modelo de resposta:** **Camadas** são divisões **lógicas** do software (apresentação, negócio, dados) — podem rodar em uma única máquina. **Tiers** são divisões **físicas** (cada camada em máquina/servidor próprio). A arquitetura de 3 camadas separa apresentação, regras de negócio e dados, trazendo: reuso das regras de negócio por múltiplos clientes, escalabilidade independente por camada, segurança (o usuário não acessa o banco diretamente) e manutenção centralizada das regras. 3 tiers implica 3 camadas; o inverso não é verdadeiro.

**D2.** Compare SOAP e REST e explique a diferença entre orquestração e coreografia em SOA.

> **Modelo de resposta:** **SOAP** é um **protocolo** baseado em XML (envelope, header opcional, body obrigatório), descrito por **WSDL** e registrado em **UDDI**, com suporte a WS-Security — mais rígido e formal. **REST** é um **estilo arquitetural** com recursos identificados por URI, métodos HTTP, **stateless**, cache e formatos leves (JSON) — mais simples e adequado a web/mobile. Em SOA, **orquestração** significa que um **orquestrador central** (ex.: BPEL) controla o fluxo dos serviços; **coreografia** ocorre **sem controlador central**, com cada participante reagindo a eventos dos demais.

---

*Base: `01.Sistemas Operacionais e Arquitetura` e `04.Desenvolvimento de Software` (Aulas 11 — camadas/MVC/RMI; 12 — SOA/ESB; 13 — SOAP/REST/WSDL/UDDI; 18 — monolítico×micro). Complemento: microsserviços, containers e mensageria moderna — ver apostila T8 (PDPJ-Br).*