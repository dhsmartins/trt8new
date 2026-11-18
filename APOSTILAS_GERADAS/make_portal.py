#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o Portal de Estudos TRT8 (layout SPA com menu lateral).

Uso:  python -I make_portal.py
Saida: Portal_de_Estudos_TRT8.html (na mesma pasta)

Layout: menu lateral com categorias > apostilas > subtopicos (checkboxes).
A apostila abre no conteudo a direita (iframe). As marcacoes de "lido"
funcionam tanto no menu suspenso quanto no painel do topico aberto,
com progresso salvo em localStorage.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Portal_de_Estudos_TRT8.html")

TI = [
    ("T1", "T1 — Processo de Desenvolvimento de Software", "Apostila_T1_Processo_de_Desenvolvimento_de_Software_TRT8"),
    ("T2", "T2 — Gestão de Projetos e Governança de TI", "Apostila_T2_Gestao_de_Projetos_e_Governanca_de_TI_TRT8"),
    ("T3", "T3 — Programação", "Apostila_T3_Programacao_TRT8"),
    ("T4", "T4 — Banco de Dados", "Apostila_T4_Banco_de_Dados_TRT8"),
    ("T5", "T5 — Desenvolvimento Web e Mobile", "Apostila_T5_Desenvolvimento_Web_e_Mobile_TRT8"),
    ("T6", "T6 — Arquiteturas de Sistemas", "Apostila_T6_Arquiteturas_de_Sistemas_TRT8"),
    ("T7", "T7 — DevOps e DevSecOps", "Apostila_T7_DevOps_e_DevSecOps_TRT8"),
    ("T8", "T8 — Arquitetura de Desenvolvimento PDPJ-Br", "Apostila_T8_PDPJ-Br_TRT8"),
    ("T9", "T9 — Ciência de Dados e IA", "Apostila_Topico9_Ciencia_de_Dados_e_IA_TRT8"),
    ("T10", "T10 — Business Intelligence", "Apostila_T10_Business_Intelligence_TRT8"),
    ("T11", "T11 — Sistemas Operacionais", "Apostila_T11_Sistemas_Operacionais_TRT8"),
    ("T12", "T12 — Redes de Computadores", "Apostila_T12_Redes_de_Computadores_TRT8"),
    ("T13", "T13 — Serviços de Rede", "Apostila_T13_Servicos_de_Rede_TRT8"),
    ("T14", "T14 — Gerenciamento de Redes", "Apostila_T14_Gerenciamento_de_Redes_TRT8"),
    ("T15", "T15 — Nuvem Computacional", "Apostila_T15_Nuvem_Computacional_TRT8"),
    ("T16", "T16 — Segurança da Informação", "Apostila_T16_Seguranca_da_Informacao_TRT8"),
    ("T17", "T17 — Normativos PDPJ-Br", "Apostila_T17_Normativos_PDPJ-Br_TRT8"),
]
DIREITO = [
    ("CONST", "Direito Constitucional", "Apostila_Direito_Constitucional_TRT8"),
    ("ADM", "Direito Administrativo", "Apostila_Direito_Administrativo_TRT8"),
    ("LEG", "Noções de Legislação", "Apostila_Legislacao_TRT8"),
    ("DH", "Noções de Direitos Humanos", "Apostila_Direitos_Humanos_TRT8"),
    ("PCD", "Direitos das Pessoas com Deficiência", "Apostila_Direitos_das_Pessoas_com_Deficiencia_TRT8"),
]
GERAIS = [
    ("PORT", "Língua Portuguesa", "Apostila_Lingua_Portuguesa_TRT8"),
    ("MAT", "Matemática e Raciocínio Lógico", "Apostila_Matematica_e_Raciocinio_Logico_TRT8"),
]
CATEGORIES = [
    ("Tecnologia da Informação", TI),
    ("Direito e Legislação", DIREITO),
    ("Conhecimentos Gerais", GERAIS),
]


def extract_items(md_path):
    """Extrai os subtopicos (H1 de modulos/pegadinhas/questoes) do .md."""
    with open(md_path, encoding="utf-8") as fh:
        text = fh.read()
    items = []
    for line in text.splitlines():
        if not line.startswith("# "):
            continue
        heading = line[2:].strip()
        upper = heading.upper()
        if upper.startswith("MÓDULO") or upper.startswith("RESUMO DE PEGADINHAS") or upper.startswith("CADERNO"):
            items.append(re.sub(r"\s+", " ", heading))
    if not items:
        heads = [ln[2:].strip() if ln.startswith("# ") else ln[3:].strip()
                 for ln in text.splitlines() if ln.startswith("# ") or ln.startswith("## ")]
        items = [h for h in heads[2:] if h and not h.upper().startswith("TRT8")][:12]
    return items


def build_topics():
    topics = []
    for cat_name, entries in CATEGORIES:
        for tid, title, base in entries:
            md_v1 = os.path.join(HERE, base + ".md")
            md_v2 = os.path.join(HERE, base + "_v2.md")
            if not os.path.exists(md_v1) and not os.path.exists(md_v2):
                continue
            versions = []
            if os.path.exists(os.path.join(HERE, base + ".html")):
                versions.append({"label": "V1", "href": base + ".html"})
            if os.path.exists(os.path.join(HERE, base + "_v2.html")):
                versions.append({"label": "V2", "href": base + "_v2.html"})
            src = md_v2 if os.path.exists(md_v2) else md_v1
            items = [{"id": tid + "-i" + str(i), "text": t} for i, t in enumerate(extract_items(src))]
            topics.append({
                "id": tid,
                "title": title,
                "category": cat_name,
                "versions": versions,
                "items": items,
            })
    return topics


TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Portal de Estudos — TRT8 | Analista de TI</title>
<style>
:root{
  --bg:#f4f6fb; --card:#ffffff; --side:#10162a; --side2:#1a2340; --text:#1c2333;
  --muted:#667085; --smuted:#9aa6c2; --accent:#4f46e5; --accent2:#0d9488;
  --ok:#16a34a; --border:#e4e8f2; --sborder:#263149; --barbg:#e8ebf5; --hover:#243056;
  --shadow:0 4px 18px rgba(28,35,51,.08);
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#0f1420; --card:#171e2e; --text:#e8ecf6; --muted:#93a0b8;
    --border:#263149; --barbg:#232c42; --shadow:0 4px 18px rgba(0,0,0,.35);
  }
}
*{box-sizing:border-box}
html,body{height:100%}
body{
  margin:0;display:flex;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
  background:var(--bg);color:var(--text);overflow:hidden
}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
button{font-family:inherit}

/* ---------- MENU LATERAL ---------- */
#sidebar{
  width:320px;min-width:320px;height:100vh;background:var(--side);color:#e8ecf6;
  display:flex;flex-direction:column;border-right:1px solid var(--sborder);
  transition:margin-left .25s ease
}
#sidebar.collapsed{margin-left:-320px}
.side-head{padding:16px 16px 10px;border-bottom:1px solid var(--sborder)}
.side-head h1{margin:0;font-size:1.02rem;line-height:1.35}
.side-head p{margin:4px 0 10px;font-size:.76rem;color:var(--smuted)}
#search{
  width:100%;padding:9px 12px;border-radius:9px;border:1px solid var(--sborder);
  background:var(--side2);color:#e8ecf6;font-size:.86rem;outline:none
}
#search:focus{border-color:var(--accent)}
.side-progress{padding:12px 16px;border-bottom:1px solid var(--sborder)}
.side-progress .row{display:flex;justify-content:space-between;font-size:.78rem;color:var(--smuted);margin-bottom:6px}
.bar{height:8px;border-radius:99px;background:var(--side2);overflow:hidden}
.bar>.fill{height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#22d3ee,#4f46e5);transition:width .3s}

.side-nav{flex:1;overflow-y:auto;padding:8px 0 20px}
.side-nav::-webkit-scrollbar{width:8px}
.side-nav::-webkit-scrollbar-thumb{background:var(--sborder);border-radius:99px}

.cat-group{margin:2px 0 6px}
.cat-btn{
  width:100%;display:flex;align-items:center;gap:8px;padding:9px 14px;
  background:transparent;border:0;color:var(--smuted);font-size:.72rem;font-weight:700;
  letter-spacing:.6px;text-transform:uppercase;cursor:pointer;text-align:left
}
.cat-btn:hover{color:#fff;background:var(--hover)}
.cat-btn .chev{transition:transform .18s;font-size:.7rem}
.cat-group.open>.cat-btn .chev{transform:rotate(90deg)}
.cat-body{display:none;padding:2px 0 6px}
.cat-group.open>.cat-body{display:block}

.topic-block{margin:1px 8px;border-radius:10px;overflow:hidden}
.topic-btn{
  width:100%;display:flex;align-items:center;gap:8px;padding:8px 10px;
  background:transparent;border:0;color:#cdd6ee;font-size:.86rem;cursor:pointer;text-align:left;border-radius:9px
}
.topic-btn:hover{background:var(--hover);color:#fff}
.topic-btn .chev{font-size:.65rem;transition:transform .18s;color:var(--smuted);width:12px}
.topic-block.open>.topic-btn{background:var(--hover);color:#fff}
.topic-block.open>.topic-btn .chev{transform:rotate(90deg)}
.topic-btn .tname{flex:1;line-height:1.3}
.topic-btn .tbadge{
  font-size:.68rem;padding:2px 7px;border-radius:99px;background:var(--side2);color:var(--smuted);white-space:nowrap
}
.topic-btn .tbadge.has{background:var(--ok);color:#fff}
.topic-items{display:none;padding:2px 6px 8px 22px}
.topic-block.open>.topic-items{display:block}

.it{display:flex;gap:7px;align-items:flex-start;padding:5px 6px;border-radius:7px;cursor:pointer;font-size:.78rem;color:var(--smuted)}
.it:hover{background:var(--hover);color:#e8ecf6}
.it input{margin-top:2px;accent-color:var(--ok);width:14px;height:14px;flex-shrink:0;cursor:pointer}
.it.done span{text-decoration:line-through;color:#6b7694}
.it .txt{line-height:1.35}

.side-foot{padding:12px 16px;border-top:1px solid var(--sborder);display:flex;flex-direction:column;gap:8px}
.side-link{
  display:flex;align-items:center;gap:9px;padding:9px 12px;border-radius:9px;
  background:var(--side2);color:#cdd6ee;font-size:.86rem;cursor:pointer;border:0;width:100%;text-align:left
}
.side-link:hover{background:var(--hover);color:#fff}
.side-link.active{outline:2px solid var(--accent)}
.side-actions{display:flex;gap:8px}
.side-actions button{
  flex:1;padding:8px;border-radius:9px;border:1px solid var(--sborder);background:transparent;
  color:var(--smuted);font-size:.76rem;cursor:pointer
}
.side-actions button:hover{border-color:var(--accent);color:#fff}

/* ---------- CONTEUDO ---------- */
#content{flex:1;height:100vh;display:flex;flex-direction:column;min-width:0}
.topbar{
  display:flex;align-items:center;gap:12px;padding:12px 18px;background:var(--card);
  border-bottom:1px solid var(--border);box-shadow:var(--shadow);z-index:5
}
#btn-toggle{
  width:38px;height:38px;border-radius:10px;border:1px solid var(--border);background:transparent;
  font-size:1.1rem;cursor:pointer;color:var(--text);flex-shrink:0
}
#btn-toggle:hover{border-color:var(--accent);color:var(--accent)}
#page-title{font-size:1.05rem;font-weight:700;flex:1;line-height:1.3;min-width:0}
#page-title small{display:block;font-size:.75rem;font-weight:500;color:var(--muted)}
.ver-tabs{display:flex;gap:6px;flex-shrink:0}
.ver-tabs button{
  padding:7px 14px;border-radius:9px;border:1px solid var(--border);background:transparent;
  color:var(--muted);font-size:.8rem;font-weight:600;cursor:pointer
}
.ver-tabs button.on{background:var(--accent);border-color:var(--accent);color:#fff}

.view{flex:1;display:flex;min-height:0}
.view.hidden{display:none}

/* painel de checklist do topico aberto */
.check-panel{
  width:290px;min-width:290px;border-right:1px solid var(--border);background:var(--card);
  display:flex;flex-direction:column;height:100%
}
.check-head{padding:14px 14px 10px;border-bottom:1px solid var(--border)}
.check-head h3{margin:0 0 8px;font-size:.86rem;color:var(--accent2)}
.check-head .row{display:flex;justify-content:space-between;font-size:.75rem;color:var(--muted);margin-bottom:6px}
.check-head .bar{background:var(--barbg)}
.check-head .bar>.fill{background:linear-gradient(90deg,var(--accent),var(--accent2))}
.check-list{flex:1;overflow-y:auto;padding:8px}
.check-list .it{color:var(--muted)}
.check-list .it:hover{background:var(--barbg);color:var(--text)}
.check-list .it.done span{text-decoration:line-through;color:var(--muted);opacity:.7}
.check-foot{padding:10px 12px;border-top:1px solid var(--border);display:flex;gap:8px}
.check-foot button{
  flex:1;padding:8px;border-radius:9px;border:1px solid var(--border);background:transparent;
  color:var(--muted);font-size:.76rem;cursor:pointer
}
.check-foot button:hover{border-color:var(--accent);color:var(--accent)}

#frame-wrap{flex:1;min-width:0;height:100%;background:#fff}
#apostila-frame{width:100%;height:100%;border:0;display:block}

.ph-wrap{flex:1;overflow-y:auto;padding:28px}
.ph-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px;margin-top:16px}
.ph{border:2px dashed var(--border);border-radius:14px;padding:24px;text-align:center;color:var(--muted)}
.ph h4{margin:8px 0 6px;color:var(--text)}
.ph .tag{display:inline-block;padding:3px 10px;border-radius:99px;background:var(--barbg);font-size:.72rem;font-weight:700;letter-spacing:.4px;text-transform:uppercase}
h2.cat-title{margin:6px 0 4px;font-size:1.12rem;color:var(--accent2);border-left:5px solid var(--accent2);padding-left:10px}
.note{margin-top:18px;font-size:.86rem;color:var(--muted);line-height:1.65;max-width:820px}

.empty{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--muted);gap:10px;padding:30px;text-align:center}
.empty .big{font-size:3rem}

@media (max-width:900px){
  .check-panel{display:none}
  #sidebar{position:fixed;z-index:40;box-shadow:8px 0 30px rgba(0,0,0,.35)}
}
</style>
</head>
<body>

<aside id="sidebar">
  <div class="side-head">
    <h1>📚 Portal de Estudos — TRT8</h1>
    <p>Analista Judiciário · Analista de TI</p>
    <input id="search" type="search" placeholder="🔍 Filtrar apostilas e subtópicos…">
  </div>
  <div class="side-progress">
    <div class="row"><span id="gp-text">0 / 0 subtópicos</span><span id="gp-pct">0%</span></div>
    <div class="bar"><div class="fill" id="gp-fill"></div></div>
  </div>
  <nav class="side-nav" id="side-nav"></nav>
  <div class="side-foot">
    <button class="side-link" data-page="revisao">🔁 Revisão <em style="margin-left:auto;font-style:normal;font-size:.7rem;color:#6b7694">em breve</em></button>
    <button class="side-link" data-page="exercicios">✏️ Exercícios <em style="margin-left:auto;font-style:normal;font-size:.7rem;color:#6b7694">em breve</em></button>
    <div class="side-actions">
      <button id="btn-expandir">▾ expandir tudo</button>
      <button id="btn-reset">limpar progresso</button>
    </div>
  </div>
</aside>

<section id="content">
  <div class="topbar">
    <button id="btn-toggle" title="Mostrar/ocultar menu lateral">☰</button>
    <div id="page-title">Bem-vindo!<small>Escolha uma apostila no menu lateral</small></div>
    <div class="ver-tabs" id="ver-tabs"></div>
  </div>

  <div class="view" id="view-apostila">
    <aside class="check-panel" id="check-panel">
      <div class="check-head">
        <h3>✅ Marcar como estudado</h3>
        <div class="row"><span id="cp-text">0 / 0</span><span id="cp-pct">0%</span></div>
        <div class="bar"><div class="fill" id="cp-fill"></div></div>
      </div>
      <div class="check-list" id="check-list"></div>
      <div class="check-foot">
        <button id="cp-all">✓ tudo lido</button>
        <button id="cp-none">✗ limpar</button>
      </div>
    </aside>
    <div id="frame-wrap">
      <iframe id="apostila-frame" title="Apostila"></iframe>
    </div>
  </div>

  <div class="view hidden" id="view-revisao">
    <div class="ph-wrap">
      <h2 class="cat-title">Área de Revisão — espaço reservado</h2>
      <div class="ph-grid">
        <div class="ph"><span class="tag">em breve</span><h4>Revisão espaçada</h4>
          <p>Cronograma automático (1d · 7d · 15d · 30d) por apostila concluída, com alertas do que revisar em cada dia.</p></div>
        <div class="ph"><span class="tag">em breve</span><h4>Flashcards de pegadinhas</h4>
          <p>Cards viráveis com as pegadinhas de cada tópico, para revisão ativa rápida.</p></div>
        <div class="ph"><span class="tag">em breve</span><h4>Mapa de pontos fracos</h4>
          <p>Cruzamento do seu progresso com o desempenho nos exercícios, destacando os subtópicos a reforçar.</p></div>
      </div>
      <p class="note">Este é o espaço que construiremos juntos na próxima etapa. Nada aqui é salvo ainda.</p>
    </div>
  </div>

  <div class="view hidden" id="view-exercicios">
    <div class="ph-wrap">
      <h2 class="cat-title">Exercícios — espaço reservado</h2>
      <div class="ph-grid">
        <div class="ph"><span class="tag">em breve</span><h4>Banco de questões por tópico</h4>
          <p>Questões objetivas e discursivas organizadas por apostila, no estilo FCC/CEBRASPE/FGV, com correção comentada.</p></div>
        <div class="ph"><span class="tag">em breve</span><h4>Simulados</h4>
          <p>Provas cronometradas misturando tópicos, com gabarito e estatísticas de acerto por disciplina.</p></div>
        <div class="ph"><span class="tag">em breve</span><h4>Redação e discursivas</h4>
          <p>Modelos de resposta e correção das questões discursivas das apostilas.</p></div>
      </div>
      <p class="note">Os cadernos de questões comentados já existem dentro de cada apostila; aqui reuniremos tudo em um único banco de exercícios navegável.</p>
    </div>
  </div>

  <div class="view hidden" id="view-welcome">
    <div class="empty">
      <div class="big">📖</div>
      <h2>Portal de Estudos TRT8</h2>
      <p>Abra o menu lateral, expanda uma apostila e comece a estudar.<br>
      Marque os subtópicos conforme avança — o progresso fica salvo neste navegador.</p>
    </div>
  </div>
</section>

<script>
const DATA = __DATA__;
const KEY = 'portal_trt8_progress_v1';

let state = {};
try { state = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { state = {}; }

let currentTopic = null;
let currentVersion = null;

function save() {
  try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
}
function isDone(id) { return !!state[id]; }
function topicStats(t) {
  let done = 0;
  t.items.forEach(function (it) { if (isDone(it.id)) done++; });
  return { done: done, total: t.items.length };
}
function refreshGlobal() {
  let done = 0, total = 0;
  DATA.forEach(function (t) { const s = topicStats(t); done += s.done; total += s.total; });
  const pct = total ? Math.round(done * 100 / total) : 0;
  document.getElementById('gp-text').textContent = done + ' / ' + total + ' subtópicos';
  document.getElementById('gp-fill').style.width = pct + '%';
  document.getElementById('gp-pct').textContent = pct + '%';
}
function refreshBadges(t) {
  const badge = document.querySelector('.topic-btn[data-topic="' + t.id + '"] .tbadge');
  if (badge) {
    const s = topicStats(t);
    badge.textContent = s.done + '/' + s.total;
    badge.className = 'tbadge' + (s.total && s.done === s.total ? ' has' : '');
  }
}
function refreshTopicPanel(t) {
  const s = topicStats(t);
  const pct = s.total ? Math.round(s.done * 100 / s.total) : 0;
  document.getElementById('cp-text').textContent = s.done + ' / ' + s.total + ' subtópicos';
  document.getElementById('cp-pct').textContent = pct + '%';
  document.getElementById('cp-fill').style.width = pct + '%';
}

/* ---------- construção do menu lateral ---------- */
function makeCheckbox(it, onChange) {
  const wrap = document.createElement('label');
  wrap.className = 'it' + (isDone(it.id) ? ' done' : '');
  const cb = document.createElement('input');
  cb.type = 'checkbox';
  cb.checked = isDone(it.id);
  cb.dataset.itemId = it.id;
  cb.addEventListener('change', function () {
    if (cb.checked) state[it.id] = true; else delete state[it.id];
    save();
    syncCheckbox(it.id, cb.checked);
    const t = findTopicByItem(it.id);
    if (t) { refreshBadges(t); if (currentTopic && currentTopic.id === t.id) refreshTopicPanel(t); }
    refreshGlobal();
  });
  const txt = document.createElement('span');
  txt.className = 'txt';
  txt.textContent = it.text;
  wrap.appendChild(cb);
  wrap.appendChild(txt);
  return wrap;
}

function syncCheckbox(itemId, checked) {
  document.querySelectorAll('input[data-item-id="' + itemId + '"]').forEach(function (cb) {
    cb.checked = checked;
    const wrap = cb.closest('.it');
    if (wrap) wrap.className = 'it' + (checked ? ' done' : '');
  });
}

function findTopicByItem(itemId) {
  for (let i = 0; i < DATA.length; i++) {
    if (DATA[i].items.some(function (x) { return x.id === itemId; })) return DATA[i];
  }
  return null;
}
function findTopic(id) {
  return DATA.find(function (t) { return t.id === id; });
}

function renderSidebar() {
  const nav = document.getElementById('side-nav');
  nav.textContent = '';
  const cats = [];
  DATA.forEach(function (t) { if (cats.indexOf(t.category) < 0) cats.push(t.category); });

  cats.forEach(function (cat) {
    const group = document.createElement('div');
    group.className = 'cat-group open';
    group.dataset.cat = cat.toLowerCase();

    const btn = document.createElement('button');
    btn.className = 'cat-btn';
    btn.innerHTML = '<span class="chev">▸</span><span>' + cat + '</span>';
    btn.addEventListener('click', function () { group.classList.toggle('open'); });
    group.appendChild(btn);

    const body = document.createElement('div');
    body.className = 'cat-body';

    DATA.filter(function (t) { return t.category === cat; }).forEach(function (t) {
      const block = document.createElement('div');
      block.className = 'topic-block';
      block.dataset.topic = t.id;

      const tbtn = document.createElement('button');
      tbtn.className = 'topic-btn';
      tbtn.dataset.topic = t.id;
      const s = topicStats(t);
      tbtn.innerHTML = '<span class="chev">▸</span>' +
        '<span class="tname">' + t.title + '</span>' +
        '<span class="tbadge' + (s.total && s.done === s.total ? ' has' : '') + '">' + s.done + '/' + s.total + '</span>';
      tbtn.addEventListener('click', function () {
        block.classList.toggle('open');
        if (block.classList.contains('open')) openTopic(t.id);
      });
      block.appendChild(tbtn);

      const items = document.createElement('div');
      items.className = 'topic-items';
      t.items.forEach(function (it) { items.appendChild(makeCheckbox(it)); });
      block.appendChild(items);
      body.appendChild(block);
    });
    group.appendChild(body);
    nav.appendChild(group);
  });
}

/* ---------- conteúdo: abrir apostila na mesma página ---------- */
function openTopic(id) {
  const t = findTopic(id);
  if (!t || !t.versions.length) return;
  currentTopic = t;

  // destaque no menu
  document.querySelectorAll('.topic-block').forEach(function (b) {
    if (b.dataset.topic === id) b.classList.add('open');
  });
  document.querySelectorAll('.side-link').forEach(function (l) { l.classList.remove('active'); });

  // título
  const title = document.getElementById('page-title');
  title.textContent = '';
  title.appendChild(document.createTextNode(t.title));
  const small = document.createElement('small');
  small.textContent = 'marque os subtópicos conforme estuda — à esquerda ou no menu lateral';
  title.appendChild(small);

  // abas de versão (V1 / V2)
  const vt = document.getElementById('ver-tabs');
  vt.textContent = '';
  t.versions.forEach(function (v, i) {
    const b = document.createElement('button');
    b.textContent = v.label + (v.label === 'V2' ? ' · completa' : '');
    b.className = (i === t.versions.length - 1) ? 'on' : '';
    b.addEventListener('click', function () {
      vt.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      currentVersion = v.href;
      document.getElementById('apostila-frame').src = v.href;
    });
    vt.appendChild(b);
  });
  // versão inicial: V2 se existir, senão a última
  const initial = t.versions[t.versions.length - 1];
  currentVersion = initial.href;

  // iframe
  const frame = document.getElementById('apostila-frame');
  frame.src = initial.href;

  // painel de checklist
  const list = document.getElementById('check-list');
  list.textContent = '';
  t.items.forEach(function (it) { list.appendChild(makeCheckbox(it)); });
  refreshTopicPanel(t);

  // mostrar view de apostila
  showView('apostila');
}

function showView(name) {
  ['apostila', 'revisao', 'exercicios', 'welcome'].forEach(function (n) {
    document.getElementById('view-' + n).classList.toggle('hidden', n !== name);
  });
}

/* ---------- eventos globais ---------- */
document.getElementById('btn-toggle').addEventListener('click', function () {
  document.getElementById('sidebar').classList.toggle('collapsed');
});

document.getElementById('search').addEventListener('input', function (ev) {
  const q = ev.target.value.trim().toLowerCase();
  document.querySelectorAll('.topic-block').forEach(function (block) {
    const t = findTopic(block.dataset.topic);
    if (!t) return;
    const hay = (t.title + ' ' + t.items.map(function (i) { return i.text; }).join(' ')).toLowerCase();
    const match = !q || hay.indexOf(q) >= 0;
    block.style.display = match ? '' : 'none';
    if (q && match) block.classList.add('open');
    if (!q) block.classList.remove('open');
  });
  document.querySelectorAll('.cat-group').forEach(function (g) {
    const any = Array.from(g.querySelectorAll('.topic-block')).some(function (b) { return b.style.display !== 'none'; });
    g.style.display = any ? '' : 'none';
    if (q) g.classList.add('open');
  });
});

document.getElementById('btn-expandir').addEventListener('click', function () {
  const blocks = document.querySelectorAll('.topic-block');
  const anyClosed = Array.from(blocks).some(function (b) { return !b.classList.contains('open'); });
  blocks.forEach(function (b) {
    if (b.style.display === 'none') return;
    b.classList.toggle('open', anyClosed);
  });
  this.textContent = anyClosed ? '▴ recolher tudo' : '▾ expandir tudo';
});

document.getElementById('btn-reset').addEventListener('click', function () {
  if (!confirm('Apagar TODO o progresso marcado neste navegador?')) return;
  state = {}; save();
  document.querySelectorAll('input[data-item-id]').forEach(function (cb) {
    cb.checked = false;
    const wrap = cb.closest('.it');
    if (wrap) wrap.className = 'it';
  });
  DATA.forEach(function (t) { refreshBadges(t); });
  if (currentTopic) refreshTopicPanel(currentTopic);
  refreshGlobal();
});

document.getElementById('cp-all').addEventListener('click', function () {
  if (!currentTopic) return;
  currentTopic.items.forEach(function (it) { state[it.id] = true; save(); syncCheckbox(it.id, true); });
  refreshBadges(currentTopic); refreshTopicPanel(currentTopic); refreshGlobal();
});
document.getElementById('cp-none').addEventListener('click', function () {
  if (!currentTopic) return;
  currentTopic.items.forEach(function (it) { delete state[it.id]; save(); syncCheckbox(it.id, false); });
  refreshBadges(currentTopic); refreshTopicPanel(currentTopic); refreshGlobal();
});

document.querySelectorAll('.side-link[data-page]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    document.querySelectorAll('.side-link').forEach(function (l) { l.classList.remove('active'); });
    btn.classList.add('active');
    const name = btn.dataset.page;
    document.getElementById('page-title').innerHTML =
      (name === 'revisao' ? 'Área de Revisão<small>espaço reservado — em breve</small>' : 'Exercícios<small>espaço reservado — em breve</small>');
    document.getElementById('ver-tabs').textContent = '';
    showView(name);
  });
});

// inicia
renderSidebar();
refreshGlobal();
showView('welcome');
</script>
</body>
</html>
"""


def main():
    topics = build_topics()
    n_items = sum(len(t["items"]) for t in topics)
    data_json = json.dumps(topics, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", data_json)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("OK: %s (%d topicos, %d subtopicos, %d bytes)" % (OUT, len(topics), n_items, len(html.encode("utf-8"))))


if __name__ == "__main__":
    main()