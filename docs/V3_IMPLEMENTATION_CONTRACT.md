# 📜 Vibe UI v3: Master Implementation Contract
## Technical Blueprint, Data Schemas, System Invariants & Component Contracts

> **هدف این سند:** ایجاد یک قرارداد فنی و مهندسی ۱۰۰٪ ضدابهام (Anti-Ambiguity Contract) که مشخصات معماری سند مادر را به اینترفیس‌ها، فرمت داده‌ها، ساختار ورودی/خروجی و شروط قبولی کدها در Codebase ترجمه می‌کند تا هر برنامه‌نویس یا ایجنتی بتواند بدون کوچک‌ترین نیاز به تفسیر شخصی یا آزمون‌وخطا، فازها را پیاده‌سازی کند.

---

## 🏛️ ۱. ساختار پکیج‌ها و پوشه‌های Codebase

```text
E:\programming\vibe-ui-skills/
├── data/                               # پایگاه دانش متمرکز (Single Source of Truth)
│   ├── taxonomy.json                  # ۲۴ دامین، تگ‌ها و مترادف‌های دوزبانه
│   ├── styles.json                    # ۱۲ سبک لنگری استاندارد V3
│   ├── priors.json                    # اولویت‌های طراحی هر دامین (Design Priors)
│   ├── typography.json                # جفت‌های فونت هماهنگ انگلیسی و فارسی
│   └── palettes.json                  # پالت‌های رنگی OKLCH با کنتراست تضمینی
├── scripts/
│   ├── search.py                      # موتور بازیابی سریع و کم‌مصرف توکن (CLI)
│   └── test_search.py                 # تست‌های تطبیق و اعتبارسنجی سرچ
├── schemas/
│   ├── intent-contract.v1.json        # اسکیمای خواست کاربر (Design Intent)
│   ├── decision-contract.v1.json      # اسکیمای تصمیم نهایی سیستم (Design Decision)
│   └── critic-report.v1.json          # اسکیمای گزارش ارزیابی منتقد طراحی
├── evals/
│   ├── run_evals.py                   # موتور ارزیابی فیزیکی ۲.۰ (Playwright + WCAG)
│   ├── design_critic.py               # منتقد طراحی سبک‌آگاه (Style-Aware Critic)
│   ├── benchmark/
│   │   ├── prompts_100_stratified.json # دیتاست ۱۰۰ سناریوی استاندارد A/B
│   │   └── run_benchmark.py           # ارزیابی خودکار و محاسبه User Effort
│   └── fixtures/                      # نمونه‌های تست منفی و مثبت
└── packages/
    ├── tokens/                        # پکیج npm توکن‌ها (@omid-io/tokens)
    └── vibe-ui-vscode/                # افزونه VS Code
```

---

## 🧩 ۲. قراردادهای فنی مؤلفه‌های سیستم (Component Contracts)

---

### مؤلفه ۱: پایگاه دانش داده‌ها (Knowledge Base Data Store)
* **هدف:** ایجاد دیتابیس لوکال بدون وابستگی به شبکه برای تمام پلتفرم‌ها (پایتون، نود، اکستنشن).
* **مسیر فایل‌ها:** `data/taxonomy.json`, `data/styles.json`, `data/priors.json`, `data/typography.json`, `data/palettes.json`
* **فرمت داده‌ها (Persistence):** JSON معتبر UTF-8 بدون بمب توکنی (فایل‌های مینیفای‌نشده و ساختاریافته).

#### اسکیمای `data/taxonomy.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "domains": [
    {
      "id": "beauty_clinical_wellness",
      "name_en": "Beauty, Dermatology & Clinical Wellness",
      "name_fa": "زیبایی، پوست و سلامت بالینی",
      "aliases": ["کلینیک", "پوست", "زیبایی", "لیزر", "dermatology", "aesthetic", "spa", "cosmetics"],
      "primary_mode": "persuade",
      "default_trust_level": "very_high",
      "visual_energy": "calm_restrained",
      "recommended_styles": ["quiet_luxury", "soft_humanist", "minimal_swiss"],
      "forbidden_styles": ["neobrutalism", "harsh_terminal", "acid_green"]
    }
  ]
}
```

#### اسکیمای `data/styles.json`:
```json
{
  "styles": [
    {
      "id": "quiet_luxury",
      "family": "Quiet Luxury",
      "name_fa": "مجلل آرام و متین",
      "geometry": { "radius": "8px", "border_width": "1px", "border_opacity": 0.15 },
      "typography": { "display_category": "serif", "body_category": "sans" },
      "elevation": "diffused_soft",
      "backdrop_blur_limit": 2,
      "density_support": ["airy", "balanced"],
      "tailwind_signatures": ["font-serif", "border-stone-200", "bg-stone-50", "tracking-wide"]
    }
  ]
}
```

* **قوانین تخطی‌ناپذیر (Invariants):**
  1. هیچ فایلی در `data/` نباید ایموجی خام داشته باشد.
  2. تمام کدهای رنگی باید در فضای استاندارد OKLCH یا Hex معتبر همراه با معادل OKLCH ثبت شوند.
  3. تمام دامین‌ها باید دارای آرایه `aliases` با حداقل ۵ کلیدواژه فارسی و ۵ کلیدواژه انگلیسی باشند.

---

### مؤلفه ۲: موتور بازیابی سریع و صفر-توکن (`scripts/search.py`)
* **هدف:** کوئری گرفتن از دیتابیس لوکال بدون مصرف توکن کانتکست و تحویل سریع خلاصه طراحی (Design Brief).
* **ورودی (Input):**
  * `query` (رشته متنی پرامپت کاربر، مثلاً "سایت کلینیک پوست")
  * `--mode` (اختیاری: `persuade`, `operate`, `read`, `experience`)
  * `--style` (اختیاری: برای حالت Expert Mode)
* **خروجی (Output Interface):** JSON ساختاریافته (Design Brief) در کمتر از ۱۰ میلی‌ثانیه:
```json
{
  "query": "کلینیک پوست",
  "matched_domain": "beauty_clinical_wellness",
  "confidence": 0.94,
  "product_mode": "persuade",
  "priors": { "trust": "very_high", "energy": "calm_restrained" },
  "top_candidates": [
    { "style": "quiet_luxury", "score": 92.4, "reason": "High trust + calm luxury fit" },
    { "style": "soft_humanist", "score": 84.0, "reason": "Friendly clinical warmth" }
  ],
  "typography_pairing": { "display": "Playfair Display", "body": "Inter", "persian": "Vazirmatn" },
  "palette_recommendation": "stone_clinical_gold"
}
```
* **شروط قبولی (Acceptance Criteria):**
  1. زمان اجرا زیر ۲۰ میلی‌ثانیه (`execution_time < 20ms`).
  2. بازگشت ضریب اطمینان عددی (`confidence` بین ۰.۰ تا ۱.۰).
  3. پشتیبانی کامل از ی و ک عربی و نرمال‌سازی خودکار متن فارسی.

---

### مؤلفه ۳: مدیر استراتژیک طراحی (Design Director)
* **ورودی (Inputs):** پرامپت متنی کاربر + رفرنس‌های اختیاری + پرفرنس‌های صریح.
* **خروجی (Output):** سند قرارداد مقصود کاربر (`DesignIntentContract`):
```json
{
  "product_domain": "beauty_clinical_wellness",
  "audience": "high_ticket_clients",
  "product_mode": "persuade",
  "confidence": 0.94,
  "ambiguity_status": "low_ambiguity",
  "selected_direction": "Editorial Premium & Calm Restraint",
  "hard_constraints": [
    "WCAG AA contrast >= 4.5:1",
    "bilingual RTL support",
    "zero horizontal overflow on 320px"
  ]
}
```
* **قانون آستانه اطمینان و تعامل (VoI Protocol):**
  * `confidence >= 0.80`: استنتاج کاملاً خودکار، صفر سوال اضافی.
  * `0.50 <= confidence < 0.80`: استنتاج خودکار همراه با پیام تایید ۱-خطی.
  * `confidence < 0.50`: عدم فال‌بک سایلنت؛ ارائه ۳ مسیر کاندید با زبان انسانی یا پرسیدن حداکثر ۱ سوال باارزش (VoI).

---

### مؤلفه ۴: موتور توصیه و حل تعارض (Recommendation & Conflict Resolver)
* **ورودی:** `DesignIntentContract` + داده‌های `data/`.
* **فرمول نمره‌دهی:**
  $$\text{Score}(S) = 0.25 \cdot \text{DomainFit} + 0.20 \cdot \text{AudienceFit} + 0.20 \cdot \text{ModeFit} + 0.15 \cdot \text{ToneFit} + 0.10 \cdot \text{PlatformFit} + 0.10 \cdot \text{A11yFit} - \text{Penalty}$$
* **منطق حل تعارض (Conflict Resolver):**
  ```text
  IF (User_Style_Preference in Domain.forbidden_styles) {
      Do not abort;
      Synthesize "Controlled Hybrid Style";
      Record conflict in decision_trace;
  }
  ```
* **خروجی:** قرارداد تصمیم نهایی طراحی (`DesignDecisionContract`) شامل آبجکت `decision_trace`.

---

### مؤلفه ۵: منتقد طراحی سبک‌آگاه (Style-Aware Design Critic)
* **ورودی:** کد خروجی (HTML / Next.js TSX / Tailwind DOM).
* **خروجی:** گزارش منتقد (`CriticReport`):
```json
{
  "hard_gates_pass": true,
  "hard_gate_failures": [],
  "quality_score": 86.5,
  "scorecard": {
    "visual_hierarchy": 14.0,
    "anti_slop_distinctiveness": 13.5,
    "domain_fit": 14.0,
    "usability": 9.0,
    "typography": 9.0,
    "responsive": 9.0,
    "state_completeness": 8.0,
    "brand_coherence": 5.0,
    "performance_budget": 5.0
  },
  "defects_ranked": [
    { "severity": "medium", "type": "state", "msg": "Missing loading skeleton on cards" }
  ]
}
```
* **شروط قبولی (Acceptance Gate):**
  $$\text{Accepted} = (\mathbf{HardGates} == \text{True}) \land (\text{QualityScore} \ge 80)$$

---

### مؤلفه ۶: حلقه اصلاح خودکار (Priority-Based Auto-Refinement)
* **ورودی:** لیست `defects_ranked` از منتقد طراحی.
* **رفتار:**
  1. پاپ کردن بالاترین عیب بر اساس صف اولویت:
     $$\text{Critical Blockers} \longrightarrow \text{High-Impact Visual} \longrightarrow \text{Usability} \longrightarrow \text{Polish}$$
  2. اعمال پچ جراحی موضعی (Surgical Patch) روی کامپوننت مربوطه بدون بازتولید کل فایل.
  3. سنجش مجدد تمام گیت‌های سخت (Anti-Regression Validation).
* **قید توقف (Bounded Loop):** حداکثر ۲ دور تکرار. در صورت عدم رفع عیب غیرحیاتی، خروجی با یادداشت فنی تحویل می‌شود.

---

### مؤلفه ۷: پلتفرم ارزیابی فیزیکی ۲.۰ (Verification Engine)
* **مسیر فایل:** `evals/run_evals.py`
* **آزمون‌های اجباری:**
  1. `WCAG 2.2 AA Contrast Math`: تفکیک رنگ با فرمول درخشندگی نسبی ($L_1 + 0.05) / (L_2 + 0.05) \ge 4.5$.
  2. `Mobile Viewport Matrix`: رندر فیزیکی در ابعاد ۳۲۰، ۳۷۵ و ۷۶۸ پیکسل با Playwright و اطمینان از `scrollWidth <= clientWidth`.
  3. `Zero Raw Emojis`: صفر درصد ایموجی متنی در TSX و HTML و الزام آیکون برداری SVG.
  4. `Focus-Visible Rings`: داشتن استایل فوکوس کیبورد.
  5. `Reduced-Motion Support`: پاسخ به کوئری مدیا در انیمیشن‌ها.

---

## 📊 ۳. شاخص‌های سنجش زحمت کاربر و بنچ‌مارک (Evaluation KPIs)

| شاخص | فرمول محاسبه | هدف V3 | مرجع اعتبارسنجی |
| :--- | :--- | :--- | :--- |
| **First-Pass Quality** | $\frac{\text{Passed on First Generation}}{\text{Total Generations}} \times 100$ | **$\ge 70\%$** | ۱۰۰ سناریوی استاندارد در `evals/benchmark/` |
| **User Correction Count** | میانگین دفعات پرامپت اصلاحی کاربر تا تحویل | **$< 1.5$ بار** | لاگ سشن‌های چت و آزمون A/B |
| **Correction Tokens** | مجموع توکن‌های پرامپت اصلاحی کاربر | **$< 150$ توکن** | مصرف توکن ایجنت |
| **Layout Shift (CLS)** | متریک ثبات بصری هنگام لود فونت و مدیا | **$< 0.1$** | خروجی ابزار تله‌متری Playwright |

---

## 🔒 ۴. قوانین قطعی سازگاری با گذشته (Backward Compatibility Invariants)

1. **سازگاری کدهای موجود:** تمام فایل‌های نمونه در `examples/` و استارترکیت Next.js در `examples/nextjs-starter/` باید پس از هر تغییر، بدون ارور بیلد شوند (`npm run build` و `python evals/run_evals.py` با کد خروج ۰).
2. **عدم حذف سبک‌های ۵گانه قبلی:** سبک‌های پنج‌گانه فعلی (`minimalist_saas`, `glassmorphic_luxury`, `neobrutalism`, `swiss_editorial`, `stripe_clean`) در اسکیمای جدید به عنوان زیرمجموعه سبک‌های لنگری معتبر باقی می‌مانند.
3. **عدم انحصار به وابستگی آنلاین:** عملکرد اصلی `search.py` و اعتبارسنجی‌ها باید کاملاً آفلاین و متکی به فایل‌های لوکال باشد.
