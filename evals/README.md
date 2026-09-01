# 🧪 Vibe UI Evaluation Suite (`evals/`)

This directory contains formal evaluation benchmarks for measuring AI coding agent outputs when guided by **`mr-ui-designer`** and the Vibe UI Skills Suite.

---

## 🎯 Purpose of the Eval Suite

Prompt libraries often fail silently because LLMs drift into generic templates ("AI slop") or violate accessibility/RTL invariants. This suite provides **verifiable test specifications** that test:
1. **Visual Anti-Slop & Novelty:** Absence of predictable cliché gradients or flat gray borders.
2. **Accessibility & WCAG AA:** Proper semantic tags (`<button>`, `<bdi>`), keyboard reachability, and visible focus rings.
3. **Semantic RTL Resilience:** Preservation of physical macro coordinates while correctly mirroring directional cues and isolating English terms.
4. **Performance Budgets:** Strict caps on backdrop-filter layers and mandatory reduced-motion wrapping.

---

## 📂 Test Cases in this Suite

| Test Case File | Domain Archetype | Key Verification Focus |
| :--- | :--- | :--- |
| [`saas_dashboard_eval.md`](saas_dashboard_eval.md) | `HIGH_PERFORMANCE_SAAS` | Minimalist SaaS chemistry, JetBrains Mono metrics, tool call chips, max 3 blur layers. |
| [`persian_rtl_landing_eval.md`](persian_rtl_landing_eval.md) | `HIGH_TICKET_SERVICE` | Vazirmatn font stack, fixed macro coordinates, `<bdi>` punctuation isolation, no flipped grids. |
| [`ai_chat_interface_eval.md`](ai_chat_interface_eval.md) | `AI_NATIVE_ASSISTANT` | Accessible thinking state button, streaming response bubbles, human approval card. |

---

## ⚡ How to Run an Evaluation

1. Send the `Prompt` defined in any eval file to your AI agent (Claude Code, Cursor, Antigravity, Copilot).
2. Feed the agent's output through the **`ui-verifier`** skill.
3. Verify that the generated code satisfies all **Expected Properties** and triggers zero **Forbidden Patterns**.
4. Confirm an overall **PASS** status on the UI-Verifier Scorecard.
