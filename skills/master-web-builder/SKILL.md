---
name: master-web-builder
description: The Master Web Builder & Adaptive Visual Architecture Engine (v2026). Transforms minimal prompts into Awwwards-grade masterpieces across 5 distinct visual chemistries (Minimalist SaaS, Glassmorphism 2.0, Neobrutalism, Swiss Editorial, and Stripe Light). Automatically selects or adapts the right visual skeleton, micro-physics, and PAS copywriting.
triggers: ["master web builder", "master_web_builder", "مستر وب بیلدر", "طراحی سایت", "وبسایت بساز", "build website", "landing page", "ui style"]
---

# 👑 Master Web Builder & Adaptive Visual Architecture Engine (v2026)

The `master-web-builder` engine eliminates generic "AI slop" by strictly enforcing **bespoke, intentional visual chemistry**. Instead of forcing one rigid style, it provides **5 Production-Grade Design Archetypes**.

---

## 🎨 The 5 Master Visual Chemistries

The agent autonomously detects the domain or explicit user request and selects the matching chemistry:

```
                  ┌─► 1. Minimalist High-Performance SaaS (Linear / Vercel / Raycast)
                  ├─► 2. Luxury Obsidian & Glassmorphism 2.0 (AI Flagships / Web3 / Luxury)
PROMPT / DOMAIN ──┼─► 3. Neobrutalism & Playful High-Contrast (Creative / Gumroad / Notion)
                  ├─► 4. Swiss Editorial & Paper Craft (Portfolios / Journalism / Architecture)
                  └─► 5. Modern Crisp Light (Stripe / Apple / Fintech)
```

---

### 1. ⚡ Minimalist High-Performance SaaS (Linear / Vercel Style)
*Best for: Developer tools, B2B SaaS, Analytics, Modern Dashboards.*
- **Canvas:** Pure Charcoal / Pitch Zinc (`#09090b` or `#000000`)
- **Borders:** Crisp, razor-sharp 1px borders (`border: 1px solid rgba(255, 255, 255, 0.08)`)
- **Lighting:** Ultra-subtle directional linear gradients (`linear-gradient(180deg, rgba(255,255,255,0.03) 0%, transparent 100%)`)
- **Typography:** Inter / Geist / JetBrains Mono for metrics.
- **Micro-Interactions:** Subtle hover outline glow (`hover:border-zinc-600`), keyboard shortcuts HUD (`⌘K`).

---

### 2. 💎 Luxury Obsidian & Glassmorphism 2.0
*Best for: AI Flagship products, Luxury brands, High-ticket services, Cutting-edge showcases.*
- **Canvas:** Deep Obsidian Velvet (`#0a0812` / `oklch(0.12 0.012 260)`)
- **Atmosphere:** SVG Fractal Noise overlay + Ambient Mesh Glow (`radial-gradient` multi-stop blur).
- **Glassmorphism 2.0:** Dual-layer surface with **Fresnel Specular Inset Reflection**:
```css
.glass-luxury {
  background: linear-gradient(135deg, rgba(25, 20, 32, 0.70) 0%, rgba(14, 16, 20, 0.60) 100%);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 
    inset 0 1px 1px 0 rgba(255, 255, 255, 0.16),
    0 16px 32px -8px rgba(0, 0, 0, 0.45);
}
```

---

### 3. 🎨 Neobrutalism & Bold High-Contrast (Gumroad / Figma Style)
*Best for: Creative apps, creator economy, youth brands, bold portfolios.*
- **Canvas:** Vibrant Pastels or Clean Chalk (`#f4f0ea`, `#ffea79`, `#d8b4fe`)
- **Borders:** Heavy, solid black strokes (`border: 2px solid #000000`)
- **Shadows:** Hard offset non-blurred drop shadows (`box-shadow: 4px 4px 0px 0px #000000`)
- **Interactive:** Button active state physical press (`transform: translate(2px, 2px); box-shadow: 2px 2px 0 #000`).

---

### 4. 📰 Swiss Editorial & Paper Craft
*Best for: Long-form reading, agencies, architectural firms, high-end portfolios.*
- **Canvas:** Warm Natural Paper (`#fbfaf8` or `#f5f4ef`)
- **Typography:** High-contrast Serif titles (Playfair, Newsreader) + clean Sans body (Inter/Switzer).
- **Grid:** Asymmetric multi-column editorial layout with generous breathing whitespace.
- **Accents:** Vermillion / Deep Forest Ink (`#e11d48`, `#1c1917`).

---

### 5. ☀️ Modern Crisp Light (Stripe / Apple / Fintech)
*Best for: Fintech, e-commerce, banking, consumer apps, health tech.*
- **Canvas:** Pure Snow & Slate (`#ffffff` with `#f8fafc` surface cards)
- **Elevation:** Diffuse multi-stage soft ambient shadows (`box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 10px 25px -5px rgba(0,0,0,0.04)`)
- **Accents:** Electric Indigo (`#6366f1`) or Emerald (`#10b981`).
- **Cards:** Clean pill badges, micro-icon indicators, crystal-clear accessible contrast.

---

## 🕹️ Universal Interactive Modules

Regardless of the chosen visual style, the agent can equip pages with high-value interactive primitives:
1. **120fps Lerp Comparison Slider:** (Mathematical linear interpolation for before/after visual showcases).
2. **Magnetic Spring CTAs:** (Dynamic cursor-following or physics spring ease).
3. **Bento Grid Architecture:** (Dynamic 3 or 4-column asymmetric cards with sparklines & AI badges).
4. **Directional LTR/RTL Compatibility:** (Universal logical CSS properties `ms-*`, `me-*`, `start-*`, `end-*`).

---

## 📐 Inviolable Fixed-Structure Content-Only RTL Protocol

When building Persian, Arabic, or Bilingual LTR/RTL interfaces:
1. **Never Flip Page Architecture or Grids:**
   - Navbars, grid column orders, theme switcher tabs, card coordinates, and interactive sliders must remain 100% physically fixed in place.
   - Do NOT mirror the entire layout structure or reverse column orders.
2. **Apply RTL Exclusively to Textual Content:**
   - Paragraphs, article prose, headings, and descriptions receive `direction: rtl` and appropriate text alignment.
3. **BiDi Resilience & Mixed English Brand Names:**
   - When Persian sentences contain or start with English terms (e.g. `Claude Code`, `Cursor`, `API`), punctuation and layout must remain clean without scrambling (`unicode-bidi: plaintext` / `<bdi>`).
4. **Code & Technical Metrics Remain Strictly LTR:**
   - Code blocks, CLI commands, URLs, version pills, and telemetry data (`99.98%`, `+2.4%`) must always remain `direction: ltr !important; text-align: left !important` with monospace font.

