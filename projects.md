---
layout: page
title: Projects
subtitle: Selected Projects 
author: Adnan Sadik
meta_description: "Projects - Adnan Sadik | Machine Learning, Data Science, and Quantitative Finance projects including cryptocurrency trading systems and AI-powered tools"
keywords: "Adnan Sadik projects, machine learning projects, data science portfolio, crypto trading, AI file organizer, Bayesian filtering, statistical decision making"
---

<style>
  html[data-theme="dark"], html[data-theme="dark"] body {
    background: #18120f !important;
    color: #F5E8C7 !important;
  }
  @media (prefers-color-scheme: dark) {
    html:not([data-theme]) body {
      background: #18120f !important;
      color: #F5E8C7 !important;
    }
  }
</style>

<!-- Dark mode script disabled for now
<script>
  (function() {
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var dataTheme = document.documentElement.getAttribute('data-theme');
    if (prefersDark || dataTheme === 'dark') {
      document.documentElement.style.background = '#18120f';
      document.body.style.background = '#18120f';
      document.documentElement.style.color = '#F5E8C7';
      document.body.style.color = '#F5E8C7';
    }
  })();
</script>
-->

<div class="projects-container">

<div class="projects-section">

<div class="completed-projects-card">
<h2> Completed Projects</h2>

<div class="project-item">
<div class="project-header">
<h3>Sparse Attention CUDA Kernel</h3>
<div class="tech-stack">
<span class="tech-tag">CUDA</span>
<span class="tech-tag">C++</span>
<span class="tech-tag">PyTorch</span>
</div>
</div>
<ul class="project-highlights">
  <li>Wrote a sparse attention kernel in CUDA with Longformer style masking (local window + global stride tokens); tiles with no active pairs are skipped entirely, bringing complexity from $O(n^2)$ down to $O(n \cdot w)$.</li>
  <li>Initial version stored a full score array per thread scaled with sequence length which spilled to global memory at longer sequences; rewrote with Flash Attention style online softmax, dropping per-thread memory to $O(1)$ and achieving $1.4$--$1.8\times$ speedup.</li>
  <li>Wrapped kernels as a PyTorch extension via pybind11 and benchmarked against PyTorch dense attention on a T4 GPU across sequence lengths $64$ to $512$.</li>
</ul>

<div class="cuda-card">
  <div class="cuda-top">
    <div class="cuda-top-left">
      <div class="cuda-tag">CUDA · GPU Kernels</div>
      <div class="cuda-title">Sparse <span>Attention</span> Kernel</div>
    </div>
  </div>
  <hr class="cuda-divider">
  <div class="cuda-body">
    <div class="cuda-grid-wrap">
      <div class="cuda-grid-label">sparse pattern</div>
      <div class="cuda-attn-grid" id="cuda-grid"></div>
      <div class="cuda-legend">
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-local)"></div>local</div>
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-global-c)"></div>global</div>
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-skip);border:1px solid var(--cuda-border)"></div>skip</div>
      </div>
    </div>
    <div class="cuda-right">
      <div class="cuda-stats">
        <div class="cuda-stat"><div class="cuda-s-val">1.8×</div><div class="cuda-s-lbl">v2 speedup<br>over v1</div></div>
        <div class="cuda-stat"><div class="cuda-s-val">O(n·w)</div><div class="cuda-s-lbl">sparse<br>complexity</div></div>
        <div class="cuda-stat"><div class="cuda-s-val">O(1)</div><div class="cuda-s-lbl">per-thread<br>memory</div></div>
      </div>
      <div class="cuda-diff">
        <div class="cuda-diff-title">v1 → v2 key changes</div>
        <div class="cuda-diff-row">
          <span class="cuda-d-label">score storage</span>
          <span><span class="cuda-d-old">full array</span> → <span class="cuda-d-new">streaming</span></span>
        </div>
        <div class="cuda-diff-row">
          <span class="cuda-d-label">softmax</span>
          <span><span class="cuda-d-old">materialized</span> → <span class="cuda-d-new">online</span></span>
        </div>
        <div class="cuda-diff-row">
          <span class="cuda-d-label">register spill</span>
          <span><span class="cuda-d-old">yes</span> → <span class="cuda-d-new">eliminated</span></span>
        </div>
      </div>
    </div>
  </div>
</div>

<a href="https://github.com/yayme/CUDA-kernel" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>Volatility Inference with SDEs & Data Assimilation</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Stochastic Differential Equations</span>
<span class="tech-tag">Data Assimilation</span>
</div>
</div>
<ul class="project-highlights">
  <li>Estimated instantaneous volatility of cryptocurrency by combining a Heston-lite SDE with Kalman and Particle Filter; absolute log returns used as ground truth. Kalman R² ≈ 0.9998, Particle Filter R² ≈ 0.48–0.67, GARCH R² ≈ 0.09–0.17. Both filters outperform traditional GARCH models.</li>
  <li>Estimated smoothed volatility of cryptocurrency by combining a mean-reverting SDE with Kalman and Particle Filter; 100-period rolling std used as ground truth. Kalman R² ≈ 0.996–0.997, Particle Filter R² ≈ 0.995–0.999, GARCH R² ≈ 0.33–0.63. Both methods outperform GARCH for smoothed volatility tracking.</li>
</ul>

<div class="vol-card">
  <div class="vol-top">
    <div class="vol-top-left">
      <div class="vol-tag">SDEs · Bayesian Filtering · Crypto</div>
      <div class="vol-title">Volatility Inference<br>with <span>SDEs</span></div>
    </div>
  </div>
  <hr class="vol-divider">
  <div class="vol-body">
    <div class="vol-chart-wrap">
      <div class="vol-chart-label">R² by method</div>
      
      <div class="vol-bar-group">
        <div class="vol-bar-title">pipeline 1 · instantaneous</div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">Kalman</span>
          <div class="vol-bar-track"><div class="vol-bar-fill kalman" style="width:100%"></div></div>
          <span class="vol-bar-val">0.9</span>
        </div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">Particle Filter</span>
          <div class="vol-bar-track"><div class="vol-bar-fill pf" style="width:63%"></div></div>
          <span class="vol-bar-val">~0.60</span>
        </div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">GARCH</span>
          <div class="vol-bar-track"><div class="vol-bar-fill garch" style="width:13%"></div></div>
          <span class="vol-bar-val">~0.13</span>
        </div>
      </div>
      
      <div class="vol-bar-group">
        <div class="vol-bar-title">pipeline 2 · rolling</div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">Kalman</span>
          <div class="vol-bar-track"><div class="vol-bar-fill kalman" style="width:99.7%"></div></div>
          <span class="vol-bar-val">0.9</span>
        </div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">Particle Filter</span>
          <div class="vol-bar-track"><div class="vol-bar-fill pf" style="width:99.7%"></div></div>
          <span class="vol-bar-val">0.9</span>
        </div>
        <div class="vol-bar-row">
          <span class="vol-bar-name">GARCH</span>
          <div class="vol-bar-track"><div class="vol-bar-fill garch" style="width:48%"></div></div>
          <span class="vol-bar-val">~0.48</span>
        </div>
      </div>
      
      <div class="vol-legend">
        <div class="vol-leg"><div class="vol-leg-dot" style="background:var(--vol-bar-kalman)"></div>Kalman</div>
        <div class="vol-leg"><div class="vol-leg-dot" style="background:var(--vol-bar-pf)"></div>Particle Filter</div>
        <div class="vol-leg"><div class="vol-leg-dot" style="background:var(--vol-bar-garch);border:1px solid var(--vol-border)"></div>GARCH</div>
      </div>
    </div>
    
    <div class="vol-right">
      <div class="vol-stats">
        <div class="vol-stat"><div class="vol-s-val">0.9</div><div class="vol-s-lbl">Kalman R²<br>pipeline 1</div></div>
        <div class="vol-stat"><div class="vol-s-val">0.9</div><div class="vol-s-lbl">Particle Filter R²<br>pipeline 2</div></div>
      </div>
      <div class="vol-pipes">
        <div class="vol-pipes-title">pipelines</div>
        <div class="vol-pipe-row" style="flex-direction:column; align-items:flex-start; gap:2px;">
          <div style="display:flex; justify-content:space-between; width:100%;">
            <span class="vol-p-label">P1 · instantaneous</span>
            <span class="vol-p-model">Heston-lite SDE</span>
          </div>
          <div style="font-size:8px; color:var(--vol-muted);">target: absolute log returns as proxy for instantaneous volatility</div>
        </div>
        <div class="vol-pipe-row" style="flex-direction:column; align-items:flex-start; gap:2px;">
          <div style="display:flex; justify-content:space-between; width:100%;">
            <span class="vol-p-label">P2 · rolling</span>
            <span class="vol-p-model">OU mean-revert SDE</span>
          </div>
          <div style="font-size:8px; color:var(--vol-muted);">target: rolling standard deviation over 100-period window</div>
        </div>
      </div>
    </div>
  </div>
</div>

<a href="https://github.com/yayme/Volatility-Inference-with-SDEs-Data-Assimilation" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
<a href="https://drive.google.com/file/d/1zqIqxCBXAAsep4-_TvGf_RJfOWSF8ySd/view?usp=sharing" class="project-link">
<span class="link-icon">📄</span> Full Report
</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>SignalCraft: Crypto Alpha Discovery System</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Quant Research</span>
<span class="tech-tag">Backtesting</span>
</div>
</div>
<p>Developed a modular pipeline to identify and backtest predictive signals from crypto spot data. Achieved ~52% hit rate and Sharpe ratio > 1 using ensemble models and adaptive trading strategies.</p>
<a href="https://github.com/yayme/Crypto-SignalCraft" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>


<div class="project-item">
<div class="project-header">
<h3>Yut AI - Korean Traditional Board Game AI</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Game Theory</span>
<span class="tech-tag">Bayesian Optimization</span>
</div>
</div>
<p>Developed strategy bots for Yut, a traditional Korean board game competition. Tested minimax tree search and heuristic-based strategies. Final approach used heuristic evaluation with Bayesian optimization (Gaussian Process + UCB) for weight tuning. Consistently outperforms baseline strategy with 54-56% win rate.</p>
<a href="https://github.com/yayme/COE-Yutnori" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>AI-powered File Organizer</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">NLP</span>
<span class="tech-tag">PyInstaller</span>
<span class="tech-tag">Watchdog</span>
<span class="tech-tag">spaCy</span>
</div>
</div>
<ul class="project-highlights">
  <li>Developed an automated file organization system using AI-driven content-based classification, improving file management efficiency by 40%.</li>
  <li>Calculated document similarity using two approaches: TF-IDF vectorization with cosine similarity, and semantic embeddings from spaCy’s en_core_web_md model.</li>
  <li>Integrated real-time file monitoring with Watchdog to automatically organize files into user-defined folders, reducing manual sorting time by 60%.</li>
</ul>
<a href="https://github.com/yayme/Desktop_file_organizer" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>Statistical Decision Making - Class Project</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Bayesian Inference</span>
<span class="tech-tag">Classification Models</span>
</div>
</div>
<ul class="project-highlights">
  <li>Implemented Bayesian inference methods (MLE, MAP, posterior mean) for robust parameter estimation in probabilistic models.</li>
  <li>Optimized inventory with the Newsvendor Problem, reducing losses by 49.08% vs heuristic methods.</li>
  <li>Developed and deployed multiple classification models, including KNN, Logistic Regression, and Single feature models, to predict healthcare readmissions, achieving AUCs of 0.68, 0.80, and 0.78, respectively.</li>
  <li>Achieved up to 7.8% cost savings through predictive model optimization, improving decision-making in healthcare resource allocation.</li>
</ul>
<a href="https://github.com/yayme/Statistical-Decision-Making" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>


<div class="project-item">
<div class="project-header">
<h3>Real-time Sarcasm Detector</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">PyTorch</span>
<span class="tech-tag">NLP</span>
</div>
</div>
<p>Built a BERT-based sarcasm classifier with Hugging Face and TweetEval for real-time inference, demonstrating advanced natural language processing capabilities.</p>
<a href="https://github.com/yayme/Bazinga-" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>

</div>

<style>
/* Projects Page Styling */
.projects-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background: rgba(255, 250, 242, 0.98);
  color: #3A2C29;
  border-radius: 18px;
  box-shadow: 0 18px 45px rgba(34, 22, 16, 0.18);
  transition: background-color 0.3s ease, color 0.3s ease;
}

[data-theme="dark"] .projects-container {
  background: rgba(24, 18, 15, 0.95);
  color: #F5E8C7;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.45);
}

.current-project-card, .completed-projects-card {
  background: #FAF3E0;
  color: #3A2C29;
  border-radius: 12px;
  margin-bottom: 2rem;
  padding: 1.5rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  transition: background-color 0.3s ease, color 0.3s ease;
}

[data-theme="dark"] .current-project-card,
[data-theme="dark"] .completed-projects-card {
  background: #2C1810;
  color: #F5E8C7;
  box-shadow: 0 3px 12px rgba(0,0,0,0.18);
}

.current-project-card h2, .completed-projects-card h2 {
  color: #3A2C29;
  border-bottom: 3px solid #D95F18;
  padding-bottom: 0.5rem;
  margin-bottom: 2rem;
  font-weight: bold;
  font-size: 1.6rem;
}

.project-item {
  background: linear-gradient(135deg, rgba(245, 232, 199, 0.3) 0%, rgba(250, 243, 224, 0.3) 100%);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.project-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(217, 95, 24, 0.05), transparent);
  transition: all 0.6s ease;
}

.project-item:hover {
  transform: translateY(-5px) translateX(3px);
  border-color: #D95F18;
  box-shadow: 0 8px 25px rgba(58, 44, 41, 0.15);
  background: linear-gradient(135deg, rgba(245, 232, 199, 0.5) 0%, rgba(250, 243, 224, 0.5) 100%);
}

.project-item:hover::before {
  left: 100%;
}

.project-item.featured {
  border: 2px solid #D95F18;
  background: linear-gradient(135deg, rgba(217, 95, 24, 0.1) 0%, rgba(245, 232, 199, 0.3) 100%);
}

.project-item.featured:hover {
  transform: scale(1.02);
  box-shadow: 0 12px 30px rgba(217, 95, 24, 0.2);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.project-item h3 {
  color: #3A2C29;
  font-weight: 600;
  font-size: 1.3rem;
  margin: 0;
  line-height: 1.3;
  flex: 1;
  min-width: 250px;
}

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.tech-tag {
  background: #D95F18;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.tech-tag:hover {
  background: #C4470D;
  transform: scale(1.05);
}

.project-status {
  background: #28a745;
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 1rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.7; }
  100% { opacity: 1; }
}

.project-item p {
  color: #3A2C29;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.project-link {
  background: #3A2C29;
  color: white !important;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  text-decoration: none !important;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.project-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: all 0.5s ease;
}

.project-link:hover {
  background: #D95F18;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(217, 95, 24, 0.3);
}

.project-link:hover::before {
  left: 100%;
}

.link-icon {
  font-size: 1rem;
  transition: all 0.3s ease;
}

.project-link:hover .link-icon {
  transform: scale(1.1);
}

/* Dark Mode Support */
[data-theme="dark"] .current-project-card,
[data-theme="dark"] .completed-projects-card {
  background: rgba(58, 36, 24, 0.8);
  border-color: #5A3825;
}

[data-theme="dark"] .current-project-card h2,
[data-theme="dark"] .completed-projects-card h2 {
  color: #F5E8C7 !important;
  border-bottom-color: #FF8A4C;
}

[data-theme="dark"] .project-item {
  background: linear-gradient(135deg, rgba(58, 36, 24, 0.6) 0%, rgba(44, 24, 16, 0.6) 100%);
  border-color: #5A3825;
}

[data-theme="dark"] .project-item:hover {
  border-color: #FF8A4C;
  background: linear-gradient(135deg, rgba(58, 36, 24, 0.8) 0%, rgba(44, 24, 16, 0.8) 100%);
}

[data-theme="dark"] .project-item.featured {
  border-color: #FF8A4C;
  background: linear-gradient(135deg, rgba(255, 138, 76, 0.1) 0%, rgba(58, 36, 24, 0.6) 100%);
}

[data-theme="dark"] .project-item h3 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .project-item p {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .tech-tag {
  background: #FF8A4C;
  color: #2C1810;
}

[data-theme="dark"] .tech-tag:hover {
  background: #FF6B2B;
}

[data-theme="dark"] .project-status {
  background: #4CAF50;
  color: #2C1810;
}

[data-theme="dark"] .project-link {
  background: #FF8A4C;
  color: #2C1810 !important;
}

[data-theme="dark"] .project-link:hover {
  background: #FF6B2B;
  box-shadow: 0 4px 12px rgba(255, 138, 76, 0.3);
}

/* CUDA Infographics Styles */
:root {
  --cuda-bg: rgba(255,250,242,0.98);
  --cuda-bg2: #FAF3E0;
  --cuda-text: #3A2C29;
  --cuda-muted: #8a7060;
  --cuda-accent: #D95F18;
  --cuda-border: #D6C6A9;
  --cuda-local: #a07848;
  --cuda-global-c: #D95F18;
  --cuda-skip: #e8dcc8;
}

html[data-theme="dark"], html[data-theme="dark"] body {
  --cuda-bg: rgba(24,18,15,0.95);
  --cuda-bg2: #2C1810;
  --cuda-text: #F5E8C7;
  --cuda-muted: #9a7d65;
  --cuda-accent: #FF8A4C;
  --cuda-border: #5A3825;
  --cuda-local: #c4976a;
  --cuda-global-c: #FF8A4C;
  --cuda-skip: #1e140f;
}

@media (prefers-color-scheme: dark) {
  html:not([data-theme]) body {
    --cuda-bg: rgba(24,18,15,0.95);
    --cuda-bg2: #2C1810;
    --cuda-text: #F5E8C7;
    --cuda-muted: #9a7d65;
    --cuda-accent: #FF8A4C;
    --cuda-border: #5A3825;
    --cuda-local: #c4976a;
    --cuda-global-c: #FF8A4C;
    --cuda-skip: #1e140f;
  }
}

.cuda-card {
  margin: 1.5rem 0;
  padding: 20px 22px;
  border: 1px solid var(--cuda-border);
  border-radius: 8px;
  background: var(--cuda-bg);
  font-family: 'IBM Plex Mono', monospace;
  color: var(--cuda-text);
}

.cuda-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.cuda-top-left {
  flex: 1;
}

.cuda-tag {
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--cuda-accent);
  margin-bottom: 6px;
}

.cuda-title {
  font-family: 'Syne', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--cuda-text);
  line-height: 1.2;
}

.cuda-title span {
  color: var(--cuda-accent);
}

.cuda-divider {
  border: none;
  border-top: 1px solid var(--cuda-border);
  margin-bottom: 14px;
}

.cuda-body {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px;
  align-items: start;
}

.cuda-grid-wrap {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cuda-grid-label {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cuda-muted);
}

.cuda-attn-grid {
  display: inline-grid;
  grid-template-columns: repeat(7, 11px);
  gap: 1.5px;
}

.cuda-cell {
  width: 11px;
  height: 11px;
  border-radius: 1px;
}

.cuda-c-local {
  background: var(--cuda-local);
  opacity: 0.85;
}

.cuda-c-global {
  background: var(--cuda-global-c);
}

.cuda-c-skip {
  background: var(--cuda-skip);
}

.cuda-legend {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.cuda-leg {
  display: flex;
  align-items: center;
  gap: 3px;
  font-size: 8px;
  color: var(--cuda-muted);
}

.cuda-leg-dot {
  width: 7px;
  height: 7px;
  border-radius: 1px;
  flex-shrink: 0;
}

.cuda-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cuda-stats {
  display: flex;
  gap: 8px;
}

.cuda-stat {
  flex: 1;
  background: var(--cuda-bg2);
  border: 1px solid var(--cuda-border);
  border-radius: 5px;
  padding: 8px 10px;
  text-align: center;
}

.cuda-s-val {
  font-family: 'Syne', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--cuda-accent);
  line-height: 1;
  margin-bottom: 3px;
}

.cuda-s-lbl {
  font-size: 8px;
  color: var(--cuda-muted);
  letter-spacing: 0.05em;
  line-height: 1.3;
}

.cuda-diff {
  background: var(--cuda-bg2);
  border: 1px solid var(--cuda-border);
  border-radius: 5px;
  padding: 9px 11px;
}

.cuda-diff-title {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cuda-muted);
  margin-bottom: 6px;
}

.cuda-diff-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 9px;
  padding: 3px 0;
  border-bottom: 1px solid var(--cuda-border);
  gap: 6px;
}

.cuda-diff-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.cuda-d-label {
  color: var(--cuda-muted);
}

.cuda-d-old {
  text-decoration: line-through;
  color: var(--cuda-muted);
  opacity: 0.6;
}

.cuda-d-new {
  color: var(--cuda-accent);
  font-weight: 500;
}

/* Volatility Infographics Styles */
:root {
  --vol-bg: rgba(255,250,242,0.98);
  --vol-bg2: #FAF3E0;
  --vol-text: #3A2C29;
  --vol-muted: #8a7060;
  --vol-accent: #D95F18;
  --vol-border: #D6C6A9;
  --vol-bar-kalman: #D95F18;
  --vol-bar-pf: #a07848;
  --vol-bar-garch: #D6C6A9;
}

html[data-theme="dark"] {
  --vol-bg: rgba(24,18,15,0.95);
  --vol-bg2: #2C1810;
  --vol-text: #F5E8C7;
  --vol-muted: #9a7d65;
  --vol-accent: #FF8A4C;
  --vol-border: #5A3825;
  --vol-bar-kalman: #FF8A4C;
  --vol-bar-pf: #c4976a;
  --vol-bar-garch: #5A3825;
}

@media (prefers-color-scheme: dark) {
  html:not([data-theme]) {
    --vol-bg: rgba(24,18,15,0.95);
    --vol-bg2: #2C1810;
    --vol-text: #F5E8C7;
    --vol-muted: #9a7d65;
    --vol-accent: #FF8A4C;
    --vol-border: #5A3825;
    --vol-bar-kalman: #FF8A4C;
    --vol-bar-pf: #c4976a;
    --vol-bar-garch: #5A3825;
  }
}

.vol-card {
  margin: 1.5rem 0;
  padding: 20px 22px;
  border: 1px solid var(--vol-border);
  border-radius: 8px;
  background: var(--vol-bg);
  font-family: 'IBM Plex Mono', monospace;
  color: var(--vol-text);
}

.vol-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.vol-top-left {
  flex: 1;
}

.vol-tag {
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--vol-accent);
  margin-bottom: 6px;
}

.vol-title {
  font-family: 'Syne', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--vol-text);
  line-height: 1.2;
}

.vol-title span {
  color: var(--vol-accent);
}

.vol-divider {
  border: none;
  border-top: 1px solid var(--vol-border);
  margin-bottom: 14px;
}

.vol-body {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px;
  align-items: start;
}

.vol-chart-wrap {
  min-width: 130px;
}

.vol-chart-label {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--vol-muted);
  margin-bottom: 8px;
}

.vol-bar-group {
  margin-bottom: 9px;
}

.vol-bar-title {
  font-size: 8px;
  color: var(--vol-muted);
  margin-bottom: 4px;
}

.vol-bar-row {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 2px;
}

.vol-bar-name {
  font-size: 8px;
  color: var(--vol-muted);
  width: 62px;
  flex-shrink: 0;
  text-align: right;
}

.vol-bar-track {
  flex: 1;
  height: 7px;
  background: var(--vol-bg2);
  border-radius: 1px;
  overflow: hidden;
  position: relative;
}

.vol-bar-fill {
  height: 100%;
  border-radius: 1px;
}

.vol-bar-val {
  font-size: 8px;
  color: var(--vol-text);
  width: 30px;
  flex-shrink: 0;
}

.vol-bar-fill.kalman {
  background: var(--vol-bar-kalman);
}

.vol-bar-fill.pf {
  background: var(--vol-bar-pf);
}

.vol-bar-fill.garch {
  background: var(--vol-bar-garch);
}

.vol-legend {
  display: flex;
  gap: 8px;
  margin-top: 6px;
}

.vol-leg {
  display: flex;
  align-items: center;
  gap: 3px;
  font-size: 8px;
  color: var(--vol-muted);
}

.vol-leg-dot {
  width: 7px;
  height: 7px;
  border-radius: 1px;
  flex-shrink: 0;
}

.vol-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.vol-stats {
  display: flex;
  gap: 8px;
}

.vol-stat {
  flex: 1;
  background: var(--vol-bg2);
  border: 1px solid var(--vol-border);
  border-radius: 5px;
  padding: 8px 10px;
  text-align: center;
}

.vol-s-val {
  font-family: 'Syne', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--vol-accent);
  line-height: 1;
  margin-bottom: 3px;
}

.vol-s-lbl {
  font-size: 8px;
  color: var(--vol-muted);
  letter-spacing: 0.05em;
  line-height: 1.3;
}

.vol-pipes {
  background: var(--vol-bg2);
  border: 1px solid var(--vol-border);
  border-radius: 5px;
  padding: 9px 11px;
}

.vol-pipes-title {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--vol-muted);
  margin-bottom: 6px;
}

.vol-pipe-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 9px;
  padding: 3px 0;
  border-bottom: 1px solid var(--vol-border);
  gap: 6px;
}

.vol-pipe-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.vol-p-label {
  color: var(--vol-muted);
}

.vol-p-model {
  color: var(--vol-text);
  font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
  .projects-container {
    padding: 0.5rem;
  }
  
  .current-project-card, .completed-projects-card {
    padding: 1.5rem;
  }
  
  .project-item {
    padding: 1rem;
  }
  
  .project-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .project-item h3 {
    font-size: 1.1rem;
    min-width: auto;
  }
  
  .tech-stack {
    margin-top: 0.5rem;
  }
  
  .project-link {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}
</style>

<script>
// Generate CUDA sparse attention grid
document.addEventListener('DOMContentLoaded', function() {
  const N = 7, W = 1, GS = 3;
  const g = document.getElementById('cuda-grid');
  if (g) {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        const c = document.createElement('div');
        const isG = i % GS === 0 || j % GS === 0;
        const isL = Math.abs(i - j) <= W;
        c.className = 'cuda-cell ' + (isG ? 'cuda-c-global' : isL ? 'cuda-c-local' : 'cuda-c-skip');
        g.appendChild(c);
      }
    }
  }
});
</script>