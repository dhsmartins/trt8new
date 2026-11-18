# Apostilas TRT8 — Analista Judiciário (Analista de TI)

Apostilas de estudo baseadas no edital do concurso **TRT8 — Analista Judiciário — Área de TI**, organizadas por tópico do conteúdo programático.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `APOSTILAS GERADAS/` | Apostilas em Markdown (`.md`) e HTML (`.html`), geradoras (`make_html.py`, `make_portal.py`) e o portal de estudos (`Portal_de_Estudos_TRT8.html`) |
| `Conteudo_Programatico_TRT8_Analista_TI.md` | Conteúdo programático do edital |

## Como usar as apostilas

Cada tópico tem um `.md` (fonte) e um `.html` (estudo). Os HTMLs abrem direto no navegador e incluem:

- Conteúdo detalhado por módulo
- **Resumo de pegadinhas de prova**
- **Caderno de questões comentadas** (estilo FCC/CEBRASPE/FGV, com gabarito e modelo de resposta para discursivas)

### Gerar um HTML a partir de um `.md`

```bash
cd APOSTILAS GERADAS
python -I make_html.py "Apostila_T8_PDPJ-Br_TRT8_v2.md" "Título curto"
```

O `python -I` é intencional: impede que módulos locais sombreados sejam carregados (segurança com dados não confiáveis).

## Portal de estudos

Abra `APOSTILAS GERADAS/Portal_de_Estudos_TRT8.html` no navegador:

- Menu lateral com categorias e submenus suspensos por apostila
- Checkbox para marcar subtópicos como estudados (salvo no `localStorage`)
- Abertura da apostila na mesma página (abas V1/V2)
- Espaços reservados para Revisão e Exercícios

## Aviso sobre normas legais

Alguns normativos citados (ex.: Regimento Interno TRT8 atualizado em 22/06/2026, Resoluções CNJ/CSJT posteriores a 2020) **não constam da base local de 2020**. O conteúdo é complementar e baseado no edital; **confira sempre os textos oficiais no portal do CNJ** antes da prova.

## Licença

Material de estudo pessoal. Não oficial do TRT8/CNJ.
