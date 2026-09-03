# Vibe UI v3 — Master Implementation Contract (Final)
## Design Intelligence, Recommendation, Design Genome, Critic, Refinement, Verification & Benchmark

> **هدف سند:** تبدیل چشم‌انداز Vibe UI V3 به یک قرارداد اجرایی دقیق و قابل‌سنجش؛ به‌گونه‌ای که implementation توسط انسان یا agent بدون تفسیر معماریِ اضافی انجام شود و هر رفتار مهم دارای schema، invariant، scoring rule، failure mode و acceptance criteria باشد.

**Status:** Final Implementation Contract  
**Scope:** V3 Design Intelligence  
**Primary Goal:** کمینه‌کردن دخالت کاربر در رسیدن به یک UI جذاب، متمایز، مناسب محصول و قابل‌اعتماد  
**Source baseline:** V3 Design Intelligence Roadmap + existing V3 Master Implementation Contract

---

# 0. Non-Negotiable Product Objective

Vibe UI باید از:

> Static UI Skills + Style Catalog

به:

> **Design Decision Engine + Design Director + Self-Critic + Verification Platform**

تبدیل شود.

ورودی ایده‌آل:

```text
«برای یک SaaS مدیریت مالی، حرفه‌ای، مدرن و قابل اعتماد، خیلی شلوغ نباشه و روی موبایل هم خوب باشه.»
```

سیستم باید بتواند:

```text
Prompt
→ Intent Extraction
→ Confidence
→ Recommendation
→ Design Decision
→ Design Genome
→ Design Contract
→ Generation
→ Critique
→ Refinement
→ Verification
→ Evidence-backed Delivery
```

کاربر حرفه‌ای باید بتواند هر تصمیم را override کند.

کاربر عادی نباید مجبور باشد design jargon بداند.

---

# 1. System Layers

```text
L1  Product Intent
L2  Design Intelligence
L3  Knowledge Base
L4  Recommendation
L5  Design Genome
L6  Generation
L7  Critique
L8  Refinement
L9  Verification
L10 Benchmark / Learning
```

## Source of Truth

هر policy، taxonomy، scoring rule و design knowledge باید تا حد ممکن از data/contractهای canonical خوانده شود.

هیچ runtime نباید نسخه مستقل و ناسازگار از همان knowledge را hardcode کند.

---

# 2. Recommended Repository Structure

```text
vibe-ui-skills/
├── data/
│   ├── taxonomy.json
│   ├── domains.json
│   ├── styles.json
│   ├── priors.json
│   ├── typography.json
│   ├── palettes.json
│   ├── layouts.json
│   ├── density.json
│   ├── motion.json
│   ├── interaction-patterns.json
│   ├── states.json
│   ├── anti-patterns.json
│   └── compatibility.json
│
├── schemas/
│   ├── intent-contract.v1.json
│   ├── decision-contract.v1.json
│   ├── design-genome.v1.json
│   ├── design-contract.v1.json
│   ├── critic-report.v1.json
│   ├── verification-report.v1.json
│   └── benchmark-result.v1.json
│
├── skills/
│   ├── design-director/
│   ├── visual-chemistry/
│   ├── ui-kit/
│   ├── physics/
│   ├── conversion-copy/
│   ├── design-critic/
│   ├── auto-refiner/
│   └── ui-verifier/
│
├── scripts/
│   ├── search.py
│   ├── validate_data.py
│   ├── generate_indexes.py
│   └── test_search.py
│
├── packages/
│   ├── design-contract/
│   ├── design-intelligence/
│   ├── verifier/
│   ├── tokens/
│   └── vibe-ui-vscode/
│
├── evals/
│   ├── benchmark/
│   ├── fixtures/
│   ├── visual/
│   ├── accessibility/
│   └── performance/
│
└── docs/
    ├── V3_PRODUCT_VISION.md
    ├── V3_ARCHITECTURE.md
    ├── V3_DESIGN_INTELLIGENCE_SPEC.md
    ├── V3_IMPLEMENTATION_CONTRACT.md
    └── V3_ACCEPTANCE_TEST_SPEC.md
```

---

# 3. Contract Types

سه قرارداد اصلی باید مستقل باشند.

## 3.1 DesignIntentContract

نماینده آن چیزی است که کاربر می‌خواهد.

## 3.2 DesignDecisionContract

نماینده تصمیماتی است که سیستم گرفته است.

## 3.3 VerificationContract / Report

نماینده الزامات و نتایج verification است.

قاعده:

```text
User Intent
≠
System Decision
≠
Verification Result
```

---

# 4. DesignIntentContract

## Required Concepts

```json
{
  "product_domain": {},
  "audience": {},
  "product_mode": {},
  "business_goal": {},
  "brand_personality": [],
  "tone": [],
  "visual_energy": {},
  "density": {},
  "platform": [],
  "language": [],
  "hard_constraints": [],
  "soft_preferences": [],
  "references": [],
  "inference": {},
  "confidence": {},
  "ambiguity": {}
}
```

## Value Provenance

هر value باید مشخص کند:

```text
source:
  user_explicit
  inferred
  default
  reference_extracted
  system_policy
```

Explicit user requirements از inferred values بالاترند.

---

# 5. Confidence Model

هر inference مهم باید confidence داشته باشد.

```text
0.80–1.00
→ Auto Decide

0.50–0.79
→ Decide + expose concise confirmation

< 0.50
→ Ask one high-value question OR offer three human-readable candidates
```

## Confidence Requirements

Confidence نباید صرفاً عدد تولیدشده توسط LLM باشد.

باید بر اساس evidence قابل‌ردیابی یا scoring داخلی ساخته شود.

هر confidence باید:

```text
value
evidence_count
evidence_quality
source_types
calibration_version
```

داشته باشد.

---

# 6. Ambiguity & VoI Protocol

سیستم در حالت ambiguity حق ندارد بی‌دلیل سؤال‌های متوالی بپرسد.

حداکثر:

```text
1 high-value question
```

یا:

```text
3 candidate directions
```

سؤال باید بیشترین اثر را روی تصمیمات downstream داشته باشد.

اولویت پرسش:

```text
Product Goal
→ Audience
→ Tone / Brand Personality
→ Platform
→ Style
→ Decorative Preferences
```

سؤال درباره موارد کم‌اهمیت مثل radius یا shadow در ابتدای flow ممنوع است.

---

# 7. Product Mode

حداقل modes:

```text
persuade
operate
read
experience
```

هر domain می‌تواند primary mode پیشنهادی داشته باشد.

Product mode روی scoring تمام تصمیم‌های بعدی اثر دارد.

---

# 8. Recommendation Engine

## Inputs

```text
DesignIntentContract
+
Knowledge Base
```

## Outputs

```text
ranked_candidates[]
selected_candidate
score
confidence
decision_trace
conflicts
```

---

# 9. Candidate Scoring Contract

Scoring پایه:

```text
Score =
0.25 * DomainFit
+
0.20 * AudienceFit
+
0.20 * ModeFit
+
0.15 * ToneFit
+
0.10 * PlatformFit
+
0.10 * A11yFit
-
Penalty
```

این وزن‌ها باید versioned باشند.

در نسخه‌های بعدی می‌توان وزن‌ها را با benchmark calibration تغییر داد.

## Score Range

```text
0.0 ≤ score ≤ 1.0
```

نمایش UI می‌تواند score را به 0–100 تبدیل کند.

---

# 10. Scoring Method

هر dimension باید تعریف محاسباتی داشته باشد.

## DomainFit

اولویت تطبیق:

```text
exact domain
→ domain family
→ semantic tags
→ aliases
→ general fallback
```

## AudienceFit

تطبیق بین audience نیازمندشده و ویژگی‌های candidate.

## ModeFit

سازگاری style/layout/interaction با product mode.

## ToneFit

تطبیق personality/mood/tone.

## PlatformFit

تطبیق mobile/desktop/touch/keyboard/RTL/LTR.

## A11yFit

جریمه برای styleها و patterns دارای ریسک accessibility.

---

# 11. Domain Priors

Priors باید **soft preferences** باشند، نه قانون مطلق.

نمونه:

```text
Fintech:
  trust > novelty

Healthcare:
  clarity + serenity > decoration

Developer Tools:
  efficiency + density > marketing

Creative:
  distinction > standardization

E-commerce:
  conversion clarity > experimentation
```

User hard constraints می‌توانند prior را override کنند.

---

# 12. Hard Constraints vs Soft Preferences

## Hard Constraints

نمونه:

```text
required language
required platform
brand color
WCAG target
RTL support
no horizontal overflow
user-explicit style
required component
legal requirement
```

## Soft Preferences

نمونه:

```text
mood
novelty
shadow strength
radius preference
decorative effects
animation intensity
```

## Resolution Rule

```text
Hard Constraint
>
Explicit User Preference
>
Strong Domain Prior
>
System Default
```

هیچ conflict نباید silently حل شود.

---

# 13. Conflict Resolver

اگر user چیزی بخواهد که با domain prior ناسازگار است:

```text
Do not reject automatically.
Do not silently override.
Synthesize compatible controlled variant.
Record conflict.
```

مثال:

```text
Healthcare
+
User wants Brutalist
=
Controlled Brutalist Healthcare
```

در decision_trace باید ثبت شود:

```json
{
  "conflict": "style_vs_domain_prior",
  "user_preference": "neobrutalist",
  "domain_prior": "calm_restrained",
  "resolution": "controlled_hybrid",
  "reason": "preserve explicit user preference while reducing readability/accessibility risk"
}
```

---

# 14. Decision Trace

هر design decision مهم باید traceable باشد.

حداقل:

```json
{
  "decision_id": "style-001",
  "decision_type": "style",
  "selected": "editorial",
  "score": 0.89,
  "confidence": 0.92,
  "alternatives": [],
  "evidence": [],
  "rules": [],
  "user_override": false,
  "conflicts": []
}
```

Decision trace باید debugging، critic و benchmark را تغذیه کند.

---

# 15. Design Genome

Genome باید composable باشد.

حداقل dimensions:

```text
Style
Mood
Domain
Audience
Product Mode
Brand Personality
Typography
Color
Layout
Density
Radius
Depth
Motion
Texture
Iconography
Interaction
Content Tone
Platform
Accessibility
```

---

# 16. Style Representation

هر Style باید حداقل شامل این‌ها باشد:

```json
{
  "id": "quiet_luxury",
  "family": "Quiet Luxury",
  "traits": [],
  "geometry": {},
  "typography": {},
  "color_affinities": [],
  "layout_affinities": [],
  "density_support": [],
  "motion_profile": {},
  "interaction_profile": {},
  "best_for": [],
  "avoid_for": [],
  "a11y_risks": [],
  "performance_risks": [],
  "anti_patterns": []
}
```

---

# 17. Style Composition

Styleها باید قابل ترکیب باشند.

نمونه:

```text
Editorial
+
Quiet Luxury
+
Data Dense
```

ترکیب باید compatibility check داشته باشد.

هر ترکیب:

```text
compatible
partially-compatible
conflicting
```

علامت‌گذاری شود.

---

# 18. Style Acceptance Rule

Style جدید فقط در صورتی پذیرفته شود که حداقل یکی از این‌ها را معنی‌دار افزایش دهد:

```text
geometry diversity
layout diversity
typography diversity
density diversity
interaction diversity
motion diversity
content presentation diversity
```

صرف تغییر:

```text
color
shadow
radius
```

Style Family جدید محسوب نمی‌شود.

---

# 19. Style Universe

V3 باید از تعداد محدودی style شروع کند اما catalog نباید به همان تعداد محدود شود.

هدف اولیه:

```text
24–40 genuinely distinct style families
```

این عدد KPI نیست.

معیار اصلی:

```text
Design Space Coverage
```

---

# 20. Typography Intelligence

Typography Engine باید تصمیم بگیرد:

```text
display family
body family
mono family
Persian family
Latin family
scale
weight
line-height
tracking
fallback
```

Font pairing باید language-aware باشد.

---

# 21. Color Intelligence

Color Engine باید تولید کند:

```text
brand
surface
text
muted text
primary action
secondary action
success
warning
error
info
```

Palette باید:

```text
light
dark
contrast
semantic roles
```

را پشتیبانی کند.

---

# 22. Layout Intelligence

تصمیمات:

```text
grid
container
columns
alignment
spacing rhythm
whitespace
asymmetry
content hierarchy
responsive transformation
```

Responsive نباید فقط resize باشد.

---

# 23. State Intelligence

componentهای مهم باید این stateها را در نظر بگیرند:

```text
default
hover
focus
active
disabled
loading
success
error
empty
offline
permission
validation
streaming
```

State coverage باید بخشی از Critic و Verification باشد.

---

# 24. Interaction Intelligence

Patterns شامل:

```text
navigation
menus
tabs
dialogs
drawers
forms
search
filters
tables
pagination
multi-step flows
notifications
toasts
```

باید متناسب با Product Mode انتخاب شوند.

---

# 25. Responsive Intelligence

حداقل target:

```text
320
375
768
1024
1440
```

در صورت نیاز:

```text
mobile
tablet
desktop
wide
```

باید composition و information architecture را adapt کند.

---

# 26. Brand Intelligence

Referenceهای کاربر می‌توانند شامل:

```text
logo
brand colors
screenshots
existing UI
guidelines
fonts
copy examples
```

باشند.

سیستم باید:

```text
extract principles
preserve hard brand constraints
adapt soft characteristics
avoid cloning
```

---

# 27. Reference Analysis

Reference نباید مستقیماً clone شود.

Pipeline:

```text
Reference
→ Extract Design Principles
→ Classify
→ Map to Genome
→ Generate New Design
→ Compare at Principle Level
```

---

# 28. Design Director Output

Design Director باید:

```text
intent
confidence
ambiguity
candidate directions
selected direction
hard constraints
soft preferences
decision trace
```

را تولید کند.

---

# 29. Design Contract

پس از Recommendation، Contract نهایی شامل:

```text
intent
decision
genome
content rules
component strategy
responsive rules
accessibility requirements
performance requirements
verification requirements
```

باشد.

این Contract ورودی اصلی Generation است.

---

# 30. Design Critic

Critic باید مستقل از Generator باشد.

## Dimensions

```text
visual hierarchy
composition
spacing rhythm
typography
color hierarchy
distinctiveness
domain fit
brand coherence
state completeness
responsive integrity
interaction quality
accessibility
motion
performance
genericity / AI slop
```

---

# 31. Critic Scoring

هر dimension:

```text
0–100
```

شود.

Quality Score نهایی weighted و versioned باشد.

Quality score هرگز نباید جای Hard Gate را بگیرد.

---

# 32. Hard Gates

حداقل:

```text
Schema PASS
Build PASS
Critical Accessibility PASS
Keyboard Critical PASS
No Critical Overflow
Required RTL/LTR PASS
Required Motion Behavior PASS
```

اگر Hard Gate fail شود:

```text
FINAL = REJECT
```

حتی با Quality Score بالا.

---

# 33. Severity Taxonomy

```text
BLOCKER
CRITICAL
HIGH
MEDIUM
LOW
INFO
```

قواعد:

```text
BLOCKER / CRITICAL
→ reject

HIGH
→ refinement required when fixable

MEDIUM
→ refinement preferred

LOW / INFO
→ may be delivered with report
```

---

# 34. Critic Report

نمونه:

```json
{
  "hard_gates_pass": false,
  "quality_score": 82.4,
  "scorecard": {},
  "defects_ranked": [
    {
      "id": "DEF-001",
      "severity": "critical",
      "type": "accessibility",
      "message": "...",
      "evidence": {},
      "suggested_fix": {}
    }
  ]
}
```

---

# 35. Priority-Based Auto-Refinement

ترتیب:

```text
Critical Blockers
→ High-Impact Visual
→ Usability
→ Polish
```

Refinement باید surgical باشد.

ترجیح:

```text
targeted patch
>
full regeneration
```

مگر اینکه defect structural باشد.

---

# 36. Refinement Contract

هر patch باید داشته باشد:

```text
target
reason
expected_effect
patch
pre_score
post_score
regression_result
```

Patch بدون post-verification معتبر نیست.

---

# 37. Refinement Acceptance

بعد از هر patch:

```text
all previous hard gates must remain passing
AND
quality must not regress materially
```

قاعده پیش‌فرض:

```text
post_score >= pre_score
```

مگر اینکه patch یک blocker را حل کند و trade-off آن صریحاً ثبت شده باشد.

---

# 38. Bounded Refinement Loop

حداکثر:

```text
2 iterations
```

برای V3.

اگر defect غیرحیاتی باقی ماند:

```text
Deliver with technical note
```

اگر blocker باقی ماند:

```text
Reject
```

---

# 39. Verification Engine

Verification باید سه دسته evidence تولید کند:

```text
Static Evidence
Runtime Evidence
Visual Evidence
```

---

# 40. Schema Verification

از یک implementation استاندارد JSON Schema برای validation استفاده شود.

Validator اختصاصی فقط برای domain-specific invariants مجاز باشد.

Rule:

```text
Unknown / unsupported schema semantics
→ FAIL CLOSED
```

هیچ exceptionی نباید silently ignored شود.

---

# 41. Accessibility Verification

ترکیب:

```text
axe-core
+
Accessibility Tree
+
Keyboard E2E
+
Computed Styles
+
Project-specific invariants
```

موارد:

```text
accessible name
role
state
label
keyboard reachability
focus order
focus visibility
contrast
target size
reduced motion
heading hierarchy
dialog semantics
live regions
```

---

# 42. Contrast Verification

Contrast باید تا حد ممکن effective rendered foreground/background را اندازه‌گیری کند.

موارد زیر باید پوشش داده شوند:

```text
text
links
buttons
inputs
placeholder
icons
badges
focus states
hover states
disabled states
text on gradients/images
```

اگر صرفاً approximation استفاده شد، گزارش باید آن را approximation بنامد.

---

# 43. Mobile / Responsive Verification

در viewportهای target:

```text
scrollWidth <= clientWidth
```

و بررسی:

```text
clipping
overflow
touch targets
text wrapping
navigation integrity
layout collapse
```

---

# 44. Keyboard Verification

باید interaction واقعی را تست کند:

```text
Tab
Shift+Tab
Enter
Space
Escape
Arrow keys where applicable
```

و focus order واقعی بررسی شود.

`element.focus()` به‌تنهایی برای keyboard compliance کافی نیست.

---

# 45. Reduced Motion Verification

فقط matchMedia کافی نیست.

باید بررسی شود:

```text
animation duration reduced
transition behavior reduced
non-essential motion disabled
```

در صورت امکان از rendered behavior evidence استفاده شود.

---

# 46. Visual Regression

Visual test باید baseline داشته باشد.

حداقل matrix:

```text
320
375
768
1024
1440
```

در محصولات مهم:

```text
light
dark
RTL
LTR
```

معیار:

```text
pixel diff
layout diff
critical region diff
```

---

# 47. Performance Verification

حداقل:

```text
LCP
CLS
INP
Long Tasks
Layout Shifts
```

Static heuristics مثل blur count فقط secondary signals هستند.

---

# 48. Benchmark System

Benchmark باید از روز اول V3 وجود داشته باشد.

Dataset هدف اولیه:

```text
100–500 stratified prompts
```

تنوع:

```text
domains
product modes
prompt length
language
ambiguity
platform
brand constraints
style constraints
```

---

# 49. Baseline Evaluation

هر benchmark باید حداقل مقایسه کند:

```text
V2 / current baseline
vs
V3
```

معیارها:

```text
First-Pass Quality
Correction Count
Correction Tokens
Time to Accept
Human Preference
Accessibility
Visual Diversity
Domain Fit
```

---

# 50. User Effort KPI

KPIهای اصلی:

```text
Correction Count < 1.5
Correction Tokens < 150
First-Pass Quality >= 70%
CLS < 0.1
```

اهداف باید با benchmark baseline دوباره calibrate شوند.

---

# 51. Human Evaluation

بخشی از benchmark باید blind-reviewed شود.

ابعاد:

```text
visual quality
originality
domain fit
usability
brand coherence
professionalism
```

Automated score و human score باید با هم مقایسه شوند.

---

# 52. AI Slop / Genericity Evaluation

Anti-slop نباید فقط regex باشد.

ارزیابی باید ترکیبی باشد:

```text
forbidden patterns
layout diversity
typography diversity
visual hierarchy
style conformity
repetition detection
human review
```

هیچ heuristic واحدی نباید ادعای «non-generic» را اثبات کند.

---

# 53. Search Engine Contract

`search.py` باید:

```text
offline
bounded output
fast
deterministic
locale-aware
```

باشد.

هدف performance:

```text
P50 < 10ms
P95 < 20ms
```

نه یک hard single-point latency.

---

# 54. Search Normalization

حداقل:

```text
Persian ی/ک normalization
Arabic variants
Unicode normalization
case normalization
whitespace normalization
alias matching
```

Fallback نباید silent باشد.

---

# 55. Knowledge Base Invariants

```text
No raw emoji in data files
All colors valid
All domains have bilingual aliases
All IDs unique
No broken references
No circular compatibility references
All referenced styles/domains exist
```

---

# 56. Cross-Component Invariants

```text
INV-001
Explicit user hard constraints cannot be silently overridden.

INV-002
Critical accessibility failure rejects output.

INV-003
Every recommendation has score + confidence + reason.

INV-004
Every automatic refinement re-runs hard gates.

INV-005
Every major design decision has provenance.

INV-006
All runtimes consume canonical knowledge.

INV-007
Low-confidence inference cannot silently fallback.

INV-008
Package builds do not depend on example applications.

INV-009
Version metadata has one canonical source.

INV-010
Verification claims must correspond to executable evidence.

INV-011
No "100% WCAG verified" claim may be emitted from heuristic-only checks.

INV-012
Benchmark results must record evaluator version.
```

---

# 57. Error Handling

All components must distinguish:

```text
User Error
Validation Error
Inference Uncertainty
Knowledge Gap
Implementation Error
Verification Failure
Infrastructure Failure
```

Failure must never be silently converted to success.

---

# 58. Provenance

Every generated DesignDecision should carry:

```text
contract_version
knowledge_version
scoring_version
evaluator_version
prompt_id
decision_trace
```

این برای reproducibility ضروری است.

---

# 59. Versioning

یک release manifest canonical:

```json
{
  "release": "3.0.0",
  "schema": "1.0.0",
  "knowledge": "1.0.0",
  "cli": "3.0.0",
  "verifier": "3.0.0",
  "extension": "3.0.0"
}
```

تمام packageها باید از آن sync شوند.

CI باید version drift را fail کند.

---

# 60. Package Isolation

هر package باید dependencyهای build خود را داشته باشد.

ممنوع:

```text
package A
→ node_modules
→ example app B
```

هر package باید مستقل install/build/test شود.

---

# 61. CLI Safety

CLI باید:

```text
dry-run
force
backup
skip
diff
rollback
```

را در عملیات destructive پشتیبانی کند.

Default نباید فایل موجود را silently overwrite کند.

---

# 62. VS Code Architecture

VS Code extension باید از همان Design Intelligence / Verification core استفاده کند.

ممنوع:

```text
Extension heuristic
≠
Core evaluator
```

پیام «verified» فقط در صورت اجرای verifier واقعی مجاز است.

WebView باید:

```text
CSP
nonce-based scripts
minimal permissions
explicit event listeners
```

داشته باشد.

---

# 63. Installer / Supply Chain

Installer pipeline:

```text
Download
→ Verify checksum/signature
→ Extract temp
→ Validate manifest
→ Atomic install
→ Preserve previous version
→ Rollback on failure
```

---

# 64. Acceptance Test Contract

هر feature قبل از merge باید مشخص کند:

```text
Input
Procedure
Expected output
Evidence
Failure condition
```

هیچ acceptance criterion مبهمی مثل:

> «باید خوب کار کند»

مجاز نیست.

---

# 65. Phase Implementation Order

## Phase 1 — Foundation Hardening

- version source of truth
- package isolation
- schema standardization
- data validation
- CI hardening

## Phase 2 — Contracts

- Intent Contract
- Decision Contract
- Genome Contract
- Design Contract
- Critic Report
- Verification Report

## Phase 3 — Knowledge Base

- taxonomy
- domains
- styles
- typography
- palettes
- layouts
- density
- states
- interactions
- anti-patterns
- compatibility

## Phase 4 — Design Director

- inference
- confidence
- ambiguity
- VoI
- candidate generation

## Phase 5 — Recommendation Engine

- scoring
- priors
- conflict resolution
- decision trace

## Phase 6 — Design Genome

- composition
- constraints
- overrides
- compatibility

## Phase 7 — Generation Integration

- contract-driven generation
- component selection
- state coverage
- responsive strategy

## Phase 8 — Design Critic

- scorecard
- defects
- evidence
- severity

## Phase 9 — Auto Refinement

- priority queue
- surgical patch
- regression protection
- bounded loop

## Phase 10 — Verification 2.0

- schema
- accessibility
- keyboard
- responsive
- RTL
- motion

## Phase 11 — Visual + Performance

- visual regression
- screenshot baselines
- CWV
- performance budgets

## Phase 12 — Style Universe Expansion

- identify catalog gaps from benchmark
- add distinct style families
- validate diversity contribution

## Phase 13 — Benchmark + Human Evaluation

- 100–500 prompt suite
- V2 baseline
- human evaluation
- user-effort metrics

## Phase 14 — Unified Orchestrator

```text
Prompt
→ Director
→ Recommendation
→ Genome
→ Contract
→ Generate
→ Critic
→ Refine
→ Verify
→ Deliver
```

## Phase 15 — Developer Experience

- CLI
- VS Code
- reports
- debugging
- overrides

## Phase 16 — Security / Release

- signed artifacts
- provenance
- reproducible builds
- installer hardening
- rollback

## Phase 17 — Production Validation

- full benchmark
- regression suite
- independent audit
- KPI signoff

## Phase 18 — Continuous Design Intelligence

- feedback
- benchmark expansion
- knowledge updates
- scoring calibration
- taxonomy evolution

---

# 66. Definition of Done

V3 is not considered complete merely because all code exists.

V3 is Done only when:

## User

- simple prompt works
- expert override works
- max one high-value question in ambiguity flow
- decisions are understandable

## Intelligence

- inference works
- confidence works
- recommendation works
- decision trace works
- genome works
- conflict resolution works

## Generation

- Design Contract drives generation
- state coverage exists
- responsive strategy exists

## Critique

- critic is independent
- scorecard is repeatable
- defects have evidence/severity

## Refinement

- bounded
- priority-based
- regression protected

## Verification

- hard gates work
- runtime evidence exists
- visual regression exists
- performance checks exist

## Benchmark

- V3 beats baseline on the agreed KPI set
- first-pass target achieved
- user effort reduced
- human preference improves

---

# 67. Release Gate

Final V3 release requires:

```text
ALL HARD GATES PASS
+
BENCHMARK TARGETS PASS
+
NO CRITICAL OPEN DEFECTS
+
PACKAGE BUILDS PASS
+
INSTALLER VERIFIED
+
VERSION CONSISTENCY PASS
+
DOCUMENTATION CONSISTENT
```

---

# 68. What V3 Must Optimize For

Priority order:

```text
1. User Intent Fit
2. Usability
3. Accessibility
4. Domain Fit
5. Visual Quality
6. Distinctiveness
7. Performance
8. Novelty
```

Novelty must never damage the first items.

---

# 69. What V3 Must Not Become

V3 should not become:

```text
a larger prompt collection
a larger style list
a giant hardcoded if/else system
a heuristic-only accessibility checker
a regeneration loop
a single opaque score
a dependency-heavy monolith
```

---

# 70. Final Architectural Principle

> **Vibe UI must not ask the user to become a designer in order to use the system. It must understand the product, infer the design problem, recommend an appropriate visual language, compose a complete design system, generate the UI, critique its own output, repair the highest-impact problems, and provide evidence that the result satisfies the required quality gates.**

The ultimate loop is:

```text
USER INTENT
    ↓
DESIGN DIRECTOR
    ↓
INFERENCE + CONFIDENCE
    ↓
RECOMMENDATION
    ↓
DECISION TRACE
    ↓
DESIGN GENOME
    ↓
DESIGN CONTRACT
    ↓
GENERATION
    ↓
STYLE-AWARE CRITIC
    ↓
PRIORITY REFINEMENT
    ↓
VERIFICATION
    ↓
EVIDENCE
    ↓
DELIVERY
```

**Primary V3 success metric:**

> **A normal user should reach an attractive, distinctive, context-appropriate and verified UI with minimal correction prompts.**

Style count is a supporting metric, not the product goal.

---

# 71. Final Implementation Rule

اگر بین:

```text
کمتر feature
+
بیشتر reliability
```

و:

```text
بیشتر feature
+
کمتر reliability
```

انتخاب وجود داشت، V3 باید همیشه گزینه اول را انتخاب کند.

**Design Intelligence بدون Measurement قابل اعتماد نیست.  
Measurement بدون Decision Intelligence صرفاً linting است.  
Vibe UI V3 باید هر دو را یکپارچه کند.**

---

# 72. پیوست مهندسی: حل قطعی ۷ مجهول کلیدی و گره‌های فنی (Resolution of 7 Core Unknowns)

برای به صفر رساندن آزمون‌وخطا در حین اجرا، تمام مجهولات احتمالی شناسایی و با راهکار قطعی مهندسی بسته شدند:

### ۱. مجهول سازگاری با گذشته (Backward Compatibility)
* **گره:** آیا ارتقای اسکیما و معرفی سبک‌های جدید، باعث شکسته شدن بیلدها، تست‌های ریاضی قبلی یا اگزمپل‌های موجود می‌شود؟
* **پاسخ قطعی:** خیر. ارتقا به صورت **سازگار افزایشی (Additive Extension)** انجام می‌شود:
  - مقادیر ۵ سبک قبلی در اسکیما حفظ شده و مقادیر جدید به آن اضافه می‌شوند.
  - فیلدهای جدید (candidate_directions, style_genome, state_matrix) به صورت اختیاری (optional) تعریف می‌شوند تا تست‌های قبلی همچنان با کد خروج ۰ پاس شوند.

### ۲. پردازش زبان طبیعی و تطبیق دامین با مدل اطمینان (Bilingual NLP & No Silent Fallbacks)
* در 	axonomy.json برای هر دامین ده‌ها تگ و مترادف دوزبانه تعریف شده و حروف نرمالایز می‌شوند.
* **جلوگیری از خطای پنهان:** اگر ضریب اطمینان زیر ۰.۵۰ باشد، سیستم هرگز به صورت خاموش (Silently) به دامین دیگر تغییر جهت نمی‌دهد؛ بلکه با اعلام سطح اطمینان، پروتکل ۳ کاندیدا یا ۱ سوال باارزش (VoI) را فعال می‌کند. دامین عمومی صرفاً در صورتی استفاده می‌شود که کاربر صراحتاً بگوید: «تصمیم را به خودت می‌سپارم».

### ۳. لود پایدار فونت‌ها و جبران شیفت چیدمان (Font Metric Compensation & CLS Prevention)
* استفاده از فونت استاندارد **وزیرمتن (Vazirmatn)** از CDN جهانی Google Fonts.
* برای جلوگیری از پرش و شیفت لایه‌بندی در قطع اینترنت یا تاخیر لود (FOIT/FOUT)، فونت‌های پشتیبان سیستمی با ویژگی‌های جبران متریک فونت (ont-display: swap, size-adjust) تنظیم می‌شوند تا شاخص Cumulative Layout Shift همواره زیر ۰.۱ ( < 0.1$) باقی بماند.

### ۴. منتقد طراحی سبک‌آگاه (Style-Aware Critic)
* خط‌کش نقد برای هر سبک مجزاست؛ مثلاً سایه سخت مشکی در نئوبروتالیسم مجاز است، اما در سوئیسی خطا محسوب می‌شود.

### ۵. اشتراک داده بین پایتون، نود و اکستنشن (Single Source of Truth)
* داده‌ها در قالب فایل‌های JSON استاندارد در پوشه data/ ذخیره می‌شوند و مستقیماً توسط پایتون، تایپ‌اسکریپت، CLI و اکستنشن بدون تبدیل کدهای موازی خوانده می‌شوند.

### ۶. اصلاح خودکار اولویت‌بندی شده و مهار رگرسیون (Priority Refinement & Anti-Regression)
* سقف تکرار: حداکثر ۲ دور. هر پچ اصلاحی صرفاً روی بزرگ‌ترین نقص شناسایی‌شده (از صف اولویت: بحرانی ➔ ظاهر ➔ کاربردپذیری) متمرکز می‌شود.
* **تست ضد رگرسیون:** بعد از اعمال هر پچ، تمام گیت‌های سخت (Hard Gates) مجدداً ارزیابی می‌شوند تا اطمینان حاصل شود اصلاح یک نقص ظاهری، منجر به افت کنتراست یا خرابی کیبورد نشده است.

### ۷. پرامپت کوتاه در برابر بلند (Assisted vs. Expert Mode)
* کاربر عادی با پرامپت یک‌خطی ۳ مسیر ملموس دریافت می‌کند؛ کاربر حرفه‌ای با پرامپت تخصصی، تنظیمات خود را بدون مداخله دریافت می‌کند.
