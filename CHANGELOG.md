# Changelog

All notable changes to the **Vibe UI Skills** repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.2.1] - 2026-09-03

### Added
- Real GitHub Actions CI workflow in `.github/workflows/ci.yml` running multi-version Python matrix tests (`run_evals.py` and `--json`) and automated Node 20 Next.js 15 production compilation (`npm run build`).
- Integrated `audit_nextjs_starter()` within `evals/run_evals.py` providing automated scorecards for `examples/nextjs-starter` (typed OKLCH tokens, App Router layout, AI primitives, zero raw emojis, and GPU compositing budget).
- Explicit `dir="ltr"` attribute in `examples/nextjs-starter/app/layout.tsx` for accessibility and BiDi layout stability.
- Dedicated `⚡ 30-Second Setup: Multi-IDE Quick Start` section in `README.md` and `README.fa.md` with zero-friction adapter setup for Cursor (`.cursorrules`), Claude Code (`CLAUDE.md`), Windsurf (`.windsurfrules`), and Antigravity.

### Changed
- Comprehensive de-hyping pass across `README.md` and `README.fa.md`: removed promotional adjectives ("Masterpiece", "Awwwards-grade") and decorative crown emojis in favor of deterministic contract-driven engineering specifications.
- Connected real GitHub Actions CI badge (`.github/workflows/ci.yml`) to the repository header.
- Updated evaluation runner suite version to `2.2.1`.

---

## [2.2.0] - 2026-09-03

### Added
- Comprehensive system architecture specification in `ARCHITECTURE.md` detailing the 6-skill unidirectional pipeline, JSON schema data contracts, the 5 visual chemistries matrix, and fixed-structure semantic RTL invariants.
- Next.js 15 App Router production starter in `examples/nextjs-starter/` featuring React 19, TypeScript, typed OKLCH design tokens (`lib/tokens.ts`), AI component primitives (`AiThinkingDrawer.tsx`, `HeroSection.tsx`), and fixed-structure RTL support.
- Mathematical WCAG 2.2 AA relative luminance calculation in `evals/run_evals.py` ($L = 0.2126 R' + 0.7152 G' + 0.0722 B'$) ensuring contrast ratios $\ge 4.5:1$ (body copy) and $\ge 3:1$ (headings).
- Negative schema test fixtures in `evals/fixtures/` (`invalid_archetype.json`, `out_of_range_entropy.json`, `touch_target_below_24px.json`) verifying strict rejection of non-compliant design contracts with exit code 1.
- Machine-readable `--json` CLI reporting flag in `evals/run_evals.py` for automated CI/CD pipeline integration.
- Version-pinned installation support in `install.ps1` and `install.sh` via `-Version` / `--version` flag with automatic tag normalization and safe `.bak` backups.
- Actionable `⚡ 2-Minute Quick Start` section in `README.md` and `README.fa.md` with concrete 3-step developer workflows.

### Changed
- Aligned sample JSON design spec in `skills/autonomous-intent-expander/SKILL.md` to conform strictly with `schemas/design-spec.v1.schema.json`.
- Calibrated repository documentation tone from promotional rhetoric to empirical, data-driven engineering claims (WCAG AA contrast, 0px mobile overflow, $\le 3$ blur layer compositing budget, 70+ components, deltaTime physics).
- Separated Windows PowerShell execution commands from bash blocks in `README.md` and `README.fa.md`, providing explicit `powershell -ExecutionPolicy Bypass -File .\install.ps1` syntax.

### Fixed
- Fixed broken badge navigation anchor `#-the-sub-skills-arsenal` in `README.md` to resolve to `#-the-6-sub-skills-arsenal-commanded-by-mr-ui-designer`.
- Fixed broken Persian badge navigation anchor in `README.fa.md`.
- Converted raw code spans for `neobrutalist_store_eval.md` and `swiss_editorial_eval.md` in `evals/README.md` into clickable markdown links.

### Security
- Reinforced automated schema validation against untrusted or malformed design contracts.
- Maintained strict isolation of code and telemetry blocks from bidirectional RTL text processing.

---

## [2.1.0] - 2026-08-15

### Added
- Interactive GitHub Pages showcase (`showcase/index.html`) featuring real-time visual chemistry switching and responsive inspection.
- Formal security policy in `SECURITY.md` establishing vulnerability disclosure protocols and supported release versions.
- Comprehensive third-party license attribution matrix in `THIRD_PARTY_NOTICES.md` (covering Shadcn UI, Beautiful UI, Transitions.dev, BeUI, and Lenis).
- BiDi punctuation isolation standard utilizing `<bdi>` tags for mixed Latin/Persian technical phrases.

### Fixed
- Resolved horizontal layout overflow on 375px mobile viewports within Bento grid cards.
- Fixed focus indicator visibility for keyboard navigation across all interactive demo buttons.

---

## [2.0.0] - 2026-07-01

### Added
- Autonomous quality gate skill `ui-verifier` (`skills/ui-verifier/SKILL.md`) implementing 5-pillar verification (Visual Anti-Slop, Multi-Device Responsive, WCAG 2.2 AA, Compositing Budget, Semantic RTL).
- Canonical machine-readable JSON Schema in `schemas/design-spec.v1.schema.json` (Draft 2020-12) for parameterized interface generation.
- 4 standalone production-ready HTML/CSS preview examples (`saas_ai_hero.html`, `persian_rtl_bento.html`, `neobrutalist_creative_store.html`, `swiss_editorial_article.html`).
- Drop-in IDE adapters for Cursor (`.cursorrules`), Claude Code (`CLAUDE.md`), GitHub Copilot (`copilot-instructions.md`), and Windsurf (`.windsurfrules`).
- Automated evaluation runner in `evals/run_evals.py` and benchmark specifications in `evals/`.
- Automated GitHub Actions CI workflow in `.github/workflows/evals.yml`.

### Changed
- Replaced standard linear CSS transitions with frame-rate-independent deltaTime exponential physics loop ($\alpha = 1 - e^{-\lambda \cdot \Delta t}, \lambda = 14$).
- Standardized color system on the perceptual OKLCH color model across all 5 visual chemistries.
- Enforced strict ban on unicode emojis in production interfaces in favor of precision SVG vector sprites.

---

## [1.1.0] - 2026-05-20

### Added
- Master frontend architect orchestrator agent `mr-ui-designer` (`mr-ui-designer/AGENT.md`) to coordinate specialized sub-skills.
- Specification synthesis skill `autonomous-intent-expander` (`skills/autonomous-intent-expander/SKILL.md`) with 3-tier Ambiguity Budget and 8 domain archetypes.
- 30 Golden Prompts reference cheat sheets in `PROMPTS.md` and `PROMPTS.fa.md`.
- Multi-agent terminal installer scripts `install.ps1` (PowerShell) and `install.sh` (Bash).

### Fixed
- Fixed layout collapse issues during right-to-left language switching.

---

## [1.0.0] - 2026-04-01

### Added
- Initial release of the Vibe UI Skills suite for AI coding assistants.
- Core design skills: `visual-chemistry-engine`, `ui-kit`, `vibe-physics-engine`, and `conversion-copy-engine`.
- 5 foundational visual chemistries: Minimalist SaaS, Luxury Glass, Neobrutalism, Swiss Editorial, and Modern Crisp Light.
- Component catalog references for Shadcn UI, AI-native primitives, and Bento grids.
- Native Persian RTL language support and documentation (`README.fa.md`).
- MIT open-source license.
