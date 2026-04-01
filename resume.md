---
layout: page
title: Resume
subtitle: Minimalistic Resume
author: Adnan Sadik
meta_description: "Resume - Adnan Sadik | Machine Learning & Data Science Experience in AI research and statistical learning"
keywords: "Adnan Sadik resume, data scientist, machine learning experience, AI researcher, KAIST"
---

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

<div class="resume-container">

<div class="interest-card">
<h2>Interest</h2>
<h3>Data → Signal → Model → Decision</h3>
<p><em>Statistics, Machine Learning, AI, Quantitative Finance, Game Theory, Social/Economic Modeling</em></p>
</div>

<div class="section-card">
<h2 id="work-experience">Work Experience</h2>

<div class="experience-item">
  <div class="company-header">
    <h3>Huawei, Hong Kong SAR</h3>
    <span class="role">Research & Software Intern</span>
    <span class="date">Dec 2025 – Mar 2026</span>
  </div>
  <p>Worked at Huawei Theory Lab on Algorithms and AI Systems, focusing on LLM inference algorithms and optimal cache management using C++ and CUDA.</p>
</div>



<div class="experience-item">
  <div class="company-header">
    <h3>IBS Biomedical Mathematics Group, South Korea</h3>
    <span class="role">Machine Learning Research Intern</span>
    <span class="date">Dec 2024 – June 2025</span>
  </div>
  <p>Developed ML pipelines for classifying sleep disorders and contributing to two research projects.</p>
</div>
<div class="experience-item">
  <div class="company-header">
    <h3>Mercor</h3>
    <span class="role">AI Reasoning Expert & Mathematical Problem Designer</span>
    <span class="date">Sep 2025 – Dec 2025</span>
  </div>
  <p>Designed mathematical reasoning problems for IMO Frontier Math project. Created challenging problem sets testing advanced mathematical concepts and logical reasoning for AI model evaluation.</p>
</div>

<div class="experience-item">
  <div class="company-header">
    <h3>Users & Informations Lab, KAIST</h3>
    <span class="role">Undergraduate Researcher, Project: ChatGPT Voices</span>
    <span class="date">Aug 2024 -- Dec 2024</span>
  </div>
  <p>Built a cultural benchmark dataset for low resource language and evaluated LLMs on language and reasoning tasks. Coauthored research paper accepted into AACL-IJCNLP 2025 Workshop.</p>
</div>

<div class="experience-item">
  <div class="company-header">
    <h3>Data Strategy Lab, KAIST</h3>
    <span class="role">Research Intern</span>
    <span class="date">Apr 2024 – May 2024</span>
  </div>
  <p>Studied fairness in AI; reviewed and researched bias mitigation techniques.</p>
</div>

<!-- New section for Other Experience -->
<h3 style="margin-top:2rem; color:#D95F18;">Other Experience</h3>

<div class="experience-item">
  <div class="company-header">
    <h3>Art of Problem Solving (AoPS)</h3>
    <span class="role">Olympiad Math Grader</span>
    <span class="date">2023 – Present</span>
  </div>
  <p>Graded advanced mathematics olympiad problems and provided detailed feedback to students participating in math competitions.</p>
  
</div>

</div>

<div class="section-card">
<h2>Technical Skills</h2>

<ul class="skills-list">
  <li><strong>Languages:</strong> Python, C++, C, F#, SQL, JavaScript, Scala</li>
  <li><strong>Libraries & Frameworks:</strong> CUDA, PyTorch, NumPy, Pandas, Scikit-learn, SciPy, Django, FastAPI</li>
  <li><strong>Tools:</strong> PostgreSQL, Docker, Shell Scripting</li>
  <li><strong>Software Development:</strong> Object Oriented Programming, Algorithm Design, Functional Programming, Concurrency, Multithreading, Parallel Computing, Database Management</li>
  <li><strong>Mathematics & Statistics:</strong> Stochastic Modeling (Markov Processes, Birth Death Models, Quasi Steady State), Time Series (State Space Models), Statistical Inference, Linear Models, Convex Optimization</li>
</ul>

</div>

<div class="section-card">
<h2>Projects</h2>

<div class="project-item">
<div class="project-header">
<h3>Sparse Attention CUDA Kernel</h3>
<div class="tech-stack">
<span class="tech-tag">CUDA</span>
<span class="tech-tag">C++</span>
<span class="tech-tag">PyTorch</span>
</div>
</div>
<p>Efficient sparse attention kernel with Longformer masking and Flash Attention style online softmax, achieving 1.8× speedup and O(1) memory complexity.</p>

<div class="cuda-card">
  <div class="cuda-top">
    <div class="cuda-top-left">
      <div class="cuda-tag">CUDA · GPU Kernels</div>
      <div class="cuda-title">Sparse <span>Attention</span></div>
    </div>
  </div>
  <hr class="cuda-divider">
  <div class="cuda-body">
    <div class="cuda-grid-wrap">
      <div class="cuda-grid-label">sparse pattern</div>
      <div class="cuda-attn-grid" id="cuda-grid-resume"></div>
      <div class="cuda-legend">
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-local)"></div>local</div>
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-global-c)"></div>global</div>
        <div class="cuda-leg"><div class="cuda-leg-dot" style="background:var(--cuda-skip);border:1px solid var(--cuda-border)"></div>skip</div>
      </div>
    </div>
    <div class="cuda-right">
      <div class="cuda-stats">
        <div class="cuda-stat"><div class="cuda-s-val">1.8×</div><div class="cuda-s-lbl">speedup</div></div>
        <div class="cuda-stat"><div class="cuda-s-val">O(n·w)</div><div class="cuda-s-lbl">complexity</div></div>
        <div class="cuda-stat"><div class="cuda-s-val">O(1)</div><div class="cuda-s-lbl">memory</div></div>
      </div>
    </div>
  </div>
</div>
<a href="https://github.com/yayme/CUDA-kernel" class="project-link">GitHub</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>Volatility Inference with SDEs & Data Assimilation</h3>
<div class="tech-stack">
<span class="tech-tag">SDE</span>
<span class="tech-tag">Kalman Filter</span>
<span class="tech-tag">Particle Filter</span>
</div>
</div>
<p>Estimated instantaneous and smoothed volatility of cryptocurrency using Heston-lite and mean-reverting SDEs with Kalman/Particle Filters. Both approaches achieve ~0.9 R², significantly outperforming traditional GARCH models.</p>

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
<a href="https://github.com/yayme/Volatility-Inference-with-SDEs-Data-Assimilation" class="project-link">GitHub</a>
</div>

<div class="project-item">
<h4>SignalCraft: Crypto Alpha Discovery System</h4>
<div class="tech-stack">Python, Quant Research, Backtesting</div>
<p>Developed a modular pipeline to identify and backtest predictive signals from crypto spot data. Achieved ~52% hit rate and Sharpe ratio > 1 using ensemble models and adaptive trading strategies.</p>
<a href="https://github.com/yayme/Crypto-SignalCraft" class="project-link">GitHub</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>Yut AI: Korean Traditional Board Game</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Game Theory</span>
<span class="tech-tag">Bayesian Optimization</span>
</div>
</div>
<p>Built a game AI agent using minimax lookahead with Bayesian optimization, achieving 56.5% win rate with 8 optimized policy weights.</p>

<div class="yut-card">
  <div class="yut-top">
    <div>
      <div class="yut-tag">Game AI · Bayesian Optimization</div>
      <div class="yut-title"><span>Yut</span> AI</div>
    </div>
  </div>
  <hr class="yut-divider">
  <div class="yut-body">
    <div class="yut-chart-wrap">
      <div class="yut-chart-label">win rate</div>
      <div class="yut-bar-row">
        <span class="yut-bar-name">Bayes-tuned</span>
        <div class="yut-bar-track"><div class="yut-bar-fill" style="width:100%;background:var(--yut-bar-best)"></div></div>
        <span class="yut-bar-val">56.5%</span>
      </div>
      <div class="yut-bar-row">
        <span class="yut-bar-name">baseline</span>
        <div class="yut-bar-track"><div class="yut-bar-fill" style="width:50%;background:var(--yut-bar-poor)"></div></div>
        <span class="yut-bar-val">50.0%</span>
      </div>
    </div>
    <div class="yut-right">
      <div class="yut-stats">
        <div class="yut-stat"><div class="yut-s-val">56.5%</div><div class="yut-s-lbl">best win<br>rate</div></div>
        <div class="yut-stat"><div class="yut-s-val">8</div><div class="yut-s-lbl">weights<br>tuned</div></div>
      </div>
    </div>
  </div>
</div>
<a href="https://github.com/yayme/COE-Yutnori" class="project-link">GitHub</a>
</div>

<div class="project-item">
<div class="project-header">
<h3>AI Agent for Automated File Management</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">NLP</span>
<span class="tech-tag">Embeddings</span>
</div>
</div>
<p>Real-time file sorter using semantic embeddings to automatically classify and organize files, achieving 40% efficiency gain and 60% time savings.</p>

<div class="fo-card">
  <div class="fo-top">
    <div>
      <div class="fo-tag">Agentic Automation · NLP</div>
      <div class="fo-title">File <span>Organizer</span></div>
    </div>
  </div>
  <hr class="fo-divider">
  <div class="fo-body">
    <div class="fo-pipeline">
      <div class="fo-pipeline-label">pipeline</div>
      <div class="fo-step">
        <span class="fo-step-num">1</span>
        <div class="fo-step-body">
          <div class="fo-step-title">trigger</div>
          <div class="fo-step-desc">Watchdog monitors filesystem</div>
        </div>
      </div>
      <div class="fo-step">
        <span class="fo-step-num">2</span>
        <div class="fo-step-body">
          <div class="fo-step-title">embedding</div>
          <div class="fo-step-desc">spaCy encodes content</div>
        </div>
      </div>
      <div class="fo-step">
        <span class="fo-step-num">3</span>
        <div class="fo-step-body">
          <div class="fo-step-title">classify</div>
          <div class="fo-step-desc">Cosine similarity match</div>
        </div>
      </div>
      <div class="fo-step">
        <span class="fo-step-num">4</span>
        <div class="fo-step-body">
          <div class="fo-step-title">dispatch</div>
          <div class="fo-step-desc">Route to folder</div>
        </div>
      </div>
    </div>

    <div class="fo-right">
      <div class="fo-stats">
        <div class="fo-stat"><div class="fo-s-val">40%</div><div class="fo-s-lbl">efficiency<br>gain</div></div>
        <div class="fo-stat"><div class="fo-s-val">60%</div><div class="fo-s-lbl">time<br>saved</div></div>
      </div>
    </div>
  </div>
</div>
<a href="https://github.com/yayme/Desktop_file_organizer" class="project-link">GitHub</a>
</div>



</div>

<div class="section-card">
<h2>Honors & Awards</h2>

<div class="award-item">
<strong>Top Quartile, Best-in-University Jane Street Prize</strong> – Simon Marais Mathematics Competition, 2024
</div>

<div class="award-item">
<strong>Bronze Medalist</strong> – International Mathematical Olympiad (IMO), 2020, 2021
</div>

<div class="award-item">
<strong>Bronze Medalist</strong> – Asian Pacific Mathematical Olympiad (APMO), 2021, 2022
</div>

<div class="award-item">
<strong>Bronze Medalist</strong> – Bangladesh Olympiad in Informatics, 2022
</div>

<div class="award-item">
<strong>Competitive Programming</strong> – Candidate Master (94th percentile), Codeforces; 5★ (99th percentile), Codechef
</div>

</div>

<div class="section-card">
<h2>Certifications</h2>

<div class="certification-item">
<h4>Bloomberg Market Concepts (BMC)</h4>
<p>Comprehensive financial markets education covering Economics, Currencies, Fixed Income, and Equities.</p>
<a href="https://portal.bloombergforeducation.com/certificates/5gjUKVbqNyprfVUKpEvhMjSj" class="certification-link" target="_blank">🏆 View Certificate</a>
</div>

</div>

<div class="section-card">
<h2>Leadership and Volunteer Experience</h2>

<div class="leadership-item">
<h4>Tutor</h4>
<p>Tutored KAIST freshmen in Calculus and Programming; mentored students for math olympiads.</p>
</div>

<div class="leadership-item">
<h4>Country Representative</h4>
<p>Handled student finances and onboarding; facilitated communication with faculty and student body.</p>
</div>

</div>

<div class="section-card">
<h2>Other Interests</h2>

<div class="interest-item">
<h4>Competitive Chess</h4>
<p>Top 1% on Chess.com; winner of national and regional tournaments.</p>
</div>

</div>

</div>

<style>
/* CSS Variables for Project Cards */
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
  
  --yut-bg: rgba(255,250,242,0.98);
  --yut-bg2: #FAF3E0;
  --yut-text: #3A2C29;
  --yut-muted: #8a7060;
  --yut-accent: #D95F18;
  --yut-border: #D6C6A9;
  --yut-bar-best: #D95F18;
  --yut-bar-mid: #a07848;
  --yut-bar-base: #c8b89a;
  --yut-bar-poor: #D6C6A9;
  
  --fo-bg: rgba(255,250,242,0.98);
  --fo-bg2: #FAF3E0;
  --fo-text: #3A2C29;
  --fo-muted: #8a7060;
  --fo-accent: #D95F18;
  --fo-border: #D6C6A9;
}

html[data-theme="dark"] {
  --cuda-bg: rgba(24,18,15,0.95);
  --cuda-bg2: #2C1810;
  --cuda-text: #F5E8C7;
  --cuda-muted: #9a7d65;
  --cuda-accent: #FF8A4C;
  --cuda-border: #5A3825;
  --cuda-local: #c4976a;
  --cuda-global-c: #FF8A4C;
  --cuda-skip: #1e140f;
  
  --yut-bg: rgba(24,18,15,0.95);
  --yut-bg2: #2C1810;
  --yut-text: #F5E8C7;
  --yut-muted: #9a7d65;
  --yut-accent: #FF8A4C;
  --yut-border: #5A3825;
  --yut-bar-best: #FF8A4C;
  --yut-bar-mid: #c4976a;
  --yut-bar-base: #7a5c40;
  --yut-bar-poor: #5A3825;
  
  --fo-bg: rgba(24,18,15,0.95);
  --fo-bg2: #2C1810;
  --fo-text: #F5E8C7;
  --fo-muted: #9a7d65;
  --fo-accent: #FF8A4C;
  --fo-border: #5A3825;
}

@media (prefers-color-scheme: dark) {
  html:not([data-theme]) {
    --cuda-bg: rgba(24,18,15,0.95);
    --cuda-bg2: #2C1810;
    --cuda-text: #F5E8C7;
    --cuda-muted: #9a7d65;
    --cuda-accent: #FF8A4C;
    --cuda-border: #5A3825;
    --cuda-local: #c4976a;
    --cuda-global-c: #FF8A4C;
    --cuda-skip: #1e140f;
    
    --yut-bg: rgba(24,18,15,0.95);
    --yut-bg2: #2C1810;
    --yut-text: #F5E8C7;
    --yut-muted: #9a7d65;
    --yut-accent: #FF8A4C;
    --yut-border: #5A3825;
    --yut-bar-best: #FF8A4C;
    --yut-bar-mid: #c4976a;
    --yut-bar-base: #7a5c40;
    --yut-bar-poor: #5A3825;
    
    --fo-bg: rgba(24,18,15,0.95);
    --fo-bg2: #2C1810;
    --fo-text: #F5E8C7;
    --fo-muted: #9a7d65;
    --fo-accent: #FF8A4C;
    --fo-border: #5A3825;
  }
}

@media (prefers-color-scheme: dark) {
  html:not([data-theme]) {
    --cuda-bg: rgba(24,18,15,0.95);
    --cuda-bg2: #2C1810;
    --cuda-text: #F5E8C7;
    --cuda-muted: #9a7d65;
    --cuda-accent: #FF8A4C;
    --cuda-border: #5A3825;
    --cuda-local: #FF8A4C;
    --cuda-global-c: #c4976a;
    --cuda-skip: #5A3825;
    
    --yut-bg: rgba(24,18,15,0.95);
    --yut-bg2: #2C1810;
    --yut-text: #F5E8C7;
    --yut-muted: #9a7d65;
    --yut-accent: #FF8A4C;
    --yut-border: #5A3825;
    --yut-bar-best: #FF8A4C;
    --yut-bar-mid: #c4976a;
    --yut-bar-base: #7a5c40;
    --yut-bar-poor: #5A3825;
    
    --fo-bg: rgba(24,18,15,0.95);
    --fo-bg2: #2C1810;
    --fo-text: #F5E8C7;
    --fo-muted: #9a7d65;
    --fo-accent: #FF8A4C;
    --fo-border: #5A3825;
  }
}

/* Resume Page Styling */
.resume-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  background: rgba(255, 250, 242, 0.98);
  color: #3A2C29;
  border-radius: 18px;
  box-shadow: 0 18px 45px rgba(34, 22, 16, 0.18);
  transition: background-color 0.3s ease, color 0.3s ease;
}

[data-theme="dark"] .resume-container {
  background: rgba(24, 18, 15, 0.95);
  color: #F5E8C7;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.45);
}

.interest-card {
  background: linear-gradient(135deg, #F5E8C7 0%, #FAF3E0 100%);
  border: 2px solid #D6C6A9;
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  text-align: center;
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  transition: all 0.3s ease;
}

.section-card {
  background: #FAF3E0;
  color: #3A2C29;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  transition: background-color 0.3s ease, color 0.3s ease;
}

[data-theme="dark"] .interest-card {
  background: linear-gradient(135deg, #3A2418 0%, #2C1810 100%);
  border-color: #5A3825;
  color: #F5E8C7;
}

[data-theme="dark"] .interest-card h2,
[data-theme="dark"] .interest-card h3 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .interest-card h3 {
  color: #FF8A4C !important;
}

[data-theme="dark"] .section-card {
  background: #2C1810;
  color: #F5E8C7;
  box-shadow: 0 3px 12px rgba(0,0,0,0.18);
}

/* Resume Card Styling */
.interest-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(58, 44, 41, 0.15);
  border-color: #D95F18;
}

.interest-card h2 {
  color: #3A2C29;
  margin-bottom: 1rem;
  font-weight: bold;
}

.interest-card h3 {
  color: #D95F18;
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.section-card h2 {
  color: #3A2C29;
  border-bottom: 3px solid #D95F18;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  font-weight: bold;
  font-size: 1.4rem;
}

.experience-item, .project-item, .leadership-item {
  background: linear-gradient(135deg, rgba(245, 232, 199, 0.3) 0%, rgba(250, 243, 224, 0.3) 100%);
  border: 1px solid #D6C6A9;
  border-radius: 8px;
  padding: 1.2rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.experience-item:hover, .project-item:hover, .leadership-item:hover {
  transform: translateX(5px);
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  border-color: #D95F18;
  background: rgba(245, 232, 199, 0.5);
}

.company-header {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.6rem;
}

.company-header h3 {
  color: #3A2C29;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.role {
  color: #D95F18;
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 0.25rem;
}

.date {
  color: #6D5A4D;
  font-style: italic;
  font-size: 0.9rem;
}

.tech-stack {
  background: #D95F18;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  font-size: 0.85rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 0.8rem;
}

.project-link {
  background: #3A2C29;
  color: white !important;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  text-decoration: none !important;
  font-weight: 600;
  display: inline-block;
  margin-top: 0.5rem;
  transition: all 0.3s ease;
}

.project-link:hover {
  background: #D95F18;
  transform: scale(1.05);
}

.award-item, .interest-item {
  background: rgba(217, 95, 24, 0.1);
  border-left: 4px solid #D95F18;
  padding: 1rem 1.2rem;
  margin-bottom: 1rem;
  border-radius: 0 8px 8px 0;
  transition: all 0.3s ease;
}

.award-item:hover, .interest-item:hover {
  background: rgba(217, 95, 24, 0.15);
  transform: translateX(5px);
  border-left-width: 6px;
}

.certification-item {
  background: rgba(255, 138, 76, 0.05);
  border: 1px solid #D6C6A9;
  border-left: 4px solid #D95F18;
  border-radius: 8px;
  padding: 1rem 1.2rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
  transition: all 0.3s ease;
}

.certification-item:hover {
  transform: translateX(5px);
  border-left-width: 6px;
  background: rgba(255, 138, 76, 0.08);
  border-color: #C4470D;
}

.certification-item h4 {
  color: #3A2C29;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.certification-link {
  display: inline-block;
  background: #D95F18;
  color: white !important;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  margin-top: 0.5rem;
  transition: all 0.3s ease;
}

.certification-link:hover {
  background: #C4470D;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(196, 71, 13, 0.3);
}

/* Dark Mode Support */
[data-theme="dark"] .interest-card {
  background: linear-gradient(135deg, #3A2418 0%, #2C1810 100%);
  border-color: #5A3825;
  color: #F5E8C7;
}

[data-theme="dark"] .interest-card h2,
[data-theme="dark"] .interest-card h3 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .interest-card h3 {
  color: #FF8A4C !important;
}

[data-theme="dark"] .section-card {
  background: rgba(58, 36, 24, 0.8);
  border-color: #5A3825;
  color: #F5E8C7;
}

[data-theme="dark"] .section-card h2 {
  color: #F5E8C7 !important;
  border-bottom-color: #FF8A4C;
}

[data-theme="dark"] .experience-item,
[data-theme="dark"] .project-item,
[data-theme="dark"] .leadership-item,
[data-theme="dark"] .certification-item {
  background: rgba(58, 36, 24, 0.6);
  border-color: #5A3825;
  color: #F5E8C7;
}

[data-theme="dark"] .experience-item h3,
[data-theme="dark"] .experience-item h4,
[data-theme="dark"] .project-item h3,
[data-theme="dark"] .project-item h4,
[data-theme="dark"] .leadership-item h3,
[data-theme="dark"] .leadership-item h4,
[data-theme="dark"] .certification-item h4 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .company-header h3 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .role {
  color: #FF8A4C !important;
}

[data-theme="dark"] .date {
  color: #D6C6A9 !important;
}

[data-theme="dark"] .experience-item:hover,
[data-theme="dark"] .project-item:hover,
[data-theme="dark"] .leadership-item:hover,
[data-theme="dark"] .certification-item:hover {
  background: rgba(58, 36, 24, 0.8);
  border-color: #FF8A4C;
}

[data-theme="dark"] .tech-stack {
  background: #FF8A4C;
  color: #2C1810;
}

[data-theme="dark"] .project-link {
  background: #FF8A4C;
  color: #2C1810 !important;
}

[data-theme="dark"] .project-link:hover {
  background: #FF6B2B;
}

[data-theme="dark"] .certification-link {
  background: #FF8A4C;
  color: #2C1810 !important;
}

[data-theme="dark"] .certification-link:hover {
  background: #FF6B2B;
}

[data-theme="dark"] .award-item,
[data-theme="dark"] .interest-item {
  background: rgba(255, 138, 76, 0.1);
  border-left-color: #FF8A4C;
  color: #F5E8C7;
}

[data-theme="dark"] .award-item strong,
[data-theme="dark"] .interest-item h4 {
  color: #F5E8C7 !important;
}

/* Skills List Styling */
.skills-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.skills-list li {
  margin-bottom: 0.6rem;
  line-height: 1.5;
  color: #3A2C29;
}

[data-theme="dark"] .skills-list li {
  color: #F5E8C7;
}

/* Project Header & Tech Stack (for resume cards) */
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

/* Dark mode for project header */
[data-theme="dark"] .project-item h3 {
  color: #F5E8C7 !important;
}

[data-theme="dark"] .tech-tag {
  background: #FF8A4C;
  color: #2C1810;
}

[data-theme="dark"] .tech-tag:hover {
  background: #FF6B2B;
}

/* CUDA Card Styles */
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

/* YUT Card Styles */
.yut-card {
  margin: 1.5rem 0;
  padding: 20px 22px;
  border: 1px solid var(--yut-border);
  border-radius: 8px;
  background: var(--yut-bg);
  font-family: 'IBM Plex Mono', monospace;
  color: var(--yut-text);
}

.yut-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.yut-tag {
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--yut-accent);
  margin-bottom: 6px;
}

.yut-title {
  font-family: 'Syne', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--yut-text);
  line-height: 1.2;
}

.yut-title span {
  color: var(--yut-accent);
}

.yut-divider {
  border: none;
  border-top: 1px solid var(--yut-border);
  margin-bottom: 14px;
}

.yut-body {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px;
  align-items: start;
}

.yut-chart-wrap {
  min-width: 148px;
}

.yut-chart-label {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--yut-muted);
  margin-bottom: 8px;
}

.yut-bar-row {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 4px;
}

.yut-bar-name {
  font-size: 8px;
  color: var(--yut-muted);
  width: 72px;
  flex-shrink: 0;
  text-align: right;
}

.yut-bar-track {
  flex: 1;
  height: 7px;
  background: var(--yut-bg2);
  border-radius: 1px;
  overflow: hidden;
}

.yut-bar-fill {
  height: 100%;
  border-radius: 1px;
}

.yut-bar-val {
  font-size: 8px;
  color: var(--yut-text);
  width: 28px;
  flex-shrink: 0;
}

.yut-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.yut-stats {
  display: flex;
  gap: 8px;
}

.yut-stat {
  flex: 1;
  background: var(--yut-bg2);
  border: 1px solid var(--yut-border);
  border-radius: 5px;
  padding: 8px 10px;
  text-align: center;
}

.yut-s-val {
  font-family: 'Syne', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--yut-accent);
  line-height: 1;
  margin-bottom: 3px;
}

.yut-s-lbl {
  font-size: 8px;
  color: var(--yut-muted);
  letter-spacing: 0.05em;
  line-height: 1.3;
}

/* Volatility Card Styles */
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

/* File Organizer Card Styles */
.fo-card {
  margin: 1.5rem 0;
  padding: 20px 22px;
  border: 1px solid var(--fo-border);
  border-radius: 8px;
  background: var(--fo-bg);
  font-family: 'IBM Plex Mono', monospace;
  color: var(--fo-text);
}

.fo-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.fo-tag {
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--fo-accent);
  margin-bottom: 6px;
}

.fo-title {
  font-family: 'Syne', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--fo-text);
  line-height: 1.2;
}

.fo-title span {
  color: var(--fo-accent);
}

.fo-divider {
  border: none;
  border-top: 1px solid var(--fo-border);
  margin-bottom: 14px;
}

.fo-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  align-items: start;
}

.fo-pipeline {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.fo-pipeline-label {
  font-size: 8px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--fo-muted);
  margin-bottom: 8px;
}

.fo-step {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 7px 10px;
  background: var(--fo-bg2);
  border: 1px solid var(--fo-border);
  border-radius: 0;
  border-bottom: none;
  position: relative;
}

.fo-step:first-of-type {
  border-radius: 5px 5px 0 0;
}

.fo-step:last-of-type {
  border-radius: 0 0 5px 5px;
  border-bottom: 1px solid var(--fo-border);
}

.fo-step-num {
  font-size: 8px;
  font-weight: 500;
  color: var(--fo-accent);
  min-width: 12px;
  margin-top: 1px;
}

.fo-step-body {
  flex: 1;
}

.fo-step-title {
  font-size: 9px;
  font-weight: 500;
  color: var(--fo-text);
  margin-bottom: 1px;
}

.fo-step-desc {
  font-size: 8px;
  color: var(--fo-muted);
  line-height: 1.4;
}

.fo-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fo-stats {
  display: flex;
  gap: 8px;
}

.fo-stat {
  flex: 1;
  background: var(--fo-bg2);
  border: 1px solid var(--fo-border);
  border-radius: 5px;
  padding: 8px 10px;
  text-align: center;
}

.fo-s-val {
  font-family: 'Syne', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--fo-accent);
  line-height: 1;
  margin-bottom: 3px;
}

.fo-s-lbl {
  font-size: 8px;
  color: var(--fo-muted);
  letter-spacing: 0.05em;
  line-height: 1.3;
}

/* Responsive Design */
  .resume-container {
    padding: 0.5rem;
  }
  
  .interest-card, .section-card {
    padding: 1.5rem;
  }
  
  .experience-item, .project-item, .leadership-item {
    padding: 1rem;
  }
  
  .company-header {
    text-align: left;
  }
}
</style>

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

<script>
// Generate CUDA sparse attention grid for resume
document.addEventListener('DOMContentLoaded', function() {
  const N = 7, W = 1, GS = 3;
  const g = document.getElementById('cuda-grid-resume');
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

