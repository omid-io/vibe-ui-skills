# 🧠 Vibe UI v3: Decision Engine Specification
## Confidence Thresholds, Multi-Factor Scoring, Conflict Resolution & Decision Trace

---

## ۱. مدل آستانه اطمینان و ارزش اطلاعات (Confidence & VoI Model)

به جای برخورد دوگانه (باینری) با پرامپت کاربر («مبهم یا غیرمبهم»)، سیستم برای هر بعد استنتاج یک ضریب اطمینان ($C \in [0.0, 1.0]$) محاسبه می‌کند:

$$\bar{C} = w_d C_{\text{domain}} + w_a C_{\text{audience}} + w_m C_{\text{mood}}$$

| آستانه اطمینان ($\bar{C}$) | رفتار سیستم (System Behavior) | تجربه کاربری (UX) |
| :--- | :--- | :--- |
| **بالا ($\bar{C} \ge 0.80$)** | **استنتاج ۱۰۰٪ خودکار (Full Autonomous)** | صفر سوال، صفر وقفه. سیستم مستقیماً وارد تولید می‌شود. |
| **متوسط ($0.50 \le \bar{C} < 0.80$)** | **استنتاج همراه با تایید ۱-خطی (Inference with Soft Confirmation)** | سیستم استنتاج می‌کند و یک اعلان ۱ خطی می‌دهد: *«سبک Quiet Luxury بر اساس تم پزشکی انتخاب شد؛ در صورت تمایل به تغییر بفرمایید.»* |
| **پایین ($\bar{C} < 0.50$)** | **پروتکل ارزش اطلاعات (Value of Information - VoI)** | پرسیدن حداکثر ۱ سوال باارزش یا ارائه **۳ مسیر کاندید با زبان انسانی و ملموس**. |

---

## ۲. فرمول نمره‌دهی چندعاملی موتور توصیه (Recommendation Scoring)

هر سبک کاندید بر اساس فرمول زیر نمره‌گذاری و وزن‌دهی می‌شود تا تصمیم کاملاً ریاضی و شفاف باشد:

$$\text{Score}(S) = \sum_{i} w_i \cdot \text{Fit}_i(S) - \sum_{j} \text{Penalty}_j(S)$$

### ضرایب انطباق (Fit Dimensions):
1. **Domain Fit ($w_1 = 0.25$):** میزان تناسب سبک با صنعت (مثلاً Data-Dense برای بورس = ۱.۰؛ برای کلینیک زیبایی = ۰.۱).
2. **Audience Fit ($w_2 = 0.20$):** سن، تحصیلات و نوع ارتباط مخاطب (عمومی، مهندس، ثروتمند).
3. **Product Mode Fit ($w_3 = 0.20$):** هدف تعامل (Persuade, Operate, Read, Experience).
4. **Tone & Personality Fit ($w_4 = 0.15$):** میزان هم‌خوانی لحن (جدی، دوستانه، ساختارشکن).
5. **Platform / Device Fit ($w_5 = 0.10$):** اولویت موبایل، تبلت یا دسکتاپ.
6. **Accessibility / Performance Headroom ($w_6 = 0.10$):** میزان ریسک کنتراست و بار پردازشی.

### جریمه‌ها (Penalties):
* جریمه ضد الگوها (Anti-pattern Penalty): کسر ۴۰ نمره در صورت استفاده از سبک نامناسب در دامین پرریسک (مثلاً نئوبروتالیسم برای بیمارستان).

---

## ۳. تفکیک قیدهای سخت از ترجیحات نرم و حل تعارض (Conflict Resolver)

یکی از شایع‌ترین سناریوها، تعارض بین سلیقه کاربر و محدودیت‌های صنعت است:
* **قید سخت (Hard Constraint):** خط قرمزهای غیرقابل‌مذاکره (مثلاً در امور مالی: خوانایی قطعی اعداد، کنتراست WCAG AA، صفر انیمیشن کندکننده).
* **ترجیح نرم (Soft Preference):** سلیقه دلخواه کاربر (مثلاً: «من عاشق سبک نئوبروتالیسم هستم»).

### الگوریتم حل تعارض (Conflict Resolution Matrix):
```text
IF (User_Preference CONFLICTS_WITH Domain_Hard_Constraint) {
    DO NOT outright reject;
    Synthesize a "Controlled Hybrid";
    Example: 
      User asks for "Brutalism" on a "Banking App"
      ➔ Resolved: "Controlled Swiss Brutalism" 
         (Sharp dark borders and high contrast, but retaining strict tabular fonts and zero decorative visual noise).
}
```

---

## ۴. ردپای تصمیمات طراحی (Design Decision Trace)

برای پایان دادن به حدس و گمان و فراهم کردن قابلیت دیباگ سریع، هر خروجی شامل یک آبجکت استاندارد `decision_trace` است که توضیح می‌دهد چرا هر المان انتخاب شده است:

```json
{
  "decision_trace": {
    "recommended_style": "quiet_luxury",
    "composite_score": 92.4,
    "scoring_breakdown": {
      "domain_fit": 0.95,
      "audience_fit": 0.90,
      "mode_fit": 0.92,
      "accessibility_headroom": 0.96
    },
    "rationale": [
      "High-trust clinical domain requires calm, non-sterile prestige.",
      "Target audience responds to high-contrast serif typography and warm stone tones.",
      "Mobile-first responsive cadence prioritized for booking funnels."
    ],
    "alternatives_considered": [
      { "style": "soft_humanist", "score": 84.2, "rejection_reason": "Slightly too informal for high-ticket clinical procedures" },
      { "style": "minimal_swiss", "score": 78.5, "rejection_reason": "Too cold/sterile for wellness & dermatology" }
    ]
  }
}
```

---

## ۵. پشتیبانی از هویت برند موجود و الهام از نمونه‌ها (Brand & Reference Ingestion)

1. **Brand-Aware Enhancement:**  
   اگر کاربر رنگ سازمانی، کد هگز، یا فایل لوگو ارائه داد:
   * رنگ‌های اصلی قفل می‌شوند (`locked_brand_palette`).
   * سیستم مقادیر OKLCH متناظر را تولید کرده و کنتراست پس‌زمینه و المان‌ها را بر اساس همان رنگ برند کالیبره می‌کند.
2. **Reference Principle Extraction:**  
   اگر کاربر گفت: «سبکی شبیه به Linear اما گرم‌تر می‌خواهم»:
   * اصول معماری Linear (بوردرهای ۱ پیکسلی، دارک عمیق، کنتراست لبه‌ای) استخراج می‌شود.
   * پالت رنگی با اضافه کردن تهینه‌های زیتونی/خاکی ملایم (Warm Shift) بازتولید می‌شود، بدون کپی‌کاری ناشیانه.
