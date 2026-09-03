<div align="center">

<img src="assets/icon.png" alt="Vibe UI Suite Logo" width="96" height="96" style="border-radius: 18px; margin-bottom: 12px;">

# اکوسیستم Vibe UI Suite

**مهندسی قراردادمحور فرانت‌اند، قیدهای دیزاین‌سیستم و موتور اعتبارسنجی ران‌تایم برای دستیاران کدنویسی هوش مصنوعی.**

[![CI Pipeline](https://github.com/omid-io/vibe-ui-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/omid-io/vibe-ui-skills/actions/workflows/ci.yml)
[![npm version](https://img.shields.io/npm/v/@omid-io/tokens.svg?color=cb3837&label=npm)](https://www.npmjs.com/package/@omid-io/tokens)
[![Open VSX](https://img.shields.io/badge/Open--VSX-omid--io.vibe--ui--vscode-purple.svg)](https://open-vsx.org/extension/omid-io/vibe-ui-vscode)
[![VS Code Marketplace](https://img.shields.io/badge/VS_Code_Marketplace-omid--io.vibe--ui--vscode-blue.svg)](https://marketplace.visualstudio.com/items?itemName=omid-io.vibe-ui-vscode)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG_2.2-AA_Mathematical-success.svg)](evals/)

<p align="center">
  <a href="README.md"><strong>English Documentation</strong></a> •
  <a href="ARCHITECTURE.md"><strong>مستندات معماری سیستم</strong></a> •
  <a href="docs/ENTERPRISE_ADAPTATION.md"><strong>راهنمای تطبیق سازمانی</strong></a> •
  <a href="https://omid-io.github.io/vibe-ui-skills/showcase/"><strong>شوکیس تعاملی زنده</strong></a>
</p>

</div>

---

مجموعه **Vibe UI Suite** چارچوبی ساختاریافته، ماشین‌فهم و قابل‌سنجش در اختیار ادیتورها و ایجنت‌های هوش مصنوعی (Cursor، Claude Code، Windsurf و Antigravity) قرار می‌دهد تا رابط‌های کاربری را با اصول واقعی مهندسی فرانت‌اند طراحی، پیاده‌سازی و اعتبارسنجی کنند.

به جای اتکا به پرامپت‌نویسی شکننده («یک داشبورد شیک و مدرن بساز»)، این سیستم یک پایپ‌لاین صریح مشابه کامپایلر ایجاد می‌کند:

```text
قصد و خواسته کاربر
    ↓
بسط نیت و خواسته (قرارداد فنی ۳۰ پارامتری)
    ↓
اسکیمای ماشین‌فهم (design-spec.v1.schema.json)
    ↓
انتخاب استایل دیزاین + رسیپی‌های کامپوننت
    ↓
پیاده‌سازی کد (Next.js 15 / React 19 / Tailwind OKLCH)
    ↓
ارزیابی استاتیک (اسکیما، ریاضیات کنتراست، تست‌های منفی)
    ↓
ارزیابی زنده در مرورگر (پلی‌رایت در ویوپورت موبایل ۳۷۵ پیکسل)
    ↓
خروجی تست‌شده یا گزارش دقیق خطاهای مهندسی
```

> **شفافیت روز نخست:** این پروژه هم‌اکنون در نسخه `v2.4.0` است و به صورت مداوم در حال تکامل می‌باشد. از نقدها، باگ‌ریپورت‌ها و مشارکت‌های مهندسان فرانت‌اند صمیمانه استقبال می‌کنیم.

---

## ⚡ راه‌اندازی سریع با خط فرمان CLI (پیشنهادی)

بدون نیاز به کپی دستی فایل‌ها یا نوشتن کانفیگ، پروژه‌تان را در چند ثانیه به قراردادهای Vibe UI مجهز کنید:

### ۱. راه‌اندازی قراردادهای محیط کار (`init`)

```bash
npx @omid-io/tokens init
```
این دستور تعاملی در ترمینال:
1. استایل بصری پروژه را انتخاب می‌کند (`Minimalist SaaS`، `Luxury Glass`، `Neobrutalism`، `Swiss Editorial`، `Stripe Crisp Light`).
2. قوانین ادیتور هوش مصنوعی مورد نظر شما را می‌سازد (`.cursorrules`، `CLAUDE.md`، `.windsurfrules`).
3. متغیرهای استاندارد OKLCH را در فایل `vibe-tokens.css` تولید می‌کند.

### ۲. تزریق کامپوننت‌های تست‌شده هوش مصنوعی (`add`)

```bash
# دراور تاشوی استدلال هوش مصنوعی با ترنزیشن گرید و پالس رادار
npx @omid-io/tokens add thinking-drawer

# هاد تله‌متری با ساختار ایزوله LTR برای نمایش لتنسی و توکن‌ها
npx @omid-io/tokens add telemetry-hud

# بج اعتبارسنجی ریاضیاتی کنتراست WCAG 2.2 AA / AAA
npx @omid-io/tokens add contrast-badge
```
کامپوننت‌ها مستقیماً داخل پوشه `components/vibe-ui/` پروژه شما تزریق می‌شوند.

### ۳. مشاهده فهرست کامپوننت‌ها (`list`)

```bash
npx @omid-io/tokens list
```

---

## 💻 افزونه ادیتورها (VS Code & Cursor)

افزونه رسمی Vibe UI مستقیماً در سایدبار ادیتور شما فعال است:

- **VS Code Marketplace:** [`omid-io.vibe-ui-vscode`](https://marketplace.visualstudio.com/items?itemName=omid-io.vibe-ui-vscode)
- **Open-VSX Registry:** [`omid-io.vibe-ui-vscode`](https://open-vsx.org/extension/omid-io/vibe-ui-vscode) (مخصوص Cursor، Windsurf، VSCodium)

### امکانات افزونه:
- **ماشین‌حساب زنده کنتراست WCAG 2.2:** محاسبه آنی و ریاضیاتی نسبت روشنایی ($L_1 / L_2$) با انتخاب رنگ و نمایش زنده وضعیت قبولی AA و AAA.
- **درج ۱-کلیک کامپوننت:** کلیک روی دکمه **Insert into Active Editor** برای نوشتن کد کامپوننت در موقعیت مکان‌نما.
- **دستور بررسی سریع فایل:** با فشردن `Ctrl+Shift+P` و اجرای `Vibe UI: Audit Active File Contrast`.

---

## 🏛️ معماری: پایپ‌لاین هماهنگی ۶ مهارت تخصصی

هماهنگی فرآیندها توسط ایجنت معمار ارشد فرانت‌اند (**`mr-ui-designer`**) انجام می‌شود که ۶ ساب‌اسکیل تخصصی را هدایت می‌کند:

| مهارت تخصصی | نقش و محدوده وظایف | تضمین کلیدی |
| :--- | :--- | :--- |
| **`autonomous-intent-expander`** | بسط پرامپت با بودجه ابهام‌زدایی کالیبره‌شده | پرهیز از حدس زدن الزامات کسب‌وکار و تبدیل به قرارداد ۳۰ پارامتری |
| **`visual-chemistry-engine`** | انتخاب سیستم زیبایی‌شناسی یکپارچه | ۵ استایل متمایز با قانون جلوگیری از شباهت به وبسایت‌های قبلی |
| **`ui-kit`** | کامپوننت‌ها و الگوهای تعاملی هوش مصنوعی | دراور پردازش فکر، چیپ ابزارها، هاد تله‌متری، الگوهای بنتو |
| **`vibe-physics-engine`** | فیزیک انیمیشن، رنگ‌های ادراکی و بودجه GPU | فضای رنگی OKLCH، منحنی اسپرینگ، سقف حداکثر ۳ لایه بلور |
| **`conversion-copy-engine`** | روایت ارزش و سناریوی شفاف محصول | متن‌های داده‌محور؛ ممنوعیت اکید نظرات ساختگی و فوریت فیک |
| **`ui-verifier`** | گیت‌های اعتبارسنجی کیفیت و دسترس‌پذیری | محاسبات استاتیک + تست زنده DOM در مرورگر پلی‌رایت |

---

## 🎨 ۵ استایل بصری و شیمی دیزاین

1. **Minimalist SaaS:** سادگی تک‌رنگ، بردرهای ظریف، تراکم اطلاعات بالا، تایپوگرافی کاربردی (`oklch(0.12 0.01 260)`).
2. **Luxury Obsidian / Glass 2.0:** سطوح تیره، هایلایت‌های فرنل، تاکیدهای طلایی ظریف، مدیریت بودجه بلور GPU (`oklch(0.08 0.02 270)`).
3. **Neobrutalism:** کارت‌های اشباع، سایه‌های سخت هندسی ۳ پیکسلی مشکی، بدون بلور، مرزهای صریح فیزیکی (`oklch(0.98 0.02 95)`).
4. **Swiss Editorial:** گرید نامتقارن، چیدمان متن‌محور الهام‌گرفته از مکتب بین‌المللی سوئیس (`oklch(0.97 0.005 80)`).
5. **Stripe Crisp Light:** دیزاین روشن داکیومنت‌های فنی، خطوط تفکیک میکرونی، سایه‌های محو (`oklch(0.99 0.002 250)`).

---

## 🌐 اصل راست‌چین‌سازی معنادار با ساختار ثابت (Semantic RTL)

رابط‌های کاربری تولیدشده توسط هوش مصنوعی معمولاً با اعمال ناشیانه `dir="rtl"` دچار به‌هم‌ریختگی چیدمان، معکوس شدن منوهای ناوبری و وارونگی چارت‌ها می‌شوند.

قانون قطعی Vibe UI:
- **پایداری ساختار کلان:** ستون‌ها، سایدبار، نوبار و محور چارت‌ها ۱۰۰٪ ثابت و بدون جهش فیزیکی باقی می‌مانند.
- **RTL صرفاً روی محتوا:** جهت راست‌به‌چپ فقط روی پاراگراف‌ها، متون و عناوین با ویژگی‌های منطقی CSS (`margin-inline-start`) اعمال می‌شود.
- **ایزولاسیون دوزبانه (BiDi):** کدهای فنی، دستورات ترمینال، تله‌متری و آدرس‌های URL با تگ `<bdi>` یا `dir="ltr"` محافظت می‌شوند.

---

## 🧪 موتور ارزیابی و تست‌های ران‌تایم

```bash
# ۱. اجرای آزمون‌های استاتیک و تست‌های منفی
python evals/run_evals.py

# ۲. خروجی ماشین‌فهم جهت پایپ‌لاین‌های CI
python evals/run_evals.py --json

# ۳. آزمون زنده در مرورگر واقعی با پلی‌رایت
python evals/run_evals.py --browser
```

### تفاوت آزمون‌های قطعی و تحلیلی:

| گیت کنترلی | ماهیت | روش ارزیابی | محدوده پوشش |
| :--- | :--- | :--- | :--- |
| **اعتبارسنجی اسکیما** | قطعی | اعتبارسنجی با Draft 2020-12 | تست ۳۰ پارامتر با `additionalProperties: false` |
| **رد تست‌های منفی** | قطعی | بررسی کد خروج ۱ در ترمینال | رد آنتروپی غیرمجاز، کهن‌الگوی نامعتبر، تاچ‌تارگت زیر ۲۴px |
| **کنتراست WCAG AA** | قطعی | فرمول $L = 0.2126 R' + 0.7152 G' + 0.0722 B'$ | تضمین کنتراست $\ge 4.5:1$ برای متن و $\ge 3.0:1$ برای عناوین |
| **سرریز در موبایل** | ران‌تایم | موتور Chromium با Playwright | اطمینان از عدم سرریز افقی (`scrollWidth <= clientWidth`) در ۳۷۵px |
| **المان‌های کلیک‌پذیر** | استاتیک | پیمایش درخت DOM | عدم وجود `<div onclick>` خام و الزام به استفاده از دکمه |
| **فوکوس کیبورد** | استاتیک | استخراج استایل‌ها | الزام به تعریف استایل‌های `:focus-visible` |
| **سقف بلور GPU** | تحلیلی | استخراج لایه‌ها | حداکثر ۳ لایه `backdrop-filter` فعال |

---

## 🛡️ آنچه Vibe UI هست — و آنچه نیست

### آنچه هست:
- یک سیستم کنترل کیفی، دیزاین‌سیستم و لینتر قراردادمحور برای ادیتورهای هوش مصنوعی.
- یک پایپ‌لاین DAG که قصد کاربر، قواعد دیزاین، کد کامپوننت و تست‌ها را تفکیک می‌کند.
- مجموعه‌ای از گیت‌های محاسباتی که کدهای دارای نقص بصری را ریجکت می‌کند.

### آنچه نیست:
- ادعایی مبنی بر اینکه کد هوش مصنوعی بدون نیاز به بررسی انسان ۱۰۰٪ بی‌نقص است.
- جایگزین تست‌های جامع اسکرین‌ریدر و دستیابی صوتی در دسترس‌پذیری.
- جایگزین دیزاین‌سیستم شرکتی؛ این ابزار با سند [`docs/ENTERPRISE_ADAPTATION.md`](docs/ENTERPRISE_ADAPTATION.md) به کامپوننت‌های داخلی سازمان شما متصل می‌شود.

---

## 🤝 مشارکت و جامعه متن‌باز

پروژه Vibe UI Suite تحت مجوز **MIT** منتشر شده است. ما مشتاقانه از پیشنهادات، ایشوها و مشارکت‌های شما استقبال می‌کنیم:

```bash
git clone https://github.com/omid-io/vibe-ui-skills.git
cd vibe-ui-skills
python evals/run_evals.py
```

توسعه‌دهنده: [امید ظفری](https://github.com/omid-io) • ثبت ایشو: [GitHub Issues](https://github.com/omid-io/vibe-ui-skills/issues)
