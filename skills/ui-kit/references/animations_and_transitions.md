# ⚡ Physics-Based Animations & Transitions (Transitions.dev & BeUI)

Zero-dependency CSS/JS motion patterns, spring transitions, and micro-interactions.

---

## 1. Zero-JS Smooth Accordion (Grid Row Expansion)

Expands elements from `0px` to `auto` height purely in CSS without hardcoding `max-height`.

```html
<div class="accordion-item rounded-2xl border border-border bg-card overflow-hidden">
  <button class="w-full flex items-center justify-between p-4 text-start font-semibold text-sm text-foreground" onclick="this.nextElementSibling.classList.toggle('is-open')">
    <span>How does zero-JS height transition work?</span>
    <svg class="w-4 h-4 text-muted-foreground transform transition-transform duration-300 group-hover:text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
    </svg>
  </button>
  
  <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] [&.is-open]:grid-rows-[1fr]">
    <div class="overflow-hidden px-4 pb-4 text-xs text-muted-foreground leading-relaxed border-t border-border/40 pt-3">
      By transitioning `grid-template-rows` between `0fr` and `1fr`, the container smoothly animates to its exact natural content height without layout recalculation bugs.
    </div>
  </div>
</div>
```

---

## 2. Animated Gradient Glow Shimmer Button (BeUI)

```html
<button class="relative inline-flex items-center justify-center p-0.5 overflow-hidden rounded-2xl font-bold group shadow-xl">
  <!-- Glowing Animated Gradient Layer -->
  <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-primary via-accent to-secondary rounded-2xl opacity-70 group-hover:opacity-100 transition-opacity duration-300 animate-gradient-x"></span>
  
  <!-- Surface -->
  <span class="relative px-5 py-2.5 transition-all ease-out bg-background rounded-[14px] text-xs font-semibold text-foreground group-hover:bg-opacity-90 flex items-center gap-2">
    <span>Explore Documentation</span>
    <svg class="w-4 h-4 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </span>
</button>
```

---

## 3. Spring Physics Toggle Switch

```html
<label class="relative inline-flex items-center cursor-pointer">
  <input type="checkbox" value="" class="sr-only peer">
  <div class="w-11 h-6 bg-muted peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-border after:border after:rounded-full after:h-5 after:w-5 after:transition-all after:duration-300 after:ease-[cubic-bezier(0.34,1.56,0.64,1)] peer-checked:bg-primary"></div>
</label>
```
