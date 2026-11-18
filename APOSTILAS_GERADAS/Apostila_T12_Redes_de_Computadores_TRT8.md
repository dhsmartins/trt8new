# APOSTILA — TÓPICO 12: REDES DE COMPUTADORES
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Tipos e meios de transmissão; comutação por circuitos, por pacotes e por células; redes PAN, LAN, MAN, WAN, WPAN, WLAN, WMAN e WWAN; protocolos e elementos de interconexão; modelo OSI; TCP/IP; IPv4 e IPv6 (segmentação, endereçamento, DNS); TCP, UDP, IPSec, ARP, SSH, SMTP, HTTP, FTP, LDAP, DNS, DHCP, POP e IMAP; cabeamento estruturado ABNT NBR 14565:2019; fibras ópticas mono e multimodo; IEEE 802.1Q, 802.1X, 802.3, Spanning Tree e RSTP; wireless 802.11ac, 802.11ax e 802.11be.
>
> **Base de conhecimento:** `02.Redes de Computadores` (Aulas 00–12) e `01.Sistemas Operacionais e Arquitetura` (Aula08 — LDAP/AD) — Curso Regular TI 2020.2 + **complemento** (802.11ax/be, NBR 14565:2019).

---

# MÓDULO I — CLASSIFICAÇÃO, MEIOS E COMUTAÇÃO

## 1. Redes por alcance

| Rede | Alcance | Exemplo |
|---|---|---|
| **PAN** | ~10 m | Bluetooth |
| **LAN** | Prédio/campus | Ethernet |
| **MAN** | Cidade | Metro Ethernet |
| **WAN** | País/continente | MPLS, Internet |

- Variante sem fio: **WPAN, WLAN, WMAN, WWAN**. CAN/TAN também citadas. *Forouzan*: LAN/MAN = "não comutadas"; WAN = "comutada".
- **Topologias**: barramento, estrela, anel (Token Ring), malha/mesh, árvore. Topologia **física × lógica**. Meio compartilhado: **CSMA/CD** (com fio) e **CSMA/CA** (sem fio).

## 2. Meios de transmissão

- **Guiados**: par trançado (UTP/STP), coaxial, **fibra óptica**. **Não guiados**: rádio, micro-onda, satélite, infravermelho. Capacidade por **Nyquist/Shannon**; multiplexação **FDM/TDM/WDM**.
- **Categorias UTP** (conector RJ-45, padrão T568A/B; limite prático 100 m; regra 5-4-3 para repetidores): CAT5 (100 MHz/100 Mbps), CAT5e (125 MHz/1 Gbps), CAT6 (250 MHz/10 Gbps até 55 m), CAT6a (500 MHz/10 Gbps), CAT7 (600 MHz), CAT7a (1000 MHz).

| Fibra | Monomodo | Multimodo |
|---|---|---|
| Núcleo | Pequeno (~9 µm) | Maior (50 ou 62,5 µm) |
| Fonte | Somente **laser** | LED ou laser |
| Atenuação | **Menor** | Maior |
| Distância | Centenas de km (WAN) | Curtas (ex.: 550 m em 1000BASE-SX) |
| Exemplo | 1000BASE-LX (1310 nm, até 40 km) | 1000BASE-SX (550 m; medida por **OFL**) |

*Pegadinha*: "monomodo 62,5/125 µm" é **falso** — 62,5 µm é **multimodo**. Conectores: SC, ST, MT-RJ. **NBR 14565 (cabeamento estruturado)** aparece em questões; a versão **2019** é o texto atual do edital (complementar).

## 3. Comutação

- **Por circuito**: caminho dedicado; desperdício quando ocioso; bloqueio se não houver recurso.
- **Por pacote**: caminho compartilhado, sem rota pré-estabelecida (datagrama/circuito virtual).
- **Por célula (ATM)**: células fixas de **53 bytes = 5 B cabeçalho + 48 B carga**; circuitos virtuais VPI/VCI; camadas AAL/SAR/CS.

---

# MÓDULO II — ELEMENTOS DE INTERCONEXÃO E MODELOS OSI/TCP-IP

## 1. Dispositivos

- **Hub/repetidor**: regenera sinal; **1 domínio de colisão** e 1 de broadcast; half-duplex.
- **Bridge**: **L2**; separa tráfego por MAC.
- **Switch**: isola domínios de colisão **por porta** (tabela MAC/CAM); sem VLANs, mantém 1 domínio de broadcast. Modos: **Store-and-Forward, Cut-Through, Fragment Free**.
- **Roteador**: **L3** (IP), tabelas de roteamento; **separa broadcasts**.
- **Gateway**: **L7**; converte protocolos (ex.: voz).

## 2. OSI (7) × TCP/IP (4)

| OSI | TCP/IP | PDU | Exemplos |
|---|---|---|---|
| Aplicação | Aplicação | Dados | HTTP, SMTP, DNS |
| Apresentação | Aplicação | Dados | ASCII, SSL/TLS, MIME |
| Sessão | Aplicação | Dados | NetBIOS, RPC |
| Transporte | Transporte | Segmentos | TCP, UDP |
| Rede | Internet | Pacotes | IP, ICMP, ARP* |
| Enlace (LLC/MAC) | Acesso à rede | Quadros | Ethernet, 802.11 |
| Física | Acesso à rede | Bits | Cabos, rádio |

*ARP opera entre enlace e rede. Hosts implementam todas as camadas; dispositivos intermediários até a sua camada. **MPLS** = "camada 2.5" (Label 20 bits; campo Exp/QoS 3 bits = 8 classes; FEC; LSR/LER; LIB).

## 3. Ethernet (IEEE 802.3)

- Ethernet 10 Mbps half-duplex; **FastEthernet** 100 Mbps (100BaseTX/FX); **GigabitEthernet** 1000 Mbps full-duplex (jumbo frames até 9000 B; precisa switch em estrela). CSMA/CD no half-duplex; controle de fluxo (802.3x) no full-duplex.
- *Pegadinha*: "FastEthernet atinge 200 Mbps full-duplex" — impreciso: taxa nominal é **100 Mbps por direção**. "GigabitEthernet tem QoS nativamente" — **falso** (precisa 802.1p/q, 802.3x, RSVP).

## 4. STP/RSTP/MSTP

- **STP (802.1d)**: **root bridge** = menor bridge ID; BPDUs; estados blocking/listening/learning/forwarding; convergência até **50 s**. **RSTP**: forwarding/learning/**discarding** (mais rápido). **MSTP**: múltiplas instâncias.

---

# MÓDULO III — VLANs, 802.1X E WIRELESS

## 1. IEEE 802.1Q / 802.1P / 802.1X

- **802.1Q**: **tag/trunk**; VLAN por porta, MAC ou endereço de rede; modos aberto/fechado/misto.
- **802.1P**: 3 bits de prioridade = **QoS na camada 2**.
- **802.1X**: autenticação **por porta** — **suplicante, authenticator, servidor de autenticação (RADIUS)**; encapsula via **EAP/EAPOL** (TLS, MD5, TTLS, PEAP, LEAP).

## 2. Sem fio (IEEE 802.11)

| Padrão | Faixa | Canal | Modulação | Taxa | Antenas |
|---|---|---|---|---|---|
| 802.11a | 5 GHz | 20 MHz | OFDM | 54 Mbps | — |
| 802.11b | 2,4 GHz | 20 MHz | DSSS (HR-DSSS) | 11 Mbps | alcance ~7× o de "a" |
| 802.11g | 2,4 GHz | 20 MHz | DSSS+OFDM | 54 Mbps | — |
| 802.11n | 2,4+5 GHz | 20–40 MHz | OFDM/**MIMO** | 600 Mbps | 4 |
| 802.11ac | **5 GHz** | 40–160 MHz | OFDM/MIMO | até 7000 Mbps | 8 |

- "a" é **incompatível** com "b". Acesso DCF/PCF. Segurança: WEP/WPA quebrados; **WPA2** recomendado (ver tópico 16).
- **802.11ax (Wi-Fi 6) e 802.11be (Wi-Fi 7)** *(complemento — ausentes na base de 2020)*: **ax** = 2,4/5/6 GHz, OFDMA, MU-MIMO uplink, TWT (economia de energia), maior densidade; **be** = Wi-Fi 7 (320 MHz, 4096-QAM, Multi-Link Operation).
- **WPAN**: Bluetooth = **802.15.1** (2,4 GHz); ZigBee = 802.15.4 (baixa potência). **WMAN/WiMAX 802.16** (10–66 GHz; 802.16d com MIMO; 802.16e com mobilidade).

---

# MÓDULO IV — IPv4, IPv6 E PROTOCOLOS

## 1. IPv4

- 32 bits / 4 octetos. Classes pelos primeiros bits: **0=A, 10=B, 110=C, 1110=D**. Máscara = operação **AND**; subnetting; **VLSM**; **CIDR/supernetting**.
- **Privadas**: **A 10.0.0.0/8** (16.777.216 hosts), **B 172.16.0.0/12** (1.048.576), **C 192.168.0.0/16** (65.536). Loopback **127.0.0.1**. Campo TOS/DSCP (6 dos 8 bits, RFC 2474). Fragmentação pelo roteador.
- **NAT/PAT**: estático 1:1; dinâmico; **NAPT/NAT overload N:1** (portas); NAT reverso (round-robin/load balancing); NAT **altera o cabeçalho IP**.

## 2. IPv6

| IPv4 | IPv6 |
|---|---|
| 32 bits, 4 octetos | **128 bits**, 8 grupos hexadecimais |
| Cabeçalho variável 20–60 B | Cabeçalho **fixo 40 B** (8 campos) |
| Broadcast | **Sem broadcast** (ND substitui ARP; MLD substitui IGMP) |
| Fragmentação no roteador | **Só na origem** (ICMPv6 "packet too big") |
| IPSec opcional | **IPSec obrigatório** |
| ARP | **Neighbor Discovery** |

- Compressão "::" (uma vez por endereço); máscara padrão **/64** em LAN; autoconfiguração link-local **FE80::/64** com **EUI-64**; multicast **FF00::/8**; loopback **::1**; não especificado **::0**. Transição: Dual Stack, tunelamento, tradução.

## 3. ARP, ICMP, IGMP

- **ARP**: mapeia **IP↔MAC**; ARP Request **broadcast FF:FF:FF:FF:FF:FF**; ARP Reply unicast; cache. **RARP**: inverso. **ICMP**: diagnóstico (ping/traceroute) — **não é camada de transporte**. **IGMP**: grupos multicast.

## 4. TCP × UDP

| TCP | UDP |
|---|---|
| Orientado a conexão (**3-way handshake**) | Sem conexão |
| Confiável (ACK, retransmissão) | Não confiável, sem ACK |
| Ordenação (números de seq.) | Sem ordenação |
| Controle de fluxo (janela deslizante) e de congestão | Sem controle |
| Mais lento, mais overhead | Rápido, leve (DNS, VoIP, DHCP) |

**Portas essenciais**: FTP-dados 20, FTP-controle 21, **SSH 22**, Telnet 23, **SMTP 25**, **DNS 53** (UDP+TCP), **HTTP 80**, **POP3 110**, **IMAP 143**, SNMP 161/162, **HTTPS 443**, CIFS/SMB 445, SMTPS 465, SMTP-TLS 587, IMAPS 993, POP3S 995, RDP 3389. **DHCP: servidor 67/UDP, cliente 68/UDP**.

## 5. Protocolos de aplicação

- **HTTP**: cliente-servidor, request/response, **stateless** (cookies tornam stateful); v1.0 não persistente × v1.1 persistente; métodos GET/POST/PUT/DELETE/**CONNECT (proxy)**; códigos 2xx sucesso, 3xx redirecionamento; cache no cliente/proxy. HTTPS = 443 com SSL/TLS.
- **E-mail**: MUA (cliente) × MTA (servidor). **SMTP 25** (587 anti-spam; 465 SMTPS): ASCII 7-bit, **store-and-forward**. **POP3 110**: baixa e **remove** do servidor, 1 dispositivo (APOP/MD5). **IMAP 143/993**: mensagens **permanecem no servidor**, múltiplos dispositivos, pastas remotas, leitura offline. MIME estende RFC 822.
- **DHCP**: evolução do BOOTP; hierárquico (relay agents); **DORA**: **D**iscovery (broadcast de 0.0.0.0) → **O**ffer (por MAC) → **R**equest (broadcast) → **A**CK (lease). Reserva estática por MAC (servidores/impressoras).
- **FTP**: portas **20+21**, outband (2 conexões); modo ativo (vulnerável em firewall) × passivo; sem criptografia nativa (SFTP sobre SSH).
- **DNS**: porta **53** (UDP consultas; TCP >512 B e transferências de zona); hierarquia (raiz ".", FQDN); zonas (master/slave, **AXFR**); zonas reversas/PTR; Root Hints; consultas iterativa × **recursive (mais usada)**; registros **A, CNAME, PTR, NS, MX, SOA** (serial, refresh 3600, retry 600); BIND (v9); forwarders.
- **Telnet 23 × SSH 22**: Telnet **sem criptografia**; SSH seguro (chaves assimétricas; SSH1 vulnerável a MITM; SSH2; **SFTP** tunelado).
- **LDAP**: porta **389/TCP** (LDAPv3); baseado em X.500; nomenclatura hierárquica (**DN/RDN**; atributos DC/O/OU); operações Bind/Search/Add/Delete/Modify/Compare/StartTLS. **AD**: serviço de diretório Microsoft que usa LDAP (ver tópico 11).

---

# RESUMO DE PEGADINHAS DE PROVA

1. **Monomodo ~9 µm só laser**; 62,5/125 µm = **multimodo**. Multimodo mede por **OFL**.
2. **ATM: células de 53 bytes** (5+48).
3. **Hub** = 1 domínio de colisão; **switch** isola colisões por porta; **roteador** separa broadcasts (L3).
4. **ICMP não é camada de transporte**; ARP opera entre enlace e rede.
5. **IPSec: opcional IPv4, obrigatório IPv6**. IPv6: **sem broadcast**; fragmentação **só na origem**.
6. **DHCP: 67 servidor / 68 cliente** (não confundir com 53/DNS ou 69/TFTP).
7. **POP3 remove** (1 dispositivo); **IMAP mantém** no servidor (vários dispositivos).
8. **STP converge até 50 s**; RSTP é mais rápido (discarding).
9. **802.11a (5 GHz) incompatível com 802.11b (2,4 GHz)**; "b" tem alcance ~7× maior.
10. **FastEthernet = 100 Mbps por direção** (não 200). **Gigabit não tem QoS nativa**.
11. **Zabbix suporta SNMP** (falso dizer o contrário). **SNMP usa 161/162**, não 22.
12. **DNS 53**: UDP para consultas, TCP para transferências de zona (AXFR).
13. **FTP = 20 (dados) + 21 (controle)**, duas conexões.
14. **NAT altera o cabeçalho IP**; NAPT usa portas (N:1).
15. **VLSM** = máscaras variáveis na mesma rede; **CIDR/supernetting** agrega rotas.
16. **802.11ax = Wi-Fi 6; 802.11be = Wi-Fi 7** (complemento — base só vai até "ac").
17. **NBR 14565:2019** = norma de **cabeamento estruturado** (edital cita a versão 2019).
18. **MPLS = camada 2.5**; label de 20 bits; Exp/QoS 3 bits.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) A fibra óptica monomodo possui núcleo de 62,5 µm e é indicada para longas distâncias em WANs.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **62,5 µm** é **multimodo**. **Monomodo** tem núcleo ~**9 µm**, só laser, atenuação menor, centenas de km.

---

**Questão 2.** (FCC-style) O dispositivo que opera na camada de rede (L3), mantém tabelas de roteamento e separa domínios de broadcast é:
a) hub.
b) bridge.
c) switch.
d) roteador.
e) repetidor.

> **Resposta: d.** **Roteador** = L3 (IP), separa broadcasts. Switch/Bridge = L2 (colisão por porta/MAC); Hub = L1.

---

**Questão 3.** (CESPE-style) O protocolo ICMP é classificado como protocolo de camada de transporte, equivalente ao TCP e ao UDP.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **ICMP** é de **rede** (diagnóstico: ping/traceroute), **não** de transporte.

---

**Questão 4.** (FCC-style) Na versão IPv6, em relação ao IPv4, ocorre:
a) ampliação do endereço para 128 bits e eliminação do broadcast.
b) redução do endereço para 64 bits.
c) obrigatoriedade de NAT.
d) fragmentação apenas em roteadores intermediários.
e) IPSec opcional.

> **Resposta: a.** IPv6: **128 bits**, **sem broadcast** (ND/MLD), fragmentação **só na origem**, **IPSec obrigatório**.

---

**Questão 5.** (CESPE-style) No DHCP, o processo de obtenção de endereço IP segue a sequência Discovery, Offer, Request e ACK (DORA).
a) Certo. b) Errado.

> **Resposta: a (Certo).** **DORA**: Discovery (broadcast) → Offer (por MAC) → Request (broadcast) → ACK (lease). Portas: servidor **67**, cliente **68**.

---

**Questão 6.** (FCC-style) O protocolo que baixa as mensagens de e-mail para o cliente e as remove do servidor, sendo adequado a um único dispositivo, é:
a) SMTP.
b) IMAP.
c) POP3.
d) MIME.
e) LDAP.

> **Resposta: c.** **POP3 (110)** baixa e **remove** (1 dispositivo). **IMAP (143)** mantém no servidor (vários dispositivos). **SMTP (25)** envia.

---

**Questão 7.** (CESPE-style) O padrão IEEE 802.1Q refere-se à autenticação de acesso à rede por porta, baseada em suplicante, authenticator e servidor RADIUS.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é **802.1X** (EAP/EAPOL). **802.1Q** = **VLAN tag/trunk**. **802.1P** = QoS L2 (3 bits).

---

**Questão 8.** (FCC-style) A convergência do Spanning Tree Protocol (STP 802.1d) pode levar até:
a) 5 segundos.
b) 15 segundos.
c) 30 segundos.
d) 50 segundos.
e) 90 segundos.

> **Resposta: d.** STP: até **50 s** (listening + learning). **RSTP** converge muito mais rápido (estados forwarding/learning/**discarding**).

---

**Questão 9.** (CESPE-style) As células do ATM possuem tamanho fixo de 53 bytes, sendo 5 bytes de cabeçalho e 48 bytes de carga útil.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Comutação por **células**: 53 = **5 + 48**.

---

**Questão 10.** (FCC-style) O protocolo ARP tem como finalidade:
a) traduzir nomes de domínio em endereços IP.
b) mapear endereços IP em endereços MAC (e vice-versa).
c) configurar endereços IP automaticamente.
d) rotear pacotes entre redes.
e) criptografar tráfego HTTP.

> **Resposta: b.** **ARP** = IP↔**MAC** (request broadcast; reply unicast). **DNS** = nome→IP; **DHCP** = configuração automática.

---

**Questão 11.** (CESPE-style) A diferença entre TCP e UDP é que o TCP é orientado a conexão, confiável, com controle de fluxo e de congestão, enquanto o UDP é sem conexão, sem confirmação e mais leve.
a) Certo. b) Errado.

> **Resposta: a (Certo).** TCP: 3-way handshake, ACK, ordenação, janela deslizante. UDP: rápido/leve (DNS, VoIP, DHCP) — sem ACK nem ordenação.

---

**Questão 12.** (FGV-style) Sobre meios de transmissão e fibra óptica, é correto afirmar:
a) a fibra multimodo utiliza somente laser e atinge centenas de km.
b) a fibra monomodo tem núcleo maior (50 ou 62,5 µm) e usa LED.
c) a fibra monomodo tem núcleo pequeno (~9 µm), usa laser e tem menor atenuação, indicada para WAN.
d) UTP CAT5 suporta 10 Gbps.
e) fibra multimodo mede-se pelo método OTDR exclusivamente.

> **Resposta: c.** Monomodo ~9 µm, laser, menor atenuação, longas distâncias. Multimodo 50/62,5 µm, LED/laser, curtas (OFL). CAT5 = 100 Mbps.

---

**Questão 13.** (CESPE-style) O padrão IEEE 802.11a opera na faixa de 2,4 GHz e é compatível com o padrão 802.11b.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **802.11a** = **5 GHz** e é **incompatível** com "b" (2,4 GHz). "b" tem alcance ~7× maior.

---

**Questão 14.** (FCC-style) Sobre DNS, é correto afirmar:
a) usa exclusivamente TCP na porta 53.
b) consultas usam UDP na porta 53; transferências de zona usam TCP.
c) não suporta registros MX.
d) o registro SOA não contém serial.
e) a consulta recursiva é menos usada que a iterativa.

> **Resposta: b.** DNS **53**: **UDP** consultas; **TCP** transferências (AXFR, >512 B). SOA tem serial/refresh/retry; MX = mail; **recursive** é a mais usada.

---

**Questão 15.** (CESPE-style) O cabeamento estruturado é normatizado no Brasil pela ABNT NBR ISO/IEC 27001, que trata de segurança da informação.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Cabeamento estruturado = **ABNT NBR 14565** (versão **2019** no edital). A **NBR ISO/IEC 27001** trata de **SGSI** (segurança da informação — ver tópico 16).

---

## Questões discursivas

**D1.** Explique o modelo OSI e o modelo TCP/IP, relacionando as camadas, as PDUs e exemplos de protocolos.

> **Modelo de resposta:** O **OSI** tem 7 camadas: Aplicação, Apresentação, Sessão, Transporte, Rede, Enlace e Física. O **TCP/IP** tem 4: Aplicação, Transporte, Internet e Acesso à rede. As PDUs são: dados (aplicação/presentação/sessão), **segmentos** (transporte — TCP/UDP), **pacotes** (rede — IP/ICMP) e **quadros** (enlace — Ethernet/802.11) e bits (física). Hosts implementam todas as camadas; dispositivos intermediários atuam até a sua camada (switch = L2, roteador = L3). O ARP opera entre enlace e rede; o MPLS é dito "camada 2.5".

**D2.** Diferencie TCP de UDP e explique o funcionamento do DHCP (DORA) e as diferenças entre POP3 e IMAP.

> **Modelo de resposta:** **TCP** é orientado a conexão (3-way handshake), confiável (ACK/retransmissão), ordenado, com controle de fluxo e de congestão — indicado a transferências confiáveis. **UDP** é sem conexão, sem confirmação, mais leve e rápido — indicado a DNS, VoIP e DHCP. O **DHCP** atribui endereços IP automaticamente pelo processo **DORA**: Discovery (broadcast), Offer (por MAC), Request (broadcast) e ACK (lease), nas portas 67 (servidor) e 68 (cliente). **POP3** baixa as mensagens e as **remove** do servidor (adequado a um único dispositivo); **IMAP** mantém as mensagens **no servidor**, permitindo acesso de múltiplos dispositivos e pastas remotas.

---

*Base: `02.Redes de Computadores` (Aulas 00–12) e `01.Sistemas Operacionais e Arquitetura` (Aula08 — LDAP/AD). Complemento: 802.11ax (Wi-Fi 6) e 802.11be (Wi-Fi 7), ABNT NBR 14565:2019 — ausentes da base de 2020. Segurança de redes wireless e VPN: ver apostila T16. Serviços (proxy, Apache/IIS, JBoss) e SNMP/QoS/ferramentas de monitoramento: ver apostilas T13 e T14.*