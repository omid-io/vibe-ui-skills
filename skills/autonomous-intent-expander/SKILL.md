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

3. **30-Parameter Structured Specification Pipeline:**
   Synthesize an explicit specification covering all 30 parameters:
   - **P01-P05: Psychological & Intent Foundations** (Archetype, Target Persona, Core Pain-Point, Primary CTA, Secondary Micro-Conversion).
   - **P06-P08: Trust & Conversion Mechanics** (Objection Neutralization, Social Proof Density, Urgency/Exclusivity Driver).
   - **P09-P13: Visual Chemistry & Design Tokens** (Canvas Base, Surface Layers, Metallic/Vibe Accent, Functional Colors, Radius/Border Token).
   - **P14-P17: Typography & Spatial Rhythm** (Display Font, Body Font, Tabular Metric Font, 8pt Spacing Cadence).
   - **P18-P21: Motion & Micro-Interactions** (Scroll Mechanics, Interactive Hero Component, SVG Vector Iconography, Transition Curves).
   - **P22-P25: Narrative & Neuro-Copywriting** (BLUF Value Hook, Problem Matrix, Clinical/Evidence Proof, Brand Voice Register).
   - **P26-P28: Semantic SEO & AEO Engine** (Schema.org Root Entity, Wikidata Entity Link, 5-Decimal Geo-Coordinates).
   - **P29-P30: Technical Performance & Boundary Gates** (Core Web Vitals Budget, Zero-Touch Boundary Isolation).
