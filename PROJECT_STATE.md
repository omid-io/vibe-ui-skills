# Project State: vibe-ui-skills

## Real-Time Status & Active Milestone
- **Active Phase**: Phase 6 — Continuous Evaluation & Ecosystem Release (v2.4.2 Hardened Reference Implementation)
- **Status**: **Hardened Reference Implementation & Continuous Evaluation Pipeline**. Official release `v2.4.2` verified across all audit gates; non-destructive CLI (`@omid-io/tokens`) with `--force` backups and `--dry-run`; live Chromium DOM physical pixel contrast calculations verified; 30-parameter closed-world schema hardened with cycle-safe `$ref` resolution and combinator support; clean documentation and single source of truth manifest (`version.json`).

## Completed Milestones
- [x] **R1: System Architecture & Documentation**:
  - Authored comprehensive [`ARCHITECTURE.md`](ARCHITECTURE.md) (419 lines) defining 6-skill orchestration DAG, JSON Schema machine contracts, 5 visual chemistries, and fixed-structure semantic RTL.
  - Published [`CHANGELOG.md`](CHANGELOG.md) adhering to Keep a Changelog and Semantic Versioning (v2.2.0).
  - Added `⚡ 2-Minute Quick Start` guide in [`README.md`](README.md) and [`README.fa.md`](README.fa.md), normalized PowerShell commands, and grounded claims in empirical metrics.
- [x] **R2: Mathematical & Negative Evaluation Suite**:
  - Upgraded [`evals/run_evals.py`](evals/run_evals.py) with pure-Python relative luminance math ($L = 0.2126 R' + 0.7152 G' + 0.0722 B'$), OKLCH conversion, and recursive schema validator.
  - Added negative test fixtures in [`evals/fixtures/`](evals/fixtures/) (`invalid_archetype.json`, `out_of_range_entropy.json`, `touch_target_below_24px.json`) confirming exit code 1 on violations.
  - Added machine-readable `--json` flag for CI pipeline integration.
- [x] **R3: Modern Production Starter (Next.js 15 & React 19)**:
  - Authored 13 production files under [`examples/nextjs-starter/`](examples/nextjs-starter/) featuring App Router, TypeScript 5, and Tailwind CSS.
  - Implemented typed OKLCH tokens ([`examples/nextjs-starter/lib/tokens.ts`](examples/nextjs-starter/lib/tokens.ts)).
  - Implemented AI component primitives ([`AiThinkingDrawer.tsx`](examples/nextjs-starter/components/AiThinkingDrawer.tsx), [`HeroSection.tsx`](examples/nextjs-starter/components/HeroSection.tsx)) with zero-emoji SVGs and fixed-structure semantic RTL.
- [x] **R4: Supply-Chain & Release Integrity**:
  - Added `-Version` / `--version` parameter to [`install.ps1`](install.ps1) and [`install.sh`](install.sh) for immutable, version-pinned installations.
  - Tagged `v2.2.0` on git.
- [x] **R5: Multi-Model Evaluation & Hardening**:
  - Resolved structural DOM edge case in [`examples/neobrutalist_creative_store.html`](examples/neobrutalist_creative_store.html).
- [x] **R5: v2.2.1 Deep Hardening & Adversarial Audit Fixes**:
  - Created real GitHub Actions CI pipeline in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) with Python 3.10/3.12 eval matrix and Node 20 Next.js 15 production compilation (`npm run build`).
  - Added `audit_nextjs_starter()` to [`evals/run_evals.py`](evals/run_evals.py) issuing automated scorecards for `examples/nextjs-starter` (typed tokens, layout semantics, AI primitives, zero raw emojis, and GPU compositing budget).
  - Validated local Next.js 15 App Router production build: compiled in 42s with zero TypeScript or type-stripping errors.
  - De-hyped documentation across [`README.md`](README.md) and [`README.fa.md`](README.fa.md): eliminated promotional claims ("Awwwards-grade", "Masterpiece", crown emojis) and connected live GitHub Actions badge.
  - Formulated 30-Second Multi-IDE Quick Start for Cursor (`.cursorrules`), Claude Code (`CLAUDE.md`), Windsurf (`.windsurfrules`), and Antigravity.
- [x] **R6: v2.3.0 Ecosystem, Tooling & Runtime Conformance Shipped**:
  - **1-Minute Setup Verification & Recipe Catalog**: Added sanity check prompt, troubleshooting guide, safe install hierarchy, and 70+ component index to [`README.md`](README.md) and [`README.fa.md`](README.fa.md).
  - **VS Code & Cursor Extension (`packages/vibe-ui-vscode`)**: Created full extension with Webview Visual Chemistry sidebar, in-editor WCAG contrast/anti-slop diagnostics, and packaged installable binary [`vibe-ui-vscode-2.3.0.vsix`](packages/vibe-ui-vscode/vibe-ui-vscode-2.3.0.vsix).
  - **Scoped NPM Design Tokens (`@vibe-ui/tokens`)**: Created [`packages/tokens`](packages/tokens) with dual ESM/CJS export, TypeScript `.d.ts` declarations, typed OKLCH colors, physics motion curves, and zero-config Tailwind plugin.
  - **Enterprise Architecture Guide**: Authored [`docs/ENTERPRISE_ADAPTATION.md`](docs/ENTERPRISE_ADAPTATION.md) for Figma token translation and company UI library bindings.
  - **Headless Playwright Browser Verification (`--browser`)**: Added runtime Chromium DOM inspection to [`evals/run_evals.py`](evals/run_evals.py), caught and fixed 25px horizontal overflow on mobile 375px viewport in [`examples/saas_ai_hero.html`](examples/saas_ai_hero.html), and added `browser-runtime-evals` job to [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
  - **GitHub Roadmap Board Updated**: All issues #1 through #5 moved to `Done` on [`Vibe UI — Engineering Roadmap & Ecosystem RFCs`](https://github.com/users/omid-io/projects/3).

- [x] **R7: Multi-Registry Publishing & Release Infrastructure (v2.3.0 Live Worldwide)**:
  - **VS Code Marketplace**: [`omid-io.vibe-ui-vscode`](https://marketplace.visualstudio.com/items?itemName=omid-io.vibe-ui-vscode) verified and 100% live worldwide.
  - **Open-VSX Registry**: [`omid-io.vibe-ui-vscode`](https://open-vsx.org/extension/omid-io/vibe-ui-vscode) live with official 128x128 icon and claimed namespace `omid-io`.
  - **NPM Registry**: [`@omid-io/tokens`](https://www.npmjs.com/package/@omid-io/tokens) published and installable globally.
  - **GitHub Secrets & CI/CD Workflow**: Stored `NPM_TOKEN` and `OPENVSX_TOKEN` in repo secrets via `gh secret set`; created [`.github/workflows/publish.yml`](.github/workflows/publish.yml) for automated publishing on git release.
  - **Release Runbook**: Authored [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md) documenting 10-second manual update protocol for Marketplace and automated CI for NPM/Open-VSX.

- [x] **R8: v2.4.0 Ecosystem: CLI Scaffolding, Component Registry & Interactive Studio**:
  - **Zero-Dependency CLI Tool**: Added `npx @omid-io/tokens init` (scaffolding editor contracts & OKLCH variables) and `npx @omid-io/tokens add <component>` (`thinking-drawer`, `telemetry-hud`, `contrast-badge`).
  - **Interactive VS Code Extension Studio**: Added live WCAG 2.2 contrast calculator with color pickers and instant pass/fail ratios; added interactive component catalog with 1-click **Insert into Active Editor**.
  - **Multi-Registry Publication**: `@omid-io/tokens` v2.4.0 live on NPM; `omid-io.vibe-ui-vscode` v2.4.0 live on Open-VSX; packaged `vibe-ui-vscode-2.4.0.vsix` and published GitHub [Release v2.4.0](https://github.com/omid-io/vibe-ui-skills/releases/tag/v2.4.0).

- [x] **R9: Multi-LLM Adversarial Audit & Documentation Overhaul**:
  - Executed independent Round 3 review across ChatGPT-4o, Grok, and Claude 3.7 Sonnet.
  - Eliminated promotional superlatives in favor of calm, high-signal engineering documentation.
  - Hardened `schemas/design-spec.v1.schema.json` with `additionalProperties: false` and synced version `2.4.0`.
  - Added explicit "What Vibe UI Is / What It Is Not" and deterministic vs. heuristic verification matrix to `README.md` and `README.fa.md`.

- [x] **R10: Adversarial Audit & Contract Hardening**:
  - **Closed-World Validator Enforcement**: Implemented `additionalProperties: false` enforcement inside `validate_json_instance()` in `evals/run_evals.py` rejecting undeclared keys at root and nested levels.
  - **Domain Numerical Ranges**: Added strict bounds to `schemas/design-spec.v1.schema.json` for coordinates (`latitude: [-90, 90]`, `longitude: [-180, 180]`), financial math (`precision_decimals: [0, 8]`), and Core Web Vitals budgets (`lcp_max_ms: [100, 10000]`, `cls_max: [0.0, 1.0]`, `inp_max_ms: [10, 1000]`).
  - **Browser Runtime Failure Integrity**: Hardened error boundaries so browser runtime exceptions exit with non-zero failure (`results["overall_status"] = "FAIL"`).
  - **Multi-Viewport Real DOM Assertions**: Audited both `375x667` and `320x568` in headless Chromium. Caught and resolved a 320px narrow mobile overflow in `neobrutalist_creative_store.html`.
  - **Accessible Name & Label Verification**: Asserted that every interactive button, anchor, and input has a non-empty accessible name, title, or ARIA label.
- [x] **R11: Runtime & Validator Security Hardening (v2.4.1 Release)**:
  - **Closed Dollar-Prefix Exploit & Negative Fixture**: Restricted `$schema` strictly to the exact root level (`path == "$"`). Any rogue `$`-prefixed property (e.g. `$injected_exploit`) is rejected immediately. Added and verified adversarial fixture [`evals/fixtures/illegal_dollar_property.json`](evals/fixtures/illegal_dollar_property.json).
  - **Local `$ref` Resolution with Cycle Detection & Depth Guard**: Added recursion depth limit (64) and visited reference set tracking to prevent circular reference DoS.
  - **String Constraints**: Added `minLength`, `maxLength`, and regex `pattern` validations to `validate_json_instance`.
  - **Deterministic Rendering Stabilization in Chromium**: Replaced raw `domcontentloaded` with bounded `networkidle` (3000ms timeout), `document.fonts.ready`, and double `requestAnimationFrame` before measuring geometry.
  - **Strict Visibility & `aria-hidden` Exclusion**: Filtered out elements inside `[aria-hidden="true"]`, `display: none`, `visibility: hidden`, or `opacity: 0` to prevent false passes on hidden elements.
  - **Keyboard Focus-Visible Ring Assertion**: Programmatically verified that interactive controls receive physical focus rings (`outline` or `box-shadow`) under `:focus-visible`.
  - **Prefers-Reduced-Motion Emulation**: Verified Chromium response to `(prefers-reduced-motion: reduce)`.
  - **CLI Non-Destructive Operations**: Added `--force` (with automated `.bak` backups) and `--dry-run` to `npx @omid-io/tokens` (`init` and `add`).
  - **Version Harmonization**: Pinned all installers (`install.sh`, `install.ps1`), security policy (`SECURITY.md`), architecture specification (`ARCHITECTURE.md`), and central manifest (`version.json`) to `v2.4.2`.
- [x] **R12: Multi-LLM Blind Audit Hardening (Release v2.4.2)**:
  - **Decoupled Package Builds**: Eliminated `examples/nextjs-starter/node_modules/typescript` coupling in `packages/tokens/build.js` and `packages/vibe-ui-vscode/build.js`. Added explicit devDependencies and independent build pipelines.
  - **Fail-Closed JSON Validator**: Eliminated silent `pass` in pattern evaluation in `evals/run_evals.py`; added standard combinators (`allOf`, `anyOf`, `oneOf`, and `maxItems`).
  - **Extension Diagnostics Correction**: Removed misleading "100% WCAG AA verified" message in `packages/vibe-ui-vscode/src/extension.ts` on simple token presence; explicitly scoped to heuristic scan with instructions to run browser runtime eval.
  - **WebView Security Hardening**: Injected strict Content-Security-Policy (CSP) meta tag into VS Code webview and decoupled implicit global `event` in `switchTab`.
  - **Eliminated Hype Remnants**: Cleaned legacy marketing terms ("Awwwards-grade", "120fps", "battle-tested") across all HTML showcases (`index.html`, `showcase/index.html`), prompts, and agent descriptions.
  - **Single Source of Truth Manifest**: Coordinated version `2.4.2` across `version.json`, `package.json`, `package_vsix.py`, and `nextjs-starter/package.json`.

## Immediate Next Steps & Public Launch
- **Live Engineering Board**: [`Vibe UI — Engineering Roadmap & Ecosystem RFCs`](https://github.com/users/omid-io/projects/3)
1. **Community Distribution**: Execute Show HN, Reddit (`r/webdev`, `r/ClaudeAI`, `r/cursor`), and X launch threads.

## Modified / Created Files Index
- [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [`CHANGELOG.md`](CHANGELOG.md)
- [`README.md`](README.md)
- [`README.fa.md`](README.fa.md)
- [`evals/run_evals.py`](evals/run_evals.py)
- [`evals/README.md`](evals/README.md)
- [`evals/fixtures/invalid_archetype.json`](evals/fixtures/invalid_archetype.json)
- [`evals/fixtures/out_of_range_entropy.json`](evals/fixtures/out_of_range_entropy.json)
- [`evals/fixtures/touch_target_below_24px.json`](evals/fixtures/touch_target_below_24px.json)
- [`examples/nextjs-starter/package.json`](examples/nextjs-starter/package.json)
- [`examples/nextjs-starter/tsconfig.json`](examples/nextjs-starter/tsconfig.json)
- [`examples/nextjs-starter/next.config.ts`](examples/nextjs-starter/next.config.ts)
- [`examples/nextjs-starter/tailwind.config.ts`](examples/nextjs-starter/tailwind.config.ts)
- [`examples/nextjs-starter/postcss.config.mjs`](examples/nextjs-starter/postcss.config.mjs)
- [`examples/nextjs-starter/README.md`](examples/nextjs-starter/README.md)
- [`examples/nextjs-starter/lib/tokens.ts`](examples/nextjs-starter/lib/tokens.ts)
- [`examples/nextjs-starter/lib/utils.ts`](examples/nextjs-starter/lib/utils.ts)
- [`examples/nextjs-starter/app/globals.css`](examples/nextjs-starter/app/globals.css)
- [`examples/nextjs-starter/app/layout.tsx`](examples/nextjs-starter/app/layout.tsx)
- [`examples/nextjs-starter/app/page.tsx`](examples/nextjs-starter/app/page.tsx)
- [`examples/nextjs-starter/components/AiThinkingDrawer.tsx`](examples/nextjs-starter/components/AiThinkingDrawer.tsx)
- [`examples/nextjs-starter/components/HeroSection.tsx`](examples/nextjs-starter/components/HeroSection.tsx)
- [`install.ps1`](install.ps1)
- [`install.sh`](install.sh)
- [`.gitignore`](.gitignore)

