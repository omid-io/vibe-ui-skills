---
name: master-web-builder
description: The Master Web Builder & Vibe Architecture Engine (v2026). Transforms minimal/lazy prompts into Awwwards-grade web masterpieces. Automatically injects Noise Overlays, Ambient Mesh Glows, Glassmorphism 2.0 with Fresnel specular highlights, 120fps Lerp Before/After Sliders, Magnetic Spring Buttons, and PAS Copywriting.
triggers: ["master web builder", "master_web_builder", "مستر وب بیلدر", "طراحی سایت", "وبسایت بساز", "build website"]
---

# 👑 Master Web Builder & Visual Architecture Engine (v2026)

## 🛑 The Mandatory Visual Skeleton (Every Generated Page MUST Contain This)

You are strictly forbidden from writing "plain/ordinary" CSS. You MUST use these exact luxury visual skeletons:

### 1. Mesh Ambient Glow & Noise Grain
```css
body::before {
  content: "";
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.035'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
  mix-blend-mode: overlay;
}
.hero-ambient-glow {
  position: absolute;
  top: -120px;
  right: 20%;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(201, 171, 129, 0.20) 0%, rgba(139, 92, 246, 0.08) 50%, transparent 70%);
  filter: blur(80px);
  pointer-events: none;
}
```

### 2. Glassmorphism 2.0 with Fresnel Inset Light
```css
.glass-card-luxury {
  background: linear-gradient(135deg, rgba(25, 20, 32, 0.70) 0%, rgba(14, 16, 20, 0.60) 100%);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.16), /* Fresnel Specular */
    0 4px 8px 0 rgba(0, 0, 0, 0.25),
    0 16px 32px -8px rgba(0, 0, 0, 0.45),
    0 24px 48px -12px rgba(0, 0, 0, 0.60);
}
```

### 3. Interactive 120fps Lerp Comparison Slider
```javascript
class MasterBeforeAfterSlider {
  constructor(el) {
    this.container = el;
    this.handle = el.querySelector('.slider-handle');
    this.afterLayer = el.querySelector('.slider-after-image');
    this.targetX = 50; this.currentX = 50; this.isDown = false;
    this.init();
  }
  init() {
    const update = (clientX) => {
      const rect = this.container.getBoundingClientRect();
      const pos = ((clientX - rect.left) / rect.width) * 100;
      this.targetX = Math.max(0, Math.min(100, pos));
    };
    this.container.addEventListener('pointerdown', (e) => { this.isDown = true; update(e.clientX); });
    window.addEventListener('pointermove', (e) => { if (this.isDown) update(e.clientX); });
    window.addEventListener('pointerup', () => this.isDown = false);
    const loop = () => {
      this.currentX += (this.targetX - this.currentX) * 0.12;
      const val = this.currentX.toFixed(2);
      this.handle.style.transform = `translate3d(${val}%, 0, 0)`;
      this.afterLayer.style.clipPath = `polygon(0 0, ${val}% 0, ${val}% 100%, 0 100%)`;
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
}
```
