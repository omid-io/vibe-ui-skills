---
name: ui-kit
description: Exhaustive, domain-agnostic UI/UX Component Engine & Design Intelligence. Curated from Beautiful UI (beautifului.dev - 20 AI primitives), Shadcn UI (ui.shadcn.com - 50+ components), BeUI (beui.dev), Rare UI (rareui.com), and Transitions.dev. Provides copy-paste primitives for AI Thinking states, Streaming text, Tool chips, Approval cards, Task rows, Flowcharts, Insight sparklines, Bento grids, Physics transitions, and accessible UI controls for any tech stack (React, Next.js, Vue, Tailwind, HTML/Vanilla, Flutter) in any visual style or language (LTR/RTL).
triggers: ["ui-kit", "uikit", "beautifului", "beui", "rareui", "transitions.dev", "shadcn", "component library", "ui components", "ai ui", "کامپوننت", "طراحی رابط کاربری", "دیزاین فرانت"]
---

# 🎨 UI-Kit: Exhaustive AI-Native & Modern Component Engine

`ui-kit` is a 100% domain-agnostic, production-grade component encyclopedia. It contains the complete catalog of primitives across the 5 premier modern design ecosystems.

---

## 🌐 The 5 Pillar Resource Catalogs

| Catalog Reference | Source | Component Scope |
| :--- | :--- | :--- |
| [`references/ai_native_full_catalog.md`](references/ai_native_full_catalog.md) | **[Beautiful UI](https://beautifului.dev)** | **Complete 20 AI Primitives:** Loading State, Thinking State, Streaming Text, Approval Card, Tool Chips, Task Rows, Chat, Prompt Bar, Recommendation Card, Context Cards, Diff Table, Records Table, Filter Table, Sidebar Nav, Search HUD, Flowchart Canvas, Insight Cards / Sparklines, Code Block with Copy, Fine-tune Card, Selection Actions. |
| [`references/shadcn_full_catalog.md`](references/shadcn_full_catalog.md) | **[Shadcn UI](https://ui.shadcn.com)** | **Complete 50+ UI Primitives:** Forms & Inputs (Input, Textarea, Select, Checkbox, Switch, InputOTP, Slider), Overlays & Modals (Dialog, Sheet/Drawer, Popover, Tooltip, Dropdown), Navigation (Command Palette `Cmd+K`, Tabs, Breadcrumb), Feedback (Sonner Toast, Skeleton Shimmer, Progress), Data Display (Accordion, Avatar, Table). |
| [`references/bento_grids_and_cards.md`](references/bento_grids_and_cards.md) | **[BeUI](https://beui.dev) & [Rare UI](https://rareui.com)** | **Bento & Interactive Cards:** 3-Col & 4-Col Asymmetric Bento Grids, Glassmorphism 2.0 Inset Specular Cards, Animated Gradient Shimmer Buttons, Metric HUD Tiles. |
| [`references/physics_transitions_catalog.md`](references/physics_transitions_catalog.md) | **[Transitions.dev](https://transitions.dev)** | **Zero-Dependency Motion:** Pure CSS Grid Dynamic Height Accordions (`0fr` -> `1fr`), Spring Easing Bezier Curves, Staggered List Reveals, JS Number Flip Counters, 3D Tilt Cards. |
| [`references/tokens_and_theme_engine.md`](references/tokens_and_theme_engine.md) | **Universal Design System** | **Tokens & Layouts:** Theme Variables (Light, Dark, Custom), Directional Logical CSS (`ms-*`, `me-*`, `start-*`, `end-*`) for universal LTR & RTL support. |

---

## ⚡ Universal Usage Workflow

Whenever asked to build, design, or refactor any frontend component or view:
1. **Identify the Component Domain:** AI Reasoning, Forms, Navigation, Data Visualization, or Layout.
2. **Read the Target Reference:** Pull exact markup, Tailwind utility classes, and zero-JS transitions from `references/`.
3. **Adapt Seamlessly:** Match the target framework (React, Vue, HTML/JS, Tailwind, Flutter), color theme, and language direction (LTR / RTL).

---

## 📐 Inviolable Fixed-Structure Content-Only RTL Protocol

When implementing components in Persian, Arabic, or Bilingual LTR/RTL views:
1. **Keep Global Component & Grid Structure Fixed:**
   - Never mirror or flip column orders, navigation bars, sliders, or card coordinates. The visual layout remains physically identical across languages.
2. **Target Only Textual Content:**
   - Apply `direction: rtl` and text alignments exclusively to text nodes, titles, and paragraphs.
3. **BiDi Resilience:**
   - Ensure mixed English brand names or tech terms inside Persian sentences do not scramble punctuation (`unicode-bidi: plaintext` or `<bdi>`).
4. **Code & Telemetry Remain LTR:**
   - Code blocks, numbers, metric counters (`99.98%`), and URLs always stay strictly `direction: ltr !important; text-align: left !important`.

