# 🎨 Vibe UI & Frontend Architecture Guidelines for Claude Code

When writing or modifying frontend code, components, or styles in this project, follow the **Vibe UI Architecture Standards**:

## 🚫 1. Anti-AI-Slop & Quality Gates
- Reject default generic styling. Deliver bespoke, production-ready interfaces.
- Avoid unicode emojis as interface icons — use inline SVG icons with `stroke="currentColor"`.
- Use logical CSS properties (`ms-*`, `me-*`, `start-*`, `end-*`) for seamless universal LTR & RTL support.

## 🏛️ 2. Visual Chemistries
Support the project's selected aesthetic or adapt to context:
- **Minimalist SaaS:** Dark zinc/charcoal, crisp 1px borders, subtle 180deg gradients, monospace data metrics.
- **Glassmorphism 2.0:** Multi-layer glass cards with Fresnel inset specular reflection (`inset 0 1px 1px 0 rgba(255,255,255,0.16)`), SVG noise texture, and ambient mesh glows.
- **Neobrutalism:** Solid 2px black borders, hard non-blurred offset drop shadows (`4px 4px 0 #000`), tactile press physics.
- **Swiss Editorial:** Warm paper canvas (`#fbfaf8`), high-contrast serif typography, asymmetric grid cadence.
- **Stripe Light:** Snow white canvas, soft multi-layer diffuse shadows, accessible electric indigo/emerald accents.

## 🧩 3. AI-Native & Modern Component Library
Implement complete component primitives:
- **AI Primitives:** Thinking state accordions, Tool call status chips, Streaming chat bubbles, Approval cards.
- **Layouts:** 3-column & 4-column Bento grid architectures with integrated sparklines and metric badges.
- **Motion:** Pure CSS Grid `0fr` to `1fr` transitions for dynamic height, 120fps Lerp before/after sliders.
