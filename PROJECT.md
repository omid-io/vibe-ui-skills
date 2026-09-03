# Project: vibe-ui-skills (Industry Benchmark Elevation)

## Architecture
The `vibe-ui-skills` ecosystem is structured as an AI agent UI design system commanded by master orchestrator `mr-ui-designer`. It coordinates 6 specialized sub-skills in a unidirectional, contract-driven pipeline:
1. `autonomous-intent-expander`: Ingests user prompt, evaluates against 3-tier ambiguity budget, maps to 1 of 8 domain archetypes, outputs canonical `design-spec.json` (Draft 2020-12 schema).
2. `visual-chemistry-engine`: Selects 1 of 5 visual chemistries, enforces anti-repetition protocol across >=3 dimensions, and establishes perceptual OKLCH color token scales.
3. `ui-kit`: Ingests 20 AI-native primitives and 50+ accessible components, asymmetric Bento grids, and CSS logical properties.
4. `vibe-physics-engine`: Injects frame-rate-independent deltaTime motion loop ($\alpha = 1 - e^{-\lambda \cdot \Delta t}, \lambda = 14$), modern Lenis smooth scrolling, GPU composite transforms, and pure SVG vectors (0 unicode emojis).
5. `conversion-copy-engine`: Value-based narrative architecture, PAS framework, hero headline formulas, and anti-dark-pattern compliance.
6. `ui-verifier`: 5-pillar autonomous quality gate (Visual novelty, Responsive 375/768/1440px, WCAG 2.2 AA contrast >=4.5:1 / >=3:1, Blur compositing budget <=3, Semantic RTL stability).

The platform also provides:
- Mathematical & negative evaluation suite (`evals/run_evals.py` with `--json` reporting and test fixtures in `evals/fixtures/`).
- Modern production starter in `examples/nextjs-starter/` (Next.js 15 App Router, React 19, TypeScript, typed OKLCH tokens, AI component primitives, fixed-structure semantic RTL).
- Supply-chain integrity with version-pinned installers (`install.ps1` and `install.sh` via `-Version` flag) and official GitHub Release tag `v2.2.0`.

## Feature Inventory
Every feature identified during the comprehensive Phase 0 survey is inventoried and mapped to a discrete milestone below:

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | System Architecture Documentation | Author comprehensive `ARCHITECTURE.md` detailing the 6-skill pipeline, JSON schema data contracts, 5 visual chemistries, and fixed-structure semantic RTL architecture. | M1 | ORIGINAL_REQUEST §R1 |
| 2 | Changelog & Version Ledger | Author standard `CHANGELOG.md` adhering to Keep a Changelog and SemVer 2.0.0, documenting all versions up to v2.2.0. | M1 | ORIGINAL_REQUEST §R1 |
| 3 | Documentation Polish & Quick Start | Add 2-minute Quick Start, tone down promotional rhetoric to empirical data-backed engineering claims, and fix typos (`.\install.ps1` in bash blocks). | M1 | ORIGINAL_REQUEST §R1 |
| 4 | Persian Documentation Polish | Update `README.fa.md` with 2-minute Persian Quick Start, objective technical specifications, and fix badge anchor links. | M1 | ORIGINAL_REQUEST §R1 |
| 5 | Documentation Internal Link Audit | Resolve 100% of internal links across `README.md`, `README.fa.md`, and `evals/README.md` to existing files and valid anchor tags. | M1 | ORIGINAL_REQUEST §AC4 |
| 6 | Intent Expander Contract Alignment | Align sample design contract in `skills/autonomous-intent-expander/SKILL.md` to match `schemas/design-spec.v1.schema.json`. | M1 | Survey 1 |
| 7 | Mathematical WCAG Contrast Engine | Upgrade `evals/run_evals.py` with exact relative luminance formula ($L = 0.2126 R' + 0.7152 G' + 0.0722 B'$) and OKLCH conversion math to verify contrast ratios >=4.5:1 (body) and >=3:1 (headers). | M2 | ORIGINAL_REQUEST §R2 |
| 8 | Recursive Schema Validator | Implement recursive pure Python stdlib JSON Schema validator in `run_evals.py` checking nested properties, types, enums, const, minItems, and min/max numerical bounds. | M2 | Survey 2 |
| 9 | Negative Schema Test Fixtures | Add test fixtures in `evals/fixtures/` verifying invalid archetypes, out-of-range entropy heuristics, and touch targets <24px fail validation with exit code 1. | M2 | ORIGINAL_REQUEST §R2 |
| 10 | Machine-Readable JSON Output | Implement `--json` CLI flag in `evals/run_evals.py` emitting structured JSON summary to stdout and exiting code 0 on full pass, code 1 on failure. | M2 | ORIGINAL_REQUEST §R2 |
| 11 | Next.js 15 Starter Architecture | Implement clean Next.js 15 App Router starter in `examples/nextjs-starter/` with React 19, TypeScript, and Tailwind CSS. | M3 | ORIGINAL_REQUEST §R3 |
| 12 | Typed OKLCH Multi-Chemistry Tokens | Implement `lib/tokens.ts` exporting typed token system across all 5 visual chemistries (`MINIMALIST_SAAS`, `LUXURY_GLASS_2`, `NEOBRUTALISM`, `SWISS_EDITORIAL`, `STRIPE_CRISP_LIGHT`). | M3 | ORIGINAL_REQUEST §R3 |
| 13 | AI Component Primitive: Thinking Drawer | Implement `AiThinkingDrawer.tsx` with smooth CSS grid height animation (`0fr` to `1fr`), ARIA live regions, radar pulse status, micro-latency tool chips, and pure SVG vectors. | M3 | ORIGINAL_REQUEST §R3 |
| 14 | AI Component Primitive: Hero Section | Implement `HeroSection.tsx` with high-contrast copy, chemistry badge, embedded drawer, CTAs, and telemetry metric HUD. | M3 | ORIGINAL_REQUEST §R3 |
| 15 | Fixed-Structure Semantic RTL | Implement physical macro stability, content-only RTL, BiDi punctuation isolation (`<bdi>`), and pure LTR monospace telemetry (`.ltr-code`). | M3 | ORIGINAL_REQUEST §R3 |
| 16 | Starter Manifest & Dependency Integrity | Author `package.json` with valid JSON syntax verifiable by Node and JSON tooling. | M3 | ORIGINAL_REQUEST §AC3 |
| 17 | Version-Pinned PowerShell Installer | Upgrade `install.ps1` with `-Version` parameter, tag normalization, dynamic directory extraction, and graceful 404 handling. | M4 | ORIGINAL_REQUEST §R4 |
| 18 | Version-Pinned Shell Installer | Upgrade `install.sh` with `--version` / `-Version` parameter, dynamic directory extraction, and graceful 404 handling. | M4 | ORIGINAL_REQUEST §R4 |
| 19 | Git Release Tagging (v2.2.0) | Create annotated git release tag `v2.2.0` documenting the milestone elevation in VCS history. | M4 | ORIGINAL_REQUEST §R4 |
| 20 | GitHub Release Publication | Publish official GitHub Release `v2.2.0` with structured release notes adhering to Keep a Changelog. | M4 | ORIGINAL_REQUEST §R4 |
| 21 | Final Acceptance Gate Verification | Empirically prove all 4 Automated Verification Criteria pass cleanly (Evals JSON, negative fixtures, package.json syntax, link validation). | M5 | ORIGINAL_REQUEST §AC1-4 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Complete System Architecture & Documentation (R1) | Author `ARCHITECTURE.md`, `CHANGELOG.md`; Polish `README.md`, `README.fa.md`, `evals/README.md`; Align `autonomous-intent-expander/SKILL.md`. | Survey completed | DONE (Gate passed, 0 broken links, evals exit 0) |
| M2 | Mathematical & Negative Evaluation Suite (R2) | Upgrade `evals/run_evals.py` (WCAG contrast math, recursive stdlib validator, `--json` flag); Create `evals/fixtures/` (`valid_design_spec.json`, `invalid_archetype.json`, `out_of_range_entropy.json`, `touch_target_below_24px.json`). | Survey completed | DONE (Gate passed, math luminance exact, negative fixtures exit 1, --json valid) |
| M3 | Modern Production Starter (R3) | Create `examples/nextjs-starter/` (12 files: Next.js 15, React 19, TypeScript, `lib/tokens.ts`, `AiThinkingDrawer.tsx`, `HeroSection.tsx`, fixed-structure RTL). | M1, M2 | DONE (Gate passed, 13 files, package.json valid, OKLCH contrast >17:1, 0 emojis, semantic RTL) |
| M4 | Supply-Chain & GitHub Release Integrity (R4) | Update `install.ps1` & `install.sh` with `-Version` parameter; Create git tag `v2.2.0`; Publish GitHub release notes. | M1, M2, M3 | PLANNED |
| M5 | Final Dual-Track Verification & Acceptance Gate | Run full test suite, verify `python evals/run_evals.py --json` exit 0, verify negative fixture rejection exit 1, verify package.json syntax, verify 100% internal links, adversarial coverage hardening. | M1, M2, M3, M4 | PLANNED |

## Interface Contracts
### autonomous-intent-expander ↔ mr-ui-designer & downstream skills
- Machine contract: `schemas/design-spec.v1.schema.json`
- Top-level mandatory keys: `spec_version`, `domain_archetype`, `visual_chemistry`, `core_parameters`, `accessibility_contract`, `semantic_rtl_contract`, `novelty_budget`.
- Number bounds: `accessibility_contract.min_touch_target_px >= 24`, `novelty_budget.entropy_heuristic in [0.0, 1.0]`.

### evals/run_evals.py CLI & Schema Contract
- CLI Flags:
  - `--json`: Suppresses ASCII banners, emits pure JSON report to `sys.stdout`. Exit code 0 if all pass, 1 if any fail.
  - `--fixture <path>`: Runs evaluation against a specific fixture JSON file.
- Contrast verification:
  - Body copy vs Canvas background: Relative luminance contrast ratio >= 4.5:1.
  - Headers / Large text vs Canvas background: Relative luminance contrast ratio >= 3.0:1.
  - Calculation formula: $L = 0.2126 R' + 0.7152 G' + 0.0722 B'$ where $C' = C/12.92$ if $C \le 0.04045$ else $((C+0.055)/1.055)^{2.4}$. Ratio = $(L_1 + 0.05) / (L_2 + 0.05)$.

### examples/nextjs-starter Contract
- Framework: Next.js 15 App Router (`next: ^15.1.7`), React 19 (`react: ^19.0.0`), TypeScript (`typescript: ^5.7.3`).
- Token Interface: `lib/tokens.ts` exports `VISUAL_CHEMISTRIES` typed dictionary matching all 5 visual chemistries.
- Component Primitives:
  - `AiThinkingDrawer.tsx`: Collapsible CSS grid transition, ARIA `role="region"`, `aria-expanded`, pure SVG vectors.
  - `HeroSection.tsx`: Responsive landing hero, embedded drawer, telemetry HUD with `.ltr-code`.
- RTL Contract: Macro layout coordinates preserved, `dir="rtl"` on text only, mixed English brands in `<bdi>`, code/metrics in `.ltr-code`.

### install.ps1 & install.sh Contract
- Parameters:
  - PowerShell: `-Version <string>` (e.g. `v2.2.0` or `2.2.0`), `-Agent`, `-TargetDir`, `-Backup`, `-Force`.
  - Shell: `--version <string>` / `-Version <string>`, `--agent`, `--target`, `--force`, `--no-backup`.
- Dynamic Extraction: Selects first extracted directory regardless of name (`vibe-ui-skills-main` vs `vibe-ui-skills-2.2.0`).

## Code Layout
- `ARCHITECTURE.md`: Repository root architectural specification.
- `CHANGELOG.md`: Repository root changelog.
- `README.md` & `README.fa.md`: Repository documentation.
- `evals/run_evals.py`: Automated evaluation runner.
- `evals/fixtures/`: Schema test fixtures (`valid_design_spec.json`, `invalid_archetype.json`, `out_of_range_entropy.json`, `touch_target_below_24px.json`).
- `examples/nextjs-starter/`: Next.js 15 starter application.
- `install.ps1` & `install.sh`: Version-pinned installers.
