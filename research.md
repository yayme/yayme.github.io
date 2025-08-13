---
layout: page
title: Research
subtitle: Current research in IoT machine Learning and Markovian dynamics.
author: Adnan Sadik
meta_description: "Research - Adnan Sadik | AI, Machine Learning & Statistical Learning projects in sleep disorder classification and LLM evaluation"
keywords: "Adnan Sadik research, AI researcher, machine learning projects, data scientist, statistical learning, KAIST research"
---

<div class="research-container">

<div class="interests-overview-card">
<h2>Research Interests</h2>
<div class="interests-grid">
<div class="interest-area">
<div class="interest-icon">💹</div>
<h3>Quantitative Finance and Financial AI</h3>
</div>
<div class="interest-area">
<div class="interest-icon">🔬</div>
<h3>Applied Machine Learning and Data Science</h3>
</div>
<div class="interest-area">
<div class="interest-icon">🧬</div>
<h3>Biomedical Mathematics and Modeling</h3>
</div>
<div class="interest-area">
<div class="interest-icon">📊</div>
<h3>Statistical Learning Theory</h3>
</div>
</div>
</div>

<div class="current-research-card">
<h2>🔬 Current Research</h2>

<div class="research-project">
<div class="project-header">
<h3>Sleep Disorder Classification using Machine Learning | Modeling Stochastic Delay in Birth and death processes in biological systems</h3>
<div class="institution">
<a href="https://www.ibs.re.kr/bimag/" class="institution-link">IBS Biomedical Mathematics Group</a>
<span class="location">South Korea</span>
</div>
<span class="duration">Dec 2024 – Aug 2025</span>
</div>
<div class="project-details">
<div class="status-badge ongoing">Ongoing</div>
<div class="supervisor">
<span class="supervisor-label">Supervisor:</span>
<a href="https://mathsci.kaist.ac.kr/~jaekkim/" class="supervisor-link">Prof. Jae Kyoung Kim</a>
</div>
</div>
</div>

<div class="research-project">
<div class="project-header">
<h3>Natural Language Processing and Cultural Computing</h3>
<div class="institution">
<a href="https://uilab.kr/" class="institution-link">Users & Informations Lab</a>
<span class="location">KAIST</span>
</div>
<span class="duration">Aug 2024 -- Dec 2024</span>
</div>
<div class="project-content">
<ul class="research-highlights">
<li>Developed cultural benchmark datasets for low-resource languages</li>
<li>Evaluated Large Language Models on language understanding and reasoning tasks</li>
<li>Research paper in submission<sup><a href="#preprint-1" class="ref-link">[1]</a></sup></li>
</ul>
</div>
</div>

<div class="research-project">
<div class="project-header">
<h3>AI Fairness and Bias Mitigation</h3>
<div class="institution">
<span class="institution-name">Data Strategy Lab</span>
<span class="location">KAIST</span>
</div>
<span class="duration">Apr 2024 – May 2024</span>
</div>
<div class="project-content">
<ul class="research-highlights">
<li>Conducted comprehensive review of bias mitigation techniques in AI</li>
<li>Studied fairness metrics and their applications</li>
<li>Analyzed impact of data bias on model performance</li>
<li><strong>Focus:</strong> Algorithmic fairness, ethical AI</li>
</ul>
</div>
</div>

</div>

<div class="publications-card">
<h2>📚 Publications and Preprints</h2>

<div class="publications-section">
<h3>Preprints</h3>
<div class="publication-item" id="preprint-1">
<div class="pub-number">1.</div>
<div class="pub-content">
<h4>BLUCK: A Benchmark Dataset for Bengali Linguistic Understanding and Cultural Knowledge</h4>
<div class="authors">
Daeen Kabir, Minhajur Rahman Chowdhury Mahim, Sheikh Shafayat, <strong>Adnan Sadik</strong>, Arian Ahmed, Eunsu Kim, Alice Oh
</div>
<div class="pub-venue">
<em>arXiv preprint</em>
<a href="https://arxiv.org/abs/2505.21092" class="arxiv-link" target="_blank">arXiv:2505.21092</a>
</div>
</div>
</div>
</div>

</div>

</div>

<style>
/* Research Page Styling */
.research-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 1rem;
}

.interests-overview-card {
  background: linear-gradient(135deg, #F5E8C7 0%, #FAF3E0 100%);
  border: 2px solid #D6C6A9;
  border-radius: 15px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  transition: all 0.3s ease;
}

.interests-overview-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(58, 44, 41, 0.15);
  border-color: #D95F18;
}

.interests-overview-card h2 {
  color: #3A2C29;
  text-align: center;
  margin-bottom: 2rem;
  font-weight: bold;
  font-size: 1.8rem;
}

.interests-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.interest-area {
  text-align: center;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.interest-area:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 4px 12px rgba(58, 44, 41, 0.1);
}

.interest-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
  transition: all 0.3s ease;
}

.interest-area:hover .interest-icon {
  transform: scale(1.1);
}

.interest-area h3 {
  color: #3A2C29;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.3;
}

.current-research-card, .publications-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  transition: all 0.3s ease;
}

.current-research-card:hover, .publications-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(58, 44, 41, 0.12);
  border-color: #C4470D;
}

.current-research-card h2, .publications-card h2 {
  color: #3A2C29;
  border-bottom: 3px solid #D95F18;
  padding-bottom: 0.5rem;
  margin-bottom: 2rem;
  font-weight: bold;
  font-size: 1.6rem;
}

.research-project {
  background: rgba(245, 232, 199, 0.3);
  border: 1px solid #D6C6A9;
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.research-project::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(217, 95, 24, 0.05), transparent);
  transition: all 0.6s ease;
}

.research-project:hover {
  transform: translateX(5px);
  border-color: #D95F18;
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  background: rgba(245, 232, 199, 0.5);
}

.research-project:hover::before {
  left: 100%;
}

.project-header {
  margin-bottom: 1rem;
}

.project-header h3 {
  color: #3A2C29;
  font-weight: 600;
  font-size: 1.3rem;
  margin-bottom: 0.8rem;
  line-height: 1.4;
}

.institution {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.institution-link {
  color: #D95F18 !important;
  text-decoration: none !important;
  font-weight: 600;
  transition: all 0.3s ease;
}

.institution-link:hover {
  color: #C4470D !important;
  text-decoration: underline !important;
}

.institution-name {
  color: #3A2C29;
  font-weight: 600;
}

.location {
  color: #6D5A4D;
  font-style: italic;
}

.duration {
  color: #6D5A4D;
  font-style: italic;
  font-size: 0.9rem;
}

.project-details {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 1rem;
}

.status-badge {
  padding: 0.3rem 0.8rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
}

.status-badge.ongoing {
  background: #D95F18;
  color: white;
}

.supervisor {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.supervisor-label {
  color: #6D5A4D;
  font-weight: 500;
}

.supervisor-link {
  color: #D95F18 !important;
  text-decoration: none !important;
  font-weight: 600;
  transition: all 0.3s ease;
}

.supervisor-link:hover {
  color: #C4470D !important;
  text-decoration: underline !important;
}

.project-content {
  margin-top: 1rem;
}

.research-highlights {
  list-style: none;
  padding: 0;
  margin: 0;
}

.research-highlights li {
  position: relative;
  padding-left: 1.5rem;
  margin-bottom: 0.8rem;
  color: #3A2C29;
  line-height: 1.5;
}

.research-highlights li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: #D95F18;
  font-weight: bold;
}

.ref-link {
  color: #D95F18 !important;
  text-decoration: none !important;
  font-weight: 600;
  transition: all 0.3s ease;
}

.ref-link:hover {
  color: #C4470D !important;
  text-decoration: underline !important;
}

.publications-section h3 {
  color: #3A2C29;
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  border-left: 4px solid #D95F18;
  padding-left: 1rem;
}

.publication-item {
  display: flex;
  gap: 1rem;
  background: rgba(245, 232, 199, 0.3);
  border: 1px solid #D6C6A9;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
}

.publication-item:hover {
  transform: translateY(-2px);
  border-color: #D95F18;
  box-shadow: 0 4px 12px rgba(58, 44, 41, 0.1);
}

.pub-number {
  color: #D95F18;
  font-weight: bold;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.pub-content h4 {
  color: #3A2C29;
  font-weight: 600;
  margin-bottom: 0.8rem;
  line-height: 1.4;
}

.authors {
  color: #6D5A4D;
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.authors strong {
  color: #3A2C29;
}

.pub-venue {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.pub-venue em {
  color: #6D5A4D;
}

.arxiv-link {
  background: #3A2C29;
  color: white !important;
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  text-decoration: none !important;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.3s ease;
}

.arxiv-link:hover {
  background: #D95F18;
  transform: scale(1.05);
}

/* Dark Mode Support */
[data-theme="dark"] .interests-overview-card {
  background: linear-gradient(135deg, #3A2418 0%, #2C1810 100%);
  border-color: #5A3825;
}

[data-theme="dark"] .interests-overview-card h2 {
  color: #F5E8C7;
}

[data-theme="dark"] .interest-area {
  background: rgba(58, 36, 24, 0.5);
}

[data-theme="dark"] .interest-area:hover {
  background: rgba(58, 36, 24, 0.8);
}

[data-theme="dark"] .interest-area h3 {
  color: #F5E8C7;
}

[data-theme="dark"] .current-research-card,
[data-theme="dark"] .publications-card {
  background: rgba(58, 36, 24, 0.8);
  border-color: #5A3825;
}

[data-theme="dark"] .current-research-card h2,
[data-theme="dark"] .publications-card h2 {
  color: #F5E8C7;
  border-bottom-color: #FF8A4C;
}

[data-theme="dark"] .research-project,
[data-theme="dark"] .publication-item {
  background: rgba(58, 36, 24, 0.6);
  border-color: #5A3825;
}

[data-theme="dark"] .research-project:hover,
[data-theme="dark"] .publication-item:hover {
  background: rgba(58, 36, 24, 0.8);
  border-color: #FF8A4C;
}

[data-theme="dark"] .project-header h3,
[data-theme="dark"] .pub-content h4 {
  color: #F5E8C7;
}

[data-theme="dark"] .institution-name,
[data-theme="dark"] .research-highlights li,
[data-theme="dark"] .authors strong {
  color: #F5E8C7;
}

[data-theme="dark"] .location,
[data-theme="dark"] .duration,
[data-theme="dark"] .supervisor-label,
[data-theme="dark"] .authors,
[data-theme="dark"] .pub-venue em {
  color: #D6C6A9;
}

[data-theme="dark"] .institution-link,
[data-theme="dark"] .supervisor-link,
[data-theme="dark"] .ref-link {
  color: #FF8A4C !important;
}

[data-theme="dark"] .institution-link:hover,
[data-theme="dark"] .supervisor-link:hover,
[data-theme="dark"] .ref-link:hover {
  color: #FF6B2B !important;
}

[data-theme="dark"] .status-badge.ongoing {
  background: #FF8A4C;
  color: #2C1810;
}

[data-theme="dark"] .research-highlights li::before {
  color: #FF8A4C;
}

[data-theme="dark"] .publications-section h3 {
  color: #F5E8C7;
  border-left-color: #FF8A4C;
}

[data-theme="dark"] .pub-number {
  color: #FF8A4C;
}

[data-theme="dark"] .arxiv-link {
  background: #FF8A4C;
  color: #2C1810 !important;
}

[data-theme="dark"] .arxiv-link:hover {
  background: #FF6B2B;
}

/* Responsive Design */
@media (max-width: 768px) {
  .research-container {
    padding: 0.5rem;
  }
  
  .interests-overview-card {
    padding: 1.5rem;
  }
  
  .interests-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
  }
  
  .current-research-card, .publications-card {
    padding: 1.5rem;
  }
  
  .research-project, .publication-item {
    padding: 1rem;
  }
  
  .project-details {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .institution {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
  }
  
  .publication-item {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .pub-venue {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
}
</style>



