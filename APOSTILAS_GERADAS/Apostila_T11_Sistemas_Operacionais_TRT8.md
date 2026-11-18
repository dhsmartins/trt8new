# APOSTILA — TÓPICO 11: SISTEMAS OPERACIONAIS
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Gerenciamento de processos e fluxos de execução (threads): alocação de CPU, comunicação e sincronização entre processos, impasses (deadlocks) e esgotamento de recursos (starvation); Gerenciamento de memória: alocação, segmentação, memória virtual e paginação; Sistemas de entrada e saída; ambiente Linux (Red Hat e Oracle Linux); utilitários e comandos padrão; Microsoft Windows (Windows 11; Windows 10 legado; Windows Server 2019, 2022 e 2025); Active Directory; Powershell; WSUS.
>
> **Base de conhecimento:** `01.Sistemas Operacionais e Arquitetura` (Aulas 04–10, 12–15 — Curso Regular TI 2020.2) + **complemento** (Windows 11/Server 2019–2025, WSUS, orçamento de recursos).

---

# MÓDULO I — PROCESSOS E THREADS

## 1. Processos

- **Processo** = programa em execução (com registradores PC/IR e variáveis). **Multiprogramação/pseudoparalelismo** com 1 CPU; **troca de contexto (chaveamento)** = salvar/restaurar estado da CPU.
- **Criação**: inicialização do sistema, `fork()` (Linux), pedido do usuário, tarefa em lote. **Daemons** = background; no Linux, pai dos daemons é o **init (PID=1)**.
- **PCB (Bloco de Controle do Processo)**: PID, registradores, espaço de endereçamento, prioridade — em área **protegida do kernel**. A **Tabela de Processos** localiza o PCB.
- **Estados**: executando, pronto, bloqueado (4 transições). **CPU-bound** (pouco bloqueia) × **I/O-bound** (bloqueia seguidamente; ex.: chat).

## 2. Threads

- **Threads** (processos leves): múltiplos fluxos no **mesmo processo** compartilham código/dados. **Nível de usuário** (escalona no espaço do usuário) × **nível de kernel** (tabelas no kernel).

## 3. Comunicação e sincronização

- **Pipes** (`ls | grep x | sort -r`). **Condições de corrida** em armazenamento compartilhado (ex.: spooler de impressão). **Seção crítica** com **exclusão mútua** — 4 condições de boa solução: (1) só 1 processo por vez na seção; (2) sem suposição sobre velocidade/nº de CPUs; (3) processo fora da seção não bloqueia outros; (4) ninguém espera eternamente.
- **Semáforo**: inteiro verificado/alterado **atomicamente**; operações **down/sleep** (decrementa se >0; se 0, bloqueia) e **up/wakeup** (incrementa). **Mutex**: semáforo simplificado livre/ocupado.

## 4. Deadlock × Starvation

| Deadlock (impasse) | Starvation (inanição) |
|---|---|
| Conjunto de processos presos mutuamente, cada um com um recurso que outro precisa | Processo de baixa prioridade **nunca** é atendido ("sempre alguém fura a fila") |
| 4 condições simultâneas: **exclusão mútua, espera por recurso, não-preempção, espera circular** | Típico de sistemas com **prioridades**, sobretudo **não preemptivos** |
| **Ninguém** progride (bloqueio circular) | Os demais progridem; só o "esquecido" não |
| Ex.: thread 1 segura teclado e espera impressora; thread 2 segura impressora e espera teclado | Ex.: prioridade mínima disputando CPU com chegadas de prioridade maior |

## 5. Escalonamento de CPU

- **Preempção** = SO retira a CPU via interrupção de relógio. Ocorre **obrigatoriamente** quando o processo termina ou é bloqueado (E/S ou semáforo).
- **Lote**: não-preemptivo ou quanta longos — **FCFS**, **SJF**, **SRT** (versão preemptiva do SJF). **Interativo**: preempção fundamental — **round-robin** com quantum (ex.: chaveamento 1 ms + quantum 9 ms = 10% de sobrecarga); **prioridade**; múltiplas filas (1/2/4/8 quanta); garantido (1/N da CPU); sorteio ("bilhetes de loteria"). **Tempo real**: preempção pode ser desnecessária.

---

# MÓDULO II — GERÊNCIA DE MEMÓRIA

## 1. Alocação e swapping

- **Memory leak**: blocos alocados sem ponteiro acessível, ou dados mortos ainda referenciados.
- **Partições fixas (MFT)**: 1 processo por partição; desperdício interno. **Swapping**: processo inteiro vai/vem do disco; fragmentos exigem **compactação** (custosa). Gerenciamento por **mapa de bits** (lento procurar N bits 0) e **listas encadeadas** (P/L: início, fim, ponteiro).
- **Alocação (first-fit/next-fit/best-fit/quick-fit)**: first-fit (rápido), next-fit (retoma da última posição), best-fit (varre tudo; sobram espaços minúsculos), quick-fit (listas por tamanho; fusão cara).

## 2. Memória virtual, paginação e segmentação

- **Memória virtual**: programa+dados+pilha podem exceder a RAM; SO mantém em RAM só o que está em uso (evolução dos overlays).
- **Segmentação**: segmentos de tamanhos **variáveis** conforme a lógica do programa; endereço = nº do segmento + deslocamento; **fragmentação externa**.
- **Paginação** (maioria dos sistemas): **MMU** mapeia endereços virtuais em físicos; espaço virtual em **páginas** (= tamanho dos **quadros/page frames** físicos; ex.: 4 KB); **page fault** dispara interrupção, SO remove quadro menos usado e traz a página; **fragmentação interna** (última página parcialmente usada).

| Paginação | Segmentação |
|---|---|
| Unidades **fixas** (páginas/quadros) | Unidades **variáveis** (lógica do programa) |
| Fragmentação **interna** | Fragmentação **externa** |
| **Transparente** ao programador | **Visível** ao programador |
| Base da memória virtual moderna | Proteção por segmento |

- **Substituição de página**: **ótimo** (remove a de maior rótulo futuro — **não realizável**); **NRU** (bits R e M; classes 0–3); **LRU** (menos usada; custo alto); **FIFO**; **segunda chance** (FIFO com bit R); **relógio** (lista circular com ponteiro).

---

# MÓDULO III — E/S E ARMAZENAMENTO

- **DAS** (direto ao servidor), **NAS** (rede, opera com **arquivos**), **SAN** (rede de alta disponibilidade para discos/fitas, opera com **blocos**). **JBOD**: discos concatenados vistos como um volume — **não é RAID**.

| RAID | Ideia | Mín. discos | Tolerância | Uso útil (ex. 4×1 TB) |
|---|---|---|---|---|
| **0** | Striping | 2 | **Nenhuma** | 4 TB (100%) |
| **1** | Mirror | 2 | 1 falha (metade) | 2 TB (50%) |
| **4** | Paridade em **1 disco fixo** | 3 | 1 falha | 3 TB |
| **5** | Paridade **distribuída** | 3 | 1 falha | 3 TB (75%) |
| **6** | Dupla paridade | 4 | **2 falhas** | 2 TB (50%) |
| **10** | RAID-1 interno + RAID-0 externo | **4** | 1 falha por espelho | 2 TB |

- **Backup**: deduplicação, **snapshot**, tipos de backup. **Sistemas de arquivos**: FAT/exFAT/**NTFS (necessário ao AD)**/EXT/HFS+. **Data center**: "noves" de disponibilidade (5 noves = 99,999%, ~5 min/ano).

---

# MÓDULO IV — LINUX (RED HAT / ORACLE LINUX)

- SO **interativo, multitarefa, multiusuário**; root (home `/root`); usuários em `/home/nome`. Instalação por mídia bootável ou rede (**PXE/TFTP+DHCP**). Boot: **LILO** e **GRUB**.
- **Kernel monolítico** (Unix/Linux); módulos carregados sob demanda (`/lib/modules/versão`, `uname -a`). Shells: sh, **bash**, csh, ksh, zsh. Janelas: Gnome, KDE.
- **Foreground/background**: `&` executa em background; **CTRL+Z** suspende, `bg` manda para background, `jobs` lista, `fg %n` traz de volta. Daemons (terminados em "d": syslogd).
- **Cron/Crontab**: campos `minuto hora dia_do_mês mês dia_da_semana comando` (ex. `0 22 * * 1-5`); **Anacron** (executa pendências após desligamento; não é daemon; granularidade ≥ dia); **Fcron** combina ambos.
- Utilitários/comandos padrão (complementar ao material): `ls, cd, pwd, cp, mv, rm, mkdir, grep, find, chmod, chown, ps, top, df, du, tar, ssh, systemctl` (Red Hat/Oracle Linux: serviços via systemd; pacotes via `yum`/`dnf`).
- Serviços de rede em Linux: DNS (arquivos de zona; 127.0.0.1 localhost), DHCP, FTP, e-mail.

---

# MÓDULO V — WINDOWS, ACTIVE DIRECTORY, POWERSHELL E WSUS

## 1. Windows 11 / Windows 10 (legado) / Windows Server 2019, 2022 e 2025 *(complemento)*

- **Windows 10 legado** × **Windows 11** (requisitos de hardware mais restritos: TPM 2.0, Secure Boot; interface renovada). **Windows Server 2019** (hybrid com Azure, Windows Admin Center), **2022** (segurança: Secured-core, TLS 1.3, SMB AES-256), **2025** (novo — complementar à base de 2020).
- Instalação/configuração: periféricos, programas, **Windows Update**, acessórios; rede: DHCP, DNS (subdomínios/FQDN).

## 2. PowerShell

- Shell CLI com prompt interativo e ambiente de **scripts** para administração e automação; usa **cmdlets** (diferem de comandos de shell tradicionais); versões 1.0 (2006) a 3.0 (nativo no Server 2012/Windows 8) — atualmente 5.1 e **PowerShell 7** (cross-platform). Sessões remotas por cmdlet.

## 3. Active Directory (AD)

- **LDAP**: protocolo de acesso a objetos de diretório (**não** é o diretório em si); porta **389/TCP**. **AD** (Windows 2000+): serviço de diretórios (contas, grupos, políticas) em **BD replicado**; **exige NTFS**. **Workgroup** (independente, ≤~10 usuários) × **domínio** (base única replicada).
- **DC** (controlador de domínio: autentica, emite token) × servidor membro; promoção via **DCPROMO.EXE** (antigo) ou Gerenciador do Servidor + PowerShell (2012+). **OUs** (facultativas), partições (esquema, configuração, domínio), árvores, floresta, **Catálogo Global** (cópia completa do seu domínio + parcial dos demais), relações de confiança (transitivas; bidirecionais pai-filho; unidirecionais).
- Serviços: **AD CS** (certificados), **AD DS** (domínios), **AD FS** (federação), **AD LDS**, **AD RMS**. Arquivos: **Ntds.dit** (todos os dados), Edb.chk, Edb.log, Res1/Res2.log, Schema.ini.

## 4. WSUS *(complemento — ausente na base)*

- **WSUS (Windows Server Update Services)**: servidor Microsoft para **gerenciar e distribuir atualizações** do Windows/Microsoft em uma rede corporativa — aprovadores testam pacotes antes de liberar aos clientes (economia de banda; conformidade de patching). Integrado ao ecossistema AD/GPO.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **PCB** fica em memória **protegida**; **Tabela de Processos** localiza o PCB; **init é PID=1**.
2. **Semáforo**: DOWN com 0 **bloqueia**; UP soma 1; operação **atômica**.
3. **Deadlock** = 4 condições simultâneas; **starvation** = prioridades/sobretudo **não preemptivas**.
4. **Página = virtual; quadro = físico**. Algoritmo **ótimo é não realizável**.
5. **Paginação** = fragmentação **interna**; **segmentação** = **externa**.
6. **RAID-0 não tem redundância**; **JBOD não é RAID**; **RAID-10 exige mín. 4**; RAID-5 paridade **distribuída** (≠ RAID-4, disco fixo).
7. **NAS** opera com **arquivos**; **SAN** opera com **blocos**.
8. **NTFS** é exigido pelo **Active Directory**.
9. **LDAP = protocolo** (389), não é o diretório.
10. **Anacron** não é daemon e granularidade ≥ dia; **Cron** precisa de máquina ligada.
11. `CTRL+Z` suspende; `bg`/`fg` alternam jobs; `&` inicia em background.
12. **PowerShell** usa **cmdlets** (não comandos de shell tradicionais).
13. **SRT** = versão **preemptiva** do SJF.
14. **5 noves** = 99,999% (~5 min/ano).
15. **WSUS** = distribuição de atualizações Windows (complemento — não está na base de 2020).
16. **Ntds.dit** = arquivo de dados do AD.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) O Bloco de Controle do Processo (PCB) é armazenado na área de memória do usuário, sendo acessível ao próprio processo para auto-regulação.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O PCB fica em área **protegida do kernel**; a **Tabela de Processos** localiza-o. O processo não tem acesso direto.

---

**Questão 2.** (FCC-style) As quatro condições necessárias para a ocorrência de deadlock são:
a) exclusão mútua, espera por recurso, não-preempção e espera circular.
b) prioridade, preempção, fila e quantum.
c) fragmentação interna, externa, swapping e compactação.
d) page fault, thrashing, aging e starvation.
e) semáforo, mutex, monitor e lock.

> **Resposta: a.** Exclusão mútua + espera por recurso + **não-preempção** + espera circular. (Ex.: teclado/impresso­ra entre duas threads.)

---

**Questão 3.** (CESPE-style) O starvation ocorre quando um processo de baixa prioridade nunca é atendido, sendo mais provável em sistemas com política de escalonamento preemptiva.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Starvation é mais provável em políticas **não preemptivas** (com prioridades) — a preempção permite que o processo de baixa prioridade eventualmente rode.

---

**Questão 4.** (FCC-style) No gerenciamento de memória, a unidade lógica do espaço virtual e a unidade física da memória real são, respectivamente:
a) página e quadro (page frame).
b) quadro e página.
c) segmento e página.
d) byte e word.
e) bloco e cluster.

> **Resposta: a.** **Página** = virtual; **quadro** = físico. A MMU faz o mapeamento.

---

**Questão 5.** (CESPE-style) A segmentação de memória utiliza unidades de tamanho fixo, gerando fragmentação interna, e é totalmente transparente ao programador.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **Segmentação** = unidades **variáveis** (lógica do programa), **fragmentação externa**, **visível** ao programador. O descrito é a **paginação**.

---

**Questão 6.** (FCC-style) O algoritmo ótimo de substituição de páginas é amplamente adotado por sistemas operacionais modernos por sua eficiência comprovada.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O ótimo exige conhecer o **futuro** de uso das páginas — é **não realizável** (serve como referência teórica). Na prática: LRU, FIFO, segunda chance, relógio.

---

**Questão 7.** (CESPE-style) O RAID 0 oferece tolerância a falhas graças à redundância de dados entre os discos do conjunto.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **RAID-0** só faz **striping** — **sem redundância**. Tolerância: RAID-1 (mirror), 5 (paridade), 6 (dupla), 10.

---

**Questão 8.** (FCC-style) A diferença entre NAS e SAN é que:
a) NAS opera com blocos; SAN opera com arquivos.
b) NAS opera com arquivos (rede); SAN opera com blocos (alta disponibilidade).
c) ambos são sinônimos de DAS.
d) SAN não suporta fitas.
e) NAS exige Fibre Channel.

> **Resposta: b.** **NAS** = arquivos (compartilhamento); **SAN** = blocos (discos/fitas, HA). **DAS** é direto ao servidor.

---

**Questão 9.** (CESPE-style) No Linux, o comando `jobs` lista os processos em background; `fg %n` traz um deles para o foreground; `CTRL+Z` suspende o processo atual.
a) Certo. b) Errado.

> **Resposta: a (Certo).** `&` inicia em background; `CTRL+Z` suspende; `bg`/`fg %n` alternam; `jobs` lista.

---

**Questão 10.** (FCC-style) O Anacron difere do Cron principalmente porque:
a) é um daemon que roda continuamente.
b) executa tarefas pendentes após desligamentos, com granularidade mínima de um dia.
c) exige máquina ligada permanentemente.
d) usa apenas unidades de segundos.
e) substitui o GRUB.

> **Resposta: b.** **Anacron** não é daemon, granularidade ≥ **dia**, cobre tarefas perdidas quando a máquina estava desligada. **Cron** exige máquina ligada no horário.

---

**Questão 11.** (CESPE-style) O Active Directory pode ser instalado em sistemas de arquivos FAT32, desde que configurado em modo de compatibilidade.
a) Certo. b) Errado.

> **Resposta: b (Errado).** O AD **exige NTFS** (recursos de segurança e do arquivo Ntds.dit).

---

**Questão 12.** (FGV-style) Sobre o LDAP, é correto afirmar:
a) é o próprio diretório de objetos da Microsoft.
b) é protocolo de acesso a diretórios (porta 389), baseado no X.500.
c) é um servidor de aplicação JEE.
d) substitui o DNS em redes corporativas.
e) opera exclusivamente com Windows.

> **Resposta: b.** **LDAP = protocolo** (389/TCP, padrão aberto baseado no X.500) — o AD **usa** LDAP; não é sinônimo de diretório.

---

**Questão 13.** (CESPE-style) A política de escalonamento SRT (Shortest Remaining Time) é a versão não preemptiva do algoritmo SJF.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **SRT** é a versão **preemptiva** do SJF (se chegar processo com tempo restante menor, preempção ocorre).

---

**Questão 14.** (FCC-style) O RAID 5 caracteriza-se por:
a) paridade em um disco fixo dedicado (mínimo 3 discos).
b) dupla paridade, tolerando duas falhas simultâneas.
c) paridade distribuída entre os discos, tolerando uma falha (mínimo 3 discos).
d) espelhamento puro com 50% de aproveitamento.
e) striping sem redundância.

> **Resposta: c.** **RAID-5**: paridade **distribuída**, mín. 3 discos, tolera **1** falha. (RAID-4 = disco fixo; RAID-6 = dupla.)

---

**Questão 15.** (CESPE-style) O WSUS (Windows Server Update Services) é o serviço do Active Directory responsável pela autenticação de usuários via Kerberos.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **WSUS** distribui e gerencia **atualizações** do Windows. Autenticação Kerberos é papel do **AD DS/KDC**.

---

## Questões discursivas

**D1.** Diferencie deadlock de starvation e relacione-os com o escalonamento de CPU.

> **Modelo de resposta:** **Deadlock** é o impasse em que um conjunto de processos fica preso mutuamente — cada um segura um recurso que outro precisa — exigindo quatro condições simultâneas (exclusão mútua, espera por recurso, não-preempção e espera circular); ninguém progride. **Starvation** ocorre quando um processo de baixa prioridade nunca é atendido, pois outros de prioridade maior chegam continuamente; é mais provável em políticas **não preemptivas** com prioridades. No deadlock todos param; no starvation, os demais progridem e apenas o "esquecido" fica.

**D2.** Explique memória virtual, paginação e segmentação, incluindo os tipos de fragmentação gerados.

> **Modelo de resposta:** A **memória virtual** permite que o programa exceda a RAM física, mantendo em RAM apenas as partes em uso (transferências por página). Na **paginação**, o espaço virtual é dividido em **páginas** (tamanho fixo = quadros físicos), mapeadas pela MMU; gera **fragmentação interna** (última página parcialmente usada) e é transparente ao programador. Na **segmentação**, as unidades (segmentos) têm tamanhos **variáveis** conforme a lógica do programa; gera **fragmentação externa** e é visível ao programador, permitindo proteção por segmento.

---

*Base: `01.Sistemas Operacionais e Arquitetura` (Aulas 04 — processos/threads/deadlock/escalonamento; 05 — memória; 06 e 12 — sistemas de arquivos/backup; 07–10 — Windows/PowerShell/AD/Linux/Cron; 13 — RAID/E-S; 14 — data center) do material local (2020). Complemento: Windows 11 e Windows Server 2019/2022/2025, WSUS e utilitários atuais (systemctl/dnf) — ausentes da base de 2020.*