# APOSTILA — TÓPICO 17 (V2): NORMATIVOS DA PLATAFORMA DIGITAL DO PODER JUDICIÁRIO – PDPJ-Br
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Normativos da Plataforma Digital do Poder Judiciário – PDPJ-Br: Resolução CNJ nº 522/2023; Resolução CNJ nº 335/2020; Portaria CNJ nº 252/2020; Portaria CNJ nº 253/2020; Portaria CNJ nº 131/2021; Resolução CNJ nº 396/2021; Portaria CNJ nº 162/2021.
>
> **Base de conhecimento:** **complemento** — normativos posteriores à base local (2020). V2 ampliada: destaques normativos por normativo (o que o examinador cobra), sem caderno de questões. **Atenção:** os atos abaixo já sofreram alterações posteriores; confira sempre a versão vigente no portal do CNJ (https://www.cnj.jus.br/programas-e-acoes/pdpj/).

---

# MÓDULO I — PANORAMA E LEITURA DOS NORMATIVOS

## 1. O que é a PDPJ-Br

- **Plataforma Digital do Poder Judiciário Brasileiro (PDPJ-Br)**: ecossistema nacional de soluções digitais compartilhadas entre os órgãos do Judiciário, sob coordenação do **CNJ**, com apoio do **CSJT** e das Escolas Judiciais. Migra o processo judicial ao formato digital e padroniza fluxos, dados e integrações.
- **Objetivos**: fluxo processual digital único; interoperabilidade entre sistemas; compartilhamento de dados e serviços; redução de custos; transparência, acessibilidade e decisões orientadas a dados.

## 2. Mapa rápido dos sete normativos do edital

| Normativo | Objeto — o que decorar |
|---|---|
| **Res. CNJ 522/2023** | Regulamenta a **PDPJ-Br**: governança, arquitetura de referência, interoperabilidade, adesão de soluções |
| **Res. CNJ 335/2020** | **Processo judicial eletrônico na Justiça do Trabalho** (digitalização, autuação eletrônica, assinatura eletrônica) |
| **Port. CNJ 252/2020** | **Fluxo de serviços tecnológicos** do ecossistema (solicitação, integração, operação de soluções) |
| **Port. CNJ 253/2020** | **Padrões técnicos de integração** (contratos de API, autenticação, versionamento, testes/homologação) |
| **Port. CNJ 131/2021** | **Fórum de Arquitetura** (análise e homologação da arquitetura de soluções) |
| **Res. CNJ 396/2021** | **Interoperabilidade e credenciamento de soluções** (padrões de dados/APIs, LGPD) |
| **Port. CNJ 162/2021** | **Regras operacionais** de uso/integração e compartilhamento de dados e serviços |

### Pontos a destacar
- **Resolução** (CNJ) tem patamar normativo superior a **Portaria** (ato do presidente/órgão executivo): a banca gosta de perguntar qual instrumento trata de quê.
- **522/2023 é o "guarda-chuva"** da PDPJ; as portarias e a 396/2021 detalham fluxos, padrões e operação; a **335/2020 é do ramo trabalhista**, não da PDPJ em si.

---

# MÓDULO II — RESOLUÇÃO CNJ Nº 522/2023 (REGULAMENTAÇÃO DA PDPJ)

## 1. Objeto e alcance

- Regulamenta a **Plataforma Digital do Poder Judiciário (PDPJ-Br)**, instituindo a **arquitetura de governança**, os **padrões obrigatórios de interoperabilidade** e as regras de integração dos sistemas dos órgãos do Judiciário.
- Aplicação **nacional**, a todos os ramos e tribunais (não restrita à Justiça do Trabalho).

## 2. Governança

- **Conselho de Governança** e **Comitê Gestor de Projetos**: priorização e acompanhamento de soluções do ecossistema.
- **Fórum de Arquitetura** (detalhado na Portaria 131/2021): homologação técnica de soluções.
- **Comitês e Fóruns temáticos** (ex.: Dados, Acesso à Justiça Digital) e centros de excelência.
- Papel dos **tribunais** (incluídos TRTs): mapear sistemas, alinhar à arquitetura de referência, aderir aos padrões e informar dados para indicadores.

## 3. Ecossistema de soluções disciplinado

- **Domicílio Eletrônico**: canal oficial de comunicação e intimações eletrônicas.
- **Conta Única**: identidade digital do usuário (SSO — ver T8: Keycloak/OpenID Connect).
- **Rede Nacional de Dados** e painéis de dados; **integrações com Legislação** e **Lexml**; APIs e serviços compartilhados.

## 4. Interoperabilidade, segurança e privacidade

- Padrões obrigatórios de **APIs, formatos de dados (JSON/XML)**, versionamento e catálogo de serviços (detalhamento na Res. 396/2021 e Port. 253/2020).
- **Segurança**: autenticação/autorização, logs de auditoria, criptografia; **LGPD** como exigência transversal (privacy by design, avaliação de impacto).

### Pontos a destacar
- Decorar o **tripé 522/2023: governança + arquitetura de referência + interoperabilidade**.
- **Conta Única = identidade digital**; **Domicílio Eletrônico = comunicação oficial** — inversão é pegadinha clássica.
- A 522/2023 **não revoga** os demais atos do edital: coexistem em camadas (resolução-mãe → portarias de fluxo/padrões → operação).

---

# MÓDULO III — RESOLUÇÃO CNJ Nº 335/2020 (PROCESSO ELETRÔNICO NA JUSTIÇA DO TRABALHO)

## 1. Objeto

- Institui o **processo judicial eletrônico** no âmbito da **Justiça do Trabalho** (ramo do TRT8), com diretrizes de **digitalização** de processos e documentos, **autuação eletrônica**, **assinatura eletrônica** e preservação do **original digital**.

## 2. Diretrizes que a banca cobra

- **Princípios**: eficiência, interoperabilidade, padronização, segurança, autenticidade e acesso à justiça.
- **Digitalização**: documentos físicos → formato digital com fidedignidade; tratamento de mídias e anexos.
- **Assinatura eletrônica**: uso de certificados digitais (ICP-Brasil — ver T16) e demais meios admitidos; validade dos atos eletrônicos.
- **Integração à PDPJ**: sistemas locais (ex.: PJe) devem observar os padrões do ecossistema.

### Pontos a destacar
- **335/2020 é trabalhista** (Justiça do Trabalho); as demais resoluções/portarias do edital são do **ecossistema PDPJ (nacional)**.
- Ênfase em **fidedignidade do digitalizado** e **valor probatório do original digital** — tema recorrente.

---

# MÓDULO IV — PORTARIAS CNJ Nº 252/2020 E 253/2020 (FLUXOS E PADRÕES)

## 1. Portaria CNJ nº 252/2020 — fluxo de serviços tecnológicos

- Disciplina o **fluxo de serviços tecnológicos** do ecossistema PDPJ: solicitação, integração e operação de soluções.
- Define **responsabilidades** do tribunal solicitante, das equipes de TI e das áreas de negócio; exigência de **conformidade com a arquitetura** antes da integração.

## 2. Portaria CNJ nº 253/2020 — padrões técnicos de integração

- Fixa **padrões técnicos** de integração: **contratos de API**, autenticação/autorização, mensagens/eventos, **versionamento**, qualidade de software, **testes e homologação**.
- Interoperação com sistemas locais via **serviços compartilhados** (ex.: API Gateway, Service Discovery — ver T8).

### Pontos a destacar
- **252 = fluxo/processo** (como pedir/integrar/operar); **253 = padrão técnico** (como a integração é feita). Pergunta de associação direta.
- **Homologação e testes** obrigatórios antes da operação — o "go-live" só após conformidade.

---

# MÓDULO V — PORTARIA CNJ Nº 131/2021 (FÓRUM DE ARQUITETURA)

- Institui/organiza o **Fórum de Arquitetura da PDPJ**: colegiado **técnico** que analisa e **homologa a arquitetura** de soluções propostas por órgãos do Judiciário.
- Garante alinhamento à **arquitetura de referência**, avaliando **interoperabilidade, segurança e escalabilidade**.
- **Composição**: representantes de tribunais (incluindo TRTs/CSJT), membros do CNJ e especialistas.
- **Fluxo**: proposta → análise do Fórum → homologação (ou ajustes) → integração ao ecossistema.

### Pontos a destacar
- Fórum **não julga processos nem decide política**: é instância de **homologação técnica de arquitetura**.
- "Só entra na PDPJ quem passa pelo Fórum de Arquitetura" — essência do normativo.

---

# MÓDULO VI — RESOLUÇÃO CNJ Nº 396/2021 (INTEROPERABILIDADE E CREDENCIAMENTO)

- Estabelece **padrões e diretrizes de interoperabilidade** de sistemas e dados do Judiciário: catálogo de serviços, **APIs**, formatos (**JSON/XML**), segurança das integrações (OAuth2/OpenID — ver T8/T16), **versionamento**, gestão de contratos de API e monitoramento.
- Regras de **credenciamento de soluções** e de compartilhamento de dados entre órgãos, com **conformidade à LGPD**.
- Alinha-se ao **Decreto nº 10.278/2020** (padrões de interoperabilidade do governo federal) — referência técnica recorrente.

### Pontos a destacar
- **396/2021 = interoperabilidade + credenciamento**; a **Port. 253/2020** detalha os **padrões técnicos** de integração — não confundir os dois atos.
- **LGPD** e **padrões de dados/API** são o núcleo cobrado.

---

# MÓDULO VII — PORTARIA CNJ Nº 162/2021 (REGRAS OPERACIONAIS)

- Normas **operacionais** de uso das soluções do ecossistema: fluxos de integração, compartilhamento de dados e serviços, credenciamento de usuários.
- **Prazos, responsabilidades e indicadores de qualidade** dos serviços compartilhados.

### Pontos a destacar
- **162/2021 = operação** (o dia a dia das integrações); a **131/2021 = homologação de arquitetura**. Inverter os dois é a pegadinha mais comum do tópico.

---

# MÓDULO VIII — GOVERNANÇA, SEGURANÇA E PADRÕES (TEMA TRANSVERSAL)

- **Governança**: Conselho de Governança, Comitê Gestor de Projetos, Fóruns temáticos (Arquitetura, Dados, Acesso à Justiça); ritos de aprovação e revisão de soluções.
- **Segurança e LGPD**: autenticação (Conta Única/SSO), controle de acesso, logs, criptografia, avaliação de impacto, privacy by design — ver T16 (segurança) e T8 (arquitetura).
- **Padrões técnicos recorrentes**: API **RESTful**, **JSON**, microsserviços, documentação **Swagger/OpenAPI**, Service Discovery, API Gateway, integração assíncrona (mensageria/webhooks) — aplicação técnica na apostila **T8**; este tópico cobre os **normativos**.
- **Arquitetura de referência**: integração por serviços, interoperabilidade por API, reuso de componentes, escala horizontal, observabilidade (logs/métricas — ver T14).

### Pontos a destacar
- **LGPD é transversal a todos os sete normativos** — segurança e privacidade nunca são exceção.
- O edital cobra **datas e objetos** (ex.: 131/2021 × 162/2021; 252 × 253/2020; 335/2020 trabalhista × 522/2023 nacional).

---

# RESUMO DE PEGADINHAS DE PROVA

1. **PDPJ-Br** = Plataforma Digital do Poder Judiciário **Brasileiro** (ecossistema nacional do **CNJ**, não de um tribunal).
2. **Res. 522/2023 = regulamenta a PDPJ** (governança, arquitetura de referência, interoperabilidade, adesão de soluções).
3. **Res. 335/2020 = processo judicial eletrônico na Justiça do Trabalho** (não é a resolução da PDPJ).
4. **Port. 252/2020 = fluxo de serviços tecnológicos**; **Port. 253/2020 = padrões técnicos de integração** (associação direta).
5. **Port. 131/2021 = Fórum de Arquitetura** (análise e **homologação técnica** de soluções).
6. **Res. 396/2021 = interoperabilidade e credenciamento de soluções** (padrões de dados/APIs, LGPD).
7. **Port. 162/2021 = regras operacionais** de integração e compartilhamento (não confundir com a 131/2021).
8. **Conta Única** = identidade digital do usuário; **Domicílio Eletrônico** = canal oficial de comunicação/intimações.
9. **LGPD e segurança** são exigência **transversal** de todos os normativos.
10. **Resolução > Portaria** em hierarquia normativa (CNJ): atenção ao instrumento que trata de cada matéria.
11. **Fórum de Arquitetura** homologa a **arquitetura** antes da integração — não julga processos.
12. **Rede Nacional de Dados** = compartilhamento padronizado e seguro de dados entre órgãos do Judiciário.
13. **522/2023 não substitui** os demais atos: coexistem em camadas (resolução-mãe → fluxos/padrões → operação).
14. **252 = "como pedir/integrar"**; **253 = "como fazer tecnicamente"** (contratos de API, testes, homologação).
15. Padrões técnicos recorrentes: **API REST/JSON, Swagger/OpenAPI, Service Discovery, API Gateway** (ver T8).
16. **Decreto 10.278/2020** é referência de padrões de interoperabilidade do governo federal citada pela 396/2021.
17. **335/2020**: fidedignidade do digitalizado e valor do **original digital**; assinatura eletrônica (ICP-Brasil — ver T16).
18. Conteúdo **complementar** à base de 2020: confira as versões vigentes dos atos no portal do CNJ.
