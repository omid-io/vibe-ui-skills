# 🍱 Bento Grids & Feature Cards (BeUI & Rare UI)

Asymmetric grids, interactive cards, and high-density layouts for web applications and dashboards.

---

## 1. Asymmetric Bento Grid (4-Card Matrix)

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-6xl mx-auto">
  <!-- Large Hero Bento Card (Span 2 cols) -->
  <div class="md:col-span-2 rounded-3xl border border-border bg-card/70 p-6 backdrop-blur-xl shadow-xl flex flex-col justify-between group hover:border-primary/40 transition-all">
    <div class="space-y-2">
      <span class="px-2.5 py-1 rounded-full bg-primary/10 text-primary text-xs font-semibold">Autonomous Agents</span>
      <h3 class="text-xl font-bold text-foreground">Real-time Multi-Model Orchestration</h3>
      <p class="text-xs text-muted-foreground max-w-md">Coordinate specialized subagents with unified context trees and automatic tool delegation.</p>
    </div>
    <div class="mt-6 h-32 rounded-2xl bg-muted/40 border border-border flex items-center justify-center text-xs text-muted-foreground font-mono">
      [Interactive Agent Graph]
    </div>
  </div>

  <!-- Tall Metric Bento Card (Span 1 col) -->
  <div class="rounded-3xl border border-border bg-card/70 p-6 backdrop-blur-xl shadow-xl flex flex-col justify-between group hover:border-primary/40 transition-all">
    <div>
      <span class="text-xs font-medium text-muted-foreground">System Latency</span>
      <div class="mt-2 text-3xl font-extrabold text-foreground font-mono">18ms</div>
      <p class="text-[11px] text-emerald-500 mt-1 font-medium">⚡ 4x faster than standard endpoints</p>
    </div>
    <div class="mt-4 pt-4 border-t border-border/40 text-xs text-muted-foreground">
      Optimized with localized edge caching.
    </div>
  </div>
</div>
```

---

## 2. Glassmorphism 2.0 Card with Specular Inset Light

```css
.glass-surface {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.15),
    0 10px 25px -5px rgba(0, 0, 0, 0.3);
}
```
