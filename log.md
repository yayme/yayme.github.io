# Site maintenance log

Running record of changes to this repo, newest first. This file is listed under `exclude:` in `_config.yml`, so it is never published.

---

## 2026-10-11 — Home page makeover (markdown-file aesthetic)

Three candidates were built and previewed locally (raw-source, rendered-README, plain-document);
Adnan picked the raw-source look. `index.html` rewritten around it, preview files removed.

- **Look:** monospace "editor window" card with an `adnan-sadik.md` title bar and faded markdown
  syntax (`#`, `##`, `-`, `**`). Role lines stay monospace; descriptions use the site body font
  (Open Sans) and supervisors use Lora italic, so the three levels no longer share one font.
- **Header:** page title/subtitle front matter dropped, so no "Home" heading and no
  "AI systems | Applied mathematics..." line. Tagline is now "Mathematics & Computer Science
  (Double Major) · KAIST".
- **Experience split** into Industry (HayanMind, Huawei, Samsung Lifenology Lab) and Research
  (KAIST Users & Information Lab — Professor Alice Oh; IBS Biomedical Mathematics Lab —
  Professor Jae Kyoung Kim).
- **Content edits:** HayanMind adds "Tested domain adaptive deployment strategies"; Huawei adds
  token compression with the OpenZL framework; IBS split into two sub-projects (deep learning
  models for sleep classification; stochastic modeling for gene expression) with the Samsung
  collaboration, IoT, and domain adaptation references removed.
- **Expertise** regrouped into mathematics & statistics / machine learning / engineering.
- **Competitions moved last**, above the contact line (email · resume · github).
- **Follow-up pass:** Huawei split into two sub-projects (hybrid attention–Mamba inference;
  OpenZL token compression); research entries dropped their role titles and now read
  "Lab — Supervisor: Professor X"; MLOps added to machine learning and systems optimization to
  engineering; IMO and APMO bolded.
- **"Currently looking for"** now reads "Roles in AI/ML and performance engineering, quant
  development, and applied AI."
- **Typeface:** swapped the default system monospace for IBM Plex Mono (structure) and IBM Plex
  Sans (prose), loaded per-page via `ext-css` front matter. Lora italic still marks supervisors.

---

## 2026-10-11 — Home page expertise

Removed "CUDA" from the Expertise line in `index.html`; it now ends "Python, C++." No other page touched.

Interests line replaced with "Applied AI, deep learning, mathematical modeling." (was "Geometric and statistical understanding of data, time series AI, quantitative finance, online and offline learning, deep learning.")

---

## 2026-09-16 — Home page headline

`index.html` subtitle changed from "Applied Mathematics | Quantitative Finance | AI systems | C++" to "AI systems | Applied mathematics & Modeling | Quant finance and statistics" (Adnan's own wording, applied verbatim).

---

## 2026-09-16 — Lifenology Lab project link

Added https://lifenologylab.co.kr/project/project3_Connection_9.php everywhere the Samsung Lifenology Lab multi-agent project appears:

- `index.html` — the "Samsung Health × Wellness AI" project name in the Experience paragraph is now a link.
- `projects.md` — "🔗 View on Lifenology Lab" button at the end of the Current Project card, styled like the existing "View on GitHub" buttons.
- `resume.md` — "Lifenology Lab" link on the Samsung Lifenology Lab Project item, matching the sibling GitHub links.

Notes: the lab page lists the project as **Aria** (participants Adnan Sadik, Tajrian Samad, Mamnoon Siam; advisor 김현우 교수), while the site calls it "Samsung Health × Wellness AI". The resume's commented-out Samsung work-experience block (`resume.md:60`) was left untouched, so it has no link if re-enabled.

---

## 2026-09-14 — Home page: light edits to the original text

**Scope:** `index.html` text only. Two earlier, larger rewrites were discarded; the file was restored to the committed original (header, subtitle, front matter, layout, CSS all unchanged) and only these wording edits were made:

- **Competitive Mathematics → Competitions:** "Two-time bronze medalist at IMO and APMO" (per resume years); Jane Street Prize worded as "Jane Street Prize winner at the Simon Marais Mathematics Competition"; added "1st place in the Trading and Quant Challenges at Discover Citadel" (from the About page).
- **Experience:** HayanMind title corrected to "Machine Learning and Forward Deployed Engineer Intern" (per Adnan); "Currently" → "Most recently" (resume dates HayanMind Jun–Aug 2026); "inference performance for Hybrid LLM models" → "inference for hybrid attention–Mamba LLMs"; "Published at AACL" → "Published at an AACL-IJCNLP 2025 workshop"; IBS work rewritten as one sentence (per Adnan): both the IoT insomnia classification research with Samsung and the stochastic process modeling / domain adaptation work happened at the Institute for Basic Science Biomedical Mathematics Lab, under the supervision of Professor Jae Kyoung Kim.
- **Expertise:** added "Probability and", "stochastic processes", "Transformers", and "Python, C++, CUDA."; fixed capitalization.
- **Interests:** removed the stray spaces before "," and ".".

**Open question:** if the HayanMind internship is still ongoing, change "Most recently" back to "Currently".

---

## 2026-09-14 — Technical fixes (no content changes)

**Scope:** structural and technical fixes only. No wording, dates, numbers, or claims were edited. Changes are uncommitted.

### Changes

1. **Stray `>` after `<html>`** — `_layouts/base.html`
   - The tag was `<html lang="en">>`. Browsers read the extra `>` as body text, which ends `<head>` early. On the live site `<head>` is empty and all 68 meta/link/title tags land in `<body>` (some crawlers and link-preview bots only read `<head>`), and a `>` is rendered at the top of every page.
   - Verified: local build has 57 elements in `<head>`, none in `<body>`, no stray text.

2. **Domain is now `adnansadik.dev` everywhere** — `_config.yml` (`url`, `url-pretty`), `robots.txt` (Sitemap line)
   - Canonical links, `og:url`, sitemap, RSS, JSON-LD, and the navbar name/avatar links all pointed at `yayme.github.io`, which 301-redirects to `adnansadik.dev`.
   - Verified: zero occurrences of `yayme.github.io` in the production build.

3. **Two stray `'` characters on the resume** — `resume.md`
   - They wrapped the Volatility project block and rendered as literal quotes.

4. **Math on the Projects page** — `_includes/mathjax.html`, `projects.md`
   - Loader moved from `cdn.mathjax.org` (retired in 2017; it only serves a shim that loads MathJax 2.7.1, which ignores the v3-style config already in the file) to MathJax 3.2.2 on jsDelivr, pinned.
   - `projects.md`: added `mathjax: true`; changed the 7 inline formulas from `$…$` to `\(…\)`. Same text, now typeset.
   - Verified: 7 expressions typeset, no raw delimiters left. Posts checked for regressions: the first post's dollar amounts ($X, $2X) stay plain text; the independence post renders the same as live (see open items).

5. **`<head>` cleanup** — `_includes/head.html`
   - Removed duplicates: second `meta description`, second `keywords`, second `og:site_name`, second `twitter:image`, `property="twitter:title/description"` copies, second favicon link.
   - Removed links to files that don't exist (all 404 live): `apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `site.webmanifest`.
   - Removed hardcoded `og:image:width/height/type` (claimed a 1200×630 PNG; no share image is that size).
   - Merged the two `Person` JSON-LD blocks. Kept the first block's values verbatim, set `@type` to `"Person"` (`Student`/`Researcher` aren't schema.org types), and added the `image` field from the second block, which was then deleted (it hardcoded `yayme.github.io`).
   - Removed the LinkedIn badge script (loaded on every page; no page contains a badge).
   - Verified: all 29 JSON-LD blocks in the build parse as valid JSON; no page has a duplicated meta name/property.

6. **Leftover files no longer published** — `_config.yml` `exclude:`
   - `education_clean.md` (old copy of Education), `portfolio.md` and `www-redirect.html` (both empty), the five `*_project.html` card prototypes, `assets/timeslot_sync_view.py`, and `log.md`. All files remain in the repo.
   - Side effect of #8: the raw source of `aboutme.md` is no longer published at `/aboutme.md`.
   - Verified: none of these appear in the build output.

7. **Lighter avatar** — new `assets/img/avatar-icon.jpg`, `_config.yml` `avatar:`
   - 400×600 JPEG, 44 KB, resized from the 1024×1536 2.4 MB PNG. It is shown at most 100 px wide (navbar) and is also the default share image.
   - The original PNG is kept so existing external links to it still work.

8. **`aboutme.md` tidy-up**
   - Added front matter (`layout: page`). This is the layout it already got implicitly, so output is unchanged, but the page no longer depends on GitHub Pages' optional-front-matter plugin (the CI build doesn't have it).
   - Removed a pasted, commented-out dark-mode script sitting inside the November 2025 `<ul>`.
   - Removed a 284-line `<style>` block whose classes (`intro-card`, `interests-card`, `hobby-item`, …) aren't used on the page.
   - Verified: page renders the same; tab title unchanged.

9. **Canvas sketch** — `canvas.md`
   - Resize handler now rebuilds only when the width changes (mobile browsers fire `resize` when the URL bar shows/hides, which wiped the sketch while scrolling), and repaints the paper background after a rebuild (the canvas was left transparent).
   - Corrected a code comment that called the field divergence-free near the origin (div F = −0.8(sin 2x + cos 2y), so −0.8 at the origin).
   - Verified: height-only resize keeps the drawing; width change rebuilds with the paper background (0 transparent pixels).

### How this was verified

- Built locally with Jekyll 3.10 plus GitHub Pages' default plugins. A baseline build of the previous commit matched the live HTML except for Tag Manager lines (disabled locally) and apostrophe escaping.
- Diffed every built page before vs after; only the changes above appear.
- Browser checks at `http://localhost:4000`: head parsing, MathJax, resume, canvas resize, About, all pages' consoles, server log (no missing assets).

### Not changed — content, waiting on you

- **Stale "current" claims:** ~~home says "Currently … at HayanMind" (resume: Jun–Aug 2026)~~ (home page fixed in the entry above). Samsung is "Current Project / In Progress" on Projects and commented out of resume experience. Research shows IBS "Ongoing, Dec 2024 – Aug 2025"; resume says "Dec 2024 – June 2025". About's Recent Events end at Nov 2025.
- **Resume order:** Huawei (Dec 2025) is listed above HayanMind (Jun 2026).
- **Numbers that disagree:** Yut win rate 56.5% (resume) vs "54–56%" (Projects); Projects text says GP + UCB, card says GP + EI. CUDA "1.8× speedup" on the resume reads as vs dense attention; Projects says it's v2 over v1.
- **Typos:** "Users & Informations Lab" (`resume.md`, `research.md`); placeholder course code `MASXXX` (`education.md`).
- **Independence post:** `$(0,0), (0,1), (1,1), (1,2)$` shows with literal dollar signs (single `$` isn't a math delimiter, before or after this change). Use `$$…$$` if it's meant as math.
- **Projects:** `1.4--1.8×` shows a double hyphen (en dash intended?).
- **Canvas caption** says "curl-dominated near the origin"; F(0,0) = (0.4, 1), so the origin isn't a fixed point.
- **Structured data values** in `head.html`: nationality "South Korea", jobTitle "Research Assistant", worksFor KAIST; email is `@kaist.ac.kr` in JSON-LD/footer but gmail on the pages; `twitter:creator` is "@AdnanSadik".
- **About page** has no title (tab shows just "Adnan Sadik") and its meta description is auto-generated from the chat button and events text.
- **RSS description** is the theme default: "This website is a virtual proof that I'm awesome".

### Found during this pass — technical, not changed yet

- `_redirects/` is never built (underscore folders are skipped unless declared as a collection), so `/normalsite/about`, `/normalsite/resume`, etc. return 404 live. `/normalsite/` itself works. `normalsite.html` and `index.html`'s `redirect_from` both write `/normalsite/index.html`.
- `robots.txt`: the `Disallow` lines sit under the `DuckDuckBot` group, so they apply only to DuckDuckBot; Google ignores `Crawl-delay`.
- Visitors whose OS is in dark mode may see a dark flash: the pages' inline `prefers-color-scheme: dark` styles apply until `dark-theme.js` (end of `<body>`) forces light mode.
- The disabled dark-mode toggle is still shown at 50% opacity.
- WebSite JSON-LD declares a `?search=` SearchAction the site doesn't support.
- BlogPosting JSON-LD inserts title/subtitle without JSON escaping (breaks if a title contains `"`).
- Unused images: `image_gaussian.png` (2.6 MB), `crepe.jpg`, `path.jpg`, `thumb.png`. `Shikoku.png` is 2.4 MB (post image and cover).
- Theme scaffolding still published: `beautiful-jekyll-theme.gemspec`, `Appraisals`, `staticman.yml`, `CNAME.example`.

### Local preview

- Jekyll 3.10 and plugins were installed into the Claude session's temporary scratch folder, not system-wide. System Ruby 2.6 needs `SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk` to compile native gems (the 27.0 SDK is missing Ruby 2.6's headers).
- `.claude/launch.json` (untracked) starts the server on port 4000. Google Tag Manager is disabled locally so previews don't count as visits.
