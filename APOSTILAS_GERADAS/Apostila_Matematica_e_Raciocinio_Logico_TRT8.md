# APOSTILA — MATEMÁTICA E RACIOCÍNIO LÓGICO
## TRT8 — Analista Judiciário — Analista de TI

> **Edital:** Estrutura lógica de relações arbitrárias; dedução de novas informações e avaliação de condições. Raciocínio verbal, matemático e sequencial; orientação espacial e temporal; formação de conceitos; discriminação de elementos. Processo lógico de hipóteses a conclusões. Números inteiros e racionais: operações, potenciação, expressões numéricas, múltiplos e divisores, problemas. Frações e operações. Razões e proporções; divisão em partes proporcionais; regra de três; porcentagem (acréscimos e descontos). Estatística: tendência central (moda, mediana, média aritmética simples e ponderada) e dispersão (desvio médio, amplitude, variância, desvio padrão); leitura e interpretação de gráficos (histogramas, setores, infográficos) e tabelas.
>
> **Base de conhecimento:** `02.Raciocínio Lógico` (Aulas 00–05 — lógica proposicional, conectivos, argumentos), `03.Matemática` (Aulas 00–07 — conjuntos, frações, razões, regra de três, porcentagem, juros, médias, gráficos), `matematica e raciocinio logico` (SEFA) — Curso 2020 + **complemento** (fórmulas de mediana/moda/variância/desvio padrão, interpretação de gráficos).

---

# MÓDULO I — RACIOCÍNIO LÓGICO

## 1. Estrutura de relações e raciocínio sequencial

- **Problemas de lógica posicional/relacional**: organizar pessoas/objetos em fila, mesa, ordem de chegada. **Técnica**: montar tabela/esquema; usar **dicas positivas** (é) e **negativas** (não é); **transitividade** (se A > B e B > C, então A > C).
- **Raciocínio sequencial** (sequências): padrões numéricos (PA, PG, Fibonacci — ver Módulo III), letras (próxima letra), formas (rotação/reflexão). **Orientação espacial**: planos, vistas (planta, lateral), giros (90°, 180°). **Orientação temporal**: calendários, relógios, ordem cronológica.
- **Formação de conceitos e discriminação de elementos**: classificar por atributos (cor, forma, tamanho); identificar o elemento que **não** pertence ao grupo.

## 2. Lógica proposicional

- **Proposição**: frase declarativa com valor **verdadeiro (V)** ou **falso (F)**. **Conectivos lógicos**:

| Conectivo | Símbolo | Nome | Regra |
|---|---|---|---|
| **e** | ∧ | conjunção | V só se **ambos** V |
| **ou** | ∨ | disjunção inclusiva | F só se **ambos** F |
| **ou...ou** | ⊕ | disjunção exclusiva | V se **exatamente um** V |
| **não** | ¬ | negação | inverte V/F |
| **se...então** | → | condicional (implicação) | F só se V→F |
| **se e somente se** | ↔ | bicondicional | V se **iguais** |

- **Tabela-verdade de p → q**:

| p | q | p→q |
|---|---|---|
| V | V | **V** |
| V | F | **F** |
| F | V | **V** |
| F | F | **V** |

- **Pegadinha clássica**: **p → q ≠ q → p** (a recíproca não é equivalente). "Se chove, a rua molha" ≠ "se a rua molha, chove".
- **Necessária × suficiente**: q é **condição necessária** de p se p→q (sem q não há p); q é **condição suficiente** de p se q→p (q basta para p). **Equivale**: p→q ≡ ¬q→¬p (**contrapositiva** — sempre use nas questões).
- **Equivalências**: De Morgan: ¬(p∧q) = ¬p∨¬q; ¬(p∨q) = ¬p∧¬q. **Contradição** (sempre F) × **tautologia** (sempre V).

## 3. Argumentos

- **Validade**: a conclusão **decorre necessariamente** das premissas (estrutura), independentemente do conteúdo. **Modus ponens**: p→q, p ∴ q. **Modus tollens**: p→q, ¬q ∴ ¬p. **Falácias**: afirmar o consequente (q, p→q ∴ p — **inválido**); negar o antecedente (¬p, p→q ∴ ¬q — **inválido**).
- **Premissas**: universais ("todos A são B") × particulares ("alguns A são B"). **Silogismos**: premissa maior, menor, conclusão.
- **Condicional** "se p então q": as **contrárias** de "se p então q" são "se p então não q"; as **contraditórias** são "p e não q". *Regra de ouro: negação de "se p então q" = "p e não q"*.

---

# MÓDULO II — NÚMEROS, CONJUNTOS E EXPRESSÕES

## 1. Conjuntos

- **Operações**: união (A∪B), interseção (A∩B), diferença (A−B), complementar (Ac). **Fórmula**: n(A∪B) = n(A) + n(B) − n(A∩B). **Conjuntos disjuntos** (A∩B = ∅). **Partes de um conjunto**: 2ⁿ (n = nº de elementos).

## 2. Números inteiros e racionais

- **Inteiros**: ..., −2, −1, 0, 1, 2, ... (operações com sinais: × e ÷: mesmos sinais = +; diferentes = −). **Racionais**: p/q (q ≠ 0); decimais exatos ou periódicos.
- **Potenciação**: aᵐ × aⁿ = aᵐ⁺ⁿ; aᵐ ÷ aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ; a⁰ = 1; a⁻ⁿ = 1/aⁿ.
- **Expressões numéricas**: PEMDAS/ordem: **parênteses, potências/raízes, multiplicação/divisão, adição/subtração** (da esquerda para a direita). **Valor absoluto**: |x| (distância a zero).
- **MMC/MDC**:
  - **Fatoração** em primos; **MMC** = produto dos primos com **maior** expoente; **MDC** = produto dos primos com **menor** expoente.
  - **Problemas clássicos**: "A cada quanto tempo se encontram?" → **MMC**; "maior bloco que cabe em todos" → **MDC**. *Ex.: ônibus a cada 12 min, outro a cada 18 min → MMC(12,18) = 36 min.*

## 3. Frações

- **Operações**: soma/subtração → **MMC dos denominadores**; multiplicação → numerador×numerador, denominador×denominador; divisão → **inverter o divisor** e multiplicar. **Fração equivalente**: multiplicar/dividir num. e denom. pelo mesmo número. **Decimal ↔ fração**: 0,25 = 25/100 = 1/4.
- **Problemas**: parte × total; "1/3 de 60" = 20; **porcentagem de fração**: 50% de 1/4 = 1/8.

---

# MÓDULO III — RAZÕES, PROPORÇÕES, REGRA DE TRÊS E PORCENTAGEM

## 1. Razões e proporções

- **Razão**: a/b (comparação). **Proporção**: a/b = c/d → **produto dos meios = produto dos extremos** (a·d = b·c).
- **Divisão em partes proporcionais**: dividir um total segundo razões (ex.: 2:3:5 → soma das partes = 10; cada parte = total × (parte/10)). *Ex.: dividir R$ 1.000 na razão 2:3:5 → 200, 300, 500.*

## 2. Regra de três

- **Simples direta**: as grandezas são **diretamente proporcionais** (aumentam juntas). Montar: "x está para 10 assim como 3 está para 6" → x/10 = 3/6 → x = 5.
- **Simples inversa**: grandezas **inversamente proporcionais** (uma aumenta, a outra diminui). *Ex.: 4 operários fazem em 10 dias; 5 operários fazem em x dias → 4×10 = 5×x → x = 8.*
- **Composta**: 3+ grandezas; decompor em sucessivas regras de três.
- **Identificar**: "quanto mais...mais" = direta; "quanto mais...menos" = inversa.

## 3. Porcentagem

- **Cálculo**: x% de N = (x/100)×N. **Fração de porcentagem**: 25% = 1/4; 12,5% = 1/8; 20% = 1/5.
- **Acréscimo**: valor × (1 + i/100). **Desconto**: valor × (1 − i/100). **Sucessivos**: multiplicar (ex.: 20% + 10% de desconto = ×0,8×0,9 = 0,72 → 28% de desconto real, **não** 30%).
- **Variação percentual**: (valor final − inicial)/inicial × 100. **Pegadinha**: aumento de 50% + desconto de 50% **não** volta ao original (100→150→75).
- **Juros simples**: J = C·i·t (não há juros sobre juros). **Juros compostos**: M = C·(1+i)ᵗ (juros sobre juros).

---

# MÓDULO IV — ESTATÍSTICA E GRÁFICOS

## 1. Medidas de tendência central

- **Média aritmética simples**: soma dos valores ÷ nº de valores (x̄ = Σxᵢ/n). *Ex.: 4, 6, 8, 10 → (4+6+8+10)/4 = 7.*
- **Média aritmética ponderada**: soma dos (valor × peso) ÷ soma dos pesos (x̄ = Σ(xᵢ·pᵢ)/Σpᵢ). *Ex.: nota 6 (peso 2) e 8 (peso 3) → (12+24)/5 = 7,2.* **Usar quando** os valores têm **importâncias diferentes** (provas com pesos).
- **Mediana**: valor que **divide a distribuição ao meio** (50% abaixo, 50% acima).
  - **n ímpar** (após ordenar): mediana = valor central. *Ex.: 2, 5, 7, 9, 12 → mediana = 7.*
  - **n par**: mediana = **média dos dois valores centrais**. *Ex.: 2, 5, 7, 9 → (5+7)/2 = 6.*
  - **Pegadinha**: ordenar os dados **antes**; a mediana **não** é afetada por valores extremos.
- **Moda**: valor que **mais se repete** (pode haver **mais de uma** — "bimodal/multimodal"; pode **não haver** moda; a moda **não** precisa estar na média nem na mediana).
- *Comparação*: a **média** é sensível a outliers; a **mediana**, não; a **moda** é a mais frequente. *Ex.: 1, 2, 2, 3, 100 → média = 21,6; mediana = 2; moda = 2.*

## 2. Medidas de dispersão

- **Amplitude**: diferença entre o **maior e o menor** valor (A = xₘₐₓ − xₘᵢₙ). *Ex.: 2, 5, 7, 12 → amplitude = 10.*
- **Desvio médio**: média dos **módulos** das diferenças em relação à média (DM = Σ|xᵢ − x̄|/n). *Ex.: 2, 4, 6, 8 → média = 5; desvios: 3, 1, 1, 3 → DM = 8/4 = 2.*
- **Variância**: média dos **quadrados** dos desvios em relação à média (s² = Σ(xᵢ − x̄)²/n — para **população**; para **amostra**, dividir por n−1). *Ex.: 2, 4, 6, 8 → variância = (9+1+1+9)/4 = 5.*
- **Desvio padrão**: **raiz quadrada da variância** (s = √s²) — está **na mesma unidade** dos dados. *Ex.: √5 ≈ 2,24.*
- *Pegadinha*: **variância** usa **quadrados** (unidade ao quadrado); **desvio médio** usa **módulos**; **desvio padrão** = √variância. Quanto **maior** o desvio padrão, **mais dispersos** os dados.

## 3. Gráficos e tabelas

- **Histograma**: barras **encostadas** (variáveis contínuas em intervalos); altura = **frequência**; leitura de moda/mediana aproximadas.
- **Gráfico de setores (pizza)**: partes de um total (**%**); ângulo = (valor/total)×360°. *Ex.: 25% = 90°.*
- **Gráfico de colunas/barras**: barras **separadas** (variáveis discretas); comparar categorias.
- **Linha/temporal**: evolução ao longo do tempo.
- **Infográficos**: gráficos + texto + ícones; ler **título, fonte, legenda, unidade**.
- **Tabelas**: cruzar linhas e colunas; atenção a **unidades** (%, mil, milhar) e **escalas** dos eixos (o eixo pode começar em 100 — "truncado" — e exagerar diferenças).
- **Pegadinha clássica**: **eixo truncado** (não começa em 0) distorce a leitura; sempre ler **título, fonte, unidade e escala**.

---

# RESUMO DE PEGADINHAS DE PROVA

1. **p → q ≠ q → p** (recíproca não equivale). Usar **contrapositiva**: p→q ≡ ¬q→¬p.
2. **Negação de "se p então q"** = "**p e não q**" (não "se p então não q").
3. **Condicional** p→q é **F só** quando p=V e q=F; nos demais casos, **V**.
4. **Modus ponens** (p→q, p ∴ q) e **modus tollens** (p→q, ¬q ∴ ¬q) são válidos; **afirmar o consequente** e **negar o antecedente** são **falácias**.
5. **MMC** para "quando se encontram"; **MDC** para "maior bloco comum".
6. **Regra de três inversa**: "quanto mais...menos"; **direta**: "quanto mais...mais".
7. **Acréscimo e desconto sucessivos** não se somam: multiplicar (50% + 50% ≠ 0).
8. **Juros simples** = C·i·t; **compostos** = C·(1+i)ᵗ.
9. **Mediana** exige **ordenar** os dados; n par = média dos 2 centrais; n ímpar = central.
10. **Média ponderada** quando há **pesos**; **moda** = mais frequente (pode haver várias ou nenhuma).
11. **Variância** = média dos **quadrados**; **desvio padrão** = **raiz** da variância (mesma unidade); **desvio médio** = média dos **módulos**; **amplitude** = máx − mín.
12. **Histograma** = barras encostadas (contínuas); **pizza** = % do total (ângulo = valor/total×360).
13. **Eixo truncado** distorce; ler **título, fonte, unidade, escala**.
14. **Valor absoluto** |x| = distância a zero (sempre ≥ 0).
15. **Ordem de operações**: parênteses → potências → ×/÷ → +/−.
16. **Partes de um conjunto**: 2ⁿ. **n(A∪B)** = n(A)+n(B)−n(A∩B).
17. **Necessária × suficiente**: p→q = q é **necessário** a p; q→p = q é **suficiente** para p.
18. **De Morgan**: ¬(p∧q) = ¬p∨¬q; ¬(p∨q) = ¬p∧¬q.

---

# CADERNO DE QUESTÕES COMENTADAS (15 objetivas + 2 discursivas)

**Questão 1.** (CESPE-style) A proposição "se chove, então a rua molha" é equivalente a "se a rua molha, então chove".
a) Certo. b) Errado.

> **Resposta: b (Errado).** **p→q ≠ q→p**. A recíproca não é equivalente. A equivalente é a **contrapositiva**: "se a rua **não** molha, então **não** chove".

---

**Questão 2.** (FCC-style) A negação da proposição "se estudo, então passo" é:
a) se não estudo, então não passo.
b) se estudo, então não passo.
c) estudo e não passo.
d) não estudo e não passo.
e) não estudo ou não passo.

> **Resposta: c.** Negação de **p→q** = **p ∧ ¬q** ("**estudo e não passo**"). **a** é a **contrapositiva de ¬p→¬q** (não é a negação).

---

**Questão 3.** (CESPE-style) O valor da expressão 2³ × 2⁴ ÷ 2² é:
a) 2⁵.
b) 2⁶.
c) 2⁹.
d) 2¹.
e) 2⁴.

> **Resposta: a.** 2³⁺⁴⁻² = 2⁵. (Regra: somar expoentes na ×, subtrair na ÷.)

---

**Questão 4.** (FCC-style) O MMC de 12 e 18 é:
a) 6.
b) 12.
c) 18.
d) 36.
e) 72.

> **Resposta: d.** 12 = 2²·3; 18 = 2·3² → **MMC** = 2²·3² = **36**. (**MDC** = 2·3 = 6.)

---

**Questão 5.** (CESPE-style) Cinco operários fazem um serviço em 12 dias. Quantos dias levarão 4 operários, com a mesma produtividade?
a) 9,6 dias.
b) 15 dias.
c) 10 dias.
d) 16 dias.
e) 20 dias.

> **Resposta: b.** Regra de três **inversa** (mais operários → menos dias): 5×12 = 4×x → x = **15 dias**.

---

**Questão 6.** (FCC-style) O preço de um produto aumenta 20% e depois sofre desconto de 20%. O preço final em relação ao original:
a) é igual.
b) aumenta 4%.
c) diminui 4%.
d) diminui 40%.
e) aumenta 40%.

> **Resposta: c.** 1,20 × 0,80 = 0,96 → **diminui 4%** (acréscimos/descontos sucessivos **não** se anulam).

---

**Questão 7.** (CESPE-style) A média aritmética ponderada das notas 6 (peso 2) e 8 (peso 3) é:
a) 7,0.
b) 7,2.
c) 6,5.
d) 7,5.
e) 6,8.

> **Resposta: b.** (6×2 + 8×3)/(2+3) = (12+24)/5 = **7,2**. (Média simples seria 7,0.)

---

**Questão 8.** (FCC-style) A mediana do conjunto {2, 5, 7, 9, 12} é:
a) 5.
b) 6.
c) 7.
d) 9.
e) 12.

> **Resposta: c.** n = 5 (ímpar) → mediana = valor central (ordenado) = **7**.

---

**Questão 9.** (CESPE-style) A mediana do conjunto {2, 5, 7, 9} é:
a) 5.
b) 5,5.
c) 6.
d) 7.
e) 6,5.

> **Resposta: c.** n = 4 (par) → média dos 2 centrais: (5+7)/2 = **6**.

---

**Questão 10.** (FCC-style) A moda do conjunto {1, 2, 2, 3, 100} é:
a) 1.
b) 2.
c) 3.
d) 100.
e) 21,6.

> **Resposta: b.** **Moda** = valor mais frequente = **2**. (Média = 21,6; mediana = 2.)

---

**Questão 11.** (CESPE-style) A variância do conjunto {2, 4, 6, 8} é:
a) 2.
b) 4.
c) 5.
d) 6.
e) 8.

> **Resposta: c.** Média = 5; desvios: −3, −1, 1, 3; quadrados: 9, 1, 1, 9 → soma = 20 → variância = 20/4 = **5**. (**Desvio padrão** = √5 ≈ 2,24; **desvio médio** = 2.)

---

**Questão 12.** (FGV-style) Sobre medidas de dispersão, é correto afirmar:
a) a amplitude é a média dos desvios.
b) o desvio padrão é a raiz quadrada da variância e tem a mesma unidade dos dados.
c) a variância tem a mesma unidade dos dados.
d) o desvio médio usa quadrados.
e) amplitude = soma dos valores.

> **Resposta: b.** **Desvio padrão** = √variância (mesma unidade). Variância = unidade **ao quadrado**; desvio médio = **módulos**; amplitude = **máx − mín**.

---

**Questão 13.** (CESPE-style) No gráfico de setores, um setor que representa 25% do total corresponde a um ângulo central de:
a) 45°.
b) 60°.
c) 90°.
d) 120°.
e) 180°.

> **Resposta: c.** Ângulo = (valor/total)×360° = 0,25×360 = **90°**.

---

**Questão 14.** (FCC-style) O desvio médio do conjunto {2, 4, 6, 8} é:
a) 1.
b) 2.
c) 2,5.
d) 5.
e) 8.

> **Resposta: b.** Média = 5; |desvios|: 3, 1, 1, 3 → soma = 8 → DM = 8/4 = **2**.

---

**Questão 15.** (CESPE-style) A proposição "p → q" é falsa apenas quando:
a) p é falsa e q é verdadeira.
b) p é verdadeira e q é falsa.
c) ambas são verdadeiras.
d) ambas são falsas.
e) p é verdadeira e q é verdadeira.

> **Resposta: b.** **p→q = F só quando p=V e q=F**. Nos demais casos, V.

---

## Questões discursivas

**D1.** Explique a diferença entre média aritmética simples, média ponderada, mediana e moda, e as medidas de dispersão (amplitude, desvio médio, variância e desvio padrão).

> **Modelo de resposta:** A **média aritmética simples** é a soma dos valores dividida pelo número de valores (sensível a extremos). A **média ponderada** considera **pesos** distintos (soma dos produtos valor×peso ÷ soma dos pesos). A **mediana** é o valor central da distribuição **ordenada** (n ímpar = central; n par = média dos dois centrais), resistente a outliers. A **moda** é o valor mais frequente (pode haver várias ou nenhuma). Sobre dispersão: a **amplitude** é a diferença entre o maior e o menor; o **desvio médio** é a média dos módulos dos desvios em relação à média; a **variância** é a média dos quadrados dos desvios; o **desvio padrão** é a raiz quadrada da variância, expresso na mesma unidade dos dados — quanto maior, mais dispersos os dados.

**D2.** Explique o conceito de condicional em lógica proposicional, a diferença entre condição necessária e suficiente e o uso da contrapositiva.

> **Modelo de resposta:** A condicional **p → q** ("se p então q") é falsa **apenas** quando p é verdadeira e q é falsa; nos demais casos, é verdadeira. **q** é **condição necessária** de **p** quando p→q (sem q não há p); **q** é **condição suficiente** de **p** quando q→p (q basta para p). A **contrapositiva** (¬q→¬p) é **logicamente equivalente** a p→q e é a ferramenta central em questões — ao passo que a recíproca (q→p) **não** equivale. A negação de p→q é "p e não q" (p ∧ ¬q). Princípios válidos: **modus ponens** (p→q, p ∴ q) e **modus tollens** (p→q, ¬q ∴ ¬p); inválidos: afirmar o consequente e negar o antecedente.

---

*Base: `02.Raciocínio Lógico` (Aulas 00–05 — proposições, conectivos, tabelas-verdade, argumentos, modus ponens/tollens), `03.Matemática` (Aulas 00–07 — conjuntos, frações, razões, regra de três, porcentagem, juros, médias, gráficos), `matematica e raciocinio logico` (SEFA). Complemento: fórmulas de mediana/moda/variância/desvio padrão e interpretação de gráficos (detalhamento parcial na base de 2020).*