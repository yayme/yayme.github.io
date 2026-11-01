---
layout: page
title: Research
author: Adnan Sadik
meta_description: "Research - Adnan Sadik | Marked temporal point processes, deep learning for physiological time series, stochastic modeling of birth-death processes, and LLM evaluation"
keywords: "Adnan Sadik research, marked temporal point process, online event processing, applied AI, mathematical modeling, deep learning, KAIST, IBS, stochastic modeling"
---

<div class="rp">

<p class="rp-interests"><span class="rp-interests-label">Research interests</span> Applied AI, mathematical modeling, deep learning, marked temporal point processes, online event processing</p>

<h2>Education</h2>

<div class="rp-entry">
  <div class="rp-head"><span class="rp-org">Korea Advanced Institute of Science and Technology (KAIST)</span><span class="rp-date">2023 – Dec 2027 (expected)</span></div>
  <div class="rp-meta">B.S. Mathematics and Computer Science, double major · South Korea</div>
  <p class="rp-text">Coursework concentrated in probability theory, mathematical statistics, machine learning, deep learning, reinforcement learning, statistical decision making, and dynamic programming.</p>
</div>

<h2>Research Experience</h2>

<div class="rp-entry">
  <div class="rp-head"><span class="rp-org">Institute for Basic Science</span><span class="rp-date">Dec 2024 – Dec 2025</span></div>
  <div class="rp-meta">Research Intern, <a href="https://www.ibs.re.kr/bimag/">Biomedical Mathematics Group</a> · Supervisor: <strong>Professor Jae Kyoung Kim</strong></div>
  <p class="rp-text"><span class="rp-thread">Sleep disease prediction.</span> Using self-supervised pre-training for sleep disease classification under limited labels.</p>
  <p class="rp-text"><span class="rp-thread">Stochastic modeling in cell dynamics.</span> Inferred the non-Markovian delays hidden in birth–death processes, using likelihood-based methods and physics-informed neural networks.</p>
</div>

<div class="rp-entry">
  <div class="rp-head"><span class="rp-org"><a href="https://uilab.kr/">Users &amp; Information Lab</a>, KAIST</span><span class="rp-date">2024 – 2025</span></div>
  <div class="rp-meta">Supervisor: <strong>Professor Alice Oh</strong></div>
  <p class="rp-text">Built a benchmark for cultural and linguistic understanding in low-resource languages and evaluated proprietary and open-source models against it. Published as <em>BLUCK</em> at an AACL-IJCNLP 2025 workshop — <a href="https://aclanthology.org/2025.banglalp-1.14/">ACL Anthology</a>.</p>
</div>

<h2>Industry Experience</h2>

<div class="rp-entry">
  <div class="rp-head"><span class="rp-org">HayanMind, Seoul</span><span class="rp-date">Jun 2026 – present</span></div>
  <div class="rp-meta">Machine Learning Engineer Intern, R&amp;D Team · Supervisor: <strong>Dr. Mujin Cheon</strong></div>
  <p class="rp-text">Event processing models (marked temporal point processes) often suffer from temporal distribution shift. How can we measure whether a model is failing to adapt to it? What should the optimal retraining policy and retraining dataset selection be?</p>
</div>

<div class="rp-entry">
  <div class="rp-head"><span class="rp-org">Huawei, Hong Kong SAR</span><span class="rp-date">Jan 2026 – Mar 2026</span></div>
  <div class="rp-meta">Research and Development Intern, Systems Lab · Supervisor: <strong>Dr. Wang Peng</strong></div>
  <p class="rp-text">LLM inference for hybrid attention–Mamba architectures: throughput, latency and memory optimization in C++ and CUDA, including sparse attention kernels, across vLLM, SGLang and TensorRT.</p>
</div>

</div>

<style>
/* Plain academic layout: no cards, borders around entries, or hover effects */
.rp {
  max-width: 740px;
  margin: 0 auto;
  color: #3A2C29;
  font-size: 0.98rem;
  line-height: 1.7;
}

.rp-interests { margin: 0 0 0.5rem; color: #4A3A33; }

.rp-interests-label {
  display: block;
  font-size: 0.72rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: #8A7566;
  margin-bottom: 0.2rem;
}

.rp h2 {
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #8A7566;
  margin: 2.6rem 0 1.1rem;
  padding-bottom: 0.35rem;
  border-bottom: 1px solid #E3D6BC;
}

.rp-entry { margin-bottom: 1.9rem; }
.rp-entry:last-child { margin-bottom: 0; }

.rp-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
}

.rp-org { font-weight: 700; }

.rp-date {
  color: #8A7566;
  font-size: 0.86rem;
  white-space: nowrap;
}

.rp-meta {
  color: #6D5A4D;
  font-size: 0.9rem;
  margin-top: 0.1rem;
}

.rp-text { margin: 0.55rem 0 0; }

.rp-thread { font-style: italic; color: #5C4A3F; }

.rp a { color: #C4470D; text-decoration: none; border-bottom: 1px solid rgba(196, 71, 13, 0.3); }
.rp a:hover { color: #D95F18; border-bottom-color: #D95F18; }

[data-theme="dark"] .rp { color: #F5E8C7; }
[data-theme="dark"] .rp h2,
[data-theme="dark"] .rp-date,
[data-theme="dark"] .rp-interests-label { color: #C4B59A; }
[data-theme="dark"] .rp h2 { border-bottom-color: #5A3825; }
[data-theme="dark"] .rp-meta { color: #D6C6A9; }
[data-theme="dark"] .rp-interests,
[data-theme="dark"] .rp-text { color: #F5E8C7; }
[data-theme="dark"] .rp-thread { color: #D6C6A9; }
[data-theme="dark"] .rp a { color: #FF8A4C; }

@media (max-width: 600px) {
  .rp-head { flex-direction: column; gap: 0; }
  .rp-date { font-size: 0.82rem; }
}
</style>
