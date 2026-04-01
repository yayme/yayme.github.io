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
<h4>Volatility Inference with SDEs & Data Assimilation</h4>
<div class="tech-stack">Python, Stochastic Differential Equations, Data Assimilation</div>
<ul>
  <li>Estimated instantaneous volatility of cryptocurrency by combining a Heston-lite SDE with Kalman and Particle Filter; absolute log returns used as ground truth. Kalman R² ≈ 0.9, Particle Filter R² ≈ 0.48–0.67, GARCH R² ≈ 0.09–0.17. Both filters outperform traditional GARCH models.</li>
  <li>Estimated smoothed volatility of cryptocurrency by combining a mean-reverting SDE with Kalman and Particle Filter; 100-period rolling std used as ground truth. Kalman R² ≈ 0.9, Particle Filter R² ≈ 0.9, GARCH R² ≈ 0.33–0.63. Both methods outperform GARCH for smoothed volatility tracking.</li>
</ul>
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
  --cuda-local: #D95F18;
  --cuda-global-c: #a07848;
  --cuda-skip: #D6C6A9;
  
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
.interest-card {
  background: linear-gradient(135deg, #F5E8C7 0%, #FAF3E0 100%);
  border: 2px solid #D6C6A9;
  border-radius: 15px;
  padding: 1.2rem;
  margin-bottom: 0.8rem;
  text-align: center;
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  transition: all 0.3s ease;
}

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

/* Compact Card Styles for Resume */
@media (max-width: 768px) {
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

