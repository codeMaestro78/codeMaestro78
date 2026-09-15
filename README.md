<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>devarshi.dev — /workspace</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
  :root{
    --bg-void:#0a0b0e;
    --bg-panel:#111319;
    --bg-elevated:#15171f;
    --bg-hover:#1b1e27;
    --bg-active:#1d2029;
    --border:#242835;
    --border-soft:#1a1d26;
    --text-primary:#e9e6df;
    --text-dim:#848a9c;
    --text-faint:#4b4f5e;
    --amber:#e8a33d;
    --amber-dim:#5f4a24;
    --cyan:#5fc8c2;
    --rose:#e8607a;
    --sage:#8fbf7f;
    --font-display:'Space Grotesk', sans-serif;
    --font-mono:'IBM Plex Mono', monospace;
    --topbar-h:44px;
    --statusbar-h:26px;
  }
  *{box-sizing:border-box;}
  html,body{
    margin:0; padding:0; height:100%;
    background:var(--bg-void); color:var(--text-primary);
    font-family:var(--font-mono);
    overflow:hidden;
    -webkit-font-smoothing:antialiased;
  }
  ::selection{ background:var(--amber-dim); color:var(--amber); }
  button{ font-family:inherit; cursor:pointer; }
  input{ font-family:inherit; }

  /* ---------- background texture ---------- */
  #bgGrid{
    position:fixed; inset:-2%; z-index:0; pointer-events:none;
    background-image:
      linear-gradient(rgba(232,163,61,0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(232,163,61,0.035) 1px, transparent 1px);
    background-size:42px 42px;
    transition:transform .25s ease-out;
  }
  #bgVignette{
    position:fixed; inset:0; z-index:1; pointer-events:none;
    background:radial-gradient(ellipse at 50% 20%, rgba(232,163,61,0.05), transparent 55%),
                radial-gradient(ellipse at 50% 120%, rgba(0,0,0,0.6), transparent 60%);
  }
  #scan{
    position:fixed; inset:0; z-index:2; pointer-events:none; opacity:.5;
    background:repeating-linear-gradient(
      to bottom, rgba(255,255,255,0.012) 0px, rgba(255,255,255,0.012) 1px,
      transparent 1px, transparent 3px
    );
    animation:flicker 6s infinite steps(30);
  }
  @keyframes flicker{
    0%,100%{opacity:.5;} 42%{opacity:.5;} 43%{opacity:.42;} 44%{opacity:.5;}
    77%{opacity:.5;} 78%{opacity:.46;} 79%{opacity:.5;}
  }

  /* ---------- boot screen ---------- */
  #boot{
    position:fixed; inset:0; z-index:50; background:var(--bg-void);
    display:flex; align-items:center; justify-content:center;
    transition:opacity .6s ease, filter .6s ease;
  }
  #boot.hide{ opacity:0; filter:blur(6px); pointer-events:none; }
  #bootInner{ width:min(640px, 86vw); }
  #bootLog{
    font-size:13px; line-height:1.75; color:var(--text-dim); white-space:pre-wrap;
    min-height:220px;
  }
  #bootLog .ok{ color:var(--sage); }
  #bootLog .tag{ color:var(--amber); }
  #bootBarTrack{
    margin-top:18px; height:3px; width:100%; background:var(--border-soft); position:relative; overflow:hidden;
  }
  #bootBarFill{ position:absolute; inset:0 100% 0 0; background:var(--amber); transition:right .18s linear; }
  #bootHint{ margin-top:14px; font-size:11px; color:var(--text-faint); letter-spacing:.02em; }
  #bootCaret{ display:inline-block; width:7px; height:13px; background:var(--amber); vertical-align:-2px; animation:blink 1s step-end infinite; }
  @keyframes blink{ 50%{ opacity:0; } }

  /* ---------- app shell ---------- */
  #app{
    position:relative; z-index:3; height:100vh; display:flex; flex-direction:column;
    opacity:0; transition:opacity .7s ease;
  }
  #app.show{ opacity:1; }

  /* top bar */
  #topbar{
    height:var(--topbar-h); flex:0 0 auto; display:flex; align-items:stretch;
    background:var(--bg-elevated); border-bottom:1px solid var(--border);
  }
  #trafficWrap{ display:flex; align-items:center; gap:7px; padding:0 14px; border-right:1px solid var(--border); }
  .dot{ width:10px; height:10px; border-radius:50%; }
  .dot.r{ background:#e8607a; } .dot.y{ background:#e8b93d; } .dot.g{ background:#7bc96f; }
  #menuBtn{ display:none; background:none; border:none; color:var(--text-dim); padding:0 12px; font-size:16px; }

  #tabbar{ flex:1 1 auto; display:flex; align-items:stretch; overflow-x:auto; scrollbar-width:none; }
  #tabbar::-webkit-scrollbar{ display:none; }
  .tab{
    display:flex; align-items:center; gap:8px; padding:0 12px; height:100%;
    border-right:1px solid var(--border); color:var(--text-dim); font-size:12.5px;
    white-space:nowrap; background:transparent; position:relative;
  }
  .tab .ic{ opacity:.75; font-size:12px; }
  .tab.active{ color:var(--text-primary); background:var(--bg-panel); }
  .tab.active::after{
    content:""; position:absolute; left:0; right:0; top:-1px; height:2px; background:var(--amber);
  }
  .tab .close{ opacity:0; border:none; background:none; color:var(--text-faint); font-size:13px; padding:0 2px; line-height:1; }
  .tab:hover .close{ opacity:.8; }
  .tab .close:hover{ color:var(--rose); }

  #topRight{ display:flex; align-items:center; gap:2px; border-left:1px solid var(--border); }
  .iconbtn{
    background:none; border:none; color:var(--text-dim); font-size:12px; height:100%;
    padding:0 13px; display:flex; align-items:center; gap:6px; border-left:1px solid var(--border-soft);
  }
  .iconbtn:hover{ color:var(--amber); background:var(--bg-hover); }
  #clock{ font-size:11.5px; color:var(--text-faint); padding:0 14px; display:flex; align-items:center; letter-spacing:.03em; }

  /* body row */
  #body{ flex:1 1 auto; display:flex; min-height:0; position:relative; }

  /* sidebar */
  #sidebar{
    width:242px; flex:0 0 auto; background:var(--bg-elevated); border-right:1px solid var(--border);
    overflow-y:auto; padding:14px 0 10px;
  }
  #sidebarHead{
    font-size:10.5px; letter-spacing:.12em; color:var(--text-faint); padding:0 16px 10px;
    font-family:var(--font-display); font-weight:600;
  }
  .tree-item{
    display:flex; align-items:center; gap:8px; padding:5px 16px; font-size:12.5px; color:var(--text-dim);
    cursor:pointer; user-select:none;
  }
  .tree-item:hover{ background:var(--bg-hover); color:var(--text-primary); }
  .tree-item.open{ background:var(--bg-active); color:var(--amber); }
  .tree-item .ic{ width:14px; text-align:center; opacity:.8; font-size:11px; }
  .tree-folder{ padding-left:16px; }
  .tree-folder .tree-item{ padding-left:16px; }
  .chev{ display:inline-block; width:10px; transition:transform .18s ease; font-size:9px; color:var(--text-faint); }
  .chev.expanded{ transform:rotate(90deg); }
  .tree-children{ overflow:hidden; max-height:0; transition:max-height .22s ease; }
  .tree-children.expanded{ max-height:220px; }
  .tree-children .tree-item{ padding-left:34px; }

  #sidebarFoot{ margin-top:16px; padding:12px 16px 0; border-top:1px solid var(--border-soft); }
  .stat-line{ display:flex; justify-content:space-between; font-size:11px; color:var(--text-faint); padding:3px 0; }
  .stat-line b{ color:var(--text-dim); font-weight:500; }

  /* editor + minimap row */
  #editorRow{ flex:1 1 auto; display:flex; min-width:0; min-height:0; }
  #editorScroll{ flex:1 1 auto; overflow-y:auto; background:var(--bg-panel); position:relative; }
  #editorPad{ padding:22px 0 60px; max-width:840px; }
  .code-line{ display:flex; }
  .gutter{
    flex:0 0 auto; width:46px; text-align:right; padding-right:16px; color:var(--text-faint);
    font-size:12.5px; user-select:none; opacity:.55;
  }
  .code-line:hover .gutter{ color:var(--amber); opacity:.9; }
  .code-line:hover{ background:rgba(232,163,61,0.035); }
  .code-text{ white-space:pre-wrap; word-break:break-word; font-size:13px; line-height:1.72; padding-right:24px; }

  .tok-key{ color:var(--cyan); } .tok-str{ color:var(--sage); } .tok-num{ color:var(--amber); }
  .tok-bool{ color:var(--rose); } .tok-punc{ color:var(--text-faint); } .tok-comment{ color:var(--text-faint); font-style:italic; }
  .tok-head{ color:var(--amber); font-weight:600; font-family:var(--font-display); }
  .tok-bullet{ color:var(--amber); } .tok-label{ color:var(--cyan); }
  .tok-dim{ color:var(--text-faint); }
  .tok-strong{ color:var(--text-primary); font-weight:600; }
  .tok-link{ color:var(--cyan); text-decoration:underline; text-decoration-color:rgba(95,200,194,.35); }

  #emptyState{
    flex:1; display:flex; align-items:center; justify-content:center; flex-direction:column; gap:10px; color:var(--text-faint);
  }
  #emptyState .glyph{ font-size:30px; opacity:.5; }
  #emptyState p{ font-size:12.5px; }
  #emptyState kbd{ background:var(--bg-elevated); border:1px solid var(--border); padding:2px 6px; border-radius:3px; color:var(--text-dim); font-size:11px; }

  /* minimap */
  #minimap{
    width:78px; flex:0 0 auto; background:var(--bg-panel); border-left:1px solid var(--border-soft);
    padding:14px 10px; overflow:hidden; cursor:pointer;
  }
  .mm-line{ height:2px; margin-bottom:3px; background:var(--text-faint); opacity:.28; border-radius:1px; }
  .mm-line.h1{ background:var(--amber); opacity:.55; }
  .mm-line.h2{ background:var(--cyan); opacity:.4; }
  #mmViewport{ position:absolute; right:0; width:78px; border-top:1px solid var(--amber-dim); border-bottom:1px solid var(--amber-dim); background:rgba(232,163,61,0.05); pointer-events:none; }

  /* terminal drawer */
  #terminal{
    flex:0 0 auto; height:0; overflow:hidden; background:var(--bg-void); border-top:1px solid var(--border);
    display:flex; flex-direction:column; transition:height .22s ease;
  }
  #terminal.open{ height:260px; }
  #termHead{
    display:flex; align-items:center; justify-content:space-between; padding:7px 14px; border-bottom:1px solid var(--border-soft);
    font-size:11px; color:var(--text-faint); letter-spacing:.05em; flex:0 0 auto;
  }
  #termHead .lbl{ display:flex; align-items:center; gap:7px; }
  #termHead .lbl .pulse{ width:6px; height:6px; border-radius:50%; background:var(--sage); box-shadow:0 0 6px var(--sage); }
  #termClose{ background:none; border:none; color:var(--text-faint); font-size:14px; }
  #termClose:hover{ color:var(--rose); }
  #termBody{ flex:1 1 auto; overflow-y:auto; padding:10px 14px; font-size:12.5px; line-height:1.7; }
  .term-line{ white-space:pre-wrap; word-break:break-word; }
  .term-prompt{ color:var(--amber); }
  .term-path{ color:var(--cyan); }
  .term-out{ color:var(--text-dim); }
  .term-err{ color:var(--rose); }
  .term-hd{ color:var(--text-primary); font-weight:600; }
  #termInputRow{ display:flex; align-items:center; padding:8px 14px 12px; gap:8px; flex:0 0 auto; }
  #termInputRow .term-prompt{ flex:0 0 auto; }
  #termInput{
    flex:1 1 auto; background:none; border:none; outline:none; color:var(--text-primary); font-size:12.5px; caret-color:var(--amber);
  }

  /* status bar */
  #statusbar{
    height:var(--statusbar-h); flex:0 0 auto; background:var(--amber); color:#191207;
    display:flex; align-items:center; justify-content:space-between; font-size:11px; padding:0 12px;
    font-weight:500; letter-spacing:.01em;
  }
  #statusbar .grp{ display:flex; align-items:center; gap:14px; height:100%; }
  #statusbar .sitem{ display:flex; align-items:center; gap:5px; }
  #statusbar button{ background:none; border:none; color:#191207; font-size:11px; font-weight:500; }
  #statusbar button:hover{ opacity:.7; }

  /* command palette */
  #paletteOverlay{
    position:fixed; inset:0; z-index:40; background:rgba(5,6,8,0.55); backdrop-filter:blur(2px);
    display:none; align-items:flex-start; justify-content:center; padding-top:14vh;
  }
  #paletteOverlay.open{ display:flex; }
  #palette{
    width:min(520px, 90vw); background:var(--bg-elevated); border:1px solid var(--border);
    box-shadow:0 20px 60px rgba(0,0,0,.5); animation:paletteIn .14s ease;
  }
  @keyframes paletteIn{ from{ transform:translateY(-6px); opacity:0;} to{ transform:translateY(0); opacity:1;} }
  #paletteInputRow{ display:flex; align-items:center; gap:10px; padding:13px 16px; border-bottom:1px solid var(--border); }
  #paletteInputRow span{ color:var(--amber); font-size:13px; }
  #paletteInput{ flex:1; background:none; border:none; outline:none; color:var(--text-primary); font-size:13.5px; }
  #paletteList{ max-height:280px; overflow-y:auto; padding:6px; }
  .pitem{ display:flex; align-items:center; gap:10px; padding:9px 10px; font-size:12.5px; color:var(--text-dim); }
  .pitem .ic{ width:16px; text-align:center; opacity:.7; }
  .pitem .meta{ margin-left:auto; font-size:10.5px; color:var(--text-faint); }
  .pitem.sel{ background:var(--bg-hover); color:var(--text-primary); }
  .pitem.sel .ic{ color:var(--amber); }

  /* mobile */
  @media (max-width: 860px){
    #menuBtn{ display:flex; align-items:center; }
    #sidebar{
      position:absolute; left:0; top:0; bottom:0; z-index:20; transform:translateX(-100%);
      transition:transform .2s ease; box-shadow:20px 0 40px rgba(0,0,0,.4);
    }
    #sidebar.open{ transform:translateX(0); }
    #minimap{ display:none; }
    #editorPad{ padding:16px 0 60px; }
    .gutter{ width:32px; padding-right:8px; }
  }

  @media (prefers-reduced-motion: reduce){
    *{ animation-duration:.001ms !important; transition-duration:.001ms !important; }
  }
</style>
</head>
<body>

<div id="bgGrid"></div>
<div id="bgVignette"></div>
<div id="scan"></div>

<!-- boot -->
<div id="boot">
  <div id="bootInner">
    <div id="bootLog"></div>
    <div id="bootBarTrack"><div id="bootBarFill"></div></div>
    <div id="bootHint">press any key to skip<span id="bootCaret"></span></div>
  </div>
</div>

<!-- app -->
<div id="app">
  <div id="topbar">
    <button id="menuBtn" class="iconbtn" aria-label="toggle sidebar">☰</button>
    <div id="trafficWrap">
      <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    </div>
    <div id="tabbar"></div>
    <div id="topRight">
      <button class="iconbtn" id="paletteBtn">⌘K &nbsp;jump to…</button>
      <button class="iconbtn" id="termToggleBtn">⌁ terminal</button>
      <div id="clock">--:--:-- IST</div>
    </div>
  </div>

  <div id="body">
    <aside id="sidebar">
      <div id="sidebarHead">EXPLORER — devarshi/workspace</div>
      <div id="tree"></div>
      <div id="sidebarFoot">
        <div class="stat-line"><span>role</span><b>AI/ML · Full-Stack</b></div>
        <div class="stat-line"><span>based in</span><b>Ahmedabad, IN</b></div>
        <div class="stat-line"><span>status</span><b style="color:var(--sage)">available</b></div>
      </div>
    </aside>

    <div id="editorRow">
      <div id="editorScroll">
        <div id="editorPad"></div>
      </div>
      <div id="emptyState" style="display:none;">
        <div class="glyph">◈</div>
        <p>No file open — press <kbd>⌘K</kbd> to jump to one</p>
      </div>
      <div id="minimap"><div id="mmViewport"></div></div>
    </div>
  </div>

  <div id="terminal">
    <div id="termHead">
      <div class="lbl"><span class="pulse"></span> TERMINAL — bash</div>
      <button id="termClose">✕</button>
    </div>
    <div id="termBody"></div>
    <div id="termInputRow">
      <span class="term-prompt">devarshi@portfolio</span><span class="term-out">:</span><span class="term-path">~</span><span class="term-out">$</span>
      <input id="termInput" autocomplete="off" spellcheck="false" />
    </div>
  </div>

  <div id="statusbar">
    <div class="grp">
      <div class="sitem">⎇ main</div>
      <div class="sitem" id="stActiveLang">plaintext</div>
      <div class="sitem" id="stLnCol">Ln 1, Col 1</div>
    </div>
    <div class="grp">
      <button id="stContact">✉ say hello</button>
      <div class="sitem">UTF-8</div>
      <div class="sitem">AI Engineer Mode: ON</div>
    </div>
  </div>
</div>

<!-- command palette -->
<div id="paletteOverlay">
  <div id="palette">
    <div id="paletteInputRow"><span>⌘</span><input id="paletteInput" placeholder="Jump to a file or run a command…" /></div>
    <div id="paletteList"></div>
  </div>
</div>

<script>
(function(){
  "use strict";
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ============================= DATA ============================= */
  var FILES = {
    "about.md": {
      lang:"markdown", icon:"◆",
      raw:
"# about.md\n\n"+
"**Devarshi Lalani**\n"+
"AI/ML Engineer · Full-Stack Engineer\n\n"+
"Based in Ahmedabad, Gujarat, IN · UTC+05:30\n\n"+
"## summary\n"+
"AI Engineer with hands-on experience building LLM-powered\n"+
"applications, agentic workflows, and AI orchestration platforms,\n"+
"backed by a strong software engineering foundation in Python and\n"+
"full-stack development. Experienced with LangChain/LangGraph\n"+
"pipelines, retrieval-grounded AI features, and ML/DL fundamentals.\n\n"+
"## currently\n"+
"Software Development Engineer @ Acqurie.io\n"+
"Mar 2026 – Present\n\n"+
"## education\n"+
"B.E. Computer Science and Technology\n"+
"L J University, Ahmedabad, India — Nov 2022 – Sept 2026"
    },
    "skills.json": {
      lang:"json", icon:"{ }",
      raw:
"{\n"+
'  "generative_ai_llm": ["OpenAI API", "Gemini", "HuggingFace", "LangChain", "RAG", "Prompt Engineering", "Vector DBs (FAISS)"],\n'+
'  "ai_agents_orchestration": ["Agentic workflows", "LangGraph", "AI tools/skills", "AI orchestration platforms"],\n'+
'  "machine_learning": ["Scikit-learn", "Regression", "Classification", "Clustering", "Feature Engineering", "NLP", "Embeddings", "VADER"],\n'+
'  "deep_learning": ["TensorFlow", "ANN", "LSTM", "CNN", "RNN/GRU"],\n'+
'  "languages": ["Python", "TypeScript", "JavaScript", "Java", "C++"],\n'+
'  "frontend": ["React.js", "Tailwind CSS"],\n'+
'  "backend": ["Node.js", "FastAPI", "Django", "REST APIs"],\n'+
'  "data": ["PostgreSQL", "Prisma ORM", "Redis", "Pandas", "NumPy", "SQL"],\n'+
'  "cloud_devops": ["AWS", "Google Cloud Vertex AI", "Vercel", "Railway", "Docker", "Git", "Postman"]\n'+
"}"
    },
    "experience.log": {
      lang:"log", icon:"☰",
      raw:
"commit a1c2f9e  (HEAD -> main, acqurie.io)\n"+
"Date:   Mar 2026 – Present\n\n"+
"    Software Development Engineer @ Acqurie.io\n\n"+
"    - Built agentic AI workflows and orchestration features for a\n"+
"      multi-tenant platform (LangChain, LangGraph, RAG-based tools)\n"+
"    - Designed an LLM usage-metering & credit system to track and\n"+
"      bill LLM consumption per tenant\n"+
"    - Implemented Stripe subscription billing for the platform's\n"+
"      V2 product\n"+
"    - Contributed backend + frontend platform work (Python,\n"+
"      TypeScript, Node.js, React) for AI-driven product features\n\n"+
"commit 7b40dd1  (fxis.ai)\n"+
"Date:   Jan 2026 – Mar 2026\n\n"+
"    Machine Learning Intern @ fxis.ai\n\n"+
"    - Studied and applied supervised & unsupervised ML algorithms\n"+
"    - Strengthened foundations in classical ML and deep learning\n"+
"    - Hands-on exposure to ML/DL experimentation workflows\n\n"+
"commit 2e91c05  (feynn-labs)\n"+
"Date:   Feb 2025 – Jun 2025\n\n"+
"    Machine Learning Intern @ Feynn Labs\n\n"+
"    - Designed AI agents automating market segmentation analysis,\n"+
"      helping SMBs identify high-value prospects 40% faster\n"+
"    - Built a regression-based financial health optimizer\n"+
"      (95% model accuracy) forecasting SME cash flow\n"+
"    - Developed financial modeling algorithms supporting\n"+
"      data-driven decision-making"
    },
    "projects/allotiq.md": {
      lang:"markdown", icon:"◆",
      raw:
"# AllotIQ — Agentic IPO Intelligence Platform\n"+
"live: allotiq.in\n\n"+
"- AI workspace generating LLM-based company briefs, structured\n"+
"  multi-section analyst reports with citations, and a grounded\n"+
"  research chat — LangChain + GPT-4o-mini on a FastAPI backend\n"+
"- Guardrails against hallucination (citation validation,\n"+
"  report-structure enforcement) plus cost controls (response\n"+
"  caching, rate/usage budgets)\n"+
"- Deterministic scoring engine (subscription, GMP, sentiment,\n"+
"  institutional signals) combined with LLM analysis to produce\n"+
"  apply/wait/avoid recommendations\n"+
"- Deployed the AI service + scheduled data pipelines on Railway,\n"+
"  feeding a PostgreSQL/Prisma backend on Vercel\n\n"+
"stack: LangChain · FastAPI · GPT-4o-mini · PostgreSQL · Prisma · Railway · Vercel"
    },
    "projects/mlcli.md": {
      lang:"markdown", icon:"◆",
      raw:
"# MLCLI — Open-Source ML/DL Training CLI\n"+
"package: mlcli-toolkit (pip)\n\n"+
"- Open-source CLI automating model training, evaluation, and\n"+
"  experiment tracking\n"+
"- Modular Model Registry supporting Scikit-learn and TensorFlow\n"+
"  (DNN / CNN / RNN / LSTM / GRU) model families\n\n"+
"stack: Python · Scikit-learn · TensorFlow"
    },
    "projects/alphavista.md": {
      lang:"markdown", icon:"◆",
      raw:
"# AlphaVista — Stock Analysis Platform\n\n"+
"- Combines real-time market data with ML-based price prediction\n"+
"  and NLP sentiment analysis (TensorFlow, Scikit-learn, VADER)\n"+
"- Integrated live financial data APIs with Redis caching for\n"+
"  performance\n\n"+
"stack: TensorFlow · Scikit-learn · VADER · Redis"
    },
    "projects/blockchain-tx-ui.md": {
      lang:"markdown", icon:"◆",
      raw:
"# blockchain-tx-ui\n\n"+
"- Published an open-source npm package for real-time blockchain\n"+
"  transaction tracking\n"+
"- Modular, reusable UI components for wallet connection and\n"+
"  transaction status display\n\n"+
"stack: TypeScript · React"
    },
    "education.yml": {
      lang:"yaml", icon:"⚙",
      raw:
"university: L J University, Ahmedabad, India\n"+
"degree: B.E. Computer Science and Technology\n"+
"duration: Nov 2022 – Sept 2026\n\n"+
"certifications:\n"+
"  - name: MLOps for Generative AI\n"+
"    issuer: Google Cloud\n"+
"    date: April 2025\n"+
"  - name: AWS Cloud Technical Essentials\n"+
"    issuer: Coursera\n"+
"    date: March 2025\n"+
"  - name: Exploratory Data Analysis for Machine Learning\n"+
"    date: January 2025"
    },
    "contact.sh": {
      lang:"bash", icon:">_",
      raw:
"#!/bin/bash\n"+
"# reach out — replies within 24h, IST\n\n"+
'export EMAIL="devarshilalani.devflow@gmail.com"\n'+
'export LINKEDIN="linkedin.com/in/devarshilalani05"\n'+
'export GITHUB="github.com/codeMaestro78"\n'+
'export PHONE="+91 8469176994"\n\n'+
'echo "run ./contact.sh --reach-out to say hi"'
    }
  };

  var FILE_ORDER = ["about.md","skills.json","experience.log","projects/allotiq.md","projects/mlcli.md","projects/alphavista.md","projects/blockchain-tx-ui.md","education.yml","contact.sh"];

  /* ============================= HIGHLIGHTING ============================= */
  function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

  function hlJSON(line){
    line = esc(line);
    line = line.replace(/"(\\.|[^"\\])*"(\s*:)?/g, function(m, _g, colon){
      if(colon !== undefined){ return '<span class="tok-key">'+m.slice(0, m.length-colon.length)+'</span>'+colon; }
      return '<span class="tok-str">'+m+'</span>';
    });
    line = line.replace(/\b(true|false|null)\b/g, '<span class="tok-bool">$1</span>');
    line = line.replace(/([{}\[\],])/g, '<span class="tok-punc">$1</span>');
    return line;
  }

  function hlYAML(line){
    var m = line.match(/^(\s*-?\s*)([a-zA-Z_][\w -]*)(:)(.*)$/);
    if(m){
      var rest = esc(m[4]);
      return esc(m[1])+'<span class="tok-key">'+esc(m[2])+'</span><span class="tok-punc">:</span><span class="tok-str">'+rest+'</span>';
    }
    return esc(line);
  }

  function hlLog(line){
    if(/^commit /.test(line)) return '<span class="tok-num">'+esc(line)+'</span>';
    if(/^Date:/.test(line)) return '<span class="tok-label">Date:</span><span class="tok-dim">'+esc(line.slice(5))+'</span>';
    if(/^\s*-\s/.test(line)) return '<span class="tok-bullet">'+esc(line.replace(/^(\s*)-/, '$1▸'))+'</span>';
    if(/^\s{4}\S/.test(line)) return '<span class="tok-strong">'+esc(line)+'</span>';
    return '<span class="tok-dim">'+esc(line)+'</span>';
  }

  function hlMD(line){
    if(/^#\s?/.test(line)) return '<span class="tok-head"># '+esc(line.replace(/^#\s?/,''))+'</span>';
    if(/^##\s?/.test(line)) return '<span class="tok-head">## '+esc(line.replace(/^##\s?/,''))+'</span>';
    if(/^-\s/.test(line)) return '<span class="tok-bullet">▸</span><span class="tok-dim">'+esc(line.slice(1))+'</span>';
    if(/^(live|stack|package):/.test(line)){
      var i = line.indexOf(":");
      return '<span class="tok-label">'+esc(line.slice(0,i+1))+'</span><span class="tok-str">'+esc(line.slice(i+1))+'</span>';
    }
    var out = esc(line);
    out = out.replace(/\*\*(.+?)\*\*/g, '<span class="tok-strong">$1</span>');
    return out;
  }

  function hlBash(line){
    if(/^#!/.test(line)) return '<span class="tok-comment">'+esc(line)+'</span>';
    if(/^#/.test(line)) return '<span class="tok-comment">'+esc(line)+'</span>';
    var m = line.match(/^export\s+([A-Z_]+)=("(.*)")$/);
    if(m) return '<span class="tok-key">export</span> <span class="tok-label">'+m[1]+'</span><span class="tok-punc">=</span><span class="tok-str">"'+esc(m[3])+'"</span>';
    if(/^echo /.test(line)) return '<span class="tok-key">echo</span><span class="tok-str">'+esc(line.slice(4))+'</span>';
    return esc(line);
  }

  function highlightLine(lang, line){
    switch(lang){
      case "json": return hlJSON(line);
      case "yaml": return hlYAML(line);
      case "log": return hlLog(line);
      case "markdown": return hlMD(line);
      case "bash": return hlBash(line);
      default: return esc(line);
    }
  }

  /* ============================= STATE ============================= */
  var openTabs = [];
  var activeFile = null;
  var termOpen = false;
  var termHistory = [];
  var termHistIdx = -1;

  var editorPad = document.getElementById('editorPad');
  var editorScroll = document.getElementById('editorScroll');
  var emptyState = document.getElementById('emptyState');
  var tabbar = document.getElementById('tabbar');
  var minimap = document.getElementById('minimap');
  var mmViewport = document.getElementById('mmViewport');
  var stLnCol = document.getElementById('stLnCol');
  var stActiveLang = document.getElementById('stActiveLang');

  function fileIcon(path){ return FILES[path] ? FILES[path].icon : "◆"; }
  function fileName(path){ return path.split('/').pop(); }

  function openFile(path, opts){
    if(!FILES[path]) return;
    if(openTabs.indexOf(path) === -1) openTabs.push(path);
    activeFile = path;
    renderTabs();
    renderEditor();
    if(!opts || !opts.keepSidebar){
      highlightSidebarActive(path);
    }
    if(window.innerWidth <= 860){ document.getElementById('sidebar').classList.remove('open'); }
  }

  function closeFile(path, ev){
    if(ev) ev.stopPropagation();
    var idx = openTabs.indexOf(path);
    if(idx === -1) return;
    openTabs.splice(idx,1);
    if(activeFile === path){
      activeFile = openTabs.length ? openTabs[Math.max(0, idx-1)] : null;
    }
    renderTabs();
    renderEditor();
  }

  function renderTabs(){
    tabbar.innerHTML = "";
    openTabs.forEach(function(path){
      var tab = document.createElement('div');
      tab.className = 'tab' + (path === activeFile ? ' active' : '');
      tab.innerHTML = '<span class="ic">'+fileIcon(path)+'</span><span>'+fileName(path)+'</span><button class="close" aria-label="close">×</button>';
      tab.addEventListener('click', function(){ openFile(path); });
      tab.querySelector('.close').addEventListener('click', function(e){ closeFile(path, e); });
      tabbar.appendChild(tab);
    });
  }

  function renderEditor(){
    if(!activeFile){
      editorScroll.style.display = 'none';
      emptyState.style.display = 'flex';
      minimap.style.display = window.innerWidth<=860 ? 'none':'block';
      stActiveLang.textContent = 'plaintext';
      stLnCol.textContent = 'Ln 1, Col 1';
      return;
    }
    editorScroll.style.display = 'block';
    emptyState.style.display = 'none';

    var file = FILES[activeFile];
    var lines = file.raw.split('\n');
    stActiveLang.textContent = file.lang;

    var htmlLines = lines.map(function(line, i){
      var hl = highlightLine(file.lang, line) || '&nbsp;';
      return '<div class="code-line" data-ln="'+(i+1)+'"><div class="gutter">'+(i+1)+'</div><div class="code-text">'+hl+'</div></div>';
    }).join('');
    editorPad.innerHTML = htmlLines;
    editorScroll.scrollTop = 0;

    Array.prototype.forEach.call(editorPad.querySelectorAll('.code-line'), function(el){
      el.addEventListener('mouseenter', function(){
        stLnCol.textContent = 'Ln '+el.getAttribute('data-ln')+', Col 1';
      });
    });

    renderMinimap(lines);
  }

  function renderMinimap(lines){
    minimap.querySelectorAll('.mm-line').forEach(function(n){ n.remove(); });
    var frag = document.createDocumentFragment();
    lines.forEach(function(line){
      var d = document.createElement('div');
      var w = Math.max(6, Math.min(58, line.length * 1.15));
      d.className = 'mm-line';
      if(/^#/.test(line) || /^commit/.test(line)) d.className += ' h1';
      else if(/^(##|Date:|stack:|live:)/.test(line)) d.className += ' h2';
      d.style.width = w+'px';
      frag.appendChild(d);
    });
    minimap.insertBefore(frag, mmViewport);
    syncMinimapViewport();
  }

  function syncMinimapViewport(){
    var ratio = editorScroll.clientHeight / Math.max(editorScroll.scrollHeight,1);
    var top = (editorScroll.scrollTop / Math.max(editorScroll.scrollHeight,1)) * minimap.clientHeight;
    mmViewport.style.height = Math.max(20, ratio * minimap.clientHeight) + 'px';
    mmViewport.style.top = top + 'px';
  }
  editorScroll.addEventListener('scroll', syncMinimapViewport);
  minimap.addEventListener('click', function(e){
    var rect = minimap.getBoundingClientRect();
    var pct = (e.clientY - rect.top) / rect.height;
    editorScroll.scrollTop = pct * editorScroll.scrollHeight;
  });

  /* ============================= SIDEBAR TREE ============================= */
  var tree = document.getElementById('tree');
  function buildTree(){
    tree.innerHTML = "";
    var order = ["about.md","skills.json","experience.log","__projects__","education.yml","contact.sh"];
    order.forEach(function(entry){
      if(entry === "__projects__"){
        var wrap = document.createElement('div');
        var head = document.createElement('div');
        head.className = 'tree-item';
        head.innerHTML = '<span class="chev">▸</span><span class="ic">▤</span><span>projects</span>';
        var kids = document.createElement('div');
        kids.className = 'tree-children';
        ["projects/allotiq.md","projects/mlcli.md","projects/alphavista.md","projects/blockchain-tx-ui.md"].forEach(function(p){
          var it = document.createElement('div');
          it.className = 'tree-item'; it.setAttribute('data-file', p);
          it.innerHTML = '<span class="ic">'+fileIcon(p)+'</span><span>'+fileName(p)+'</span>';
          it.addEventListener('click', function(){ openFile(p); });
          kids.appendChild(it);
        });
        head.addEventListener('click', function(){
          kids.classList.toggle('expanded');
          head.querySelector('.chev').classList.toggle('expanded');
        });
        wrap.appendChild(head); wrap.appendChild(kids);
        tree.appendChild(wrap);
        kids.classList.add('expanded'); head.querySelector('.chev').classList.add('expanded');
      } else {
        var it = document.createElement('div');
        it.className = 'tree-item'; it.setAttribute('data-file', entry);
        it.innerHTML = '<span class="ic">'+fileIcon(entry)+'</span><span>'+fileName(entry)+'</span>';
        it.addEventListener('click', function(){ openFile(entry); });
        tree.appendChild(it);
      }
    });
  }
  function highlightSidebarActive(path){
    tree.querySelectorAll('.tree-item').forEach(function(n){
      n.classList.toggle('open', n.getAttribute('data-file') === path);
    });
  }
  buildTree();

  /* ============================= CLOCK ============================= */
  function tickClock(){
    var el = document.getElementById('clock');
    var d = new Date();
    var utc = d.getTime() + d.getTimezoneOffset()*60000;
    var ist = new Date(utc + 5.5*3600000);
    var hh = String(ist.getHours()).padStart(2,'0');
    var mm = String(ist.getMinutes()).padStart(2,'0');
    var ss = String(ist.getSeconds()).padStart(2,'0');
    el.textContent = hh+':'+mm+':'+ss+' IST';
  }
  tickClock(); setInterval(tickClock, 1000);

  /* ============================= TERMINAL ============================= */
  var termBody = document.getElementById('termBody');
  var termInput = document.getElementById('termInput');
  var terminal = document.getElementById('terminal');

  function termPrintRaw(html){
    var d = document.createElement('div');
    d.className = 'term-line'; d.innerHTML = html;
    termBody.appendChild(d);
    termBody.scrollTop = termBody.scrollHeight;
  }
  function termPrint(cls, text){ termPrintRaw('<span class="'+cls+'">'+esc(text)+'</span>'); }

  function termEcho(cmd){
    termPrintRaw('<span class="term-prompt">devarshi@portfolio</span><span class="term-out">:</span><span class="term-path">~</span><span class="term-out">$ '+esc(cmd)+'</span>');
  }

  var COMMANDS = {
    help: function(){
      termPrint('term-hd', 'available commands');
      termPrint('term-out', '  whoami        about.md summary');
      termPrint('term-out', '  skills        tech stack');
      termPrint('term-out', '  experience    work history');
      termPrint('term-out', '  projects      selected projects');
      termPrint('term-out', '  education     degree & certifications');
      termPrint('term-out', '  contact       how to reach me');
      termPrint('term-out', '  ls            list files');
      termPrint('term-out', '  cat <file>    print a file to this terminal');
      termPrint('term-out', '  open <file>   open a file in the editor');
      termPrint('term-out', '  clear         clear the terminal');
    },
    whoami: function(){
      termPrint('term-hd', 'Devarshi Lalani — AI/ML Engineer · Full-Stack Engineer');
      termPrint('term-out', 'Ahmedabad, IN · currently building agentic AI systems @ Acqurie.io');
    },
    skills: function(){
      Object.keys(FILES["skills.json"].raw ? {} : {});
      termPrint('term-hd', 'core stack');
      termPrint('term-out', '  LangChain · LangGraph · RAG · OpenAI API · Gemini · HuggingFace');
      termPrint('term-out', '  Python · TypeScript · React · Node.js · FastAPI');
      termPrint('term-out', '  TensorFlow · Scikit-learn · PostgreSQL · AWS · Docker');
      termPrint('term-out', 'run: open skills.json for the full breakdown');
    },
    experience: function(){
      termPrint('term-hd', 'experience');
      termPrint('term-out', '  Acqurie.io — Software Development Engineer   (Mar 2026 – Present)');
      termPrint('term-out', '  fxis.ai — Machine Learning Intern             (Jan 2026 – Mar 2026)');
      termPrint('term-out', '  Feynn Labs — Machine Learning Intern          (Feb 2025 – Jun 2025)');
    },
    projects: function(){
      termPrint('term-hd', 'projects');
      termPrint('term-out', '  AllotIQ         agentic IPO intelligence platform — allotiq.in');
      termPrint('term-out', '  MLCLI           open-source ML/DL training CLI (mlcli-toolkit)');
      termPrint('term-out', '  AlphaVista      stock analysis + ML prediction + sentiment');
      termPrint('term-out', '  blockchain-tx-ui   npm package for live tx tracking');
    },
    education: function(){
      termPrint('term-hd', 'education');
      termPrint('term-out', '  B.E. Computer Science — L J University (Nov 2022 – Sept 2026)');
      termPrint('term-out', '  Certs: MLOps for Generative AI (Google Cloud) · AWS Cloud');
      termPrint('term-out', '         Technical Essentials · EDA for Machine Learning');
    },
    contact: function(){
      termPrint('term-hd', 'contact');
      termPrint('term-out', '  email     devarshilalani.devflow@gmail.com');
      termPrint('term-out', '  linkedin  linkedin.com/in/devarshilalani05');
      termPrint('term-out', '  github    github.com/codeMaestro78');
    },
    ls: function(){
      termPrint('term-out', FILE_ORDER.join('   '));
    },
    clear: function(){ termBody.innerHTML = ''; },
  };

  function runCommand(raw){
    var cmd = raw.trim();
    if(!cmd) return;
    termEcho(cmd);
    termHistory.push(cmd); termHistIdx = termHistory.length;

    var parts = cmd.split(/\s+/);
    var base = parts[0].toLowerCase();

    if(base === 'cat' && parts[1]){
      var p = resolveFile(parts[1]);
      if(p){ FILES[p].raw.split('\n').forEach(function(l){ termPrint('term-out', l); }); }
      else termPrint('term-err', 'cat: '+parts[1]+': no such file');
      return;
    }
    if(base === 'open' && parts[1]){
      var p2 = resolveFile(parts[1]);
      if(p2){ openFile(p2); termPrint('term-out', 'opened '+p2+' in editor'); }
      else termPrint('term-err', 'open: '+parts[1]+': no such file');
      return;
    }
    if(base === 'sudo'){ termPrint('term-err', 'nice try — this shell has no root'); return; }
    if(base === 'echo'){ termPrint('term-out', parts.slice(1).join(' ')); return; }

    if(COMMANDS[base]) COMMANDS[base]();
    else termPrint('term-err', base+': command not found — try "help"');
  }

  function resolveFile(name){
    if(FILES[name]) return name;
    var found = FILE_ORDER.filter(function(p){ return fileName(p) === name; });
    return found[0] || null;
  }

  termInput.addEventListener('keydown', function(e){
    if(e.key === 'Enter'){ runCommand(termInput.value); termInput.value=''; }
    else if(e.key === 'ArrowUp'){
      if(termHistIdx > 0){ termHistIdx--; termInput.value = termHistory[termHistIdx]||''; }
      e.preventDefault();
    } else if(e.key === 'ArrowDown'){
      if(termHistIdx < termHistory.length){ termHistIdx++; termInput.value = termHistory[termHistIdx]||''; }
      e.preventDefault();
    }
  });

  function openTerminal(){
    termOpen = true; terminal.classList.add('open');
    if(termBody.children.length === 0){
      termPrint('term-hd', 'devarshi portfolio shell — type "help" to get started');
    }
    setTimeout(function(){ termInput.focus(); }, 200);
  }
  function closeTerminal(){ termOpen = false; terminal.classList.remove('open'); }
  document.getElementById('termToggleBtn').addEventListener('click', function(){ termOpen ? closeTerminal() : openTerminal(); });
  document.getElementById('termClose').addEventListener('click', closeTerminal);

  /* ============================= COMMAND PALETTE ============================= */
  var paletteOverlay = document.getElementById('paletteOverlay');
  var paletteInput = document.getElementById('paletteInput');
  var paletteList = document.getElementById('paletteList');
  var paletteItems = [];
  var paletteSel = 0;

  var ACTIONS = [
    { label:'Toggle terminal', icon:'⌁', run:function(){ termOpen?closeTerminal():openTerminal(); } },
    { label:'Copy email address', icon:'✉', run:function(){ copyEmail(); } },
    { label:'Open LinkedIn', icon:'in', run:function(){ window.open('https://linkedin.com/in/devarshilalani05','_blank'); } },
    { label:'Open GitHub', icon:'gh', run:function(){ window.open('https://github.com/codeMaestro78','_blank'); } }
  ];

  function buildPaletteItems(query){
    var q = (query||'').toLowerCase();
    var items = [];
    FILE_ORDER.forEach(function(p){
      if(fileName(p).toLowerCase().indexOf(q) !== -1 || p.toLowerCase().indexOf(q) !== -1){
        items.push({ label:fileName(p), meta:p, icon:fileIcon(p), run:function(){ openFile(p); } });
      }
    });
    ACTIONS.forEach(function(a){
      if(a.label.toLowerCase().indexOf(q) !== -1) items.push({ label:a.label, meta:'action', icon:a.icon, run:a.run });
    });
    return items;
  }

  function renderPalette(){
    paletteItems = buildPaletteItems(paletteInput.value);
    paletteList.innerHTML = '';
    if(paletteItems.length === 0){
      paletteList.innerHTML = '<div class="pitem">no matches</div>';
      return;
    }
    paletteSel = Math.min(paletteSel, paletteItems.length-1);
    paletteItems.forEach(function(it, i){
      var el = document.createElement('div');
      el.className = 'pitem' + (i===paletteSel ? ' sel':'');
      el.innerHTML = '<span class="ic">'+it.icon+'</span><span>'+it.label+'</span><span class="meta">'+it.meta+'</span>';
      el.addEventListener('mouseenter', function(){ paletteSel = i; renderPalette(); });
      el.addEventListener('click', function(){ it.run(); closePalette(); });
      paletteList.appendChild(el);
    });
  }

  function openPalette(){
    paletteOverlay.classList.add('open');
    paletteInput.value = ''; paletteSel = 0;
    renderPalette();
    setTimeout(function(){ paletteInput.focus(); }, 30);
  }
  function closePalette(){ paletteOverlay.classList.remove('open'); }

  document.getElementById('paletteBtn').addEventListener('click', openPalette);
  paletteOverlay.addEventListener('click', function(e){ if(e.target === paletteOverlay) closePalette(); });
  paletteInput.addEventListener('input', function(){ paletteSel = 0; renderPalette(); });
  paletteInput.addEventListener('keydown', function(e){
    if(e.key === 'ArrowDown'){ paletteSel = Math.min(paletteSel+1, paletteItems.length-1); renderPalette(); e.preventDefault(); }
    else if(e.key === 'ArrowUp'){ paletteSel = Math.max(paletteSel-1, 0); renderPalette(); e.preventDefault(); }
    else if(e.key === 'Enter'){ if(paletteItems[paletteSel]){ paletteItems[paletteSel].run(); closePalette(); } }
    else if(e.key === 'Escape'){ closePalette(); }
  });

  document.addEventListener('keydown', function(e){
    var mod = e.metaKey || e.ctrlKey;
    if(mod && e.key.toLowerCase() === 'k'){ e.preventDefault(); paletteOverlay.classList.contains('open') ? closePalette() : openPalette(); }
    else if(e.key === 'Escape' && paletteOverlay.classList.contains('open')){ closePalette(); }
  });

  /* ============================= CONTACT / MISC ============================= */
  function copyEmail(){
    var email = "devarshilalani.devflow@gmail.com";
    if(navigator.clipboard){ navigator.clipboard.writeText(email).catch(function(){}); }
    openTerminal();
    termPrint('term-hd', 'copied to clipboard');
    termPrint('term-out', email);
  }
  document.getElementById('stContact').addEventListener('click', function(){
    openFile('contact.sh'); openTerminal();
    setTimeout(function(){ runCommand('contact'); }, 150);
  });

  /* ============================= SIDEBAR MOBILE TOGGLE ============================= */
  document.getElementById('menuBtn').addEventListener('click', function(){
    document.getElementById('sidebar').classList.toggle('open');
  });

  /* ============================= PARALLAX BG ============================= */
  if(!reducedMotion){
    var grid = document.getElementById('bgGrid');
    var raf = null;
    document.addEventListener('mousemove', function(e){
      if(raf) return;
      raf = requestAnimationFrame(function(){
        var x = (e.clientX / window.innerWidth - 0.5) * 10;
        var y = (e.clientY / window.innerHeight - 0.5) * 10;
        grid.style.transform = 'translate('+x+'px,'+y+'px)';
        raf = null;
      });
    });
  }

  /* ============================= BOOT SEQUENCE ============================= */
  var bootLines = [
    { t:'[    0.000000] devarshi/workspace — cold boot', c:'tag' },
    { t:'[    0.041203] mounting /home/devarshi …', c:'' },
    { t:'[    0.118422] loading modules: langchain, langgraph, react, fastapi', c:'' },
    { t:'[    0.244981] linking experience.log … 3 roles found', c:'ok' },
    { t:'[    0.360115] linking projects/ … 4 shipped', c:'ok' },
    { t:'[    0.481774] verifying skills.json … 44 tools indexed', c:'ok' },
    { t:'[    0.560310] starting terminal daemon on :7788', c:'' },
    { t:'[    0.612009] status: available for opportunities', c:'ok' },
    { t:'[    0.680044] workspace ready', c:'tag' }
  ];
  var bootLog = document.getElementById('bootLog');
  var bootFill = document.getElementById('bootBarFill');
  var bootEl = document.getElementById('boot');
  var appEl = document.getElementById('app');
  var bootDone = false;

  function finishBoot(){
    if(bootDone) return;
    bootDone = true;
    bootEl.classList.add('hide');
    appEl.classList.add('show');
    setTimeout(function(){ bootEl.style.display = 'none'; }, 650);
    openFile('about.md');
    setTimeout(function(){ if(openTabs.indexOf('skills.json')===-1) openFile('skills.json'); }, 120);
    setTimeout(function(){ openFile('about.md'); }, 200);
  }

  function runBoot(){
    if(reducedMotion){ finishBoot(); return; }
    var i = 0;
    function step(){
      if(bootDone) return;
      if(i >= bootLines.length){ setTimeout(finishBoot, 380); return; }
      var l = bootLines[i];
      var span = document.createElement('div');
      span.innerHTML = (l.c ? '<span class="'+l.c+'">'+esc(l.t)+'</span>' : esc(l.t));
      bootLog.appendChild(span);
      bootFill.style.right = (100 - ((i+1)/bootLines.length)*100) + '%';
      i++;
      setTimeout(step, 150 + Math.random()*130);
    }
    step();
  }

  window.addEventListener('keydown', function(){ if(!bootDone) finishBoot(); }, { once:false });
  bootEl.addEventListener('click', finishBoot);

  runBoot();
})();
</script>
</body>
</html>
