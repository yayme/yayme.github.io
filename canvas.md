---
layout: page
title: Canvas
subtitle: A Gallery of Ideas, Sketches, and Experiments
author: Adnan Sadik
meta_description: "Canvas - Adnan Sadik | Gallery of visual experiments, mathematical sketches, and interactive visualizations"
keywords: "canvas, gallery, visualizations, sketches, experiments, mathematics"
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

<div class="canvas-wrapper">
  <div class="canvas-container">

    <!-- Sidebar Navigation -->
    <aside class="canvas-sidebar">
      <div class="sidebar-header">
        <span class="sidebar-label">Entries</span>
      </div>
      <nav class="sidebar-nav">
        <ul class="entries-list" id="entries-sidebar"></ul>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="canvas-main" id="canvas-main"></main>

  </div>
</div>

<style>
/* ── Layout ─────────────────────────────────────────────────────────── */
.canvas-wrapper {
  padding: 2rem 1.5rem 4rem;
}

.canvas-container {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 2.5rem;
  align-items: start;
  /* No max-width: fill the available viewport */
}

/* ── Sidebar ─────────────────────────────────────────────────────────── */
.canvas-sidebar {
  position: sticky;
  top: 90px;
  background: rgba(255, 250, 242, 0.98);
  border: 1px solid #D6C6A9;
  border-radius: 10px;
  padding: 1.2rem 0.8rem;
  box-shadow: 0 2px 10px rgba(58, 44, 41, 0.07);
}

[data-theme="dark"] .canvas-sidebar {
  background: rgba(24, 18, 15, 0.96);
  border-color: #4A2E1C;
  box-shadow: 0 2px 10px rgba(0,0,0,0.25);
}

.sidebar-header {
  margin-bottom: 0.8rem;
  padding-bottom: 0.6rem;
  border-bottom: 2px solid #D95F18;
}

.sidebar-label {
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #3A2C29;
}

[data-theme="dark"] .sidebar-label {
  color: #F5E8C7;
}

.entries-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.entry-link {
  display: block;
  padding: 0.45rem 0.6rem;
  color: #5a4030;
  text-decoration: none;
  border-left: 2px solid #D6C6A9;
  border-radius: 3px;
  transition: all 0.2s ease;
  font-size: 0.78rem;
  font-weight: 500;
  line-height: 1.3;
  white-space: normal;       /* allow wrap so full title shows */
}

.entry-link:hover {
  background: rgba(217, 95, 24, 0.08);
  border-left-color: #D95F18;
  color: #D95F18;
  transform: translateX(2px);
}

.entry-link.active {
  background: rgba(217, 95, 24, 0.12);
  border-left-color: #D95F18;
  color: #D95F18;
  font-weight: 700;
}

.entry-num {
  display: block;
  font-size: 0.6rem;
  color: #b09070;
  font-weight: 400;
  letter-spacing: 0.05em;
  margin-bottom: 1px;
}

[data-theme="dark"] .entry-link {
  color: #C9B8A0;
  border-left-color: #4A2E1C;
}
[data-theme="dark"] .entry-link:hover,
[data-theme="dark"] .entry-link.active {
  background: rgba(255,138,76,0.1);
  border-left-color: #FF8A4C;
  color: #FF8A4C;
}
[data-theme="dark"] .entry-num { color: #806040; }

/* ── Main area ───────────────────────────────────────────────────────── */
.canvas-main {
  display: grid;
  gap: 2.5rem;
  min-width: 0; /* prevent grid blowout */
}

/* ── Individual entry card ───────────────────────────────────────────── */
.canvas-entry {
  background: rgba(255, 250, 242, 0.98);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 2.5rem 3rem;
  box-shadow: 0 2px 12px rgba(58, 44, 41, 0.07);
  scroll-margin-top: 100px;
  transition: box-shadow 0.25s ease, border-color 0.25s ease;
}

.canvas-entry:hover {
  box-shadow: 0 5px 22px rgba(58, 44, 41, 0.13);
  border-color: #C89060;
}

[data-theme="dark"] .canvas-entry {
  background: rgba(24, 18, 15, 0.96);
  border-color: #4A2E1C;
  box-shadow: 0 2px 12px rgba(0,0,0,0.22);
}
[data-theme="dark"] .canvas-entry:hover {
  box-shadow: 0 5px 22px rgba(0,0,0,0.35);
  border-color: #7A4828;
}

.entry-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #DDD0B8;
  gap: 1rem;
}

[data-theme="dark"] .entry-header {
  border-bottom-color: #4A2E1C;
}

.entry-title {
  color: #2A1F1A;
  font-size: 1.6rem;
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
}

[data-theme="dark"] .entry-title { color: #F5E8C7; }

.entry-date {
  color: #9a7860;
  font-size: 0.82rem;
  font-style: italic;
  white-space: nowrap;
  flex-shrink: 0;
}

[data-theme="dark"] .entry-date { color: #B09070; }

.entry-content {
  line-height: 1.8;
  color: #3A2C29;
}

[data-theme="dark"] .entry-content { color: #F0E0C8; }

.entry-caption {
  font-size: 0.82rem;
  color: #9a7860;
  margin-top: 1rem;
  font-style: italic;
  line-height: 1.5;
}

[data-theme="dark"] .entry-caption { color: #A08060; }

/* ── Empty state ─────────────────────────────────────────────────────── */
.empty-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 340px;
  border: 2px dashed #D6C6A9;
  border-radius: 12px;
  color: #9a7860;
  font-size: 1rem;
  font-style: italic;
}
[data-theme="dark"] .empty-placeholder {
  border-color: #4A2E1C;
  color: #806040;
}

/* ── Responsive ──────────────────────────────────────────────────────── */
@media (max-width: 960px) {
  .canvas-container {
    grid-template-columns: 180px 1fr;
    gap: 1.5rem;
  }
  .canvas-entry { padding: 2rem; }
}

@media (max-width: 700px) {
  .canvas-container {
    grid-template-columns: 1fr;
  }
  .canvas-sidebar {
    position: relative;
    top: 0;
  }
  .entries-list {
    flex-direction: row;
    flex-wrap: wrap;
    gap: 0.4rem;
  }
  .entry-link {
    border: 1px solid #D6C6A9;
    border-left-width: 3px;
    border-radius: 4px;
    padding: 0.35rem 0.6rem;
  }
  .entry-num { display: none; }
  .canvas-entry { padding: 1.4rem; }
  .entry-title { font-size: 1.3rem; }
}
</style>

<script>
/* ── Entry management ─────────────────────────────────────────────── */
(function () {
  const sidebar = document.getElementById('entries-sidebar');
  const mainArea = document.getElementById('canvas-main');
  let count = 0;

  window.addCanvasEntry = function (entryId, title, date, content) {
    count++;

    // Remove empty state
    const ep = document.getElementById('_empty');
    if (ep) ep.remove();

    // Sidebar link
    const li = document.createElement('li');
    const link = document.createElement('a');
    link.href = '#' + entryId;
    link.className = 'entry-link' + (count === 1 ? ' active' : '');
    link.innerHTML = `<span class="entry-num">No. ${String(count).padStart(2, '0')}</span>${title}`;
    link.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelectorAll('.entry-link').forEach(l => l.classList.remove('active'));
      this.classList.add('active');
      const el = document.getElementById(entryId);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    li.appendChild(link);
    sidebar.appendChild(li);

    // Main card
    const article = document.createElement('article');
    article.className = 'canvas-entry';
    article.id = entryId;
    article.innerHTML = `
      <div class="entry-header">
        <h2 class="entry-title">${title}</h2>
        <span class="entry-date">${date}</span>
      </div>
      <div class="entry-content">${content}</div>
    `;
    mainArea.appendChild(article);
  };

  // Empty state
  const ep = document.createElement('div');
  ep.className = 'empty-placeholder';
  ep.id = '_empty';
  ep.textContent = 'No entries yet.';
  mainArea.appendChild(ep);
})();
</script>

<script>
/* ── Pencil-sketch streamline animation ───────────────────────────── */
(function () {
  const HTML = `
    <div style="border-radius:8px;overflow:hidden;line-height:0;">
      <canvas id="sketch-canvas" style="width:100%;display:block;"></canvas>
    </div>
    <p class="entry-caption">
      Streamlines of <strong>F(x,y) = (sin y + 0.4 cos 2x,&nbsp; cos x &minus; 0.4 sin 2y)</strong>,
      integrated with Euler steps and drawn with jittered strokes to simulate pencil on paper.
      The field is curl-dominated near the origin and hyperbolic at the saddle points.
    </p>
  `;

  window.addCanvasEntry('streamlines', 'Vector Field Streamlines', 'April 2026', HTML);

  setTimeout(() => {
    const canvas = document.getElementById('sketch-canvas');
    if (!canvas) return;

    /* ── sizing ── */
    const ASPECT = 9 / 16;
    const resize = () => {
      const w = canvas.parentElement.clientWidth;
      canvas.width  = w;
      canvas.height = Math.round(w * ASPECT);
    };
    resize();
    window.addEventListener('resize', () => { resize(); initParticles(); });

    const ctx = canvas.getContext('2d');

    /* ── vector field ── */
    // F(x,y) = (sin(y) + 0.4*cos(2x),  cos(x) - 0.4*sin(2y))
    // Nice saddle/swirl topology, divergence-free near origin
    const fieldX = (x, y) => Math.sin(y) + 0.4 * Math.cos(2 * x);
    const fieldY = (x, y) => Math.cos(x) - 0.4 * Math.sin(2 * y);

    /* ── coordinate helpers ── */
    // map canvas px -> field coords [-π, π] x [-π*aspect, π*aspect]
    const RANGE = Math.PI;
    const toField = (px, py) => {
      const x = (px / canvas.width  - 0.5) * 2 * RANGE;
      const y = (py / canvas.height - 0.5) * 2 * RANGE * ASPECT;
      return [x, y];
    };
    const toCanvas = (fx, fy) => {
      const px = (fx / (2 * RANGE) + 0.5) * canvas.width;
      const py = (fy / (2 * RANGE * ASPECT) + 0.5) * canvas.height;
      return [px, py];
    };

    /* ── dark mode detection ── */
    const isDark = () =>
      document.documentElement.getAttribute('data-theme') === 'dark' ||
      (!document.documentElement.getAttribute('data-theme') &&
        window.matchMedia('(prefers-color-scheme:dark)').matches);

    /* ── paper background ── */
    const drawBackground = () => {
      ctx.fillStyle = isDark() ? '#1A120C' : '#F7F1E6';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // subtle grain
      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      const d = imageData.data;
      for (let i = 0; i < d.length; i += 4) {
        const noise = (Math.random() - 0.5) * 8;
        d[i]   = Math.min(255, Math.max(0, d[i]   + noise));
        d[i+1] = Math.min(255, Math.max(0, d[i+1] + noise));
        d[i+2] = Math.min(255, Math.max(0, d[i+2] + noise));
      }
      ctx.putImageData(imageData, 0, 0);
    };

    /* ── particles ── */
    const N = 380;
    const STEP = 0.012;        // integration step in field coords
    const MAX_AGE = 70;        // steps before reset
    const JITTER = 0.6;        // px noise on each point

    let particles = [];

    const randPos = () => {
      return [
        (Math.random() - 0.5) * 2 * RANGE,
        (Math.random() - 0.5) * 2 * RANGE * ASPECT
      ];
    };

    const initParticles = () => {
      particles = Array.from({ length: N }, (_, i) => {
        const [fx, fy] = randPos();
        return { fx, fy, age: Math.floor(Math.random() * MAX_AGE) };
      });
    };

    initParticles();
    drawBackground();

    /* ── fade overlay ── */
    let frameCount = 0;
    const FADE_EVERY = 220;

    /* ── main loop ── */
    const dark = () => isDark();
    const strokeColor = () => dark() ? 'rgba(230,210,180,' : 'rgba(40,25,15,';

    const tick = () => {
      frameCount++;

      // periodic gentle fade to prevent total buildup
      if (frameCount % FADE_EVERY === 0) {
        ctx.fillStyle = dark() ? 'rgba(26,18,12,0.18)' : 'rgba(247,241,230,0.18)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }

      for (let p of particles) {
        p.age++;

        if (p.age > MAX_AGE) {
          [p.fx, p.fy] = randPos();
          p.age = 0;
          continue;
        }

        const vx = fieldX(p.fx, p.fy);
        const vy = fieldY(p.fx, p.fy);
        const mag = Math.sqrt(vx * vx + vy * vy) + 1e-6;

        // Euler step (normalised so all streamlines travel same speed)
        const nx = p.fx + (vx / mag) * STEP;
        const ny = p.fy + (vy / mag) * STEP;

        // out of bounds -> reset
        if (Math.abs(nx) > RANGE || Math.abs(ny) > RANGE * ASPECT) {
          [p.fx, p.fy] = randPos();
          p.age = 0;
          continue;
        }

        const [x0, y0] = toCanvas(p.fx, p.fy);
        const [x1, y1] = toCanvas(nx, ny);

        // age-based opacity: fade in at birth, fade out at death
        const t = p.age / MAX_AGE;
        const alpha = 0.55 * Math.sin(Math.PI * t);

        // pencil jitter
        const jx = (Math.random() - 0.5) * JITTER;
        const jy = (Math.random() - 0.5) * JITTER;

        ctx.beginPath();
        ctx.moveTo(x0 + jx, y0 + jy);
        ctx.lineTo(x1 + (Math.random()-0.5)*JITTER, y1 + (Math.random()-0.5)*JITTER);
        ctx.lineWidth = 0.55 + Math.random() * 0.45;
        ctx.strokeStyle = strokeColor() + alpha.toFixed(3) + ')';
        ctx.lineCap = 'round';
        ctx.stroke();

        p.fx = nx;
        p.fy = ny;
      }

      requestAnimationFrame(tick);
    };

    tick();
  }, 120);
})();
</script>
