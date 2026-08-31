# 🤖 AI-Native UI Primitives (Beautiful UI / Agentic Design)

Production-ready, framework-agnostic building blocks for AI agents, chatbots, LLM tools, and generative interfaces.

---

## 1. Agent Thinking Indicator (Collapsible Thought Stream)

Visualizes real-time reasoning, background planner steps, and multi-step reflection.

```html
<!-- Generic Component: Thinking State -->
<div class="agent-thinking-card rounded-xl border border-border bg-card/60 p-4 backdrop-blur-md transition-all shadow-sm">
  <div class="flex items-center justify-between cursor-pointer select-none" onclick="this.parentElement.querySelector('.thought-content').classList.toggle('hidden')">
    <div class="flex items-center gap-3">
      <!-- Pulsing Activity Dot -->
      <div class="relative flex h-2.5 w-2.5">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-primary"></span>
      </div>
      <span class="text-xs font-semibold text-foreground/90 font-mono tracking-tight">Thinking & Reasoning...</span>
    </div>
    <div class="flex items-center gap-2">
      <span class="text-[11px] text-muted-foreground font-mono">3 steps</span>
      <svg class="w-4 h-4 text-muted-foreground transform transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </div>
  </div>
  
  <!-- Collapsible Steps -->
  <div class="thought-content mt-3 pt-3 border-t border-border/50 text-xs text-muted-foreground leading-relaxed font-mono space-y-1.5">
    <div class="flex items-start gap-2">
      <span class="text-primary font-bold">1.</span>
      <span>Querying internal vector database for relevant contextual documents</span>
    </div>
    <div class="flex items-start gap-2">
      <span class="text-primary font-bold">2.</span>
      <span>Validating schema parameters against target execution contract</span>
    </div>
    <div class="flex items-start gap-2 text-emerald-500">
      <span>✓</span>
      <span>Optimal execution route synthesized in 142ms</span>
    </div>
  </div>
</div>
```

---

## 2. Streaming Text with Blinking Token Cursor

Simulates token generation stream with smooth rendering.

```html
<!-- Generic Component: Streaming Block -->
<div class="streaming-text-block p-4 rounded-xl bg-card border border-border text-foreground text-sm leading-relaxed">
  <span class="stream-body font-sans">
    The retrieved data shows a 14.2% acceleration in inference throughput following kernel compilation.
  </span>
  <span class="inline-block w-1.5 h-4 bg-primary align-middle ms-1 rounded-sm animate-pulse"></span>
</div>
```

---

## 3. Tool Chips & Function Call Badges

Indicates execution of external tools, API requests, database queries, or sandbox commands.

```html
<div class="flex flex-wrap items-center gap-2">
  <!-- Executed Tool (Success) -->
  <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-lg bg-secondary/70 border border-border text-xs shadow-sm">
    <svg class="w-3.5 h-3.5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
    </svg>
    <span class="text-muted-foreground font-mono">tool:</span>
    <span class="text-foreground font-medium font-mono">search_database</span>
    <span class="px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-500 text-[10px] font-mono font-semibold">200 OK (28ms)</span>
  </div>

  <!-- Running Tool (Pending) -->
  <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-lg bg-primary/10 border border-primary/20 text-xs">
    <div class="w-3 h-3 rounded-full border-2 border-primary border-t-transparent animate-spin"></div>
    <span class="text-primary font-mono">api_call:</span>
    <span class="text-foreground/90 font-mono">fetch_analytics</span>
  </div>
</div>
```

---

## 4. Human-in-the-Loop Approval Card

Halts autonomous execution to request explicit user consent with diff / action payload review.

```html
<div class="approval-card rounded-2xl border border-border bg-card/95 p-5 shadow-2xl backdrop-blur-xl">
  <div class="flex items-start gap-3.5">
    <div class="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-500 shrink-0">
      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
      </svg>
    </div>
    <div class="flex-1">
      <h4 class="text-sm font-bold text-foreground">Action Confirmation Required</h4>
      <p class="text-xs text-muted-foreground mt-0.5 leading-relaxed">
        The agent is requesting permission to execute the following destructive database migration.
      </p>
    </div>
  </div>

  <!-- Action Metadata / Diff Preview -->
  <div class="mt-4 p-3 rounded-xl bg-muted/50 border border-border font-mono text-xs text-foreground/90 space-y-1.5">
    <div class="flex justify-between">
      <span class="text-muted-foreground">Target Endpoint:</span>
      <span class="font-semibold text-primary">/api/v2/cluster/reindex</span>
    </div>
    <div class="flex justify-between">
      <span class="text-muted-foreground">Affected Nodes:</span>
      <span class="font-semibold">3 Worker Replicas</span>
    </div>
  </div>

  <!-- Action Controls -->
  <div class="mt-5 flex items-center justify-end gap-2.5">
    <button type="button" class="px-4 py-2 rounded-xl text-xs font-semibold text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
      Reject
    </button>
    <button type="button" class="px-5 py-2 rounded-xl text-xs font-bold text-primary-foreground bg-primary hover:opacity-90 shadow-md transition-all">
      Approve & Execute
    </button>
  </div>
</div>
```

---

## 5. Agent Task Step Tracker (Task Rows)

```html
<div class="task-rows space-y-2">
  <!-- Step 1: Completed -->
  <div class="flex items-center justify-between p-3 rounded-xl bg-card border border-border">
    <div class="flex items-center gap-3">
      <div class="w-5 h-5 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-500">
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" /></svg>
      </div>
      <span class="text-xs text-foreground font-medium">Extracting entity relational graph</span>
    </div>
    <span class="text-[11px] text-muted-foreground font-mono">Completed (45ms)</span>
  </div>

  <!-- Step 2: In Progress -->
  <div class="flex items-center justify-between p-3 rounded-xl bg-primary/5 border border-primary/20">
    <div class="flex items-center gap-3">
      <div class="w-5 h-5 rounded-full border-2 border-primary border-t-transparent animate-spin"></div>
      <span class="text-xs text-foreground font-semibold">Synthesizing SQL partition queries</span>
    </div>
    <span class="text-[11px] text-primary font-mono animate-pulse">Running...</span>
  </div>
</div>
```

---

## 6. Universal Prompt Bar HUD

```html
<div class="prompt-bar-container w-full max-w-2xl mx-auto">
  <div class="relative flex items-center rounded-2xl bg-card/90 border border-border p-2 shadow-2xl backdrop-blur-2xl ring-1 ring-border/50 focus-within:border-primary focus-within:ring-primary/20 transition-all">
    <!-- Attachment Button -->
    <button type="button" class="p-2 text-muted-foreground hover:text-foreground rounded-xl transition-colors">
      <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" /></svg>
    </button>

    <input type="text" placeholder="Ask agent or type a command..." class="w-full bg-transparent px-3 text-sm text-foreground placeholder-muted-foreground focus:outline-none">
    
    <!-- Submit Button -->
    <button type="button" class="p-2.5 rounded-xl bg-primary text-primary-foreground font-bold hover:opacity-90 transition-opacity shadow-md">
      <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
      </svg>
    </button>
  </div>
</div>
```
