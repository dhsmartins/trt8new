# APOSTILA — TÓPICO 14: GERENCIAMENTO DE REDES DE COMPUTADORES
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Gerenciamento de redes de computadores: protocolo SNMP, agentes, gerentes e MIBs; tipos e níveis de serviço, qualidade de serviço (QoS); métricas de desempenho; métodos de avaliação de desempenho; ferramentas de monitoramento e alerta: Zabbix, Elasticsearch, Logstash, Kibana, Grafana, Prometheus e Fluentd.
>
> **Base de conhecimento:** `02.Redes de Computadores` (Aula10 — SNMP/Nagios/Zabbix/Cacti/NetFlow/sFlow/Syslog), `10.Segurança da Informação e Armazenamento de Dados` (Aula08 — QoS/métricas) — Curso Regular TI 2020.2 + **complemento** (ELK/EFK, Grafana, Prometheus, Fluentd — ausentes na base).

---

# MÓDULO I — SNMP, AGENTES, GERENTES E MIBs

## 1. Arquitetura SNMP

- **SNMP** (Simple Network Management Protocol): arquitetura de gerenciamento com **NMS (gerente/manager)** + **dispositivos gerenciados** + **agentes** (daemon; **proxy agents** para interoperabilidade entre versões). **Não é** cliente-servidor clássico.
- **MIB** (Management Information Base): base hierárquica de objetos gerenciados, modelada por **SMI** (Structure of Management Information). MIB I/II, experimental, privada.
- **Coleta**: por **request/response** (porta **161/UDP**) ou **traps** (**162/UDP** — unidirecional; ex.: alerta de 80% de banda).
- **Mensagens SNMP**: GET REQUEST, GETNEXT REQUEST, SET REQUEST, INFORM REQUEST, GET BULK, RESPONSE, TRAP.

## 2. Versões do SNMP

| Versão | Características |
|---|---|
| **v1** | Senhas em **texto simples** |
| **v2** | Autenticação via mudança de PDU, DES, GetBulk/Inform; **incompatível com v1** |
| **v2c** | Compatibilidade com v1 (community strings) |
| **v3** | **Segurança**: DES, hashes MD5/SHA, modelos **USM/TSM**, túneis SSL, senhas separadas read/write |

- **RMON** (Remote Monitoring): **v1** (camadas 1/2), **v2** (acrescenta 3/7).
- **Áreas de gerência**: desempenho; **falhas** (imediata vs. longo prazo); configuração (inventário); segurança (políticas de acesso).

---

# MÓDULO II — QoS E MÉTRICAS DE DESEMPENHO

## 1. Tipos e níveis de serviço

- Níveis de serviço e SLA/ANS (**Acordo de Nível de Serviço**) definem requisitos de desempenho por serviço (disponibilidade, latência, perda).
- **Traffic shaping**: restringe banda de aplicações volumosas (P2P, FTP). **WQF** (Weighted Fair Queuing); **token bucket** (descarta **símbolos**, não pacotes).

## 2. QoS (Quality of Service)

- Mecanismos por camada: **802.1P** (L2, 3 bits), **TOS/DSCP** no IPv4 (6 bits, RFC 2474), **MPLS** (campo Exp/QoS 3 bits = 8 classes).

| Modelo | Mecanismo | Observação |
|---|---|---|
| **IntServ** | Reserva de recursos via **RSVP** | Exige suporte dos nós intermediários; complexo; uso limitado na Internet |
| **DiffServ** | Classes de serviço (campo TOS) | **Mais simples e barato**; é o usado na Internet hoje; **não garante fim a fim** (roteadores de terceiros podem descartar a marcação) |

## 3. Métricas de desempenho

- **Largura de banda/taxa/vazão** (throughput); **perda de pacotes**; **atraso/latência/retardo** (propagação + transmissão + processamento + fila); **jitter** (variação de atraso — crítico para **VoIP/vídeo**); **disponibilidade** (noves: 99,9%... 99,999%).
- **Métodos de avaliação**: medição ativa (tráfego sintético/ex.: ping) × passiva (observação do tráfego real); baseline de tráfego; análise de tendências; testes de carga; comparação com SLA.

---

# MÓDULO III — FERRAMENTAS DE MONITORAMENTO E ALERTA

## 1. Da base local (2020)

- **Nagios**: plug-ins, arquivos de configuração, check_hpjd para impressoras; armazena em /var (MySQL ou PostgreSQL).
- **Zabbix**: open source, monitora **rede + aplicações**, **suporta SNMP** (templates/scripts), agentes e tráfego passivo, alertas e gráficos.
- **Cacti**: PHP/MySQL + **RRDTool** (gráficos históricos).
- **NetFlow** (Cisco): dispositivos L3; **IPFIX** (RFC 5101/5102); perfilamento de tráfego/custos. **sFlow** (RFC 3176): **amostragem**, versões 2–4, Gigabit+, escalável.
- **Syslog**: logs centralizados (514; TLS 6514); 3 papéis (origem/armazenamento/análise). **System Center** (Operations/Service Manager), ITIL/MOF.

## 2. Stack ELK/EFK e métricas *(complemento — ausente na base de 2020)*

- **Elasticsearch**: motor de busca/análise distribuído (NoSQL de documentos; índice invertido) — armazena e indexa logs/métricas.
- **Logstash**: coleta, transforma e envia dados (inputs/filters/outputs) para o Elasticsearch. **Fluentd**: coletor de logs leve (CNCF) — alternativa ao Logstash (stack **EFK**: Elasticsearch+Fluentd+Kibana).
- **Kibana**: visualização/dashboards sobre o Elasticsearch (gráficos, buscas, mapas).
- **Grafana**: dashboards multi-fonte (Prometheus, Elasticsearch, Zabbix, InfluxDB...) com alertas.
- **Prometheus**: coleta de **métricas** por scraping (pull), modelo dimensional com labels, **PromQL**, alertas (**Alertmanager**), exportadores (node_exporter, snmp_exporter...).
- *Padrão moderno*: **métricas → Prometheus → Grafana**; **logs → Fluentd/Logstash → Elasticsearch → Kibana**; **alertas → Alertmanager/Zabbix**.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **SNMP: 161/UDP (requests), 162/UDP (traps)** — **não** é porta 22 (SSH).
2. **MIB** = base hierárquica de objetos (modelada por **SMI**).
3. **SNMPv1** = senhas em texto simples; **v2 incompatível com v1**; **v2c** mantém compatibilidade; **v3** = segurança (USM/TSM, MD5/SHA).
4. **RMON v1** = camadas 1/2; **v2** = acrescenta 3/7.
5. **IntServ** = RSVP/reserva (complexo); **DiffServ** = classes (usado na Internet; **não garante fim a fim**).
6. **Jitter** = variação de atraso (crítico em **VoIP/vídeo**).
7. **Token bucket descarta símbolos**, não pacotes.
8. **Zabbix suporta SNMP** (falso dizer o contrário).
9. **sFlow = amostragem**; **NetFlow** = fluxos completos (Cisco), IPFIX.
10. **Prometheus** = métricas (pull/scraping, PromQL); **Elasticsearch** = logs/busca; **Kibana/Grafana** = dashboards; **Logstash/Fluentd** = coleta.
11. **Syslog 514 (TCP/UDP), 6514 (TLS)**; papéis: origem/armazenamento/análise.
12. **Fluentd** = alternativa ao Logstash (stack **EFK**).
13. **SNMP não é cliente-servidor clássico** — é gerente/agentes.
14. **Proxy agent** do SNMP permite interoperabilidade entre versões.
15. **Traps = unidirecional** (dispositivo → gerente, sem requisição).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) No protocolo SNMP, as portas UDP utilizadas para requisições e para traps são, respectivamente, 161 e 162.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **161/UDP** = requests; **162/UDP** = traps (unidirecional). (22 = SSH.)

---

**Questão 2.** (FCC-style) A Management Information Base (MIB) do SNMP corresponde a:
a) um protocolo de transporte.
b) uma base hierárquica de objetos gerenciados, modelada por SMI.
c) um servidor de aplicação.
d) um firewall.
e) um sistema de arquivos.

> **Resposta: b.** **MIB** = base hierárquica de objetos (modelada pelo **SMI**); não é protocolo nem software.

---

**Questão 3.** (CESPE-style) A versão 3 do SNMP diferencia-se das anteriores por oferecer recursos de segurança, como autenticação e criptografia, com senhas separadas para leitura e escrita.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **v3**: DES, hashes MD5/SHA, modelos USM/TSM, túneis SSL, senhas read/write separadas. v1 = texto simples.

---

**Questão 4.** (FCC-style) O modelo de QoS que realiza reserva de recursos ponta a ponta por meio do protocolo RSVP, exigindo suporte dos nós intermediários, é o:
a) DiffServ.
b) IntServ.
c) Best-Effort.
d) MPLS.
e) 802.1P.

> **Resposta: b.** **IntServ** = RSVP/reserva (complexo, uso limitado). **DiffServ** = classes (usado na Internet; sem garantia fim a fim).

---

**Questão 5.** (CESPE-style) O modelo DiffServ garante qualidade de serviço fim a fim em toda a Internet, pois todos os roteadores respeitam a marcação de classes.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **DiffServ não garante fim a fim** — roteadores de terceiros podem descartar a marcação. É simples e barato, mas sem garantia absoluta.

---

**Questão 6.** (FCC-style) A métrica de desempenho que representa a variação do atraso (latência) entre pacotes e é crítica para aplicações de VoIP e vídeo é:
a) throughput.
b) perda de pacotes.
c) jitter.
d) disponibilidade.
e) largura de banda.

> **Resposta: c.** **Jitter** = variação de atraso (instabilidade prejudicial a tempo real). Throughput = vazão.

---

**Questão 7.** (CESPE-style) O Zabbix não suporta o protocolo SNMP, sendo restrito a agentes proprietários.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Zabbix suporta SNMP** (templates/scripts), além de agentes e tráfego passivo.

---

**Questão 8.** (FCC-style) A diferença entre NetFlow e sFlow é que:
a) NetFlow usa amostragem; sFlow analisa todos os pacotes.
b) NetFlow analisa fluxos completos (Cisco/IPFIX); sFlow baseia-se em amostragem de pacotes.
c) ambos são idênticos.
d) sFlow opera apenas em camada 1.
e) NetFlow é open source exclusivo de Linux.

> **Resposta: b.** **NetFlow** = fluxos (Cisco, IPFIX); **sFlow** = **amostragem** (RFC 3176), escalável em Gigabit+.

---

**Questão 9.** (CESPE-style) O RMON (Remote Monitoring) versão 2 acrescenta monitoramento das camadas de rede e de aplicação às capacidades da versão 1, que abrange apenas as camadas física e de enlace.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **RMON v1** = camadas 1/2; **v2** = acrescenta 3/7.

---

**Questão 10.** (FCC-style) Na stack de monitoramento moderna, o componente responsável por coletar, transformar e encaminhar logs ao Elasticsearch é:
a) Kibana.
b) Grafana.
c) Logstash (ou Fluentd).
d) Prometheus.
e) Nagios.

> **Resposta: c.** **Logstash/Fluentd** = coleta/transformação. **Kibana/Grafana** = visualização; **Prometheus** = métricas (pull).

---

**Questão 11.** (CESPE-style) O Prometheus coleta métricas por modelo de push, no qual cada host envia continuamente seus valores ao servidor central.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Prometheus** usa **pull/scraping** (o servidor busca os targets/exportadores), com **PromQL** e Alertmanager.

---

**Questão 12.** (FGV-style) Sobre o SNMP, é correto afirmar:
a) a arquitetura é de cliente-servidor clássico.
b) os traps são enviados pelo gerente aos agentes mediante solicitação.
c) agentes rodam nos dispositivos gerenciados e respondem a requisições do NMS, podendo enviar traps.
d) a MIB é um protocolo de transporte.
e) o SNMPv2 é compatível com o SNMPv1.

> **Resposta: c.** **Agentes** nos dispositivos respondem ao **NMS** e emitem **traps** (unidirecionais, sem solicitação). SNMP **não** é cliente-servidor clássico; **v2 incompatível com v1** (v2c é compatível).

---

**Questão 13.** (CESPE-style) O token bucket, mecanismo de controle de tráfego, descarta pacotes excedentes da rajada.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O **token bucket** descarta **símbolos (tokens)** excedentes, não pacotes diretamente.

---

**Questão 14.** (FCC-style) As ferramentas Elasticsearch, Logstash e Kibana (ELK) relacionam-se, respectivamente, a:
a) coleta, armazenamento/busca e visualização.
b) armazenamento/busca, coleta/transformação e visualização.
c) visualização, coleta e armazenamento.
d) métricas, alertas e dashboards.
e) firewall, proxy e IDS.

> **Resposta: b.** **Elasticsearch** = armazenamento/busca (índice invertido); **Logstash** = coleta/transformação; **Kibana** = visualização. (Fluentd substitui Logstash = **EFK**.)

---

**Questão 15.** (CESPE-style) O Grafana é uma ferramenta de coleta de métricas por scraping, com linguagem de consulta própria denominada PromQL.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é o **Prometheus** (PromQL, pull). **Grafana** = **dashboards** multi-fonte (Prometheus, Elasticsearch, Zabbix...) com alertas.

---

## Questões discursivas

**D1.** Explique a arquitetura SNMP (gerente, agentes e MIBs), as diferenças entre suas versões e o papel dos traps.

> **Modelo de resposta:** O SNMP tem **NMS (gerente)** que consulta **agentes** rodando nos dispositivos gerenciados; a descrição dos objetos fica nas **MIBs** (hierárquicas, modeladas por SMI). A coleta ocorre por **request/response (161/UDP)** ou por **traps (162/UDP)**, mensagens unidirecionais enviadas pelo agente ao gerente sem solicitação (ex.: alerta de banda). **v1** tem senhas em texto simples; **v2** introduz GetBulk/Inform, mas é incompatível com v1 (a **v2c** restaura a compatibilidade); **v3** acrescenta segurança (autenticação MD5/SHA, criptografia DES, modelos USM/TSM, senhas separadas de leitura/escrita).

**D2.** Diferencie IntServ e DiffServ em QoS e explique o papel das ferramentas Zabbix, Prometheus, Elasticsearch, Logstash/Fluentd, Kibana e Grafana no monitoramento de redes.

> **Modelo de resposta:** **IntServ** reserva recursos ponta a ponta via **RSVP**, exigindo suporte dos nós intermediários (complexo, pouco usado na Internet). **DiffServ** classifica o tráfego em serviços (campo TOS/DSCP), sendo simples e adotado na Internet, mas **sem garantia fim a fim**. No monitoramento: **Zabbix** monitora rede e aplicações (suporta SNMP, alertas); **Prometheus** coleta **métricas** por scraping (PromQL, Alertmanager); **Elasticsearch** armazena e indexa logs; **Logstash/Fluentd** coletam e transformam dados (stack ELK/EFK); **Kibana** e **Grafana** são de visualização — a Kibana sobre o Elasticsearch, a Grafana multi-fonte (Prometheus, Zabbix etc.).

---

*Base: `02.Redes de Computadores` (Aula10 — SNMP/MIB/RMON/Nagios/Zabbix/Cacti/NetFlow/sFlow/Syslog) e `10.Segurança da Informação e Armazenamento de Dados` (Aula08 — QoS IntServ/DiffServ/RSVP, métricas de desempenho). Complemento: stack ELK/EFK (Elasticsearch, Logstash, Kibana, Fluentd), Grafana e Prometheus — ausentes da base de 2020 (o edital os exige explicitamente).*