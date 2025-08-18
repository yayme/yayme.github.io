---
layout: page
title: Projects
subtitle: Selected Projects 
author: Adnan Sadik
meta_description: "Projects - Adnan Sadik | Machine Learning, Data Science, and Quantitative Finance projects including cryptocurrency trading systems and AI-powered tools"
keywords: "Adnan Sadik projects, machine learning projects, data science portfolio, crypto trading, AI file organizer, Bayesian filtering, statistical decision making"
---

<div class="projects-container">

<div class="projects-section">

<div class="current-project-card">
<h2>⚡ Currently Working On</h2>
<div class="project-item featured">
<div class="project-header">
<h3>Volatility Inference with SDEs & Data Assimilation</h3>
<div class="tech-stack">
<span class="tech-tag">Python</span>
<span class="tech-tag">Stochastic Differential Equations</span>
<span class="tech-tag">Data Assimilation</span>
</div>
</div>
<ul class="project-highlights">
  <li>Estimated instantaneous volatility of cryptocurrency by combining a Heston-lite SDE with Kalman and Particle Filter; absolute log returns used as ground truth (Kalman $R^2 \approx 0.9998$, Particle Filter $R^2 \approx 0.48$–$0.67$, GARCH $R^2 \approx 0.09$–$0.17$), showing both filters outperform traditional GARCH models.</li>
  <li>Estimated smoothed volatility of cryptocurrency by combining a mean-reverting SDE with Kalman and Particle Filter; 100-period rolling std used as ground truth (Kalman $R^2 \approx 0.996$–$0.997$, Particle Filter $R^2 \approx 0.995$–$0.999$, GARCH $R^2 \approx 0.33$–$0.63$), demonstrating both methods outperform GARCH for smoothed volatility tracking.</li>
</ul>
<a href="https://github.com/yayme/Volatility-Inference-with-SDEs-Data-Assimilation" class="project-link">
<span class="link-icon">📂</span> View on GitHub
</a>
</div>
</div>

<div class="completed-projects-card">
<h2>✅ Completed Projects</h2>

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
<span class="tech-tag">Decision Theory</span>
</div>
</div>
<p>Used Bayesian inference and classification to optimize inventory and healthcare decision models, showcasing practical applications of statistical theory.</p>
<a href="https://github.com/yayme/Statistical-Decision-Making" class="project-link">
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

</div>

<style>
/* Projects Page Styling */
.projects-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 1rem;
}

.current-project-card, .completed-projects-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  transition: all 0.3s ease;
}

.current-project-card:hover, .completed-projects-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(58, 44, 41, 0.12);
  border-color: #C4470D;
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