# -*- coding: utf-8 -*-
"""Converte uma apostila (markdown) em página HTML de estudo.

Uso: python -I make_html.py <arquivo.md> "<Título curto>" "<Subtítulo>"
Saída: mesmo nome do .md com extensão .html, na mesma pasta.
"""
import re, sys
from pathlib import Path

import markdown

if len(sys.argv) < 2:
    # compat: gera o Tópico 9 se chamado sem argumentos
    SRC = Path(__file__).resolve().parent / "Apostila_Topico9_Ciencia_de_Dados_e_IA_TRT8.md"
    TITLE = "Tópico 9 — Ciência de Dados e IA"
    SUB = "TRT8 · Analista de TI · Apostila de estudo"
else:
    SRC = Path(sys.argv[1]).resolve()
    TITLE = sys.argv[2] if len(sys.argv) > 2 else SRC.stem
    SUB = sys.argv[3] if len(sys.argv) > 3 else "TRT8 · Analista de TI · Apostila de estudo"

OUT = SRC.with_suffix(".html")
SLUG = re.sub(r"[^a-z0-9]+", "-", SRC.stem.lower()).strip("-")

text = SRC.read_text(encoding="utf-8")

# Respostas de questões viram expansíveis; blockquotes comuns permanecem
def quote_to_details(m):
    body = m.group(0)
    if "Resposta" not in body.splitlines()[0] and "Modelo de resposta" not in body:
        return body
    body = "\n".join(l[2:] if l.startswith("> ") else (l[1:] if l.startswith(">") else l) for l in body.splitlines())
    inner = markdown.markdown(body)
    return ('<details class="resposta"><summary>Ver resposta e comentário</summary>'
            + inner + "</details>")

text = re.sub(r"(?:^> .*\n?)+", quote_to_details, text, flags=re.M)

body_html = markdown.markdown(text, extensions=["tables", "toc", "fenced_code"])

headings = re.findall(r'<h([23]) id="([^"]+)">(.+?)</h\1>', body_html)
toc_items = []
for lvl, hid, txt in headings:
    txt_plain = re.sub(r"<[^>]+>", "", txt)
    cls = "toc-h2" if lvl == "2" else "toc-h3"
    toc_items.append(f'<li class="{cls}"><a href="#{hid}">{txt_plain}</a></li>')
toc_html = "\n".join(toc_items)

page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} (TRT8)</title>
<style>
:root {{
  --bg: #f7f8fb; --card: #ffffff; --ink: #1c2333; --muted: #5b6472;
  --accent: #2456c4; --accent-soft: #e8eefc; --border: #d9dfe8;
  --ok: #1c7c45; --ok-soft: #e3f4ea; --warn: #9a5b00; --warn-soft: #fdf1dc;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #14171d; --card: #1c2129; --ink: #e8ecf3; --muted: #a3adbd;
    --accent: #7aa2f7; --accent-soft: #263248; --border: #323a47;
    --ok: #7fd7a2; --ok-soft: #1e3328; --warn: #f0c674; --warn-soft: #3a2f1c;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  font-size: 16px; line-height: 1.65;
}}
.layout {{ display: flex; min-height: 100vh; }}
nav {{
  width: 285px; flex-shrink: 0; position: sticky; top: 0; height: 100vh;
  overflow-y: auto; padding: 20px 14px; border-right: 1px solid var(--border);
  background: var(--card); font-size: 13.5px;
}}
nav h1 {{ font-size: 15px; margin: 0 0 4px; color: var(--accent); }}
nav .sub {{ color: var(--muted); font-size: 12px; margin-bottom: 14px; }}
nav ul {{ list-style: none; padding: 0; margin: 0; }}
nav li {{ margin: 2px 0; }}
nav a {{ color: var(--ink); text-decoration: none; display: block; padding: 4px 8px; border-radius: 6px; }}
nav a:hover {{ background: var(--accent-soft); color: var(--accent); }}
.toc-h3 a {{ padding-left: 22px; font-size: 12.5px; color: var(--muted); }}
main {{ flex: 1; padding: 32px 44px 80px; max-width: 900px; }}
h1:first-child {{
  font-size: 26px; border-bottom: 3px solid var(--accent);
  padding-bottom: 10px; margin-top: 0;
}}
h2 {{
  font-size: 21px; margin-top: 42px; padding: 8px 12px; border-radius: 8px;
  background: var(--accent-soft); color: var(--accent); border-left: 4px solid var(--accent);
}}
h3 {{ font-size: 17px; margin-top: 28px; border-bottom: 1px solid var(--border); padding-bottom: 4px; }}
table {{
  border-collapse: collapse; width: 100%; margin: 14px 0; font-size: 14.5px;
  background: var(--card); border-radius: 8px; overflow: hidden;
}}
th, td {{ border: 1px solid var(--border); padding: 8px 11px; text-align: left; }}
th {{ background: var(--accent-soft); color: var(--accent); }}
tr:nth-child(even) td {{ background: color-mix(in srgb, var(--accent-soft) 35%, transparent); }}
code {{
  background: var(--accent-soft); padding: 1px 6px; border-radius: 4px;
  font-family: Consolas, "Cascadia Code", monospace; font-size: 13.5px;
}}
blockquote {{
  border-left: 4px solid var(--warn); background: var(--warn-soft);
  margin: 12px 0; padding: 10px 16px; border-radius: 0 8px 8px 0;
}}
details.resposta {{
  border: 1px solid var(--ok); background: var(--ok-soft);
  border-radius: 8px; margin: 10px 0; padding: 0;
}}
details.resposta summary {{
  cursor: pointer; padding: 10px 16px; font-weight: 600; color: var(--ok);
  user-select: none;
}}
details.resposta > *:not(summary) {{ margin-left: 16px; margin-right: 16px; }}
hr {{ border: 0; border-top: 1px solid var(--border); margin: 30px 0; }}
strong {{ color: var(--ink); }}
a {{ color: var(--accent); }}
.progress-wrap {{ margin: 18px 0 26px; }}
.progress-bar {{
  height: 8px; border-radius: 99px; background: var(--border); overflow: hidden;
}}
.progress-fill {{
  height: 100%; width: 0; border-radius: 99px;
  background: linear-gradient(90deg, var(--accent), var(--ok));
  transition: width .35s ease;
}}
.progress-label {{ font-size: 12px; color: var(--muted); margin-top: 6px; }}
@media (max-width: 860px) {{
  nav {{ display: none; }}
  main {{ padding: 20px 18px 60px; }}
}}
</style>
</head>
<body>
<div class="layout">
<nav>
  <h1>{TITLE}</h1>
  <div class="sub">{SUB}</div>
  <div class="progress-wrap">
    <div class="progress-bar"><div class="progress-fill" id="pf"></div></div>
    <div class="progress-label" id="pl">Progresso do estudo: 0%</div>
  </div>
  <ul>
    {toc_html}
  </ul>
</nav>
<main>
{body_html}
<script>
(function () {{
  const key = '{SLUG}-progresso';
  let done = JSON.parse(localStorage.getItem(key) || '{{}}');
  const hs = [...document.querySelectorAll('main h2')];
  const fill = document.getElementById('pf');
  const label = document.getElementById('pl');
  function render() {{
    const n = hs.filter(h => done[h.textContent.trim()]).length;
    const pct = hs.length ? Math.round(n / hs.length * 100) : 0;
    fill.style.width = pct + '%';
    label.textContent = 'Progresso do estudo: ' + pct + '% (' + n + '/' + hs.length + ' módulos)';
    hs.forEach(h => {{
      const ok = done[h.textContent.trim()];
      h.style.borderLeftColor = ok ? 'var(--ok)' : 'var(--accent)';
      h.style.background = ok ? 'var(--ok-soft)' : 'var(--accent-soft)';
      h.style.color = ok ? 'var(--ok)' : 'var(--accent)';
      h.style.cursor = 'pointer';
      h.title = 'Clique para marcar/desmarcar como estudado';
    }});
  }}
  hs.forEach(h => h.addEventListener('click', () => {{
    const t = h.textContent.trim();
    done[t] = !done[t];
    if (!done[t]) delete done[t];
    localStorage.setItem(key, JSON.stringify(done));
    render();
  }}));
  render();
}})();
</script>
</main>
</div>
</body>
</html>"""

OUT.write_text(page, encoding="utf-8")
print("OK:", OUT, f"({OUT.stat().st_size} bytes)")
