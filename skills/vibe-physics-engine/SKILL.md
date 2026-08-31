---
name: vibe-physics-engine
description: Physics-based UI motion, anti-template visual architecture, Lenis momentum scrolling, GPU-accelerated glassmorphism, OKLCH perceptual tokens, and custom SVG vector styling without Unicode emojis.
triggers: ["vibe coding", "add physics", "animate", "smooth UI", "framer motion", "gsap", "fluid motion", "lenis", "oklch"]
---

# ⚡ Vibe Physics & Luxury Frontend Engine

## 🎯 Purpose
The `vibe-physics-engine` powers bespoke, high-framerate visual and interactive experiences. It mandates pure mathematical motion curves, GPU-accelerated layer compositing, OKLCH color science, and strict anti-template aesthetics.

## 🎨 1. OKLCH Obsidian & Champagne Design System
- **Canvas Base:** `oklch(0.12 0.012 260)` (Deep Obsidian Velvet Canvas)
- **Glass Surface:** `oklch(0.16 0.015 260 / 0.65)` with `backdrop-filter: blur(24px) saturate(180%)`
- **Fresnel Inset Border:** `inset 0 1px 1px 0 rgba(255, 255, 255, 0.16)`
- **Metallic Gold Accent:** `oklch(0.72 0.145 85)` (Champagne Gold)

## 🕹️ 2. Lenis Momentum Smooth Scrolling Engine
```javascript
import Lenis from '@studio-freight/lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  orientation: 'vertical',
  gestureOrientation: 'vertical',
  smoothWheel: true,
  wheelMultiplier: 1.0,
  touchMultiplier: 1.5,
  infinite: false
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
```

## 🚫 3. Strict Zero-Emoji Rule & SVG Vector Standard
- **Forbidden:** Any Unicode emoji character (e.g., 💉, 👑, ✨, 📍, ⭐).
- **Mandatory:** Bespoke inline or sprite SVG vectors with `stroke="currentColor"`, `fill="none"`, and precision stroke widths (1.5px - 2.0px).
