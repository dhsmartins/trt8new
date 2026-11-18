# APOSTILA — TÓPICO 13: SERVIÇOS DE REDE
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Serviços de rede: e-mail, DNS, DHCP, Web Proxy; servidor de aplicações JBoss EAP/WildFly; servidores web Apache HTTP Server e IIS; análise de desempenho; gerenciamento de usuários; configuração, administração e logs.
>
> **Base de conhecimento:** `02.Redes de Computadores` (Aulas 08–10, 12), `01.Sistemas Operacionais e Arquitetura` (Aulas 08 — LDAP/AD; 15 — JBoss/WildFly), `02.Básico.para.Concursos.2020/04.Informática` (Aulas 05, 08) — Curso Regular TI 2020.2 + **complemento** (IIS atual, administração de logs).

---

# MÓDULO I — SERVIÇOS DE APLICAÇÃO: E-MAIL, DNS, DHCP E PROXY

## 1. E-mail

- **MUA** (cliente: Outlook, webmail) × **MTA** (servidor↔servidor). Fluxo: MUA → SMTP → MTA → SMTP → MTA → POP3/IMAP → MUA.
- **SMTP (25)**: envio, **ASCII 7-bit**, **store-and-forward**, persistente (QUIT, timeout 5 min). Portas: 25 (MTA↔MTA), **587** (submissão, anti-spam), 465 (SMTPS). **MIME** estende RFC 822 (anexos/binários).
- **POP3 (110)**: baixa e **remove** do servidor (1 dispositivo; APOP/MD5). **IMAP (143/993 IMAPS)**: mensagens **permanecem no servidor** (vários dispositivos, pastas remotas, leitura offline, v4).

## 2. DNS

- Hierárquico (raiz ".", FQDN); **porta 53** (UDP consultas; TCP >512 B e transferências **AXFR**). Zonas master/slave; zonas reversas/**PTR**; Root Hints; forwarders; consultas **iterativa × recursiva** (mais usada).
- Registros: **A** (host→IP), **CNAME** (apelido), **PTR** (IP→nome), **NS**, **MX** (mail), **SOA** (serial, refresh 3600, retry 600). **BIND** (v9): padrão em Linux (Red Hat/Oracle Linux).

## 3. DHCP

- **DORA**: Discovery → Offer (por MAC) → Request → ACK (lease). **Portas: servidor 67/UDP, cliente 68/UDP**. Hierárquico com **relay agents**; reserva estática por MAC (servidores/impressoras); pools, máscara, gateway, DNS.

## 4. Web Proxy

- Servidor **intermediário** entre cliente e servidores externos. **Componentes básicos**: acesso à Internet + acesso à rede interna (questão PETROBRÁS 2008). Funções: esconder IP do usuário, **cache**, filtragem de conteúdo/URL, auditoria. Método **CONNECT** do HTTP associado a proxies.
- **Proxy direto** (cliente → proxy → Internet) × **proxy reverso** (Internet → proxy → servidor interno: proteção, balanceamento e cache). *Ver apostila T16 (firewall/proxy).*

---

# MÓDULO II — SERVIDORES WEB E DE APLICAÇÕES

## 1. Apache HTTP Server × IIS

- **Apache HTTP Server**: open source, multiplataforma, modular (módulos `mod_ssl`, `mod_rewrite`...), configuração por `httpd.conf`/`.htaccess`. **Mais utilizado** ao lado do IIS.
- **IIS (Internet Information Services)**: Microsoft, integrado ao Windows Server; configuração via Gerenciador/IIS Manager e PowerShell; sites, aplicações ASP.NET, certificados.
- *Questão CESPE TRT-DF/GO 2013*: os mais utilizados são **Apache HTTP Server** e **IIS** (e "Enterprise Server" como conceito genérico aceito pela banca).

## 2. JBoss EAP / WildFly

- **Servidor de aplicações JEE** (Java). **JBoss AS** (comunitário) × **JBoss EAP** (Enterprise Application Platform, suportado pela Red Hat). **WildFly** = continuação comunitária do JBoss AS.
- Modos de execução: **standalone** (instância única) × **domain** (gerenciamento centralizado de várias instâncias). Servidor web embutido: Tomcat (até v7) e **Undertow** (a partir da v8). Implantação de WAR/EAR; datasources JBoss; logs em `server.log`.

---

# MÓDULO III — GERENCIAMENTO DE USUÁRIOS

- **LDAP** (389/TCP): protocolo de acesso a diretórios (base X.500); **DN/RDN** (DC/O/OU); operações Bind/Search/Add/Delete/Modify/Compare/StartTLS.
- **Active Directory** (ver tópico 11): serviço de diretório Microsoft (contas, grupos, OUs, políticas GPO, Catálogo Global); autenticação Kerberos/NTLM; **exige NTFS**; arquivo Ntds.dit.
- Administração: criação/alteração de contas, grupos (globais/universais/dominiais), políticas de senha, auditoria de logon; em Linux: usuários/grupos (`/etc/passwd`, `/etc/shadow`, `useradd`, `sudo`).

---

# MÓDULO IV — ANÁLISE DE DESEMPENHO, LOGS E ADMINISTRAÇÃO

## 1. Análise de desempenho e tráfego

- **Sniffers** (modo promíscuo): **Wireshark** (gráfico), **TCPDump** (Unix), **WinDump** (Windows). Interpretação de capturas: números de sequência, retransmissões, **gaps vs. fora de ordem** (= rotas diferentes).
- Métricas: largura de banda/taxa/vazão, perda de pacotes, atraso/latência/retardo, **jitter**, disponibilidade (ver tópico 14).
- Monitoramento de servidores: uso de CPU/memória/discos, conexões ativas, tempo de resposta; ferramentas: **Zabbix, Nagios, Cacti, NetFlow/sFlow** (ver tópico 14).

## 2. Configuração, administração e logs

- **Syslog**: logs centralizados, **TCP/UDP 514**, SSL/TLS **6514**; 3 papéis: **origem, armazenamento e análise**. Níveis de severidade (emerg, alert, crit, err, warning, notice, info, debug).
- **Logs de servidores web**: Apache (`access.log`, `error.log`, `CustomLog`); IIS (W3C format); JBoss (`server.log`). Rotação/retenção de logs, análise de acessos, detecção de erros.
- **SIEM** (complemento): agregação e correlação de logs (Elasticsearch/Logstash/Kibana — ver tópico 14).
- *Boas práticas de administração*: menor privilégio, backups, atualizações (WSUS/patching — tópico 11), monitoramento contínuo, documentação de configuração.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **SMTP envia (25/587)**; **POP3 baixa e remove (110)**; **IMAP mantém no servidor (143)**.
2. **DNS 53**: UDP consultas, TCP transferências de zona (**AXFR**). Registros A/CNAME/PTR/MX/SOA/NS.
3. **DHCP: 67 servidor / 68 cliente**; DORA (Discovery→Offer→Request→ACK).
4. **Proxy** = intermediário (duas conexões: cliente-proxy e proxy-servidor); **proxy reverso** protege/balanceia o servidor.
5. **CONNECT** do HTTP é método associado a proxies.
6. **Apache e IIS** = os dois servidores web mais utilizados (CESPE TRT-DF/GO 2013).
7. **JBoss EAP/WildFly** = servidor **JEE**; **Undertow** a partir da v8; modos **standalone × domain**.
8. **LDAP = protocolo (389)**, não é o diretório; AD **usa** LDAP e **exige NTFS**.
9. **Syslog: 514 (TCP/UDP), 6514 (TLS)**; papéis: origem/armazenamento/análise.
10. **Sniffers**: Wireshark/TCPDump/WinDump em modo **promíscuo**.
11. **Zabbix suporta SNMP** (falso dizer o contrário).
12. **Gaps × fora de ordem** em capturas: fora de ordem = rotas diferentes; gaps podem indicar perda.
13. **WildFly** = continuação comunitária do JBoss AS; **EAP** = versão corporativa (Red Hat).
14. **POP3 = 1 dispositivo; IMAP = vários**.
15. **IIS** é Microsoft/Windows Server; **Apache** é open source/multiplataforma.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O protocolo IMAP baixa as mensagens de e-mail para o cliente e as remove do servidor, sendo indicado para usuários que acessam a caixa de entrada em um único dispositivo.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Isso é o **POP3**. **IMAP** **mantém** as mensagens no servidor (vários dispositivos, pastas remotas).

---

**Questão 2.** (FCC-style) As portas utilizadas pelo servidor e pelo cliente DHCP são, respectivamente:
a) 53 e 54.
b) 67 e 68.
c) 68 e 67.
d) 25 e 110.
e) 161 e 162.

> **Resposta: b.** DHCP: **servidor 67/UDP**, **cliente 68/UDP**. (53 = DNS; 25 = SMTP; 110 = POP3; 161/162 = SNMP.)

---

**Questão 3.** (CESPE-style) O servidor web mais utilizado na Internet, juntamente com o Internet Information Services (IIS) da Microsoft, é o Apache HTTP Server.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Apache** e **IIS** são os dois mais utilizados (questão CESPE TRT-DF/GO 2013).

---

**Questão 4.** (FCC-style) O servidor de aplicações JBoss EAP/WildFly destina-se a:
a) hospedar páginas HTML estáticas apenas.
b) executar aplicações Java EE (WAR/EAR).
c) gerenciar endereços IP.
d) servir DNS.
e) controlar impressoras de rede.

> **Resposta: b.** **JBoss/WildFly** = servidor de aplicações **JEE** (Java). Apache/IIS servem web; DHCP = IP; DNS = nomes.

---

**Questão 5.** (CESPE-style) O Web Proxy atua como intermediário entre o cliente e servidores externos, podendo ocultar o IP do usuário, armazenar cache e filtrar conteúdo.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Proxy = intermediário (duas conexões); esconde IP, cache, filtra URL/conteúdo, audita.

---

**Questão 6.** (FCC-style) O registro DNS responsável por apontar um nome de domínio para um endereço IPv4 é o registro:
a) PTR.
b) MX.
c) A.
d) SOA.
e) CNAME.

> **Resposta: c.** **A** = nome→IPv4. **PTR** = IP→nome; **MX** = mail; **CNAME** = apelido; **SOA** = autoridade da zona.

---

**Questão 7.** (CESPE-style) As transferências de zona DNS (AXFR) ocorrem via UDP na porta 53, dispensando TCP.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Transferências de zona usam **TCP** na porta 53 (UDP é para consultas; TCP também acima de 512 B).

---

**Questão 8.** (FCC-style) O proxy reverso difere do proxy direto por:
a) esconder o IP do cliente.
b) posicionar-se à frente do servidor interno, oferecendo proteção, balanceamento e cache.
c) funcionar exclusivamente em rede wireless.
d) substituir o firewall.
e) operar apenas na camada física.

> **Resposta: b.** **Reverso**: protege/balanceia o **servidor** (cache de objetos estáticos). **Direto**: intermedia o **cliente** na saída.

---

**Questão 9.** (CESPE-style) O servidor WildFly é a versão corporativa suportada pela Red Hat do JBoss AS.
a) Certo. b) Errado.

> **Resposta: b (Errado).** É o inverso: **WildFly** = continuação **comunitária**; **JBoss EAP** = versão **corporativa** (Red Hat).

---

**Questão 10.** (FCC-style) O protocolo LDAP opera na porta:
a) 23.
b) 25.
c) 80.
d) 389.
e) 443.

> **Resposta: d.** **LDAP = 389/TCP** (LDAPv3; LDAPS = 636). 23 = Telnet; 25 = SMTP; 80 = HTTP; 443 = HTTPS.

---

**Questão 11.** (CESPE-style) O Syslog pode operar nas portas TCP e UDP 514, e o envio criptografado usa a porta 6514.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Syslog: **514** (TCP/UDP); **6514** (TLS/SSL). Papéis: origem, armazenamento e análise.

---

**Questão 12.** (FGV-style) Sobre análise de tráfego com sniffers, é correto afirmar:
a) Wireshark e TCPDump capturam apenas tráfego criptografado.
b) o modo promíscuo permite capturar todos os quadros da interface, inclusive os não endereçados à máquina.
c) gaps em capturas indicam sempre rotas diferentes.
d) sniffers são exclusivos de Windows.
e) WinDump é exclusivo de Linux.

> **Resposta: b.** Modo **promíscuo** captura tudo na interface. Wireshark (gráfico), TCPDump (Unix), WinDump (Windows). **Fora de ordem** = rotas diferentes; gaps podem indicar perda.

---

**Questão 13.** (CESPE-style) No servidor de aplicações JBoss, o modo standalone é destinado ao gerenciamento centralizado de múltiplas instâncias distribuídas.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Standalone** = instância única. O **domain** é que gerencia centralizadamente várias instâncias.

---

**Questão 14.** (FCC-style) O método HTTP CONNECT é tipicamente associado a qual serviço de rede?
a) DNS.
b) DHCP.
c) Web Proxy.
d) SMTP.
e) FTP.

> **Resposta: c.** **CONNECT** abre túnel via **proxy** (ex.: HTTPS através do proxy).

---

**Questão 15.** (CESPE-style) O Active Directory pode ser implantado em sistemas de arquivos FAT32 e não depende de protocolo de diretório.
a) Certo. b) Errado.

> **Resposta: b (Errado).** AD **exige NTFS** e **usa LDAP** (389) como protocolo de diretório (Kerberos para autenticação).

---

## Questões discursivas

**D1.** Explique o funcionamento dos serviços de e-mail (SMTP, POP3 e IMAP) e as diferenças entre POP3 e IMAP.

> **Modelo de resposta:** O envio de e-mail usa **SMTP** (portas 25/587), com modelo **store-and-forward** entre MTAs; o cliente (MUA) submete mensagens ao MTA. A retirada das mensagens usa **POP3** ou **IMAP**. **POP3 (110)** baixa as mensagens e as **remove** do servidor, sendo adequado a um único dispositivo. **IMAP (143/993)** mantém as mensagens **no servidor**, permitindo acesso simultâneo de múltiplos dispositivos, organização em pastas remotas e leitura offline.

**D2.** Descreva o processo DHCP (DORA) e explique o papel do Web Proxy e do Syslog na administração de rede.

> **Modelo de resposta:** O **DHCP** configura endereços IP automaticamente pelo processo **DORA**: **Discovery** (broadcast do cliente), **Offer** (oferta do servidor por MAC), **Request** (aceite do cliente) e **ACK** (concessão do lease), nas portas 67 (servidor) e 68 (cliente), com suporte a relay agents e reservas por MAC. O **Web Proxy** é um intermediário que oculta o IP do usuário, armazena cache e filtra conteúdo (proxy direto), podendo atuar como proxy reverso para proteger e balancear servidores. O **Syslog** centraliza registros de eventos (portas 514; TLS em 6514), com papéis de origem, armazenamento e análise, essencial para auditoria, diagnóstico e conformidade.

---

*Base: `02.Redes de Computadores` (Aulas 08–10, 12), `01.Sistemas Operacionais e Arquitetura` (Aula08 — LDAP/AD; Aula15 — JBoss/WildFly), `02.Básico.para.Concursos.2020/04.Informática` (Aulas 05 e 08 — e-mail e proxy). Complemento: SIEM e administração moderna de logs — ver também apostila T14.*