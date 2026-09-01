---
name: vibe-physics-engine
description: Physics-based UI motion, anti-template visual architecture, Lenis momentum scrolling, GPU-accelerated glassmorphism, OKLCH perceptual tokens, and custom SVG vector styling without Unicode emojis.
triggers: ["vibe coding", "add physics", "animate", "smooth UI", "framer motion", "gsap", "fluid motion", "lenis", "oklch"]
---

# ⚡ Vibe Motion & Compositing Engine

## 🎯 Purpose
The `vibe-physics-engine` powers bespoke, high-framerate visual and interactive experiences. It mandates mathematical motion curves, GPU-accelerated layer compositing, refresh-rate-aware interpolation, OKLCH perceptual color science, and strict anti-template aesthetics.

---

## 🎨 1. Perceptual OKLCH Token Systems (Multi-Chemistry)

Avoid hardcoding a single dark theme. Adapt OKLCH tokens to the target visual chemistry:

### A. Luxury Obsidian (Dark Velvet)
- **Canvas Base:** `oklch(0.12 0.012 260)`
- **Glass Surface:** `oklch(0.16 0.015 260 / 0.65)` with `backdrop-filter: blur(24px) saturate(180%)`
- **Fresnel Inset Border:** `inset 0 1px 1px 0 rgba(255, 255, 255, 0.16)`
- **Primary Accent:** `oklch(0.72 0.145 85)` (Champagne Gold)

### B. Minimalist Technical SaaS (Pitch Linear)
- **Canvas Base:** `oklch(0.14 0.005 260)`
- **Surface:** `oklch(0.18 0.008 260)` with crisp 1px borders `oklch(0.24 0.01 260)`
- **Primary Accent:** `oklch(0.92 0.01 260)` (High-contrast pure white) or `oklch(0.65 0.22 265)` (Electric Indigo)

### C. Clean Architectural Light (Stripe / Apple)
- **Canvas Base:** `oklch(0.985 0.002 90)`
- **Surface:** `oklch(1.0 0 0)` with diffuse multi-layer drop shadow
- **Primary Accent:** `oklch(0.55 0.22 260)` (Deep Sapphire)

---

## 🕹️ 2. Smooth Scrolling: Native Zero-Dep & Progressive Lenis

### Option A: 100% Zero-Dependency Native Smooth Scroll (Default)
No external npm dependencies required:
```css
html {
  scroll-behavior: smooth;
}
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

### Option B: Progressive Enhancement with Modern Lenis
When momentum-based inertial scrolling is explicitly desired, use the official modern `lenis` package (never deprecated `@studio-freight/lenis`):
```javascript
import Lenis from 'lenis';

// Check user reduced-motion preference first
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion) {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
    wheelMultiplier: 1.0,
    touchMultiplier: 1.5,
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);
}
```

---

## 🏎️ 3. Frame-Rate-Independent DeltaTime Physics (Sub-Pixel Precision)
For interactive elements (e.g. before/after comparison sliders, magnetic cursors, spring cards):
```javascript
// DeltaTime-based exponential decay ensuring identical motion across 60Hz, 120Hz, and 144Hz displays
let currentX = 0;
let targetX = 0;
let lastTime = performance.now();
const lambda = 14; // Decay rate constant

function updatePosition(currentTime) {
  const dt = Math.min((currentTime - lastTime) / 1000, 0.1);
  lastTime = currentTime;
  
  const alpha = 1 - Math.exp(-lambda * dt);
  currentX += (targetX - currentX) * alpha;
  sliderElement.style.transform = `translate3d(${currentX.toFixed(2)}px, 0, 0)`;
  
  if (Math.abs(targetX - currentX) > 0.05) {
    requestAnimationFrame(updatePosition);
  }
}
```

---

## 🚫 4. Strict Zero-Emoji Rule & SVG Vector Standard
- **Forbidden:** Any Unicode emoji character (e.g., 💉, 👑, ✨, 📍, ⭐).
- **Mandatory:** Bespoke inline or sprite SVG vectors with `stroke="currentColor"`, `fill="none"`, and precision stroke widths (1.5px - 2.0px).
