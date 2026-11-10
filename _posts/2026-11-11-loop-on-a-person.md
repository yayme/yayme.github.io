---
layout: post
title: An Agentic Research Loop for Wellness Maxxing
subtitle: Six months on a Samsung Life industry–academia project — what I wanted to build, what was hard, and what I got wrong
tags: [agents, llm, samsung]
thumbnail-img: /assets/img/kaist-blossoms.jpg
author: Adnan Sadik
---

Last spring, as the cherry blossoms started falling on the KAIST campus, a friend told me about a Samsung industry academia collaboration project looking for teams. Professor Hyunwoo J. Kim from the MLV Lab had chosen the theme: agentic systems. My interest in the technology was high, so I wanted to take part. The problem was that I did not know much about agentic systems.

<div class="bn" markdown="0">

<figure class="bn-figure">
  <img src="/assets/img/kaist-blossoms.jpg" alt="Cherry blossoms falling over a path on the KAIST campus, with a scooter passing in the background">
  <figcaption>Cherry blossom season on the KAIST campus, around when this started.</figcaption>
</figure>

<p>There are a lot of good resources online. I went through Berkeley's LLM Agents course and some of the Stanford CS25 lectures, and read Anthropic's writing on building effective agents. Eventually I came across <a href="https://arxiv.org/abs/2606.24937">The Hitchhiker's Guide to Agentic AI</a> by Haggai Roitman. I loved how concretely the author explains every part. Most writing on agents is either marketing or a framework tutorial. This book gives you the failure modes with names and tells you which decisions are load bearing.</p>

<p>That still left the issue of technical implementation. Reading about loops is not the same as building one that runs unattended on somebody's health data.</p>

<p>We put together a proposal and were accepted. We were the only international team in the cohort.</p>

<hr class="rule">

<h2>What I wanted to build</h2>

<p>I was heavily inspired by Andrej Karpathy's <a href="https://github.com/karpathy/autoresearch">autoresearch</a>. His agent proposes a change to a training script, runs a short experiment, keeps the change if the metric improved and rolls it back if it did not. It repeats forever. I wanted the same loop, but running on a person's own trajectory instead of a training run.</p>

<p>The high level idea had three parts, and all three turned out to be real problems rather than implementation details.</p>

<ol>
  <li><strong>Compaction policy.</strong> How do you compact a person's history in a way that keeps what matters and can be used effectively for predictive decision making.</li>
  <li><strong>Health data injection.</strong> How does injecting daily health data actually improve what the system produces.</li>
  <li><strong>Suggestion generation and counterfactual simulation.</strong> The hardest part of the job. I wanted the suggestions to stay simple. Swap the afternoon coffee for water. Go for a 30 minute walk after work. Skip the workout today and recover. At the same time I wanted them to be meaningful, which is harder than it sounds.</li>
</ol>

<p>I was leading a team of three. The gap was never implementation. It was knowing which decisions in an agentic system are the ones that matter.</p>

<h2>How the book mapped onto the work</h2>

<p>Each of the three ideas turned out to have a name, a known failure mode, and a set of decisions somebody had already worked through. That is what made the book worth the time. It also added a fourth piece of work I had not planned for, which was everything that has to be true before you leave a loop running unattended.</p>

<div class="tbl">
  <table>
    <caption>Our steps, and where they landed in the book</caption>
    <thead><tr><th>Our step</th><th>In the book</th><th>What it changed</th></tr></thead>
    <tbody>
      <tr>
        <td>Compaction policy</td>
        <td>Memory granularity <span class="cite">§17.4.1</span>, compaction strategies <span class="cite">§19.11</span></td>
        <td>Keep the raw history at the finest grain and treat the compacted block as a view over it</td>
      </tr>
      <tr>
        <td>Health data injection</td>
        <td>Dynamic prompt assembly <span class="cite">§18.3.2</span>, context budget <span class="cite">§18.2</span></td>
        <td>Split stable knowledge from volatile personal data, and order them so the cache boundary falls between</td>
      </tr>
      <tr>
        <td>Finding hypotheses and actions</td>
        <td>Retrieval over an open key space <span class="cite">§18.4.2</span></td>
        <td>Retrieve from the literature, look up everything that can be enumerated</td>
      </tr>
      <tr>
        <td>Suggestion generation</td>
        <td>Reward design and specification failure <span class="cite">§19.2</span>, <span class="cite">§19.9.3</span></td>
        <td>Optimise for what gets done, not for the largest effect</td>
      </tr>
      <tr>
        <td>The loop itself</td>
        <td>Verification <span class="cite">§19.6</span>, termination <span class="cite">§19.7</span>, escalation <span class="cite">§19.8</span></td>
        <td>The entire fourth problem, which I had not planned for</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>Compaction: what to keep</h2>

<p>A wearable produces a lot of data and almost none of it belongs in a prompt. Months of daily readings across a handful of metrics is thousands of tokens of numbers, and the model does not need the numbers. It needs what the numbers mean for this person, in a form that supports a decision.</p>

<p>So our compaction policy is not summarization in the usual sense. It is a computation. The history reduces to baselines, current drift, and the relationships found in that person's own data. The block is small, and it is a pure function of the stored history, so the same history always produces the same block. That matters more than the token saving: a deterministic compaction means two runs on the same data cannot disagree.</p>

<p>The book has a section on memory granularity that I read after making this choice and wished I had read before <span class="cite">§17.4.1 p.369</span>. It sets out the trade-off between atomic facts, structured notes, summarized episodes and verbatim transcripts, and gives a rule I now use: store at the finest grain you can afford, then build coarser views on top, because it is easy to summarize atoms and impossible to recover atoms from a lossy summary. The raw readings stay on disk. The compacted block is a view.</p>

<p>It also warns about the way compaction fails in a system that runs for months <span class="cite">§19.11.1 p.431</span>. Periodic summarization discards detail you may need three weeks later, and you will not notice at the time. For a loop whose experiments run for weeks, that is not a hypothetical.</p>

<h2>Injection: what the model is allowed to see</h2>

<p>The naive version puts everything in one prompt. All the domain knowledge, all the safety rules, all the coaching material, plus the person's data, on every call. That is expensive, it gets worse every time you add a capability, and long context measurably degrades the answer.</p>

<p>We split it instead. Each component gets a fixed slice of knowledge and nothing else. The component that checks for concerning trends has the escalation criteria and no coaching material. The component that phrases a suggestion has the phrasing templates and the person's computed numbers, not the clinical corpus. Then one layer injects the personal facts on top of whichever slice is in play.</p>

<p>The book describes prompt construction as a concatenation of independently versioned blocks rather than one string <span class="cite">§18.3.2 p.395</span>, which is exactly what this is. Two details from it changed how we built the layer.</p>

<h3>Put the stable part first</h3>

<p>A fixed slice is a stable prefix, and a stable prefix is cacheable. A blob assembled fresh every call is not. The book puts the saving at 50 to 90 percent on the cached portion <span class="cite">§18.8.1 p.405</span>, and notes that in a loop, where system content stays constant across iterations, 60 to 80 percent of each call is typically cacheable <span class="cite">§19.13 p.432</span>. So the ordering is not cosmetic. Static slice first, injected personal facts last, and the cache boundary falls between them.</p>

<h3>Retrieval only where the set cannot be written down</h3>

<p>If I can enumerate the keys, I should not embed them. Safety thresholds and intervention protocols are a closed set, so a lookup is exact, free and reviewable line by line. Vector search over a set I can enumerate adds a failure mode and buys nothing. The book's version of this is to include only what is relevant to the current task, to save tokens and reduce confusion <span class="cite">§18.3.4 p.397</span>, and to switch to top-k retrieval only once the set gets large <span class="cite">§18.4.2 p.398</span>.</p>

<p>That left one place where retrieval genuinely earns its cost: finding what to test next. The candidate hypotheses and the candidate user actions come from the existing literature, retrieved against what the person's own data shows, rather than from a list of interventions somebody hard coded. The literature says what tends to work in general. The person's data says which of those is worth measuring on them.</p>

<p>There is a privacy consequence to building it this way that I did not plan and now consider the main benefit. Because injection happens in one place, the set of personal fields that can ever reach a model is enumerable. Every other component sees nothing personal at all. That makes the boundary structural instead of a rule somebody has to remember.</p>

<h2>Suggestions: optimising for what actually gets done</h2>

<p>The obvious approach is to find the biggest effect and recommend it. That produces a system that tells people to overhaul their diet, and nobody overhauls their diet. A plan followed 5 percent of the time produces less benefit than a small change followed 80 percent of the time. So the quantity to maximise is not the size of the effect. It is the effect times the probability the person actually does it, and the probability has to be learned from how that person has behaved, not assumed.</p>

<p>The book does not cover this problem directly, but it does name the general shape of it. Its framing of a loop as inference-time reinforcement learning <span class="cite">§19.2 p.418</span> puts reward design at the centre, and its section on reward hacking <span class="cite">§19.9.3 p.428</span> describes what happens when the specification is slightly wrong: the system satisfies the letter of the objective and misses the point entirely. A wellness system that optimises for effect size is a clean example. Every recommendation is defensible and the outcome is zero, because nothing gets done.</p>

<p>The consequence is deliberate and looks odd at first. The system will often recommend the smallest item available. Swap the afternoon coffee. Walk 20 minutes after lunch. That is correct behaviour, not a limitation, though it reads as weak advice until you see the reasoning next to it.</p>

<h3>The counterfactual part</h3>

<p>A suggestion with no visible consequence is easy to ignore. So the system projects two futures from the person's current state: the one they are on, and the one a specific change produces, propagated through the relationships found in their own data. Short sleep suppresses the next day's activity, and so on. Showing somebody where they are heading is more motivating than telling them a habit is good for them.</p>

<p>I want to be careful about what this is. It is a forward simulation through a model fitted to one person, not a prediction. The honest framing is that it shows the shape of a change, not a number you should trust to one decimal place.</p>

<h3>Why the loop needs an experiment at all</h3>

<p>Mining somebody's history gives you correlations. Correlations are confounded. Stressful days plausibly cause both the extra coffee and the bad sleep, so cutting the coffee might do nothing. The only way to get a number you can state causally is to vary the behaviour on a randomized schedule across that person's own days and compare.</p>

<p>This is where our loop stops looking like Karpathy's. His experiment takes five minutes and returns a scalar. The book is explicit that the pattern works <em>because</em> the reward signal is scalar and unambiguous <span class="cite">§19.5.5 p.423</span>. Ours takes two to four weeks and returns an estimate with a confidence interval that often includes zero.</p>

<div class="box">
  <span class="lbl">What that changes</span>
  <p>When an iteration costs five minutes you can afford to be wrong constantly. When it costs weeks of somebody's life, choosing which hypothesis to spend them on becomes the main problem in the system. Almost all the engineering moved from iterating to deciding what to iterate on.</p>
</div>

<p>It also adds a third outcome. The book's loop commits or rolls back. Ours has to say "not settled yet" and mean it, because reporting a result that cannot be distinguished from noise is worse than reporting nothing.</p>

<h2>The part I did not plan for: making it safe to leave running</h2>

<p>I started with the three problems above. Chapter 19 of the book is about the fourth one, which is everything that has to be true before you let a loop run unattended. I had solved some of it by instinct and missed the rest.</p>

<h3>Verification</h3>

<p>The system has a check between the model and the user. Every number in generated text has to trace back to a value the engine computed. If one does not, the text is thrown out and the deterministic phrasing is used instead. We built this because in wellness advice the number is the thing the person acts on, and a model that writes a plausible figure it never calculated is worse than useless.</p>

<p>The book puts this in a hierarchy and gives the reason it belongs near the top <span class="cite">§19.6.1 p.423</span>. Deterministic checks like compilers and test runners outrank LLM judges because they cannot be persuaded. Then it states the rule:</p>

<blockquote>
  <p>A loop is only as trustworthy as its least reliable verification step. Wherever a deterministic check exists, use it. Never let the generating model judge its own output: the maker and the checker must be separate.</p>
  <span class="attr">§19.6.1 p.423</span>
</blockquote>

<p>Our checker is not a model at all, so maker and checker are separate by construction. Chapter 17 gives the same mechanism a second name I like better: abstention, meaning the system says it does not know instead of fabricating something plausible <span class="cite">§17.9.1 p.374</span>.</p>

<h3>Saying nothing</h3>

<p>The book lists five ways a loop should exit <span class="cite">§19.7.1 p.424</span>: goal achieved, hard iteration cap, budget exhausted, no progress detected, fatal error. Ours has one it does not list, because its loops run against machines and ours runs against a person. The system can decide the user is not in a state to be asked anything and send nothing that day.</p>

<p>That is a success, not a failure. Coaching sent to somebody who is not receptive does not just waste the message, it costs you their attention for the next one. The scarce resource is their willingness, and spending it badly is the same mistake as burning tokens on an iteration that cannot converge.</p>

<h3>Escalation</h3>

<p>The system flags a concerning trend for a professional and never attempts a diagnosis. I built that as a product decision. The book reframes it as a threshold with an asymmetric loss behind it, and hands you the number:</p>

<blockquote>
  <p>In high-stakes domains the cost of a false negative, proceeding when the agent should have escalated, is much higher than the cost of a false positive. A medical agent should escalate at p<sub>min</sub> = 0.9; a content summarisation agent can tolerate p<sub>min</sub> = 0.5.</p>
  <span class="attr">§19.8.2 p.426</span>
</blockquote>

<p>It also says to measure the escalation rate in both directions and treat an unusually low rate as a defect, because it means the agent is overconfident <span class="cite">§19.8.3 p.427</span>. We were not measuring it at all.</p>

<h2>What the book told me I got wrong</h2>

<p>Reading Chapter 20 was uncomfortable in a useful way. It has a catalogue of graph anti-patterns and we are guilty of one of them by name.</p>

<blockquote>
  <p>When nodes communicate through undocumented state fields, writing to a field that another node reads without the dependency being declared in the graph structure, the graph's topology no longer reflects its actual data flow.</p>
  <span class="attr">§20.8.2 p.444, "Implicit State Coupling"</span>
</blockquote>

<p>That is our system. One shared state object, mutated in place, with no declared read and write sets. It works and it is hard to reason about, which is exactly what the book says happens.</p>

<p>The related point is why we cannot run the independent stages in parallel even though two of them do not depend on each other. Concurrent writes need a declared merge semantic, append or last-write-wins or a custom function, and it has to match the topology <span class="cite">§20.4.1 p.440</span>. With in-place mutation there is no declared merge, so a fan-out would be a race. The book lists that as its own anti-pattern and calls it a correctness problem rather than a performance one.</p>

<p>Three more things I would change, all of them named in the book before I would have found them:</p>

<ul>
  <li><strong>Checkpoint.</strong> It enables crash recovery, real blocking human-in-the-loop pauses, and replay for debugging, and the book says to turn it on from the start because the cost is negligible and the debugging value is enormous <span class="cite">§20.4.2 p.440</span>. A loop that ticks daily and runs experiments for weeks has no excuse.</li>
  <li><strong>Store facts bi-temporally.</strong> Separate when something was true from when the system learned it <span class="cite">§17.4.2 p.370</span>. Effects decay. A measured effect should carry a validity window and expire into a re-measurement instead of quietly going stale.</li>
  <li><strong>Instrument properly.</strong> Traces, structured logs with token counts and latency, and aggregate metrics <span class="cite">§18.7.4 p.405</span>. We had an execution trace and nothing else.</li>
</ul>

<p>There is also a section titled "When Not to Use Loops" that argues against the whole system <span class="cite">§19.12 p.432</span>. One of its five conditions is that verification is impossible, because without a feedback signal a loop degenerates into random search. A fair reading of our problem is that verification is nearly impossible: the signal is noisy, delayed by weeks, and often inconclusive.</p>

<p>My answer is that the condition says impossible, not noisy. A randomized within-person design is a real signal with quantified uncertainty attached. What it demands is that the decision rule respects that uncertainty instead of pretending the estimate is a fact.</p>

<h2>Demo day</h2>

<p>We had three meetings with Professor Kim and the Samsung Lifenology team over the six months, and presented the finished system at Demo Day at the Samsung Financial Campus in Seocho, Seoul, in front of investors, Samsung personnel and professors. The project page is <a href="https://lifenologylab.co.kr/project/project3_Connection_9.php">here</a>.</p>

<p>A demo forces you to have an answer for the question you have been avoiding. People do not ask you about your architecture. They ask what happens when it is wrong.</p>

<h2>The improvements I would attempt</h2>

<p>Mixing traditional deep learning models into the loop alongside the language model. The two are good at different things. A trained model goes from raw signal to a decision far more reliably than anything prompted, and the agentic loop is what selects the hypothesis, runs the verification, and decides whether and when to say something. The language model stays where it belongs, which is phrasing.</p>

<p>Rollout goes through canary deployment. A model change reaches a small fraction of users first and is measured there before it reaches anyone else. For a system that gives wellness suggestions, shipping a regression to everyone at once is not an acceptable failure mode.</p>

<p>The second piece is fixing the statistics for continuous operation. Once hypotheses are generated automatically and trials run indefinitely, two problems appear immediately. Many uncorrected tests will eventually declare noise conclusive. And checking the data as it accumulates invalidates a fixed-alpha interval. Both have known solutions and neither is optional at scale.</p>

<p>The thing I keep thinking about is that none of the hard parts were model problems. What to compact, what the model is allowed to see, what counts as enough evidence to tell somebody to change their routine. Those are judgement calls, and the loop just makes the consequences of getting them wrong arrive faster.</p>

<p>We received recognition and funding from Samsung Lifenology Lab to build the product.</p>

<footer class="bn-footer">
  <p><a href="https://lifenologylab.co.kr/project/project3_Connection_9.php">Project page →</a></p>
</footer>

</div>

<style>
.bn-figure { margin: 1.8rem 0; }

.bn-figure img {
  width: 100%;
  height: auto;
  border-radius: 6px;
  display: block;
}

.bn-figure figcaption {
  margin-top: 0.5rem;
  font-size: 0.86rem;
  color: #6D5A4D;
  text-align: center;
}

.bn h2 { margin-top: 2.6rem; }
.bn h3 { margin-top: 1.8rem; font-size: 1.1rem; }
.bn hr.rule { border: 0; border-top: 1px solid #E3D6BC; margin: 2.2rem 0; }

.bn .cite {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.78em;
  color: #9A5A28;
  background: #F7EDD6;
  padding: 1px 5px;
  border-radius: 3px;
  white-space: nowrap;
}

.bn .box {
  margin: 1.5rem 0;
  padding: 1rem 1.2rem;
  border-left: 3px solid #D95F18;
  background: #FBF4E4;
  border-radius: 4px;
}

.bn .box .lbl {
  display: block;
  margin-bottom: 0.4rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: #C4470D;
}

.bn .box p:last-child { margin-bottom: 0; }

.bn blockquote {
  border-left: 2px solid #D6C6A9;
  padding-left: 1rem;
  color: #4A3A33;
  font-size: 1rem;
}

.bn blockquote .attr {
  display: block;
  margin-top: 0.4rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.78rem;
  color: #8A7566;
}

.bn .tbl {
  overflow-x: auto;
  margin: 1.5rem 0;
  border: 1px solid #E3D6BC;
  border-radius: 4px;
}

.bn table {
  border-collapse: collapse;
  width: 100%;
  min-width: 30rem;
  font-size: 0.92rem;
  margin: 0;
}

.bn caption {
  caption-side: top;
  text-align: left;
  padding: 0.7rem 0.9rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #8A7566;
  border-bottom: 1px solid #E3D6BC;
}

.bn th, .bn td { padding: 0.65rem 0.9rem; text-align: left; vertical-align: top; }
.bn th {
  font-size: 0.72rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #8A7566;
  border-bottom: 1px solid #D6C6A9;
}
.bn td { border-bottom: 1px solid #EFE4CD; color: #4A3A33; }
.bn tbody tr:last-child td { border-bottom: 0; }
.bn td:first-child { font-weight: 600; color: #3A2C29; }

.bn-footer {
  margin-top: 3rem;
  padding-top: 1.2rem;
  border-top: 1px solid #E3D6BC;
  font-size: 0.9rem;
  color: #6D5A4D;
}

.bn-footer p { margin-bottom: 0.6rem; }

[data-theme="dark"] .bn .cite { background: #3A2418; color: #FF8A4C; }
[data-theme="dark"] .bn .box { background: rgba(58, 36, 24, 0.6); border-left-color: #FF8A4C; }
[data-theme="dark"] .bn .box .lbl { color: #FF8A4C; }
[data-theme="dark"] .bn blockquote { border-left-color: #5A3825; color: #F5E8C7; }
[data-theme="dark"] .bn .tbl { border-color: #5A3825; }
[data-theme="dark"] .bn td { color: #F5E8C7; border-bottom-color: #4A2F1E; }
[data-theme="dark"] .bn td:first-child { color: #F5E8C7; }
[data-theme="dark"] .bn-footer { color: #D6C6A9; border-top-color: #5A3825; }

@media (max-width: 600px) {
  .bn table { min-width: 26rem; font-size: 0.86rem; }
}
</style>
