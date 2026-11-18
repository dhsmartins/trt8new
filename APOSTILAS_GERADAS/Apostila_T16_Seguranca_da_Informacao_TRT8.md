# APOSTILA — TÓPICO 16: SEGURANÇA DA INFORMAÇÃO
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** ABNT NBR ISO/IEC 27001:2024 e ABNT NBR ISO/IEC 27002:2022; ABNT NBR ISO/IEC 27701:2026; LGPD Lei nº 13.709/2018; OWASP Top 10:2025; firewall, WAF, UTM, DMZ, Proxy, NAC, Antivírus e AntiSpam; IDS e IPS; monitoramento de tráfego; sniffer; segurança em redes sem fio: EAP, WEP, WPA, WPA2 e WPA3; VPN, VPN-SSL e ZTNA; ataques e ameaças; códigos maliciosos; ataques DoS e DDoS; criptografia assimétrica e simétrica; certificados digitais; assinaturas digitais; funções hash; controle de acesso; RBAC; MFA; TLS 1.2 e 1.3 e limitações do SSL.
>
> **Base de conhecimento:** `10.Segurança da Informação e Armazenamento de Dados` (Aulas 00–05, 11–12), `02.Redes de Computadores` (Aulas 04, 08), `04.Desenvolvimento de Software` (Aulas 13–14) — Curso Regular TI 2020.2 + **complemento** (LGPD, OWASP 2025, ISO 27001:2024/27701:2026, WPA3, ZTNA, TLS 1.3).

---

# MÓDULO I — GOVERNANÇA: ISO 27001/27002/27701 E LGPD

## 1. ISO/IEC 27001 — SGSI

- Define requisitos do **SGSI** (Sistema de Gestão de Segurança da Informação). Objetivo: **estabelecer, implementar, manter e melhorar continuamente** o SGSI (ciclo **PDCA**).
- Estrutura (10 tópicos + anexo): 1 Escopo; 2 Referência Normativa; 3 Termos; 4 Contexto; 5 Liderança; 6 Planejamento; 7 Apoio; 8 Operação; 9 Avaliação de Desempenho; 10 Melhoria. **Itens 4 a 10 são obrigatórios** para conformidade.
- **POSIC** (Política de Segurança da Informação) documentada, comunicada e disponível às partes interessadas. Liderança **top-down**. Genérica (qualquer organização).
- *Complemento (versão **2024** no edital)*: a base local cobre a **2013**; a estrutura de alto nível (Annex SL) permanece; ver a 27002:2022 para os controles.

## 2. ISO/IEC 27002 — controles

- Código de **boas práticas com controles** para o SGSI (detalha o Anexo da 27001). Versão 2013: **14 seções, 35 objetivos, 114 controles**. Seções: Políticas; Organização da SI; Segurança em RH; Gestão de Ativos (**classificação da informação**); **Controle de Acesso**; **Criptografia** (confidencialidade, integridade/autenticidade, **não repúdio**, autenticação; gerenciamento de chaves); Segurança Física; Operações; Comunicações; Aquisição/Desenvolvimento; Cadeia de Suprimentos; Incidentes; Continuidade; Conformidade.
- *Complemento (versão **2022** no edital)*: **4 temas** (Pessoas, Físico, Tecnológico, Organizacional) e **93 controles** (11 novos, incl. threat intelligence, cloud services, data masking, DLP, secure coding).
- **Procedimentos seguros de log-on** (clássico): não mostrar identificadores antes de concluir; aviso de acesso restrito; validar só com dados completos; proteção contra tentativas forçadas; registrar tentativas; mostrar última entrada; não mostrar/transmitir senha em claro; encerrar sessões inativas.

## 3. ISO/IEC 27701 — privacidade *(complemento)*

- Extensão do 27001/27002 para **gestão de privacidade da informação (PIMS)** — alinhada à **LGPD** e ao GDPR: papéis (controlador/operador), bases legais, direitos do titular, avaliação de impacto, transferência internacional. O edital cita a versão **2026**.

## 4. LGPD (Lei 13.709/2018) *(complemento)*

- **Dado pessoal** = informação relacionada a pessoa natural identificada/identificável; **dado pessoal sensível** (origem racial, convicção religiosa, opinião política, saúde, vida sexual, dado genético/biométrico).
- **Princípios**: finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação, responsabilização.
- **Bases legais** (art. 7º/11): consentimento, cumprimento de obrigação legal, execução de contrato, tutela da saúde, legítimo interesse, entre outras.
- **Direitos do titular**: confirmação, acesso, correção, eliminação, portabilidade, informação sobre compartilhamento, revogação do consentimento.
- **Papéis**: **controlador** e **operador**; **encarregado (DPO)**; **ANPD** (autoridade nacional). Segurança e boas práticas; sanções administrativas (advertência, multa até 2% do faturamento, limitada a R$ 50 milhões, bloqueio/eliminação dos dados).

---

# MÓDULO II — PERÍMETRO: FIREWALL, DMZ, WAF, UTM, PROXY, NAC

## 1. Firewall e arranjos

- **Firewall**: elemento de **borda** (princípio do **"choke point"** — ponto único de entrada/saída); permite monitoração, controle, autenticação, logs, alertas, trilhas de auditoria.
- **DMZ (rede de perímetro)**: área de serviços comuns (web, e-mail) acessível a externos e internos; tira os servidores expostos da rede interna. Evolução: **2 firewalls** (defesa em profundidade).
- Arranjos: **dual-homed host** (2 interfaces); **screened host** (firewall + **bastion host** — mínimo de serviços); **screened-subnet/DMZ** (subrede com dois firewalls); "hybrid host" (agrupa características).
- Conceitos: filtros; **proxies** (intermediário: duas conexões — cliente-proxy-servidor); **bastion hosts**; **honeypot** (servidor-iscas); **NAT** (segurança por obscuridade); **VPN** (túnel terminando no firewall). *Pegadinha*: firewall **nativamente não é antivírus nem antispam** (só em UTM/deep inspection).
- **Classificação por camada**: **bridge** (L2, **sem IP**); **filtro de pacotes estático** (L3/L4: IP/portas); **stateful** (tabela de estados; abre/fecha portas conforme a conexão TCP); **proxy** (L7; SQUID; filtra por URL); **proxy reverso** (proteção/balanceamento/cache no lado servidor); **deep inspection** (inspeção de conteúdo).

## 2. WAF, UTM, Proxy e NAC

- **WAF (Web Application Firewall)**: camada 7, protege o **servidor de aplicações web** (não a rede nem os usuários); posiciona-se à frente da aplicação; analisa fluxo **após decriptação**; appliance ou software. *Dado*: 70% do orçamento vai para tráfego de rede, mas 70% dos ataques ocorrem na **camada de aplicação**.
- **UTM**: appliance único agregando firewall, IDS/IPS, antivírus, antimalware, segurança wireless, VPN, relatórios.
- **Proxy**: intermediário (cache, filtragem, anonimato do IP); CONNECT do HTTP.
- **NAC (Network Access Control)** *(complemento)*: controle de acesso à rede por postura (802.1X, verificação de compliance — antivírus/patches — antes de liberar acesso).
- **ICAP** (Internet Content Adaptation Protocol): baseado em HTTP, leve; adaptação de conteúdo (ex.: checar vírus); geralmente na DMZ.
- **Antivírus/antispam**: antivírus (assinaturas, heurística, sandbox — complemento EDR); **antispam**: blacklists/whitelists/**greylists** (só entrega após reenvio legítimo); filtros de conteúdo (**bayesiano** — probabilístico, falsos positivos); **SPF** (valida IPs autorizados por domínio); **DKIM** (assinatura com chaves públicas — verifica cabeçalho **e** conteúdo); gerência da **porta 25**.

## 3. IDS × IPS

- **IDS**: **detecção** ("alarme") — acusa, mas **não bloqueia** (modo passivo: log/alerta; modo reativo: comanda firewall, mas o ataque já ocorreu). Tipos: **NIDS** (rede), **HIDS** (host — trata dados na origem, antes da criptografia), baseado em pilhas, **Hybrid**. Ferramenta: **SNORT** (faz também de IPS).
- **IPS**: IDS **in-line**, **bloqueio ativo e preventivo** (impede o ataque). **IDPS** = híbrido configurável.
- **Metodologias de detecção**: **Base de Conhecimento** (assinaturas/regras — baixos falsos positivos; precisa atualização; associação: IDS) × **Base de Comportamento** (heurística/estatística; detecta ataques novos; muitos falsos positivos; associação: IPS).
- **Falso negativo** (suspeito não detectado) × **falso positivo** (legítimo acusado).

---

# MÓDULO III — WIRELESS, VPN E ZTNA

## 1. Segurança sem fio

- **WEP** (1997): IV de 24 bits, chave 64/128 bits, chaves **estáticas** → **quebrado**. **TKIP**: chaves de 128 bits com IV de 48 bits.
- **WPA**: subconjunto do **802.11i**; chaves dinâmicas; **TKIP + MIC + 802.1X/RADIUS**; versões **Personal** (pré-chave) e **Enterprise** (802.1X por usuário).
- **WPA2**: implementa o **802.11i por completo**; **AES** (em vez de RC4); **4-way handshake**; Personal e Enterprise.
- **WPA3** *(complemento)*: SAE (substitui PSK), proteção em redes abertas (OWE), forward secrecy, 192-bit no modo Enterprise.
- **EAP** (Extensible Authentication Protocol): framework de autenticação — **EAP-TLS** (certificados), **EAP-MD5** (usuário/senha), **EAP-TTLS/PEAP** (usuário+senha+certificados), **EAP-LEAP** (Cisco). Usado no **802.1X**: **suplicante, authenticator, servidor de autenticação (RADIUS)**; encapsulamento **EAPOL**.

## 2. VPN e ZTNA

- **VPN**: **túnel seguro** com criptografia sobre rede pública; autenticação; confidencialidade, autenticidade, integridade. Cenários: **site-to-site**, **acesso remoto**, **extranet**. NAT entre pontos: **NAT Traversal/UDP Encapsulation**.
- Protocolos: **PPTP** (leve, 128 bits — **não considerado seguro**); **L2TP** (**sem criptografia própria** — usa IPSec; porta 1701); **OpenVPN** (open source, SSL/TLS, UDP/TCP 443); **SSTP** (Microsoft, TCP 443); **IPSec** (L3; UDP/500 IKE; protocolos IP 50 ESP e 51 AH); **MPLS VPN** (**só isola, NÃO criptografa**).
- **VPN-SSL/TLS**: túnel via TLS (OpenVPN, SSTP) — mais atravessa firewalls (443).
- **ZTNA (Zero Trust Network Access)** *(complemento)*: "**nunca confie, sempre verifique**" — acesso por identidade/contexto a recursos específicos (não à rede inteira como na VPN); microsegmentação, MFA, verificação contínua. Substitui gradualmente o modelo de perímetro/trusted network.

---

# MÓDULO IV — ATAQUES, AMEAÇAS E CÓDIGOS MALICIOSOS

## 1. Ataques

- **Scan/varredura** (NMAP: `nmap -sS 192.168.0.0/24 -p 1-150`); **spoofing** (e-mail, IP, ARP); **Man in the Middle**; **Smurf** (IP forjado + broadcast); **sniffing** (Wireshark/TCPDump; em claro permite capturar senhas).
- **Força bruta/dicionário**; **defacement** (vandalismo de página — **não** é phishing); **phishing** (página falsa por spam; **spear phishing** = alvo específico); **pharming** (DNS/cache poisoning — desvio sem o usuário perceber); **SPIM**; **engenharia social** (**vishing** = voip; **hoax**; **whaling** = executivos).
- **DoS** (esgota recursos: processamento, sessões, banda, memória) / **DDoS** (coordenado via **botnet/zumbis**; mitigação: banda, baseline, blackholes, CDNs, hardening) / **DRDoS** (refletores — como Smurf, amplificado).
- **Aplicação**: **LFI/LFR**; **XSS** (não persistente × persistente; sequestra sessões; defesa: CSP, sanitização); **CSRF/XSRF** ("cheque em branco assinado"); **SQL/LDAP/XML injection**; **zero-day**; **buffer overflow**; **session hijacking** (ativo = spoofing; passivo = monitora); **APT** (ameaça persistente avançada — 5 fases: reconhecimento, incursão, descoberta, exfiltação, ação).
- **Wireless**: wardriving, rogue AP, bluejacking (mensagens), bluesnarfing (acesso a dados Bluetooth).

## 2. Códigos maliciosos (malware)

- **Vírus** (precisa de **ação do usuário/SO**; tipos: boot/MBR, arquivo, residente, e-mail, script, macro, celular, stealth, **metamórficos/polimórficos**); **worm** (propaga-se **sozinho pela rede**, explora vulnerabilidades); **spyware** (keylogger, screenlogger, adware); **cavalo de Tróia** (aparenta legítimo); **backdoor** (acesso futuro); **rootkit** (esconde presença; escala privilégios); **bot/botnet**; **bomba lógica** (data/evento); **ransomware** (criptografa e exige resgate).
- *Pegadinha*: **vírus precisa de execução**; **worm propaga-se sozinho**.

---

# MÓDULO V — CRIPTOGRAFIA, CERTIFICADOS, HASH E CONTROLE DE ACESSO

## 1. Criptografia simétrica × assimétrica

- **Simétrica**: **mesma chave** cifra/decifra; **mais rápida**, chaves menores; segurança no **segredo da chave**; garante **confidencialidade** (cifra de substituição). Algoritmos: **DES** (56 bits efetivos; 16 rodadas; rede de **Feistel** — expansão, mistura (XOR), substituição (S-boxes = confusão), permutação (P-box = difusão)); **3DES** (168 bits com 3 chaves; 112 com 2); **AES** (blocos 128 bits; chaves 128/192/256; **sem Feistel**; SubBytes, ShiftRows, MixColumns, AddRoundKey); RC4/RC5/RC6, Blowfish, Twofish, IDEA.
- **Assimétrica (chaves públicas)**: par **privada** (exclusiva) × **pública**. **Regra de ouro**: **confidencialidade** → cifra com a **pública do RECEPTOR**; **autenticidade** → cifra com a **privada do EMISSOR**. Algoritmos: **Diffie-Hellman** (**troca de chaves**, não cifra; logaritmo discreto; com curva elíptica → **PFS**); **RSA** (fatoração de primos; 2048–4096 bits; cifragem e assinatura); **El Gamal** (PGP).
- Boas práticas: **comprimir antes de encriptar**; a chave simétrica é trocada por canal assimétrico.

## 2. Hash, assinatura e certificados

- **Funções hash**: **unidirecionais (one-way)**, saída de tamanho fixo (**message digest**). Garantem **integridade** (comparar hash recebido × recalculado) e autenticidade de senhas. Algoritmos: **MD5** (128 bits; **colisões desde 2008**), **SHA-1** (160 bits), **SHA-256/384/512**, SHA-3. Ataque: **rainbow tables** (defesa: salt).
- **Assinatura digital**: garante **integridade + autenticidade** (**NÃO confidencialidade** — mensagem vai em claro): hash → cifra com a **privada do EMISSOR** → destinatário decifra com a **pública do emissor** e compara. **Atemporal × temporal** (timestamp).
- **Certificado digital** (X.509): **AC (CA)** = "cartório"; conteúdo: chave pública, identidade, validade, assinatura da AC, cadeia. **PKI/ICP-Brasil**: AC, **AR (Registradora)**, **CRL** (revogados). Modelo completo: chave de **sessão simétrica** cifrada com a **pública do destinatário** + assinatura digital do emissor.
- **TLS 1.2/1.3 × SSL** *(complemento)*: TLS sucessor do SSL (IETF). **SSL e TLS NÃO interoperam**; TLS usa HMAC; OpenSSL suporta ambos. **TLS 1.2** (PRF, AES-GCM, SNI); **TLS 1.3** (handshake em 1-RTT, só AEAD, **sem RSA key-exchange** — só (EC)DHE (PFS), 0-RTT opcional). **Limitações do SSL**: obsoleto (SSLv3 vulnerável a POODLE), sem interoperar com TLS, chaves mais fracas; **não usar SSL** — usar TLS 1.2/1.3.
- **IPSec**: camada de rede; **AH** (autenticidade+integridade de cabeçalho+dados, **sem confidencialidade**) × **ESP** (confidencialidade+integridade+autenticidade **só dos dados**). Modos transporte × túnel. **IKE**: Main Mode × Aggressive Mode (identidades em claro); Quick Mode.

## 3. Controle de acesso, RBAC e MFA

- **AAA** = **Authentication, Authorization, Accounting** (auditoria). **Três fatores**: **sabe** (senha), **tem** (token, smart card), **é** (biometria — universalidade, singularidade, permanência, mensurabilidade).
- **MFA (autenticação multifator)** *(complemento)*: exige **2+ fatores independentes** (ex.: senha + token) — prevenção OWASP de quebra de autenticação. **2FA** = caso particular de 2 fatores.
- **RBAC (Role-Based Access Control)** *(complemento)*: acesso por **papéis/perfis** (permissões atribuídas ao papel; usuário herda do papel) — administrável, prático para grandes organizações. Outros modelos: DAC (discretionário), MAC (obrigatório), ABAC (atributos).
- **Controle de acesso**: físico (cancela, biometria, chave de rack) × lógico (login/senha, restrição por IP). **Procedimentos seguros de log-on** (ver ISO 27002).

---

# MÓDULO VI — OWASP

- **OWASP** (Open Web Application Security Project): princípios e ferramentas de segurança de aplicações — **ESAPI** (biblioteca de controles), **ZAP** (scanner/proxy de testes), projetos SAST.
- **Teste de penetração**: avaliação simulando ataque (análise ativa de vulnerabilidades).
- **OWASP Top 10** — base 2017: **Injeção** (SQL/NoSQL/OS/LDAP; parametrizar, validar no servidor); **Quebra de Autenticação** (MFA, sem credenciais padrão); **Exposição de Dados Sensíveis** (criptografia em repouso/trânsito); **XXE**; **Controle de Acesso Quebrado** (verificar direitos no servidor a cada chamada); **Configuração Incorreta de Segurança**; **XSS**; **Desserialização Insegura** (RCE); **Componentes Vulneráveis Conhecidos**; **Logging e Monitoração Insuficientes** (tempo médio de detecção de violação: **200 dias**).
- **OWASP Top 10:2025** *(complemento — edital exige a versão 2025)*: reorganização com ênfase em **Broken Access Control** (mantido no topo), **Cryptographic Failures**, **Injection** (inclui SQL/XSS/SSRF modernos), **Insecure Design**, **Security Misconfiguration**, **Vulnerable and Outdated Components**, **Identification and Authentication Failures**, **Software and Data Integrity Failures**, **Security Logging and Monitoring Failures**, **Server-Side Request Forgery (SSRF)** — verifique a versão oficial da banca; os conceitos centrais (injeção, acesso, criptografia, configuração, componentes, logs) são estáveis.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **ISO 27001** = requisitos do SGSI (**itens 4–10 obrigatórios**; PDCA); **27002** = controles (**14 seções/114 controles** na 2013; **93 controles/4 temas** na 2022).
2. **Firewall não é antivírus/antispam nativamente**; **WAF protege o servidor de aplicação**, não a rede.
3. **IDS detecta (alarme), não bloqueia**; **IPS bloqueia (in-line)**. IDS≈assinaturas; IPS≈comportamento.
4. **Falso negativo** = suspeito não detectado; **falso positivo** = legítimo acusado.
5. **SSL e TLS não interoperam**; use **TLS 1.2/1.3** (SSL obsoleto). TLS 1.3: 1-RTT, sem RSA key-exchange, PFS.
6. **AH não cifra** (autenticidade/integridade); **ESP** não cobre cabeçalho IP. **MPLS VPN não criptografa**; **PPTP não é seguro**.
7. **Assinatura digital**: hash + **privada do EMISSOR** (integridade/autenticidade, **NÃO confidencialidade**). Confidencialidade: **público do RECEPTOR**.
8. **DES = 56 bits**; 3DES = 168 (3 chaves) ou 112 (2); WEP = 64/128 com IV de 24; MD5 = 128 bits (colisões).
9. **Hash é unidirecional** (não reverte); criptografia é bidirecional.
10. **WEP quebrado**; WPA = subconjunto 802.11i (TKIP); **WPA2 = AES/802.11i completo**; **WPA3 = SAE**.
11. **Vírus precisa de execução**; **worm propaga-se sozinho**. **Ransomware** criptografa e cobra resgate.
12. **Phishing** = página falsa; **pharming** = DNS poisoning; **defacement** = vandalismo.
13. **DoS** ataca **disponibilidade**; **DRDoS** usa refletores; **DDoS** = botnet.
14. **AAA** = autenticação/autorização/**contabilização** (auditoria). **MFA** = 2+ fatores; **RBAC** = papéis.
15. **802.1X**: suplicante/authenticator/servidor (RADIUS); **EAP-TLS** usa certificados.
16. **LGPD**: controlador/operador, **encarregado (DPO)**, **ANPD**; dado sensível ≠ dado comum; sanções até 2%/R$ 50 mi.
17. **ZTNA** = "nunca confie, sempre verifique" (acesso por identidade, não à rede inteira).
18. **WPA3/OWASP 2025/ISO 27001:2024/27701:2026/ZTNA/TLS 1.3** = complementos (base local: 2020).

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O firewall, por si só, já oferece proteção contra vírus e spam, dispensando soluções dedicadas de antivírus e antispam.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Firewall **nativamente não é** antivírus/antispam (só em appliances UTM ou via deep inspection).

---

**Questão 2.** (FCC-style) O IDS caracteriza-se por:
a) bloquear ativamente o ataque em linha (in-line).
b) detectar e alertar ("alarme"), sem bloquear o tráfego.
c) substituir o firewall.
d) criptografar o tráfego.
e) gerenciar certificados.

> **Resposta: b.** **IDS** detecta/alerta (**não** bloqueia). **IPS** é in-line e **bloqueia** preventivamente.

---

**Questão 3.** (CESPE-style) Na assinatura digital, o remetente cifra o hash da mensagem com sua chave pública, garantindo confidencialidade do conteúdo.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Cifra-se o hash com a **privada do EMISSOR** (garante integridade/autenticidade, **NÃO confidencialidade** — a mensagem vai em claro). Confidencialidade: cifrar com a **pública do receptor**.

---

**Questão 4.** (FCC-style) O algoritmo simétrico adotado como padrão pelo governo dos EUA, que substituiu o DES e utiliza blocos de 128 bits com chaves de 128, 192 ou 256 bits, é:
a) RSA.
b) AES.
c) Diffie-Hellman.
d) MD5.
e) El Gamal.

> **Resposta: b.** **AES** (sem Feistel; SubBytes/ShiftRows/MixColumns/AddRoundKey). RSA/Diffie-Hellman/El Gamal são **assimétricos**; MD5 é **hash**.

---

**Questão 5.** (CESPE-style) A função hash garante confidencialidade da mensagem, pois permite recuperar o conteúdo original a partir do digest.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Hash é **unidirecional** (não reverte) e garante **integridade**, não confidencialidade.

---

**Questão 6.** (FCC-style) O protocolo WPA2, em relação ao WEP, avança por:
a) usar IV de 24 bits.
b) adotar AES e completar o padrão IEEE 802.11i (4-way handshake).
c) manter chaves estáticas.
d) dispensar autenticação.
e) usar RC4.

> **Resposta: b.** **WPA2** = **AES** + **802.11i completo** + 4-way handshake (WEP: RC4, IV 24 bits, chaves estáticas, quebrado).

---

**Questão 7.** (CESPE-style) O worm difere do vírus por propagar-se automaticamente pela rede, explorando vulnerabilidades, sem exigir ação do usuário.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Worm** propaga-se **sozinho**; **vírus** precisa de **execução** (ação do usuário/SO).

---

**Questão 8.** (FCC-style) O WAF (Web Application Firewall) tem como principal função:
a) proteger a rede inteira contra ataques de rede.
b) proteger o servidor de aplicações web (camada 7), analisando o fluxo após decriptação.
c) substituir o IDS.
d) gerenciar endereços IP.
e) criptografar e-mails.

> **Resposta: b.** **WAF** = L7, protege o **servidor web/aplicação** (não a rede nem os usuários internos).

---

**Questão 9.** (CESPE-style) No IPSec, o cabeçalho AH (Authentication Header) oferece confidencialidade dos dados, cifrando o conteúdo do pacote.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **AH** dá autenticidade+integridade (cabeçalho+dados), **sem confidencialidade** (não cifra). Quem cifra é o **ESP** (só dados).

---

**Questão 10.** (FCC-style) O certificado digital no padrão X.509 é emitido por:
a) o próprio usuário.
b) uma Autoridade Certificadora (AC), terceira parte confiável.
c) o fabricante do hardware.
d) o ISP.
e) o firewall.

> **Resposta: b.** **AC (CA)** = "cartório" que emite/atesta certificados (chave pública, identidade, validade, assinatura da AC). **PKI/ICP-Brasil**: AC, AR, CRL.

---

**Questão 11.** (CESPE-style) O TLS e o SSL interoperam naturalmente, sendo o TLS apenas uma versão mais recente do SSL.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **SSL e TLS NÃO interoperam**. TLS é sucessor (IETF) do SSL 3.0, com HMAC e autoridades intermediárias. Use **TLS 1.2/1.3**; SSL está obsoleto.

---

**Questão 12.** (FGV-style) Sobre controle de acesso e autenticação, é correto afirmar:
a) MFA exige apenas um fator de autenticação.
b) RBAC atribui permissões a papéis, aos quais os usuários são vinculados.
c) biometria é um exemplo de fator "algo que você tem".
d) AAA não inclui auditoria.
e) 2FA e MFA são conceitos opostos.

> **Resposta: b.** **RBAC** = permissões por **papéis**. **MFA** = 2+ fatores; **2FA** é caso de 2 fatores. Biometria = "**algo que você é**". **AAA** inclui **contabilização/auditoria**.

---

**Questão 13.** (CESPE-style) A LGPD aplica-se apenas a dados sensíveis, como saúde e biometria, não alcançando dados pessoais comuns como nome e endereço.
a) Certo. b) Errado.

> **Resposta: b (Errado).** A LGPD alcança **dado pessoal** (nome, endereço...) **e** **dado sensível** (saúde, biometria, origem racial...), com regimes distintos (sensível tem bases legais mais restritas).

---

**Questão 14.** (FCC-style) O ataque DoS tem por objetivo comprometer:
a) a confidencialidade dos dados.
b) a disponibilidade do serviço, esgotando recursos.
c) a integridade do banco.
d) a autenticidade do usuário.
e) a criptografia.

> **Resposta: b.** **DoS/DDoS** atacam a **disponibilidade** (processamento, sessões, banda, memória). DDoS usa **botnet**; DRDoS usa refletores.

---

**Questão 15.** (CESPE-style) O ZTNA (Zero Trust Network Access) baseia-se no princípio "nunca confie, sempre verifique", concedendo acesso contextual a recursos específicos, em contraste com o acesso amplo da VPN tradicional.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **ZTNA** = Zero Trust (identidade/contexto, microsegmentação, MFA, verificação contínua) — acesso a **recursos**, não à rede inteira (como a VPN).

---

## Questões discursivas

**D1.** Diferencie criptografia simétrica, assimétrica e funções hash, explicando o papel da assinatura digital e dos certificados.

> **Modelo de resposta:** A **criptografia simétrica** usa a mesma chave para cifrar e decifrar (rápida; ex.: AES, DES) — garante confidencialidade, mas exige troca segura de chave. A **assimétrica** usa um par público/privado (ex.: RSA, Diffie-Hellman) — para confidencialidade cifra-se com a **pública do receptor**; para autenticidade, com a **privada do emissor**. As **funções hash** são unidirecionais (MD5, SHA) e garantem **integridade** (digest). A **assinatura digital** combina hash + cifra com a privada do emissor (integridade e autenticidade, sem confidencialidade). Os **certificados X.509**, emitidos por uma **Autoridade Certificadora** confiável, vinculam identidade à chave pública, formando a PKI.

**D2.** Explique a diferença entre IDS e IPS, as funções do firewall, do WAF e do UTM e os princípios da LGPD.

> **Modelo de resposta:** O **IDS** detecta e alerta sobre tráfego suspeito ("alarme"), sem bloquear (base de conhecimento/assinaturas); o **IPS** fica in-line e bloqueia preventivamente (base de comportamento). O **firewall** controla o perímetro (choke point; filtros, stateful, proxy, DMZ), mas não é antivírus nativamente; o **WAF** protege o servidor de aplicações web (camada 7, após decriptação); o **UTM** agrega firewall, IDS/IPS, antivírus, VPN e antispam em um appliance. A **LGPD** rege o tratamento de dados pessoais e sensíveis por princípios (finalidade, necessidade, segurança, transparência, responsabilização), com papéis de controlador/operador, encarregado (DPO), direitos do titular, atuação da ANPD e sanções administrativas.

---

*Base: `10.Segurança da Informação e Armazenamento de Dados` (Aulas 00–05: controle de acesso, firewall/IDS/IPS, SSL/TLS/IPSec/VPN, ataques/malware, criptografia, assinatura/certificados; Aulas 11–12: ISO 27001/27002/27005), `02.Redes de Computadores` (Aula04: WEP/WPA/WPA2/802.1X; Aula08: TLS/HTTP2), `04.Desenvolvimento de Software` (Aulas 13–14: 2FA/OWASP). Complemento: LGPD, ISO 27001:2024/27002:2022/27701:2026, OWASP Top 10:2025, WPA3, ZTNA, TLS 1.3, NAC, RBAC/MFA — exigidos pelo edital e ausentes ou incompletos na base de 2020.*