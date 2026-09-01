---
name: autonomous-intent-expander
description: Opinionated 30-parameter intent expansion engine that synthesizes complete technical, aesthetic, and architectural specifications from sparse prompts using a calibrated Ambiguity Budget.
triggers: ["expand intent", "auto-spec", "read my mind", "full architecture", "scale this", "deepen constraints", "lazy prompt", "طراحی سایت کامل", "سند نیازمندی"]
---

# 🧠 Autonomous Intent Expander (30-Parameter Specification Engine)

## 🎯 Purpose & Philosophy
The `autonomous-intent-expander` skill eliminates friction and interrogation fatigue while preventing blind hallucinations. When a user provides a minimal or ambiguous prompt (e.g., *"Build gym website"*, *"طراحی سایت کلینیک زیبایی"*), this engine applies **opinionated default inference** governed by a strict **Ambiguity Budget**.

---

## ⚙️ Operating Rules & Ambiguity Budget

1. **The 3-Tier Ambiguity Budget:**
   - **Tier 1: Visual, Aesthetic & Component Selection (100% Autonomous):**
     Do NOT interrogate the user for layout, color palettes, visual chemistries, or component choices. Select the most cohesive, modern default and implement it directly.
   - **Tier 2: Product Architecture & Standard Workflows (Autonomous with Stated Assumptions):**
     Infer standard industry user flows and data shapes. Always report these under a clear `⚠️ Assumptions Made:` section so the user can steer if needed, without halting execution.
   - **Tier 3: High-Risk Logic, Financials, Auth & Legal/Compliance (Zero Guesswork):**
     Never blindly guess transaction logic, payment split math, HIPAA/GDPR constraints, or authentication models. If critical information is missing that changes liability or data integrity, surface the exact decision fork.

2. **Domain Archetype Classification:**
   Map the input prompt to the most fitting of 8 Master Archetypes:
   - `LUXURY_CLINICAL` (Beauty, Aesthetics, High-End Medicine, Spa)
   - `HIGH_PERFORMANCE_SAAS` (B2B, Dashboards, Developer Tools, Analytics)
   - `HIGH_TICKET_SERVICE` (Legal, Consulting, Real Estate, Wealth Management)
   - `HEAVY_INDUSTRIAL_ECOMMERCE` (Gym, Fitness, Apparel, Supplements)
   - `CREATIVE_EDITORIAL` (Agencies, Design Studios, Portfolios, Architecture)
   - `HOSPITALITY_EXPERIENCE` (Restaurants, Hotels, Event Venues)
   - `HYPER_LOCAL_TRADES` (Plumbing, HVAC, Auto Repair, Local Services)
   - `EDTECH_ACADEMY` (Courses, Certifications, Training Academies)

3. **Structured Specification Pipeline (Core vs. Conditional Parameters):**
   Synthesizes an explicit architectural contract without inflating irrelevant metadata:
   
   **A. Core Parameters (Universal for all interfaces):**
   - **P01-P05: Intent & Product Foundations** (Archetype, Target Persona, Core Job-To-Be-Done, Primary CTA, Secondary Micro-Action).
   - **P06-P08: Trust & Value Mechanics** (Objection Neutralization, Evidence Density, Transparent Risk Reversal).
   - **P09-P13: Visual Chemistry & Tokens** (Canvas Base, Surface Layers, Accent Palette, Functional Colors, Border Radius).
   - **P14-P17: Typography & Spatial Rhythm** (Display Font, Body Font, Tabular Metric Font, 8pt Spacing Cadence).
   - **P18-P21: Motion & Interaction Model** (Scroll Mechanics, Interactive Hero Module, SVG Vector Iconography, Transition Curves).
   - **P22-P24: Narrative & Copy Architecture** (BLUF Value Hook, Problem/Solution Matrix, Brand Voice Register).
   
   **B. Conditional Domain Parameters (Synthesized only when contextually relevant):**
   - **P25: Local Geo-Coordinates & Address** *(Conditional: Local Trades, Hospitality, Brick-and-Mortar only; skipped for SaaS).*
   - **P26: Clinical / Board Certification Proof** *(Conditional: Healthcare, Medical, Legal only).*
   - **P27: Public Web Schema & Wikidata Entity Graph** *(Conditional: Public discoverable SEO sites only; skipped for internal dashboards).*
   - **P28: Financial Math & Transaction Guardrails** *(Conditional: FinTech, Trading, Payment flows only).*
   - **P29-P30: Performance & Isolation Budgets** (Core Web Vitals Budget, Boundary Isolation).

---

## 📄 4. Canonical Machine-Readable Output (`design-spec.json`)

When requested or when compiling specs for downstream build pipelines, `autonomous-intent-expander` outputs this formal JSON Design Contract:

```json
{
  "$schema": "https://vibe-ui.io/schemas/design-spec.v1.json",
  "domain": "HIGH_PERFORMANCE_SAAS",
  "archetype": "minimalist_saas",
  "novelty_budget": {
    "dimensions_varied": ["hero_composition", "grid_density", "accent_palette"],
    "entropy_score": 0.85
  },
  "visual_contract": {
    "canvas": "oklch(0.14 0.005 260)",
    "surface": "oklch(0.18 0.008 260)",
    "accent": "oklch(0.65 0.22 265)",
    "border": "1px solid oklch(0.28 0.01 260)",
    "radius": "8px"
  },
  "typography": {
    "display": "Inter, system-ui, sans-serif",
    "body": "Inter, system-ui, sans-serif",
    "metrics_mono": "JetBrains Mono, monospace",
    "persian_fallback": "Vazirmatn, sans-serif"
  },
  "components_manifest": [
    "ai_thinking_state",
    "tool_execution_chip",
    "bento_grid_3col",
    "sub_pixel_slider"
  ],
  "accessibility_target": "WCAG_2.2_AA",
  "layout_direction": "bi_directional_semantic_rtl"
}
```
