---
layout: page
title: About Me
subtitle: Passionate about statistics, machine learning, and quantitative finance
meta_description: "About Adnan Sadik - Mathematics student at KAIST passionate about statistical learning, machine learning, quantitative finance, and strategic thinking. Personal story and academic interests."
keywords: "Adnan Sadik about, Adnan Sadik biography, KAIST mathematics student, statistical learning, machine learning, quantitative finance, chess player, mystery fiction, academic interests"
share-title: "About Adnan Sadik - Mathematics Student at KAIST"
share-description: "Learn about Adnan Sadik, mathematics student at KAIST with interests in statistical learning, machine learning, and quantitative finance."
---

<div class="about-container">

<div class="intro-card">
<div class="intro-content">
<p>My name is <strong>Adnan Sadik</strong>. I'm someone who enjoys solving complex problems, collaborating with driven individuals, and engaging in strategic thinking—whether in professional settings or over a good game of Chess, Avalon, or Poker.</p>

<p>I'm passionate about meaningful work, especially when it involves creativity, logic, and collaboration. Outside of work, I enjoy exploring mystery fiction—both in literature and film—as a way to unwind and spark curiosity.</p>
</div>
</div>

<div class="interests-card">
<h3>Academic Interests</h3>
<p>My academic interests lie at the intersection of mathematics, data, and decision-making. I am particularly focused on:</p>

<div class="interest-grid">
<div class="interest-item">
<div class="interest-icon">📊</div>
<h4>Statistical Learning</h4>
<p>Exploring the mathematical foundations of data analysis and inference</p>
</div>

<div class="interest-item">
<div class="interest-icon">💹</div>
<h4>Quantitative Finance</h4>
<p>Applying mathematical models to financial markets and risk management</p>
</div>

<div class="interest-item">
<div class="interest-icon">🤖</div>
<h4>Machine Learning & AI</h4>
<p>Developing intelligent systems that learn from data and make decisions</p>
</div>
</div>

<p><em>These areas excite me for their blend of theory and real-world impact, and I am always eager to explore new developments and practical applications in each.</em></p>
</div>

<div class="story-card">
<h3>My Story</h3>
<div class="story-content">
<p>Originally from a small town, my journey has taken me through diverse challenges and opportunities, eventually leading me to <strong>KAIST</strong>. Along the way, I've grown to value resilience, clarity of thought, and the importance of asking the right questions.</p>

<p>Every step forward has been driven by a desire to learn, adapt, and contribute.</p>
</div>
</div>

<div class="hobbies-card">
<h3>Beyond Academics</h3>
<div class="hobby-grid">
<div class="hobby-item">
<div class="hobby-icon">♟️</div>
<h4>Strategic Games</h4>
<p>Chess, Avalon, Poker</p>
</div>

<div class="hobby-item">
<div class="hobby-icon">📚</div>
<h4>Mystery Fiction</h4>
<p>Literature & Film</p>
</div>

<div class="hobby-item">
<div class="hobby-icon">🧠</div>
<h4>Problem Solving</h4>
<p>Complex challenges</p>
</div>
</div>
</div>

</div>

<!-- Hidden content for SEO: data scientist, AI researcher, machine learning expert, deep learning, artificial intelligence -->

<style>
/* About Me Page Styling */
.about-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
}

.intro-card {
  background: linear-gradient(135deg, #F5E8C7 0%, #FAF3E0 100%);
  border: 2px solid #D6C6A9;
  border-radius: 15px;
  padding: 2.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 15px rgba(58, 44, 41, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.intro-card::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(217, 95, 24, 0.1) 0%, transparent 70%);
  transition: all 0.5s ease;
}

.intro-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(58, 44, 41, 0.15);
  border-color: #D95F18;
}

.intro-card:hover::before {
  top: -30%;
  right: -30%;
}

.intro-content {
  position: relative;
  z-index: 1;
}

.intro-content p {
  font-size: 1.1rem;
  line-height: 1.7;
  color: #3A2C29;
  margin-bottom: 1.5rem;
}

.intro-content strong {
  color: #D95F18;
  font-weight: 700;
}

.interests-card, .story-card, .hobbies-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  transition: all 0.3s ease;
}

.interests-card:hover, .story-card:hover, .hobbies-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(58, 44, 41, 0.12);
  border-color: #C4470D;
}

.interests-card h3, .story-card h3, .hobbies-card h3 {
  color: #3A2C29;
  border-bottom: 3px solid #D95F18;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  font-weight: bold;
  font-size: 1.5rem;
}

.interest-grid, .hobby-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.interest-item, .hobby-item {
  background: rgba(245, 232, 199, 0.4);
  border: 1px solid #D6C6A9;
  border-radius: 10px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.interest-item::before, .hobby-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(217, 95, 24, 0.1), transparent);
  transition: all 0.6s ease;
}

.interest-item:hover, .hobby-item:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 8px 20px rgba(58, 44, 41, 0.15);
  border-color: #D95F18;
  background: rgba(245, 232, 199, 0.6);
}

.interest-item:hover::before, .hobby-item:hover::before {
  left: 100%;
}

.interest-icon, .hobby-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
  filter: grayscale(0.3);
  transition: all 0.3s ease;
}

.interest-item:hover .interest-icon, .hobby-item:hover .hobby-icon {
  filter: grayscale(0);
  transform: scale(1.1);
}

.interest-item h4, .hobby-item h4 {
  color: #3A2C29;
  margin-bottom: 0.8rem;
  font-weight: 600;
  font-size: 1.2rem;
}

.interest-item p, .hobby-item p {
  color: #6D5A4D;
  font-size: 0.95rem;
  line-height: 1.5;
}

.story-content {
  font-size: 1.1rem;
  line-height: 1.7;
  color: #3A2C29;
}

.story-content p {
  margin-bottom: 1.5rem;
}

.story-content strong {
  color: #D95F18;
  font-weight: 700;
}

/* Dark Mode Support */
[data-theme="dark"] .intro-card {
  background: linear-gradient(135deg, #3A2418 0%, #2C1810 100%);
  border-color: #5A3825;
}

[data-theme="dark"] .intro-card::before {
  background: radial-gradient(circle, rgba(255, 138, 76, 0.1) 0%, transparent 70%);
}

[data-theme="dark"] .intro-content p {
  color: #F5E8C7;
}

[data-theme="dark"] .intro-content strong {
  color: #FF8A4C;
}

[data-theme="dark"] .interests-card,
[data-theme="dark"] .story-card,
[data-theme="dark"] .hobbies-card {
  background: rgba(58, 36, 24, 0.8);
  border-color: #5A3825;
}

[data-theme="dark"] .interests-card h3,
[data-theme="dark"] .story-card h3,
[data-theme="dark"] .hobbies-card h3 {
  color: #F5E8C7;
  border-bottom-color: #FF8A4C;
}

[data-theme="dark"] .interests-card p,
[data-theme="dark"] .story-card p,
[data-theme="dark"] .hobbies-card p {
  color: #F5E8C7;
}

[data-theme="dark"] .interest-item,
[data-theme="dark"] .hobby-item {
  background: rgba(58, 36, 24, 0.6);
  border-color: #5A3825;
}

[data-theme="dark"] .interest-item:hover,
[data-theme="dark"] .hobby-item:hover {
  background: rgba(58, 36, 24, 0.8);
  border-color: #FF8A4C;
}

[data-theme="dark"] .interest-item::before,
[data-theme="dark"] .hobby-item::before {
  background: linear-gradient(90deg, transparent, rgba(255, 138, 76, 0.1), transparent);
}

[data-theme="dark"] .interest-item h4,
[data-theme="dark"] .hobby-item h4 {
  color: #F5E8C7;
}

[data-theme="dark"] .interest-item p,
[data-theme="dark"] .hobby-item p {
  color: #D6C6A9;
}

[data-theme="dark"] .story-content {
  color: #F5E8C7;
}

[data-theme="dark"] .story-content strong {
  color: #FF8A4C;
}

/* Responsive Design */
@media (max-width: 768px) {
  .about-container {
    padding: 0.5rem;
  }
  
  .intro-card {
    padding: 1.5rem;
  }
  
  .interests-card, .story-card, .hobbies-card {
    padding: 1.5rem;
  }
  
  .interest-grid, .hobby-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .interest-icon, .hobby-icon {
    font-size: 2.5rem;
  }
}
</style>

