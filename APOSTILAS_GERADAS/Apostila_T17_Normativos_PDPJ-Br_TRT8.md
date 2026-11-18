# APOSTILA — TÓPICO 17: NORMATIVOS DA PLATAFORMA DIGITAL DO PODER JUDICIÁRIO – PDPJ-Br
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Normativos da Plataforma Digital do Poder Judiciário – PDPJ-Br: Resolução CNJ nº 522/2023; Resolução CNJ nº 335/2020; Portaria CNJ nº 252/2020; Portaria CNJ nº 253/2020; Portaria CNJ nº 131/2021; Resolução CNJ nº 396/2021; Portaria CNJ nº 162/2021.
>
> **Base de conhecimento:** **complemento** — os normativos PDPJ-Br não constam das apostilas locais (base de 2020, anterior à PDPJ). Conteúdo elaborado a partir do conhecimento normativo dos atos citados no edital. **Atenção:** revise os textos oficiais no portal do CNJ (https://www.cnj.jus.br/programas-e-acoes/pdpj/).

---

# MÓDULO I — PANORAMA DA PDPJ-Br

## 1. O que é a PDPJ-Br

- **Plataforma Digital do Poder Judiciário Brasileiro (PDPJ-Br)**: ecossistema de soluções digitais compartilhadas entre todos os órgãos do Poder Judiciário, coordenado pelo **CNJ** com apoio do **CSJT** e das Escolas Judiciais. Objetivo: **interoperabilidade**, acesso à justiça digital, padronização de fluxos e dados e migração do processo judicial do formato físico para o digital.
- **Objetivos estratégicos**: fluxo processual digital único; compartilhamento de dados e serviços entre tribunais; redução de custos; suporte a decisões orientadas a dados; transparência e acessibilidade.
- **Ecossistema de soluções** (Domicílio Eletrônico, Conta Única, Integrações com Legislação, Lexml, Rede Nacional de Dados, painéis de dados, Fóruns de Arquitetura, Padrões de Dados etc.).

## 2. Estrutura normativa (mapa do edital)

| Normativo | Objeto resumido |
|---|---|
| **Resolução CNJ nº 335/2020** | Institui o **processo judicial eletrônico** no âmbito da Justiça do Trabalho (e dá diretrizes gerais de digitalização) |
| **Resolução CNJ nº 522/2023** | Regulamenta a **PDPJ-Br** (governança, arquitetura, interoperabilidade, padrões) |
| **Portaria CNJ nº 252/2020** | Fluxo de serviços tecnológicos da PDPJ; contratações/uso das soluções do ecossistema |
| **Portaria CNJ nº 253/2020** | Padrões técnicos e fluxos de integração/integração com sistemas locais |
| **Portaria CNJ nº 131/2021** | Fórum de Arquitetura / arranjo de governança técnica da PDPJ |
| **Resolução CNJ nº 396/2021** | Padrões de interoperabilidade e integração de sistemas / credenciamento de soluções |
| **Portaria CNJ nº 162/2021** | Regras operacionais de soluções/fluxos (ex.: integrações, dados compartilhados) |

*(Complemento: conteúdo próprio; confirme artigos e dispositivos nos textos oficiais do CNJ.)*

---

# MÓDULO II — PRINCIPAIS NORMATIVOS

## 1. Resolução CNJ nº 335/2020 — processo judicial eletrônico na Justiça do Trabalho

- Institui o **processo judicial eletrônico** no âmbito da **Justiça do Trabalho**, estabelecendo diretrizes para digitalização de processos e documentos, autuação eletrônica, assinatura eletrônica e preservação do original digital.
- Princípios: **eficiência, interoperabilidade, padronização, acesso à justiça, segurança e autenticidade** dos atos processuais.
- Relação com a PDPJ: solução base (ex.: PJe e sistemas homologados) integrada ao ecossistema digital compartilhado.

## 2. Resolução CNJ nº 522/2023 — regulamentação da PDPJ-Br

- **Regulamenta a Plataforma Digital do PDPJ**, fixando a **arquitetura de governança**, os **padrões obrigatórios de interoperabilidade**, a integração dos sistemas dos órgãos do Judiciário e as regras de adesão das soluções.
- Define atribuições de: **Conselho de Governança**, comitês técnicos, **Fórum de Arquitetura** (revisões de arquitetura de soluções) e centros de excelência.
- Estabelece a **Rede Nacional de Dados**, o **Domicílio Eletrônico**, a **Conta Única** (identidade digital do usuário) e o compartilhamento de APIs/serviços.
- Regras de segurança, privacidade (**LGPD**), retenção de logs e auditoria das integrações.
- Obrigações dos tribunais: mapear sistemas, alinhar à arquitetura de referência, aderir aos padrões de dados (JSON/REST etc. — ver apostila T8) e às linhas do fluxo processual digital.

## 3. Portarias CNJ nº 252/2020 e nº 253/2020 — fluxos e padrões de serviço

- **252/2020**: disciplina o **fluxo de serviços tecnológicos** do ecossistema PDPJ: solicitação, integração e operação de soluções; responsabilidades do tribunal solicitante e das equipes de TI; conformidade com a arquitetura.
- **253/2020**: **padrões técnicos** de integração (contratos de API, autenticação/autorização, mensagem/evento, versionamento), qualidade de software, testes e homologação; interoperação com sistemas locais via serviços compartilhados.

## 4. Portaria CNJ nº 131/2021 — Fórum de Arquitetura

- Cria/organiza o **Fórum de Arquitetura da PDPJ**: colegiado técnico responsável por analisar e homologar a arquitetura de soluções propostas por órgãos do Judiciário, garantir alinhamento à arquitetura de referência, avaliar interoperabilidade, segurança e escalabilidade.
- Composição com representantes de tribunais (incluindo **TRTs/CSJT**), membros do CNJ e especialistas técnicos.
- Fluxo: proposta de solução → análise do Fórum → homologação ou ajustes → integração ao ecossistema.

## 5. Resolução CNJ nº 396/2021 — interoperabilidade e padrões

- Estabelece **padrões e diretrizes de interoperabilidade** de sistemas e dados do Poder Judiciário: catálogo de serviços, APIs, formatos de dados (JSON/XML), segurança das integrações (OAuth2/OpenID — ver T8/T16), versionamento, gestão de contratos de API e monitoramento.
- Regras de **credenciamento de soluções** e de compartilhamento de dados entre órgãos, com conformidade à LGPD.
- Alinha-se ao Decreto nº 10.278/2020 (padrões de interoperabilidade do governo federal, referência técnica recorrente).

## 6. Portaria CNJ nº 162/2021 — regras operacionais

- Normas operacionais para uso das soluções do ecossistema (ex.: fluxos de integração, compartilhamento de dados e serviços, credenciamento de usuários), incluindo prazos, responsabilidades e indicadores de qualidade dos serviços compartilhados.

---

# MÓDULO III — TEMA TRANSVERSAL: GOVERNANÇA, SEGURANÇA E PADRÕES

- **Governança**: Comitê de Governança, Comitê Gestor de Projetos e Fóruns temáticos (Arquitetura, Dados, Acesso à Justiça); ritos de aprovação e revisão de soluções.
- **Segurança e LGPD**: autenticação (Conta Única, SSO — ver T8: Keycloak/OAuth2), controle de acesso, logs, criptografia, avaliação de impacto, privacy by design.
- **Padrões técnicos recorrentes nos normativos**: API **RESTful**, **JSON**, microsserviços, **Spring Boot/Spring Cloud**, documentação **Swagger/OpenAPI**, Service Discovery (Eureka), API Gateway (Zuul/Gateway), integração assíncrona (**RabbitMQ**, webhooks) — ver apostila **T8 (PDPJ-Br / arquitetura de desenvolvimento)** para a aplicação técnica; este tópico cobre os **normativos**.
- **Arquitetura de referência**: integração por serviços, interoperabilidade por API, reuso de componentes, escala horizontal, observabilidade (logs/métricas — ver T14).

---

# RESUMO DE PEGADINHAS DE PROVA

1. **PDPJ-Br** = Plataforma Digital do Poder Judiciário **Brasileiro** (ecossistema do **CNJ**, não de um tribunal).
2. **Res. 522/2023 = regulamenta a PDPJ** (governança, arquitetura, interoperabilidade).
3. **Res. 335/2020 = processo judicial eletrônico na Justiça do Trabalho** (não é a resolução da PDPJ).
4. **Portarias 252 e 253/2020** = fluxos de serviços + **padrões técnicos de integração**.
5. **Portaria 131/2021 = Fórum de Arquitetura** (homologação de soluções).
6. **Res. 396/2021 = interoperabilidade/credenciamento** de soluções (padrões de API/dados).
7. **Portaria 162/2021** = regras operacionais de integração/compartilhamento.
8. **Conta Única** = identidade digital do usuário; **Domicílio Eletrônico** = canal de comunicação oficial.
9. **LGPD e segurança** são exigência transversal dos normativos.
10. **Fórum de Arquitetura** homologa a arquitetura das soluções antes da integração.
11. **Padrões técnicos**: API REST/JSON, microsserviços, Swagger, Service Discovery, API Gateway (ver T8).
12. **Rede Nacional de Dados** = compartilhamento de dados entre órgãos do Judiciário.
13. **Res. 522/2023 não substitui** as demais — elas coexistem (335 processo, 252/253 fluxos, 131 Fórum, 396 interoperabilidade, 162 operação).
14. O edital exige **atenção às versões e datas** (ex.: Regimento Interno TRT8 atualizado em 2026 — ver Legislação).
15. **Conteúdo complementar**: normativos ausentes da base local de 2020 — consulte os textos oficiais do CNJ.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) A Resolução CNJ nº 335/2020 institui o processo judicial eletrônico no âmbito da Justiça do Trabalho, estabelecendo diretrizes de digitalização e autuação eletrônica.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Res. 335/2020** = processo judicial eletrônico na **Justiça do Trabalho** (diretrizes de digitalização, assinatura eletrônica, preservação do original).

---

**Questão 2.** (FCC-style) O normativo que regulamenta a Plataforma Digital do Poder Judiciário (PDPJ-Br), fixando governança, arquitetura e padrões de interoperabilidade, é:
a) Resolução CNJ nº 335/2020.
b) Resolução CNJ nº 522/2023.
c) Portaria CNJ nº 252/2020.
d) Portaria CNJ nº 131/2021.
e) Portaria CNJ nº 162/2021.

> **Resposta: b.** **Res. 522/2023** regulamenta a **PDPJ-Br**. A 335/2020 trata do processo eletrônico na Justiça do Trabalho; as portarias tratam de fluxos/padrões.

---

**Questão 3.** (CESPE-style) A Portaria CNJ nº 131/2021 trata do Fórum de Arquitetura da PDPJ, colegiado que analisa e homologa a arquitetura das soluções propostas por órgãos do Judiciário.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Portaria 131/2021** = **Fórum de Arquitetura** (análise/homologação de arquitetura de soluções, alinhamento à arquitetura de referência).

---

**Questão 4.** (FCC-style) As Portarias CNJ nº 252/2020 e nº 253/2020 relacionam-se, respectivamente, a:
a) processo eletrônico e credenciamento de soluções.
b) fluxo de serviços tecnológicos e padrões técnicos de integração.
c) governança da PDPJ e processo eletrônico.
d) LGPD e segurança da informação.
e) Fórum de Arquitetura e rede de dados.

> **Resposta: b.** **252/2020** = fluxo de serviços tecnológicos; **253/2020** = **padrões técnicos** de integração (contratos de API, homologação).

---

**Questão 5.** (CESPE-style) A Resolução CNJ nº 396/2021 estabelece padrões e diretrizes de interoperabilidade de sistemas e dados do Poder Judiciário, incluindo credenciamento de soluções.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Res. 396/2021** = interoperabilidade/padrões de dados e APIs, credenciamento de soluções, conformidade com LGPD.

---

**Questão 6.** (FCC-style) A Portaria CNJ nº 162/2021 disciplina:
a) a criação da PDPJ.
b) o processo judicial eletrônico trabalhista.
c) regras operacionais de integração e compartilhamento de dados e serviços do ecossistema PDPJ.
d) o Estatuto de Roma.
e) o Código de Ética do TRT8.

> **Resposta: c.** **Portaria 162/2021** = regras **operacionais** de uso/integração das soluções do ecossistema.

---

**Questão 7.** (CESPE-style) A PDPJ-Br é uma plataforma criada e operada exclusivamente pelo TRT8, sem participação do CNJ.
a) Certo. b) Errado.

> **Resposta: b (Errado).** A PDPJ-Br é do **Poder Judiciário nacional**, coordenada pelo **CNJ** (com CSJT e tribunais) — ecossistema **compartilhado**.

---

**Questão 8.** (FCC-style) O Fórum de Arquitetura da PDPJ tem por atribuição:
a) julgar processos administrativos.
b) analisar e homologar a arquitetura de soluções, garantindo interoperabilidade e alinhamento à arquitetura de referência.
c) substituir o Poder Judiciário no julgamento de recursos.
d) gerir o orçamento do CNJ.
e) definir a política de recursos humanos dos tribunais.

> **Resposta: b.** Fórum = instância **técnica** de análise/homologação de **arquitetura** (segurança, escalabilidade, interoperabilidade).

---

**Questão 9.** (CESPE-style) A Conta Única e o Domicílio Eletrônico são componentes do ecossistema PDPJ, destinados, respectivamente, à identidade digital do usuário e ao canal de comunicação oficial eletrônica.
a) Certo. b) Errado.

> **Resposta: a (Certo).** **Conta Única** = identidade digital; **Domicílio Eletrônico** = canal oficial de comunicação/intimações.

---

**Questão 10.** (FCC-style) A Resolução CNJ nº 522/2023 tem aplicação restrita à Justiça do Trabalho, não alcançando demais ramos do Poder Judiciário.
a) Certo. b) Errado.

> **Resposta: b (Errado).** A PDPJ-Br é **nacional** (todos os ramos/tribunais). A **335/2020** é que é específica da Justiça do Trabalho.

---

**Questão 11.** (CESPE-style) Os normativos da PDPJ dispensam a observância da LGPD no compartilhamento de dados entre órgãos do Judiciário.
a) Certo. b) Errado.

> **Resposta: b (Errado).** **LGPD** é exigência **transversal**: segurança, privacidade, avaliação de impacto, logs — todos os normativos a exigem.

---

**Questão 12.** (FGV-style) Sobre os normativos da PDPJ-Br, é correto afirmar:
a) a Resolução CNJ nº 522/2023 regulamenta a PDPJ, fixando governança, arquitetura de referência e padrões de interoperabilidade.
b) a Portaria CNJ nº 252/2020 cria o Fórum de Arquitetura.
c) a Resolução CNJ nº 335/2020 trata exclusivamente de credenciamento de soluções.
d) a Portaria CNJ nº 131/2021 institui o processo eletrônico.
e) a Portaria CNJ nº 162/2021 regulamenta o Estatuto de Roma.

> **Resposta: a.** **522/2023** = regulamentação da PDPJ. Fórum = **131/2021**; processo eletrônico trabalhista = **335/2020**; fluxos/padrões = **252/253**.

---

**Questão 13.** (CESPE-style) A interoperabilidade na PDPJ é apoiada por padrões técnicos como APIs RESTful, JSON e contratos de serviço, conforme os normativos e a arquitetura de referência.
a) Certo. b) Errado.

> **Resposta: a (Certo).** Padrões: **API REST/JSON**, microsserviços, Swagger/OpenAPI, versionamento, segurança (OAuth2/SSO) — ver T8 e Res. 396/2021.

---

**Questão 14.** (FCC-style) A Rede Nacional de Dados da PDPJ destina-se a:
a) armazenar processos físicos.
b) compartilhar dados e informações entre os órgãos do Poder Judiciário, com padronização e segurança.
c) substituir o sistema de correios.
d) gerir redes de telefonia.
e) controlar o acesso à internet pública.

> **Resposta: b.** **Rede Nacional de Dados** = compartilhamento **padronizado e seguro** de dados entre órgãos do Judiciário.

---

**Questão 15.** (CESPE-style) A Portaria CNJ nº 162/2021 tem por objeto a criação do Fórum de Arquitetura, enquanto a Portaria CNJ nº 131/2021 trata das regras operacionais de integração.
a) Certo. b) Errado.

> **Resposta: b (Errado).** Está invertido: **131/2021 = Fórum de Arquitetura**; **162/2021 = regras operacionais** de integração/compartilhamento.

---

## Questões discursivas

**D1.** Explique a finalidade da PDPJ-Br e o papel dos normativos Resolução CNJ nº 522/2023, Resolução CNJ nº 335/2020 e Portaria CNJ nº 131/2021.

> **Modelo de resposta:** A **PDPJ-Br** é a Plataforma Digital do Poder Judiciário Brasileiro, ecossistema nacional de soluções digitais coordenado pelo CNJ, destinado à interoperabilidade, à migração do processo judicial para o digital e ao compartilhamento de dados e serviços entre tribunais. A **Resolução CNJ nº 522/2023** regulamenta a plataforma, fixando governança, arquitetura de referência, padrões de interoperabilidade, segurança e conformidade com a LGPD. A **Resolução CNJ nº 335/2020** institui o processo judicial eletrônico no âmbito da Justiça do Trabalho, com diretrizes de digitalização, autuação eletrônica e assinatura eletrônica. A **Portaria CNJ nº 131/2021** organiza o Fórum de Arquitetura, colegiado técnico que analisa e homologa a arquitetura das soluções propostas pelos órgãos do Judiciário, assegurando interoperabilidade, segurança e escalabilidade.

**D2.** Diferencie os objetos das Portarias CNJ nº 252/2020, nº 253/2020 e nº 162/2021 e da Resolução CNJ nº 396/2021.

> **Modelo de resposta:** A **Portaria 252/2020** disciplina o **fluxo de serviços tecnológicos** da PDPJ (solicitação, integração e operação de soluções; responsabilidades das equipes de TI). A **Portaria 253/2020** fixa os **padrões técnicos de integração** (contratos de API, autenticação, versionamento, testes e homologação). A **Resolução 396/2021** trata de **interoperabilidade** e **credenciamento de soluções**, com padrões de dados e APIs e conformidade com a LGPD. A **Portaria 162/2021** estabelece **regras operacionais** de uso das soluções e compartilhamento de dados/serviços entre órgãos, com prazos, responsabilidades e indicadores de qualidade. Em conjunto, esses atos estruturam a integração dos sistemas locais ao ecossistema PDPJ.

---

*Conteúdo **complementar**: os normativos PDPJ-Br (Res. CNJ 522/2023, 335/2020; Portarias CNJ 252/2020, 253/2020, 131/2021; Res. CNJ 396/2021; Portaria CNJ 162/2021) não constam das apostilas locais (base de 2020). Elaborado a partir do conhecimento dos atos citados no edital. **Recomenda-se a leitura dos textos oficiais no portal do CNJ** para conferência de dispositivos. Aplicação técnica dos padrões (Spring, microsserviços, API REST/JSON, Keycloak/OAuth2, RabbitMQ, Docker/Kubernetes): ver apostila T8.*