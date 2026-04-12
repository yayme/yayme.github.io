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
        <h3>Entries</h3>
      </div>
      <nav class="sidebar-nav">
        <ul class="entries-list" id="entries-sidebar">
          <!-- Entry links will be populated here -->
        </ul>
      </nav>
      <div class="sidebar-footer">
        <p class="sidebar-note">A collection of visual explorations and ideas</p>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="canvas-main" id="canvas-main">
      <!-- Canvas entries will be added here -->
    </main>
  </div>
</div>

<style>
/* Canvas Page Layout */
.canvas-wrapper {
  padding: 2rem 1rem;
}

.canvas-container {
  max-width: 1400px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 70px 1fr;
  gap: 1rem;
  padding: 0;
}

/* Sidebar Styling */
.canvas-sidebar {
  background: rgba(255, 250, 242, 0.98);
  border: 1px solid #D6C6A9;
  border-radius: 8px;
  padding: 1rem 0.6rem;
  height: fit-content;
  position: sticky;
  top: 100px;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  margin-left: 0.25rem;
}

[data-theme="dark"] .canvas-sidebar {
  background: rgba(24, 18, 15, 0.95);
  border-color: #5A3825;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.18);
}

.sidebar-header h3 {
  color: #3A2C29;
  font-size: 0.9rem;
  font-weight: 700;
  margin: 0 0 0.8rem 0;
  border-bottom: 2px solid #D95F18;
  padding-bottom: 0.3rem;
  writing-mode: vertical-rl;
  text-orientation: mixed;
}

[data-theme="dark"] .sidebar-header h3 {
  color: #F5E8C7;
  border-bottom-color: #FF8A4C;
}

.entries-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.entries-list li {
  margin-bottom: 0;
}

.entry-link {
  display: block;
  padding: 0.4rem 0.4rem;
  color: #3A2C29;
  text-decoration: none;
  border-left: 3px solid #D6C6A9;
  border-radius: 2px;
  transition: all 0.3s ease;
  font-size: 0.75rem;
  font-weight: 500;
  writing-mode: vertical-rl;
  text-orientation: mixed;
}

.entry-link:hover {
  background: rgba(217, 95, 24, 0.1);
  border-left-color: #D95F18;
  color: #D95F18;
  transform: translateX(3px);
}

.entry-link.active {
  background: rgba(217, 95, 24, 0.15);
  border-left-color: #D95F18;
  color: #D95F18;
  font-weight: 600;
}

[data-theme="dark"] .entry-link {
  color: #F5E8C7;
  border-left-color: #5A3825;
}

[data-theme="dark"] .entry-link:hover {
  background: rgba(255, 138, 76, 0.1);
  border-left-color: #FF8A4C;
  color: #FF8A4C;
}

[data-theme="dark"] .entry-link.active {
  background: rgba(255, 138, 76, 0.15);
  border-left-color: #FF8A4C;
  color: #FF8A4C;
}

.sidebar-footer {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #D6C6A9;
  display: none;
}

[data-theme="dark"] .sidebar-footer {
  border-top-color: #5A3825;
}

.sidebar-note {
  color: #8a7060;
  font-size: 0.7rem;
  margin: 0;
  line-height: 1.2;
  font-style: italic;
  display: none;
}

[data-theme="dark"] .sidebar-note {
  color: #D6C6A9;
}

/* Main Content Area */
.canvas-main {
  display: grid;
  gap: 2rem;
}

.canvas-entry {
  background: rgba(255, 250, 242, 0.98);
  border: 1px solid #D6C6A9;
  border-radius: 12px;
  padding: 2.5rem;
  box-shadow: 0 3px 12px rgba(58, 44, 41, 0.08);
  scroll-margin-top: 100px;
  transition: all 0.3s ease;
}

.canvas-entry:hover {
  box-shadow: 0 6px 20px rgba(58, 44, 41, 0.12);
  border-color: #D95F18;
}

[data-theme="dark"] .canvas-entry {
  background: rgba(24, 18, 15, 0.95);
  border-color: #5A3825;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.18);
}

[data-theme="dark"] .canvas-entry:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  border-color: #FF8A4C;
}

.entry-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #D6C6A9;
}

[data-theme="dark"] .entry-header {
  border-bottom-color: #5A3825;
}

.entry-title {
  color: #3A2C29;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
  flex: 1;
}

[data-theme="dark"] .entry-title {
  color: #F5E8C7;
}

.entry-date {
  color: #8a7060;
  font-size: 0.9rem;
  font-style: italic;
  white-space: nowrap;
  margin-left: 1rem;
}

[data-theme="dark"] .entry-date {
  color: #D6C6A9;
}

.entry-content {
  line-height: 1.8;
  color: #3A2C29;
}

[data-theme="dark"] .entry-content {
  color: #F5E8C7;
}

/* Placeholder Styling */
.entry-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  background: linear-gradient(135deg, rgba(245, 232, 199, 0.3) 0%, rgba(250, 243, 224, 0.3) 100%);
  border: 2px dashed #D6C6A9;
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
}

[data-theme="dark"] .entry-placeholder {
  background: linear-gradient(135deg, rgba(58, 36, 24, 0.3) 0%, rgba(44, 24, 16, 0.3) 100%);
  border-color: #5A3825;
}

.placeholder-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.entry-placeholder p {
  color: #8a7060;
  font-size: 1rem;
  margin: 0;
}

[data-theme="dark"] .entry-placeholder p {
  color: #D6C6A9;
}

/* Content Block Styles for Articles */
.entry-text {
  margin-bottom: 1.5rem;
}

.entry-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 2rem 0;
  box-shadow: 0 4px 12px rgba(58, 44, 41, 0.1);
}

[data-theme="dark"] .entry-image {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.entry-math {
  background: rgba(217, 95, 24, 0.05);
  border-left: 4px solid #D95F18;
  border-radius: 4px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  overflow-x: auto;
}

[data-theme="dark"] .entry-math {
  background: rgba(255, 138, 76, 0.05);
  border-left-color: #FF8A4C;
}

.entry-code {
  background: rgba(58, 44, 41, 0.05);
  border: 1px solid #D6C6A9;
  border-radius: 6px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  overflow-x: auto;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  line-height: 1.6;
}

[data-theme="dark"] .entry-code {
  background: rgba(255, 255, 255, 0.03);
  border-color: #5A3825;
}

code {
  background: rgba(217, 95, 24, 0.1);
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

[data-theme="dark"] code {
  background: rgba(255, 138, 76, 0.1);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .canvas-container {
    grid-template-columns: 60px 1fr;
    gap: 0.8rem;
    padding: 0;
  }

  .canvas-sidebar {
    padding: 0.8rem 0.5rem;
    margin-left: 0.1rem;
  }

  .canvas-entry {
    padding: 1.5rem;
  }
}

@media (max-width: 768px) {
  .canvas-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 0 1rem;
  }

  .canvas-sidebar {
    position: relative;
    top: 0;
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 1rem;
    align-items: start;
    padding: 1rem 1.5rem;
    margin-bottom: 1rem;
  }

  .sidebar-header {
    grid-column: 1;
  }

  .sidebar-nav {
    grid-column: 2;
  }

  .entries-list {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .entries-list li {
    margin-bottom: 0;
  }

  .entry-link {
    padding: 0.5rem 0.75rem;
    border: 1px solid #D6C6A9;
    border-left: none;
    font-size: 0.85rem;
  }

  .sidebar-footer {
    grid-column: 3;
    margin: 0;
    padding: 0;
    border: none;
  }

  .entry-placeholder {
    min-height: 200px;
  }

  .entry-header {
    flex-direction: column;
  }

  .entry-date {
    margin-left: 0;
    margin-top: 0.5rem;
  }
}

@media (max-width: 480px) {
  .canvas-sidebar {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .sidebar-footer {
    grid-column: 1;
  }

  .entry-title {
    font-size: 1.4rem;
  }

  .canvas-entry {
    padding: 1rem;
  }

  .placeholder-icon {
    font-size: 2rem;
  }
}
</style>

<script>
// Canvas page entry management system
(function() {
  const sidebar = document.getElementById('entries-sidebar');
  const mainArea = document.getElementById('canvas-main');

  // Helper function to add an entry
  window.addCanvasEntry = function(entryId, title, date, content) {
    // Remove empty state if first entry
    const emptyMsg = document.getElementById('empty-msg');
    const emptyPlaceholder = document.getElementById('empty-placeholder');
    if (emptyMsg) emptyMsg.remove();
    if (emptyPlaceholder) emptyPlaceholder.remove();

    // Add to sidebar
    if (sidebar) {
      const li = document.createElement('li');
      const link = document.createElement('a');
      link.href = '#' + entryId;
      link.className = 'entry-link';
      if (sidebar.children.length === 0) {
        link.classList.add('active');
      }
      link.textContent = title;
      link.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelectorAll('.entry-link').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
        const target = document.getElementById(entryId);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
      li.appendChild(link);
      sidebar.appendChild(li);
    }

    // Add to main area
    if (mainArea) {
      const article = document.createElement('article');
      article.className = 'canvas-entry';
      article.id = entryId;
      article.innerHTML = `
        <div class="entry-header">
          <h2 class="entry-title">${title}</h2>
          <span class="entry-date">${date}</span>
        </div>
        <div class="entry-content">
          ${content}
        </div>
      `;
      mainArea.appendChild(article);
    }
  };

  // Show empty state initially
  const emptyMsg = document.createElement('li');
  emptyMsg.style.color = '#8a7060';
  emptyMsg.style.fontSize = '0.9rem';
  emptyMsg.style.padding = '1rem';
  emptyMsg.style.textAlign = 'center';
  emptyMsg.id = 'empty-msg';
  emptyMsg.textContent = 'No entries yet';
  sidebar.appendChild(emptyMsg);

  const emptyPlaceholder = document.createElement('div');
  emptyPlaceholder.className = 'entry-placeholder';
  emptyPlaceholder.style.minHeight = '400px';
  emptyPlaceholder.id = 'empty-placeholder';
  emptyPlaceholder.innerHTML = `
    <div class="placeholder-icon" style="font-size: 4rem;">✨</div>
    <h3 style="color: #3A2C29; margin-top: 1rem;">Canvas is Empty</h3>
  `;
  mainArea.appendChild(emptyPlaceholder);
})();
</script>

<script>
// WebGL Divergence Field Animation - First Entry
const initDivergenceFieldEntry = function() {
  const vertexShader = `
    attribute vec2 position;
    void main() {
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `;

  const fragmentShader = `
    precision highp float;
    uniform vec2 u_resolution;
    uniform float u_time;

    vec2 vector_field(vec2 p) {
      p += u_time * 0.5;
      float x = sin(p.y * 2.0 + u_time) * 0.5 + cos(p.x * 3.0) * 0.3;
      float y = cos(p.x * 2.0 - u_time) * 0.5 + sin(p.y * 3.0) * 0.3;
      return vec2(x, y);
    }

    float divergence(vec2 p) {
      float eps = 0.01;
      vec2 v_center = vector_field(p);
      vec2 v_px = vector_field(p + vec2(eps, 0.0));
      vec2 v_py = vector_field(p + vec2(0.0, eps));
      
      float div = ((v_px.x - v_center.x) / eps) + ((v_py.y - v_center.y) / eps);
      return div;
    }

    vec3 hsv2rgb(vec3 c) {
      vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
      vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
      return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }

    void main() {
      vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / min(u_resolution.y, u_resolution.x);
      uv *= 3.0;
      
      float div = divergence(uv);
      float magnitude = length(vector_field(uv));
      
      float hue = atan(vector_field(uv).y, vector_field(uv).x) / 6.28318530718 + 0.5;
      float saturation = magnitude / (magnitude + 1.0);
      float value = 0.5 + 0.5 * tanh(div * 2.0);
      
      gl_FragColor = vec4(hsv2rgb(vec3(hue, saturation, value)), 1.0);
    }
  `;

  const containerHTML = `
    <div style="width: 100%; height: 600px; border-radius: 8px; overflow: hidden; background: #000;">
      <canvas id="divergence-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
    </div>
  `;

  window.addCanvasEntry(
    'divergence-field',
    'Divergence Field Flow',
    'April 2026',
    containerHTML
  );

  // Initialize WebGL after entry is added
  setTimeout(() => {
    const canvas = document.getElementById('divergence-canvas');
    if (!canvas) return;

    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) {
      console.error('WebGL not supported');
      return;
    }

    // Set canvas size
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * devicePixelRatio;
    canvas.height = rect.height * devicePixelRatio;

    // Create shader program
    const createShader = (type, source) => {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(shader));
        return null;
      }
      return shader;
    };

    const vShader = createShader(gl.VERTEX_SHADER, vertexShader);
    const fShader = createShader(gl.FRAGMENT_SHADER, fragmentShader);

    const program = gl.createProgram();
    gl.attachShader(program, vShader);
    gl.attachShader(program, fShader);
    gl.linkProgram(program);

    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      console.error(gl.getProgramInfoLog(program));
      return;
    }

    gl.useProgram(program);

    // Create buffer
    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]),
      gl.STATIC_DRAW
    );

    const positionLocation = gl.getAttribLocation(program, 'position');
    gl.enableVertexAttribArray(positionLocation);
    gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

    // Get uniform locations
    const resolutionLocation = gl.getUniformLocation(program, 'u_resolution');
    const timeLocation = gl.getUniformLocation(program, 'u_time');

    // Animation loop
    let startTime = Date.now();
    const animate = () => {
      const elapsed = (Date.now() - startTime) / 1000;

      gl.viewport(0, 0, canvas.width, canvas.height);
      gl.uniform2f(resolutionLocation, canvas.width, canvas.height);
      gl.uniform1f(timeLocation, elapsed);

      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      requestAnimationFrame(animate);
    };

    animate();

    // Handle resizing
    window.addEventListener('resize', () => {
      const newRect = canvas.getBoundingClientRect();
      canvas.width = newRect.width * devicePixelRatio;
      canvas.height = newRect.height * devicePixelRatio;
    });
  }, 100);
};

// Initialize Divergence Field entry when page loads
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initDivergenceFieldEntry);
} else {
  initDivergenceFieldEntry();
}
</script>
