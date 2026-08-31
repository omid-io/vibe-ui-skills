# 🧩 Modern Accessible Primitives (ui.shadcn.com)

Universal, accessible, copy-paste primitives adaptable to Tailwind, React, Vue, or Vanilla HTML/JS.

---

## 1. Command Palette / Search HUD (`Cmd+K` / `Ctrl+K`)

```html
<div class="fixed inset-0 z-50 bg-background/80 backdrop-blur-sm flex items-start justify-center pt-24 p-4">
  <div class="w-full max-w-xl rounded-2xl border border-border bg-popover text-popover-foreground shadow-2xl overflow-hidden animate-in fade-in-0 zoom-in-95 duration-150">
    <!-- Input Bar -->
    <div class="flex items-center px-4 border-b border-border">
      <svg class="w-4 h-4 text-muted-foreground me-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
      <input type="text" placeholder="Type a command or search records..." class="w-full bg-transparent py-3.5 text-sm placeholder:text-muted-foreground focus:outline-none">
      <kbd class="px-2 py-0.5 rounded bg-muted text-[10px] font-mono text-muted-foreground border border-border">ESC</kbd>
    </div>

    <!-- Items List -->
    <div class="p-2 max-h-72 overflow-y-auto space-y-1 text-xs">
      <div class="px-3 py-1.5 text-[11px] font-semibold text-muted-foreground uppercase tracking-wider">Quick Actions</div>
      
      <button class="w-full flex items-center justify-between px-3 py-2 rounded-xl hover:bg-accent hover:text-accent-foreground transition-colors text-start">
        <div class="flex items-center gap-3">
          <svg class="w-4 h-4 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
          <span>Create New Deployment</span>
        </div>
        <kbd class="text-[10px] font-mono text-muted-foreground">⌘N</kbd>
      </button>

      <button class="w-full flex items-center justify-between px-3 py-2 rounded-xl hover:bg-accent hover:text-accent-foreground transition-colors text-start">
        <div class="flex items-center gap-3">
          <svg class="w-4 h-4 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
          <span>View Analytics Dashboard</span>
        </div>
        <kbd class="text-[10px] font-mono text-muted-foreground">⌘D</kbd>
      </button>
    </div>
  </div>
</div>
```

---

## 2. Slide-over Sheet / Drawer

```html
<div class="fixed inset-y-0 end-0 z-50 w-full max-w-md bg-card border-s border-border shadow-2xl p-6 flex flex-col justify-between">
  <div>
    <div class="flex items-center justify-between pb-4 border-b border-border">
      <h3 class="text-base font-bold text-foreground">Record Details</h3>
      <button class="p-1.5 rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>
    </div>
    <div class="mt-5 space-y-4 text-xs text-muted-foreground">
      <p>Configure parameters, authentication tokens, and webhook endpoints for this worker instance.</p>
    </div>
  </div>

  <div class="pt-4 border-t border-border flex gap-3">
    <button class="w-full py-2.5 rounded-xl bg-primary text-primary-foreground font-semibold text-xs hover:opacity-90 transition-opacity">
      Save Changes
    </button>
  </div>
</div>
```

---

## 3. Segmented Sliding Tabs

```html
<div class="inline-flex p-1 rounded-xl bg-muted border border-border">
  <button class="px-4 py-1.5 rounded-lg text-xs font-semibold bg-background text-foreground shadow-sm transition-all">
    Overview
  </button>
  <button class="px-4 py-1.5 rounded-lg text-xs font-medium text-muted-foreground hover:text-foreground transition-all">
    Analytics
  </button>
  <button class="px-4 py-1.5 rounded-lg text-xs font-medium text-muted-foreground hover:text-foreground transition-all">
    Settings
  </button>
</div>
```
