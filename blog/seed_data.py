"""Seed content for the blog app.

Articles are original write-ups grounded in public industry trends and
guides (Django survey 2025, ORM performance, HTMX, FastAPI vs Django Ninja,
Tailwind v4 container queries)—not copied verbatim from third-party sites.
"""

CATEGORIES = [
    {
        "slug": "django",
        "name_en": "Django",
        "name_fa": "جنگو",
        "description_en": (
            "Practical notes on Django architecture, templates, and the "
            "broader ecosystem."
        ),
        "description_fa": (
            "نکات کاربردی درباره معماری جنگو، قالب‌ها و اکوسیستم گسترده‌تر آن."
        ),
    },
    {
        "slug": "performance",
        "name_en": "Performance",
        "name_fa": "کارایی",
        "description_en": (
            "Database queries, caching, and profiling patterns that keep "
            "Python web apps fast in production."
        ),
        "description_fa": (
            "الگوهای کوئری پایگاه‌داده، کش و پروفایلینگ برای سریع نگه داشتن "
            "اپلیکیشن‌های وب پایتون در محیط واقعی."
        ),
    },
    {
        "slug": "frontend",
        "name_en": "Frontend",
        "name_fa": "فرانت‌اند",
        "description_en": (
            "Server-friendly UI patterns, progressive enhancement, and "
            "modern CSS techniques."
        ),
        "description_fa": (
            "الگوهای رابط کاربری سازگار با سرور، بهبود تدریجی و تکنیک‌های "
            "مدرن CSS."
        ),
    },
    {
        "slug": "apis",
        "name_en": "APIs",
        "name_fa": "APIها",
        "description_en": (
            "Typed API design, OpenAPI, and choosing the right Python "
            "framework for your service."
        ),
        "description_fa": (
            "طراحی API تایپ‌شده، OpenAPI و انتخاب فریم‌ورک مناسب پایتون "
            "برای سرویس شما."
        ),
    },
    {
        "slug": "css-design",
        "name_en": "CSS & Design",
        "name_fa": "CSS و طراحی",
        "description_en": (
            "Layout systems, responsive components, and design tooling "
            "for product UIs."
        ),
        "description_fa": (
            "سیستم‌های چیدمان، کامپوننت‌های ریسپانسیو و ابزارهای طراحی "
            "برای رابط کاربری محصول."
        ),
    },
]

TAGS = [
    {"slug": "django", "name_en": "Django", "name_fa": "جنگو"},
    {"slug": "htmx", "name_en": "HTMX", "name_fa": "HTMX"},
    {"slug": "alpine-js", "name_en": "Alpine.js", "name_fa": "Alpine.js"},
    {"slug": "postgresql", "name_en": "PostgreSQL", "name_fa": "PostgreSQL"},
    {"slug": "orm", "name_en": "ORM", "name_fa": "ORM"},
    {"slug": "caching", "name_en": "Caching", "name_fa": "کش"},
    {"slug": "redis", "name_en": "Redis", "name_fa": "Redis"},
    {"slug": "fastapi", "name_en": "FastAPI", "name_fa": "FastAPI"},
    {"slug": "django-ninja", "name_en": "Django Ninja", "name_fa": "Django Ninja"},
    {"slug": "pydantic", "name_en": "Pydantic", "name_fa": "Pydantic"},
    {"slug": "openapi", "name_en": "OpenAPI", "name_fa": "OpenAPI"},
    {"slug": "tailwind", "name_en": "Tailwind CSS", "name_fa": "Tailwind CSS"},
    {"slug": "container-queries", "name_en": "Container Queries", "name_fa": "کوئری کانتینر"},
    {"slug": "css", "name_en": "CSS", "name_fa": "CSS"},
    {"slug": "python", "name_en": "Python", "name_fa": "پایتون"},
    {"slug": "templates", "name_en": "Templates", "name_fa": "قالب‌ها"},
    {"slug": "survey", "name_en": "Survey", "name_fa": "نظرسنجی"},
]

POSTS = [
    {
        "slug": "state-of-django-2025-what-the-survey-means",
        "category": "django",
        "tags": ["django", "htmx", "alpine-js", "survey", "python"],
        "is_featured": True,
        "author_name": "",
        "featured_image_url": (
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
            "?auto=format&fit=crop&w=1600&q=80"
        ),
        "featured_image_alt_en": "Laptop open on a desk during a coding session",
        "featured_image_alt_fa": "لپ‌تاپ باز روی میز در حین کدنویسی",
        "published_days_ago": 3,
        "title_en": "What the State of Django 2025 Survey Means for Your Stack",
        "title_fa": "نتایج نظرسنجی جنگو ۲۰۲۵ چه معنایی برای استک شما دارد",
        "excerpt_en": (
            "The latest Django Developers Survey (4,600+ respondents) shows "
            "HTMX and Alpine.js rising, strong type-hint adoption, and "
            "PostgreSQL still dominant. Here is how to act on those signals."
        ),
        "excerpt_fa": (
            "آخرین نظرسنجی توسعه‌دهندگان جنگو (بیش از ۴۶۰۰ پاسخ‌دهنده) رشد "
            "HTMX و Alpine.js، پذیرش بالای تایپ‌هینت و سلطه PostgreSQL را "
            "نشان می‌دهد. اینجا چگونه به این سیگنال‌ها عمل کنید."
        ),
        "seo_title_en": "State of Django 2025: Practical Takeaways",
        "seo_title_fa": "وضعیت جنگو ۲۰۲۵: نکات کاربردی",
        "seo_description_en": (
            "Key takeaways from the 2025 Django Developers Survey: HTMX "
            "growth, AI tooling, PostgreSQL, and what to try next."
        ),
        "seo_description_fa": (
            "نکات کلیدی نظرسنجی توسعه‌دهندگان جنگو ۲۰۲۵: رشد HTMX، ابزارهای "
            "هوش مصنوعی، PostgreSQL و گام‌های بعدی."
        ),
        "content_en": """\
# What the State of Django 2025 Survey Means for Your Stack

The annual Django Developers Survey—run by the Django Software Foundation
with JetBrains—now covers more than **4,600 developers**. It is one of the
few reliable windows into how Django is actually used in production. The
2025 results are not just interesting trivia; they suggest concrete bets
for teams shipping Python web apps this year.

## Hypermedia is back in the mainstream

React and jQuery still lead overall, but the direction of travel is clear:
**HTMX** climbed from about 5% in 2021 to roughly **24%** in 2025, while
**Alpine.js** moved from 3% to about **14%**. React and Vue usage edged
down over the same period.

That shift matches what many mid-size teams already feel: a full SPA is
often more frontend ops than product value. Server-rendered Django
templates plus small interactive islands (HTMX for request/response HTML
swaps, Alpine for local UI state) keep auth, validation, and business
rules in one place.

Django 6.0’s official **template partials** (born from `django-template-partials`)
make this path even smoother—you can refresh a table row or form fragment
without inventing a second frontend app.

**Try this week:** pick one “spinner + AJAX” feature in your app and rewrite
it with `hx-get` / `hx-target`. Measure bundle size and review complexity
before and after.

## Type hints are no longer optional culture

About **63%** of respondents already use type hints in Django code; another
**17%** plan to. Roughly **84%** want type hints in Django core. That is a
strong mandate for libraries, internal packages, and new services.

Practical baseline for a portfolio or product codebase:

- Annotate view return types and service-layer functions.
- Prefer `django-stubs` + mypy/pyright in CI.
- For APIs, lean on Pydantic-backed stacks (Django Ninja or FastAPI) so
  OpenAPI stays honest.

## PostgreSQL remains the default serious backend

**PostgreSQL (~76%)** still dominates, with SQLite common for local/dev
(and increasingly discussed for smaller production workloads). MongoDB’s
survey presence helped push an official Django MongoDB backend—an example
of how survey signal can shape ecosystem investment.

If you are still on MySQL “because it was there,” plan an evaluation of
Postgres features you are missing: JSONB, partial indexes, `EXPLAIN`
clarity, and connection pooling with PgBouncer.

## AI is already in the workflow—set boundaries

AI tools jumped into the learning mix (~38%, tied with YouTube). For Django
work, ChatGPT led usage, followed by Copilot and Claude. Top tasks:
autocomplete, generating code, and boilerplate.

Treat AI like a junior pair: great for scaffolding tests and migrations,
dangerous for silent security or ORM regressions. Keep a short project
rule file (allowed patterns, forbidden shortcuts) so agents stay aligned
with your stack.

## Actionable checklist

1. Prototype one HTMX-powered interaction instead of adding another React island.
2. Turn on type checking for new modules; do not wait for a big-bang rewrite.
3. Stay on a supported Django release (most respondents already run latest).
4. Prefer Postgres for anything that will outlive a side project.
5. Document how your team uses AI so code review standards stay explicit.

Django’s strength in 2025 is boring reliability plus a living ecosystem.
The survey says the community is experienced, production-focused, and
increasingly comfortable mixing classic templates with modern
interactivity. Build for that reality—not for last decade’s default SPA.
""",
        "content_fa": """\
# نتایج نظرسنجی جنگو ۲۰۲۵ چه معنایی برای استک شما دارد

نظرسنجی سالانه توسعه‌دهندگان جنگو—با همکاری بنیاد نرم‌افزار جنگو و
JetBrains—اکنون بیش از **۴۶۰۰ توسعه‌دهنده** را پوشش می‌دهد. این یکی از
معدود پنجره‌های قابل‌اعتماد به نحوه استفاده واقعی از جنگو در پروداکشن
است. نتایج ۲۰۲۵ فقط آمار جالب نیستند؛ برای تیم‌هایی که امسال اپلیکیشن وب
پایتون می‌سازند، جهت‌گیری‌های مشخصی پیشنهاد می‌کنند.

## هایپرمدیا دوباره به جریان اصلی برگشته است

هنوز React و jQuery در مجموع پیشتازند، اما مسیر حرکت روشن است: **HTMX**
از حدود ۵٪ در ۲۰۲۱ به نزدیک **۲۴٪** در ۲۰۲۵ رسیده و **Alpine.js** از ۳٪
به حدود **۱۴٪**. در همین بازه، استفاده از React و Vue کمی کاهش یافته است.

این جابه‌جایی با حس بسیاری از تیم‌های متوسط هم‌خوان است: یک SPA کامل اغلب
بیش از ارزش محصول، هزینه عملیاتی فرانت‌اند دارد. قالب‌های سرورساید جنگو
به‌همراه جزایر تعاملی کوچک (HTMX برای جابه‌جایی HTML و Alpine برای state
محلی) احراز هویت، اعتبارسنجی و منطق کسب‌وکار را در یک جا نگه می‌دارد.

پشتیبانی رسمی **template partials** در جنگو ۶.۰ (با ریشه در
`django-template-partials`) این مسیر را ساده‌تر می‌کند—می‌توانید یک ردیف
جدول یا قطعه فرم را بدون ساختن اپ فرانت‌اند دوم تازه کنید.

**این هفته امتحان کنید:** یک قابلیت «اسپینر + AJAX» را با `hx-get` /
`hx-target` بازنویسی کنید و اندازه باندل و پیچیدگی ریویو را قبل و بعد
اندازه بگیرید.

## تایپ‌هینت دیگر فرهنگ اختیاری نیست

حدود **۶۳٪** پاسخ‌دهندگان از قبل در کد جنگو تایپ‌هینت استفاده می‌کنند و
**۱۷٪** دیگر برنامه‌اش را دارند. نزدیک به **۸۴٪** خواستار تایپ‌هینت در
هسته جنگو هستند. این سیگنال قوی برای کتابخانه‌ها، پکیج‌های داخلی و
سرویس‌های جدید است.

پایه عملی برای یک پرتفوی یا محصول:

- نوع بازگشتی ویوها و توابع لایه سرویس را annotate کنید.
- در CI از `django-stubs` به‌همراه mypy/pyright استفاده کنید.
- برای APIها به استک‌های مبتنی بر Pydantic (Django Ninja یا FastAPI)
  تکیه کنید تا OpenAPI صادق بماند.

## PostgreSQL همچنان بک‌اند جدی پیش‌فرض است

**PostgreSQL (حدود ۷۶٪)** همچنان غالب است و SQLite برای توسعه محلی (و
به‌طور فزاینده برای workloadهای کوچک پروداکشن) رایج است. حضور MongoDB در
نظرسنجی به انتشار بک‌اند رسمی Django MongoDB کمک کرد—نمونه‌ای از اینکه
سیگنال نظرسنجی چگونه سرمایه‌گذاری اکوسیستم را شکل می‌دهد.

اگر هنوز روی MySQL هستید «چون از قبل بود»، ارزیابی کنید چه قابلیت‌های
Postgres را از دست می‌دهید: JSONB، ایندکس‌های جزئی، وضوح `EXPLAIN` و
connection pooling با PgBouncer.

## هوش مصنوعی از قبل در گردش‌کار است—مرز بگذارید

ابزارهای AI وارد منابع یادگیری شده‌اند (حدود ۳۸٪، هم‌سطح با YouTube). در
کار جنگو، ChatGPT پیشتاز بوده و بعد Copilot و Claude. وظایف اصلی:
autocomplete، تولید کد و boilerplate.

AI را مثل یک جونیور در نظر بگیرید: عالی برای اسکلت تست و migration، خطرناک
برای باگ‌های امنیتی یا رگرسیون خاموش ORM. یک فایل قوانین کوتاه پروژه
نگه دارید تا ایجنت‌ها با استک شما هم‌راستا بمانند.

## چک‌لیست عملی

1. به‌جای افزودن جزیره React دیگر، یک تعامل با HTMX نمونه‌سازی کنید.
2. برای ماژول‌های جدید type checking را روشن کنید؛ منتظر بازنویسی بزرگ نمانید.
3. روی نسخه پشتیبانی‌شده جنگو بمانید (اکثر پاسخ‌دهندگان همین کار را می‌کنند).
4. برای هر چیزی فراتر از یک سایدپروجکت، Postgres را ترجیح دهید.
5. نحوه استفاده تیم از AI را مستند کنید تا استاندارد ریویو شفاف بماند.

قدرت جنگو در ۲۰۲۵، قابلیت اطمینان خسته‌کننده به‌همراه اکوسیستم زنده است.
نظرسنجی می‌گوید جامعه باتجربه، محصول‌محور و راحت‌تر با ترکیب قالب‌های
کلاسیک و تعامل مدرن است. برای همین واقعیت بسازید—نه برای SPA پیش‌فرض دهه قبل.
""",
    },
    {
        "slug": "django-performance-n-plus-one-caching-indexes",
        "category": "performance",
        "tags": ["django", "orm", "postgresql", "caching", "redis", "python"],
        "is_featured": True,
        "author_name": "",
        "featured_image_url": (
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31"
            "?auto=format&fit=crop&w=1600&q=80"
        ),
        "featured_image_alt_en": "Server racks representing database and cache infrastructure",
        "featured_image_alt_fa": "رک‌های سرور نماد زیرساخت پایگاه‌داده و کش",
        "published_days_ago": 10,
        "title_en": "Django Performance in Practice: Kill N+1, Then Cache",
        "title_fa": "کارایی جنگو در عمل: اول N+1 را بکشید، بعد کش کنید",
        "excerpt_en": (
            "Most slow Django apps are slow because of the database. Fix "
            "N+1 queries, add the right indexes, then layer Redis—scale "
            "hardware last."
        ),
        "excerpt_fa": (
            "بیشتر اپ‌های کند جنگو به‌خاطر پایگاه‌داده کندند. اول کوئری‌های "
            "N+1 را درست کنید، ایندکس مناسب بگذارید، بعد Redis—سخت‌افزار را "
            "آخر مقیاس دهید."
        ),
        "seo_title_en": "Django Performance: N+1, Indexes, Caching",
        "seo_title_fa": "کارایی جنگو: N+1، ایندکس و کش",
        "seo_description_en": (
            "A practical order of operations for Django performance: "
            "select_related, prefetch_related, indexes, and Redis caching."
        ),
        "seo_description_fa": (
            "ترتیب عملی بهینه‌سازی جنگو: select_related، prefetch_related، "
            "ایندکس و کش Redis."
        ),
        "content_en": """\
# Django Performance in Practice: Kill N+1, Then Cache

When a Django site feels sluggish, teams often reach for more workers,
bigger Postgres instances, or a CDN. Those help—but the highest ROI fixes
almost always sit in the ORM layer. Production guides from 2025–2026 keep
repeating the same order of operations for a reason.

## 1. See the queries before you “optimize”

Install **django-debug-toolbar** locally and watch the SQL panel on list
pages. In staging, log slow queries or use `connection.queries` in a
throwaway management command. You cannot fix what you do not measure.

A useful heuristic: a simple page should stay in roughly **single-digit**
queries. Spikes usually mean N+1 or accidental queries inside loops or
template tags.

## 2. Fix N+1 with the right prefetch tool

- **`select_related`** — foreign keys / one-to-one (SQL `JOIN`).
- **`prefetch_related`** — reverse FK and many-to-many (separate query,
  then join in Python). For M2M, prefer prefetch over inventing giant
  joins that duplicate rows.

```python
posts = (
    Post.objects.filter(status="published")
    .select_related("category")
    .prefetch_related("tags")
)
```

Never call related managers inside a template loop without prefetching
first. That single habit removes most “mysterious” latency.

## 3. Fetch less data

Use `only()` / `defer()` when serializers or cards need a handful of
columns. Prefer `exists()` over `count()` when you only care about
presence. Batch writes with `bulk_create` / `bulk_update` instead of
saving in a loop.

## 4. Index what you filter and order by

If every list view filters on `status` and orders by `-published_at`,
that composite path belongs in an index. Use `EXPLAIN (ANALYZE, BUFFERS)`
on Postgres before and after. Partial indexes (for example only
`status='published'`) keep hot paths small.

Avoid indexing everything “just in case”—write amplification is real.

## 5. Cache after the query plan is clean

Caching a bad queryset only freezes waste. Once queries are tight:

- Cache expensive fragments or whole pages with Django’s cache framework.
- Put **Redis** in front for shared cache across workers.
- Invalidate deliberately (signal on save, short TTLs, or queryset-aware
  helpers). Blind `cache.clear()` is not a strategy.

Connection pooling (**PgBouncer** or Django’s newer pooling options)
matters when you open many short-lived connections under load—after you
stop issuing fifty queries per request.

## A realistic checklist

| Step | Action | Done when |
|------|--------|-----------|
| Profile | Debug toolbar / slow query log | Hot endpoints identified |
| ORM | `select_related` / `prefetch_related` | N+1 gone on list/detail |
| Shape | `only` / pagination | Payloads shrink |
| Indexes | Match filters & ordering | `EXPLAIN` looks healthy |
| Cache | Redis + targeted keys | Repeat traffic is cheap |
| Infra | Pooling / scale-out | Only if still needed |

Django performance in 2026 is rarely mysterious. Eliminate unnecessary
queries, index the paths you already query, cache the expensive leftovers,
and only then buy bigger boxes. That sequence still beats premature
microservices.
""",
        "content_fa": """\
# کارایی جنگو در عمل: اول N+1 را بکشید، بعد کش کنید

وقتی سایتی با جنگو کند به‌نظر می‌رسد، تیم‌ها اغلب سراغ worker بیشتر،
اینستنس بزرگ‌تر Postgres یا CDN می‌روند. این‌ها کمک می‌کنند—اما بیشترین
بازدهی تقریباً همیشه در لایه ORM است. راهنماهای پروداکشن ۲۰۲۵–۲۰۲۶ همین
ترتیب را تکرار می‌کنند، بی‌دلیل نیست.

## ۱. قبل از «بهینه‌سازی»، کوئری‌ها را ببینید

در محیط لوکال **django-debug-toolbar** را نصب کنید و پنل SQL صفحات لیست را
ببینید. در staging کوئری‌های کند را لاگ کنید یا با `connection.queries` در
یک management command موقت بررسی کنید. آنچه اندازه نمی‌گیرید، درست
نمی‌کنید.

یک قاعده سرانگشتی: صفحه ساده باید در حدود **تک‌رقمی** کوئری بماند. جهش‌ها
معمولاً یعنی N+1 یا کوئری تصادفی داخل حلقه یا تگ قالب.

## ۲. N+1 را با ابزار درست prefetch درست کنید

- **`select_related`** — کلید خارجی / one-to-one (همان `JOIN` در SQL).
- **`prefetch_related`** — FK معکوس و many-to-many (کوئری جدا، سپس join در
  پایتون). برای M2M، prefetch را به JOINهای غول‌پیکر با ردیف تکراری ترجیح دهید.

```python
posts = (
    Post.objects.filter(status="published")
    .select_related("category")
    .prefetch_related("tags")
)
```

هرگز بدون prefetch، related manager را داخل حلقه قالب صدا نزنید. همین عادت
بیشتر تأخیرهای «عجیب» را حذف می‌کند.

## ۳. داده کمتر بگیرید

وقتی کارت یا serializer فقط چند ستون می‌خواهد از `only()` / `defer()`
استفاده کنید. اگر فقط وجود مهم است، `exists()` را به `count()` ترجیح دهید.
نوشتن‌ها را با `bulk_create` / `bulk_update` دسته‌ای کنید، نه save در حلقه.

## ۴. روی چیزی که فیلتر و مرتب می‌کنید ایندکس بگذارید

اگر هر لیست روی `status` فیلتر و با `-published_at` مرتب می‌شود، آن مسیر
ترکیبی جای ایندکس است. قبل و بعد روی Postgres از
`EXPLAIN (ANALYZE, BUFFERS)` استفاده کنید. ایندکس جزئی (مثلاً فقط
`status='published'`) مسیرهای داغ را کوچک نگه می‌دارد.

از ایندکس‌کردن همه‌چیز «برای احتیاط» بپرهیزید—هزینه نوشتن واقعی است.

## ۵. بعد از تمیز شدن query plan، کش کنید

کش کردن یک queryset بد فقط اتلاف را منجمد می‌کند. وقتی کوئری‌ها جمع‌وجور شدند:

- فرگمنت‌ها یا کل صفحه را با cache framework جنگو کش کنید.
- برای کش مشترک بین workerها **Redis** بگذارید.
- invalidation را عمدی طراحی کنید (سیگنال روی save، TTL کوتاه، یا کمک‌یار
  آگاه به queryset). `cache.clear()` کور استراتژی نیست.

Connection pooling (**PgBouncer** یا گزینه‌های جدیدتر جنگو) وقتی زیر بار
اتصال‌های کوتاه زیاد باز می‌کنید مهم می‌شود—بعد از اینکه دیگر پنجاه کوئری
در هر درخواست نمی‌زنید.

## چک‌لیست واقع‌بینانه

| گام | اقدام | تمام وقتی که |
|-----|--------|--------------|
| پروفایل | Debug toolbar / لاگ کوئری کند | endpointهای داغ مشخص شوند |
| ORM | `select_related` / `prefetch_related` | N+1 در لیست/جزئیات برود |
| شکل داده | `only` / صفحه‌بندی | payloadها کوچک شوند |
| ایندکس | منطبق با فیلتر و ordering | `EXPLAIN` سالم به‌نظر برسد |
| کش | Redis + کلیدهای هدفمند | ترافیک تکراری ارزان شود |
| زیرساخت | pooling / scale-out | فقط اگر هنوز لازم بود |

کارایی جنگو در ۲۰۲۶ معمولاً مرموز نیست. کوئری‌های اضافی را حذف کنید،
مسیرهایی که همین حالا می‌پرسید را ایندکس کنید، باقی‌مانده گران را کش کنید،
و فقط بعد جعبه بزرگ‌تر بخرید. این ترتیب هنوز از microservice زودهنگام بهتر
است.
""",
    },
    {
        "slug": "django-htmx-interactive-uis-without-a-spa",
        "category": "frontend",
        "tags": ["django", "htmx", "templates", "alpine-js", "python"],
        "is_featured": False,
        "author_name": "",
        "featured_image_url": (
            "https://images.unsplash.com/photo-1460925895917-afdab827c52f"
            "?auto=format&fit=crop&w=1600&q=80"
        ),
        "featured_image_alt_en": "Analytics dashboard metaphor for interactive web UI",
        "featured_image_alt_fa": "نماد داشبورد برای رابط کاربری تعاملی وب",
        "published_days_ago": 18,
        "title_en": "Django + HTMX: Interactive UIs Without Building a SPA",
        "title_fa": "جنگو + HTMX: رابط تعاملی بدون ساختن SPA",
        "excerpt_en": (
            "HTMX lets Django templates fetch and swap HTML fragments with "
            "simple attributes. Keep validation on the server and ship "
            "snappy UX with almost no custom JavaScript."
        ),
        "excerpt_fa": (
            "HTMX به قالب‌های جنگو اجازه می‌دهد با attributeهای ساده قطعه "
            "HTML بگیرند و جابه‌جا کنند. اعتبارسنجی را روی سرور نگه دارید و "
            "با تقریباً بدون JS سفارشی، UX تند بسازید."
        ),
        "seo_title_en": "Django and HTMX: Server-Driven Interactivity",
        "seo_title_fa": "جنگو و HTMX: تعامل سرورمحور",
        "seo_description_en": (
            "How to wire HTMX into Django: CSRF headers, partial responses, "
            "django-htmx middleware, and when to add Alpine.js."
        ),
        "seo_description_fa": (
            "اتصال HTMX به جنگو: هدر CSRF، پاسخ‌های partial، میدلور "
            "django-htmx و زمان افزودن Alpine.js."
        ),
        "content_en": """\
# Django + HTMX: Interactive UIs Without Building a SPA

Modern users expect instant feedback: live search, inline validation,
modals, and infinite lists. For years the default answer was “spin up
React.” For many Django products, **HTMX** is a better fit—especially when
your domain logic already lives in forms, permissions, and the ORM.

## What HTMX actually does

HTMX (~14KB) extends HTML with attributes like `hx-get`, `hx-post`,
`hx-target`, and `hx-swap`. The browser issues an AJAX request; your Django
view returns an **HTML fragment**; HTMX swaps it into the page. No JSON
contract, no client-side router, no duplicate validation rules.

That is why the Django survey shows HTMX climbing so quickly: it restores
the hypermedia model Django was built for, with 2020s UX expectations.

## Minimal setup that works in production

1. Include HTMX (CDN or the vendored script from **`django-htmx`**).
2. Add `HtmxMiddleware` so views can branch on `request.htmx`.
3. Put the CSRF token on every HTMX request:

```html
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>
```

4. Prefer partial templates (or Django 6 template partials) for responses
   that only refresh one region of the page.

```python
def search(request):
    q = request.GET.get("q", "")
    results = Post.objects.filter(title__icontains=q)[:20]
    template = (
        "blog/partials/search_results.html"
        if request.htmx
        else "blog/search.html"
    )
    return render(request, template, {"results": results})
```

```html
<input
  type="search"
  name="q"
  hx-get="{% url 'blog:search' %}"
  hx-trigger="keyup changed delay:300ms"
  hx-target="#results"
  hx-swap="innerHTML"
/>
<div id="results"></div>
```

## Patterns that pay off immediately

- **Inline forms:** post a form with `hx-post`, return the row or error
  markup, swap the form region.
- **Delete with confirm:** `hx-confirm` + `hx-delete` keeps UX sharp without
  a modal library.
- **Optimistic polish:** pair HTMX with small CSS transitions on `hx-swap`.
- **Local state only:** use **Alpine.js** for tabs, dropdowns, and
  client-only toggles that never need the server.

## Guardrails

- Do not return a full `base.html` for HTMX requests—ship fragments.
- Keep authorization checks in the view; HTML swaps are still HTTP.
- For complex client graphs (canvas editors, offline-first apps), a SPA
  may still win. HTMX is not anti-JavaScript; it is anti-*unnecessary*
  JavaScript frameworks.

## Why this fits a portfolio stack

If your site already uses Django templates and Tailwind, HTMX lets you
demonstrate modern UX without maintaining a separate Node toolchain for
every interaction. Recruiters and clients see ship speed; you keep one
test suite and one deployment.

Start with search, pagination, or a comment form. Once those feel native,
you will rarely reach for a full SPA for content-driven products again.
""",
        "content_fa": """\
# جنگو + HTMX: رابط تعاملی بدون ساختن SPA

کاربران امروزی بازخورد فوری می‌خواهند: جستجوی زنده، اعتبارسنجی درجا، مودال
و لیست بی‌نهایت. سال‌ها پاسخ پیش‌فرض «React راه بینداز» بود. برای بسیاری از
محصولات جنگو، **HTMX** مناسب‌تر است—مخصوصاً وقتی منطق دامنه از قبل در فرم‌ها،
مجوزها و ORM زندگی می‌کند.

## HTMX واقعاً چه می‌کند

HTMX (حدود ۱۴KB) HTML را با attributeهایی مثل `hx-get`، `hx-post`،
`hx-target` و `hx-swap` گسترش می‌دهد. مرورگر درخواست AJAX می‌فرستد؛ ویوی
جنگو یک **قطعه HTML** برمی‌گرداند؛ HTMX آن را در صفحه جابه‌جا می‌کند. نه
قرارداد JSON، نه روتر کلاینت، نه قوانین اعتبارسنجی تکراری.

به همین دلیل در نظرسنجی جنگو، HTMX این‌قدر سریع بالا آمده: مدل هایپرمدیایی
که جنگو برایش ساخته شده را با انتظار UX دهه ۲۰۲۰ برمی‌گرداند.

## راه‌اندازی حداقلی که در پروداکشن کار می‌کند

1. HTMX را اضافه کنید (CDN یا اسکریپت همراه **`django-htmx`**).
2. `HtmxMiddleware` را بگذارید تا ویوها روی `request.htmx` شاخه بزنند.
3. توکن CSRF را روی همه درخواست‌های HTMX بگذارید:

```html
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>
```

4. برای پاسخ‌هایی که فقط یک ناحیه را تازه می‌کنند، قالب partial
   (یا template partials جنگو ۶) ترجیح دهید.

```python
def search(request):
    q = request.GET.get("q", "")
    results = Post.objects.filter(title__icontains=q)[:20]
    template = (
        "blog/partials/search_results.html"
        if request.htmx
        else "blog/search.html"
    )
    return render(request, template, {"results": results})
```

```html
<input
  type="search"
  name="q"
  hx-get="{% url 'blog:search' %}"
  hx-trigger="keyup changed delay:300ms"
  hx-target="#results"
  hx-swap="innerHTML"
/>
<div id="results"></div>
```

## الگوهایی که فوری جواب می‌دهند

- **فرم درجا:** فرم را با `hx-post` بفرستید، ردیف یا خطای markup را برگردانید
  و همان ناحیه را عوض کنید.
- **حذف با تأیید:** `hx-confirm` + `hx-delete` بدون کتابخانه مودال UX تیز می‌دهد.
- **پرداخت بصری:** HTMX را با transitionهای کوچک CSS روی `hx-swap` جفت کنید.
- **فقط state محلی:** برای تب، دراپ‌داون و toggleهایی که سرور لازم ندارند از
  **Alpine.js** استفاده کنید.

## خطوط قرمز

- برای درخواست HTMX کل `base.html` برنگردانید—fragment بفرستید.
- بررسی مجوز را در ویو نگه دارید؛ جابه‌جایی HTML همچنان HTTP است.
- برای گراف‌های پیچیده کلاینت (ویرایشگر canvas، آفلاین‌اول) ممکن است SPA هنوز
  ببرد. HTMX ضد جاوااسکریپت نیست؛ ضد فریم‌ورک‌های *غیرضروری* است.

## چرا با استک پرتفوی جور است

اگر سایتتان از قبل قالب جنگو و Tailwind دارد، HTMX اجازه می‌دهد UX مدرن را
بدون نگه‌داری زنجیره Node برای هر تعامل نشان دهید. کارفرما سرعت تحویل
می‌بیند؛ شما یک مجموعه تست و یک استقرار نگه می‌دارید.

با جستجو، صفحه‌بندی یا فرم نظر شروع کنید. وقتی طبیعی شدند، برای محصولات
محتوامحور به‌ندرت دوباره سراغ SPA کامل می‌روید.
""",
    },
    {
        "slug": "fastapi-vs-django-ninja-choosing-in-2026",
        "category": "apis",
        "tags": ["fastapi", "django-ninja", "pydantic", "openapi", "python", "django"],
        "is_featured": False,
        "author_name": "",
        "featured_image_url": (
            "https://images.unsplash.com/photo-1517694712202-14dd9538aa97"
            "?auto=format&fit=crop&w=1600&q=80"
        ),
        "featured_image_alt_en": "Laptop with code editor representing API development",
        "featured_image_alt_fa": "لپ‌تاپ با ادیتور کد نماد توسعه API",
        "published_days_ago": 25,
        "title_en": "FastAPI vs Django Ninja: How to Choose in 2026",
        "title_fa": "FastAPI در برابر Django Ninja: چگونه در ۲۰۲۶ انتخاب کنیم",
        "excerpt_en": (
            "Both frameworks give you Pydantic validation and OpenAPI for "
            "free. The real decision is whether Django is already your "
            "system of record."
        ),
        "excerpt_fa": (
            "هر دو فریم‌ورک اعتبارسنجی Pydantic و OpenAPI را رایگان می‌دهند. "
            "تصمیم واقعی این است که آیا جنگو از قبل سیستم ثبت شماست یا نه."
        ),
        "seo_title_en": "FastAPI vs Django Ninja (2026)",
        "seo_title_fa": "FastAPI در برابر Django Ninja (۲۰۲۶)",
        "seo_description_en": (
            "Compare FastAPI and Django Ninja on typing, OpenAPI, auth, and "
            "when each belongs in a Python architecture."
        ),
        "seo_description_fa": (
            "مقایسه FastAPI و Django Ninja از نظر typing، OpenAPI، احراز هویت "
            "و جایگاه هرکدام در معماری پایتون."
        ),
        "content_en": """\
# FastAPI vs Django Ninja: How to Choose in 2026

Python’s API story converged: **type hints + Pydantic (+ OpenAPI)** beat
hand-written serializers for most new services. FastAPI popularized that
style; **Django Ninja** brought it to teams that already live in Django.
Benchmark posts in 2025–2026 keep showing the same lesson—raw latency is
rarely the deciding factor. Architecture is.

## What they share

- Request/response models driven by Python types (Pydantic v2 era).
- Automatic OpenAPI docs (Swagger/ReDoc-style UIs).
- Dependency injection for auth, DB sessions, and settings.
- Comfortable async handlers for I/O-bound work.

If your bar is “typed JSON API with docs,” both clear it.

## Where they diverge

### FastAPI — greenfield services

Choose FastAPI when the service is API-first and you do not need Django’s
admin, ORM, or batteries. It shines for:

- AI/ML gateways and streaming responses
- Independent microservices with their own datastore
- Teams that want a small ASGI surface and a large FastAPI ecosystem

You will assemble auth, migrations, and admin-like tooling yourself (or
via other libraries). That flexibility is the point.

### Django Ninja — evolve an existing Django app

Choose Django Ninja when Postgres models, `contrib.auth`, the admin, and
Celery are already paid for. You add a typed API layer without a second
framework:

```python
from ninja import Schema, NinjaAPI

api = NinjaAPI()

class PostOut(Schema):
    title: str
    slug: str

@api.get("/posts/", response=list[PostOut])
def list_posts(request):
    return Post.objects.filter(status="published")
```

`ModelSchema` can map ORM fields carefully—explicit field lists beat
`fields = "__all__"` so you never leak password hashes or internal flags.

## Decision rule that holds up

| Situation | Prefer |
|-----------|--------|
| New standalone API / worker-facing service | FastAPI |
| Django monolith needs a modern `/api` | Django Ninja |
| Heavy admin + complex relational domain | Django Ninja |
| Ultra-thin edge service, max ecosystem examples | FastAPI |
| “Which is faster?” as the only question | Measure—usually a wash |

Litestar and others compete in the same typed-ASGI space; evaluate them
when you need stricter startup-time typing or specific plugin models. For
most portfolio and product teams, the fork above is enough.

## Shared best practices (either stack)

1. Separate **input** and **output** schemas (`UserCreate` vs `UserRead`).
2. Validate at the HTTP boundary; pass typed objects inward—do not
   re-Pydantic the same payload in every layer.
3. Generate clients or contract tests from OpenAPI so frontend drift hurts
   earlier.
4. Trace requests (OpenTelemetry) once you cross more than one service.

## Bottom line

Do not migrate off Django to “get” FastAPI ergonomics if Django Ninja
covers your routes. Do not drag Django into a tiny async worker just to
reuse a model. Pick the framework that matches the gravity of your
existing system—then invest in schemas, tests, and observability.
""",
        "content_fa": """\
# FastAPI در برابر Django Ninja: چگونه در ۲۰۲۶ انتخاب کنیم

داستان API در پایتون همگرا شده: **تایپ‌هینت + Pydantic (+ OpenAPI)** برای
بیشتر سرویس‌های جدید، serializerهای دستی را شکست می‌دهد. FastAPI این سبک را
فراگیر کرد؛ **Django Ninja** آن را برای تیم‌هایی آورد که از قبل در جنگو
زندگی می‌کنند. پست‌های بنچمارک ۲۰۲۵–۲۰۲۶ همان درس را تکرار می‌کنند—تأخیر خام
به‌ندرت عامل تصمیم است. معماری هست.

## چه چیزهایی مشترک‌اند

- مدل درخواست/پاسخ مبتنی بر تایپ‌های پایتون (عصر Pydantic v2).
- مستندات خودکار OpenAPI (UIهای شبیه Swagger/ReDoc).
- تزریق وابستگی برای auth، نشست DB و تنظیمات.
- هندلرهای async راحت برای کار I/O-bound.

اگر معیار شما «JSON API تایپ‌شده با مستند» است، هر دو قبول می‌شوند.

## کجا از هم جدا می‌شوند

### FastAPI — سرویس‌های از صفر

وقتی سرویس API-اول است و به ادمین، ORM یا باتری‌های جنگو نیاز ندارید،
FastAPI را انتخاب کنید. در این‌ها می‌درخشد:

- درگاه‌های AI/ML و پاسخ‌های استریم
- میکروسرویس‌های مستقل با datastore خود
- تیم‌هایی که سطح ASGI کوچک و اکوسیستم بزرگ FastAPI می‌خواهند

احراز هویت، migration و ابزار شبیه ادمین را خودتان (یا با کتابخانه‌های دیگر)
سرهم می‌کنید. همان انعطاف، نقطه قوت است.

### Django Ninja — تکامل اپ جنگوی موجود

وقتی مدل‌های Postgres، `contrib.auth`، ادمین و Celery از قبل پرداخت شده‌اند،
Django Ninja را انتخاب کنید. لایه API تایپ‌شده را بدون فریم‌ورک دوم اضافه
می‌کنید:

```python
from ninja import Schema, NinjaAPI

api = NinjaAPI()

class PostOut(Schema):
    title: str
    slug: str

@api.get("/posts/", response=list[PostOut])
def list_posts(request):
    return Post.objects.filter(status="published")
```

`ModelSchema` می‌تواند فیلدهای ORM را بادقت نگاشت کند—لیست صریح فیلدها بهتر
از `fields = "__all__"` است تا هرگز هش رمز یا فلگ داخلی لو نرود.

## قاعده تصمیمی که دوام می‌آورد

| وضعیت | ترجیح |
|-------|--------|
| API یا سرویس worker از صفر | FastAPI |
| مونولیت جنگو به `/api` مدرن نیاز دارد | Django Ninja |
| ادمین سنگین + دامنه رابطه‌ای پیچیده | Django Ninja |
| سرویس لبه خیلی نازک، حداکثر مثال اکوسیستم | FastAPI |
| تنها سؤال «کدام سریع‌تر است؟» | اندازه بگیرید—معمولاً نزدیک‌اند |

Litestar و دیگران در همان فضای ASGI تایپ‌شده رقابت می‌کنند؛ وقتی typing
سخت‌گیرانه‌تر در startup یا مدل پلاگین خاص می‌خواهید ارزیابی‌شان کنید. برای
بیشتر تیم‌های پرتفوی و محصول، دوشاخه بالا کافی است.

## بهترین‌عمل‌های مشترک (هر کدام)

1. اسکیمای **ورودی** و **خروجی** را جدا کنید (`UserCreate` در برابر `UserRead`).
2. فقط در مرز HTTP اعتبارسنجی کنید؛ اشیای تایپ‌شده را به داخل بفرستید—همان
   payload را در هر لایه دوباره از Pydantic نگذرانید.
3. کلاینت یا تست قرارداد را از OpenAPI بسازید تا انحراف فرانت زودتر درد بگیرد.
4. وقتی از یک سرویس بیشتر شدید، درخواست‌ها را (OpenTelemetry) ردیابی کنید.

## جمع‌بندی

اگر Django Ninja مسیرهایتان را پوشش می‌دهد، برای «به‌دست آوردن» ارگونومی
FastAPI از جنگو مهاجرت نکنید. جنگو را فقط برای reuse یک مدل به worker کوچک
async نکشانید. فریم‌ورکی را انتخاب کنید که با جاذبه سیستم موجودتان جور
باشد—بعد روی اسکیما، تست و مشاهده‌پذیری سرمایه‌گذاری کنید.
""",
    },
    {
        "slug": "tailwind-v4-container-queries-reusable-components",
        "category": "css-design",
        "tags": ["tailwind", "container-queries", "css"],
        "is_featured": True,
        "author_name": "",
        "featured_image_url": (
            "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8"
            "?auto=format&fit=crop&w=1600&q=80"
        ),
        "featured_image_alt_en": "Design workspace with layouts on screen",
        "featured_image_alt_fa": "فضای کار طراحی با چیدمان روی صفحه",
        "published_days_ago": 32,
        "title_en": "Tailwind CSS v4 Container Queries for Components That Travel",
        "title_fa": "کوئری کانتینر در Tailwind CSS v4 برای کامپوننت‌های قابل‌حمل",
        "excerpt_en": (
            "Viewport breakpoints layout the page. Container queries let a "
            "card adapt to its slot. Tailwind v4 makes that first-class—"
            "here is the mental model."
        ),
        "excerpt_fa": (
            "بریک‌پوینت‌های viewport صفحه را می‌چینند. کوئری کانتینر اجازه "
            "می‌دهد کارت با جایگاهی که در آن نشسته سازگار شود. Tailwind v4 "
            "این را درجه یک کرده—این مدل ذهنی است."
        ),
        "seo_title_en": "Tailwind v4 Container Queries Guide",
        "seo_title_fa": "راهنمای کوئری کانتینر Tailwind v4",
        "seo_description_en": (
            "Learn when to use @container vs md: breakpoints in Tailwind "
            "CSS v4 for reusable, slot-aware components."
        ),
        "seo_description_fa": (
            "یاد بگیرید چه زمانی در Tailwind CSS v4 از @container در برابر "
            "بریک‌پوینت‌های md: برای کامپوننت‌های قابل‌استفاده مجدد استفاده کنید."
        ),
        "content_en": """\
# Tailwind CSS v4 Container Queries for Components That Travel

For a decade, responsive design mostly meant *viewport* media queries. That
works for headers and page grids. It fails for reusable components: the same
card in a wide main column and a narrow sidebar should not both wait for
`lg:` on the window.

**CSS container queries** fix that. An element styles itself based on the
size of a parent container. Tailwind CSS v4 brings this into core—no
`@tailwindcss/container-queries` plugin required.

## The two-layer mental model

| Layer | Tool | Question it answers |
|-------|------|---------------------|
| Page chrome | `sm:` `md:` `lg:` | How should the *layout shell* change with the device? |
| Component guts | `@sm:` `@md:` `@lg:` | How should *this widget* change with its slot width? |

Nav collapse, sidebar visibility, and multi-column page grids stay on
viewport variants. Card internals, comment widgets, and pricing tiles move
to container variants so they remain portable.

## Minimal pattern

```html
<article class="@container">
  <div class="flex flex-col gap-4 @md:flex-row @md:items-center">
    <img class="w-full @md:w-40" src="..." alt="" />
    <div>
      <h3 class="text-lg @md:text-xl">Title</h3>
      <p class="text-sm @lg:text-base">Summary…</p>
    </div>
  </div>
</article>
```

Mark a parent with `@container`, then swap `md:` for `@md:` on children.
Remember: container breakpoint scales differ from viewport scales
(`@md` is typically narrower than `md`). Tune via `@theme` if your design
tokens demand it.

## Nested layouts: name the container

When containers nest, query a specific ancestor:

```html
<div class="@container/main">
  <aside class="@container/sidebar">
    <div class="@md/sidebar:block @md/main:hidden">…</div>
  </aside>
</div>
```

## Gotchas that waste afternoons

1. **Unsized parents.** A flex child without a real width may report 0 for
   container queries. Ensure the container establishes inline size.
2. **Hiding the container.** `display: none` on the `@container` itself
   collapses measured width—hide an outer wrapper instead.
3. **Mixing layers carelessly.** Do not “fallback” `@md:` with `md:` on the
   same property unless you intentionally want both page and slot rules.

## Why this matters for Django + Tailwind sites

Server-rendered partials (and HTMX swaps) drop the same component into
different regions. With container queries, the browser re-resolves styles
when the slot changes—no prop-drilled `size="compact"` variants, no
Alpine watchers for width.

Ship page structure with classic breakpoints. Teach components to respect
their container. That split is the durable responsive architecture Tailwind
v4 finally makes convenient.
""",
        "content_fa": """\
# کوئری کانتینر در Tailwind CSS v4 برای کامپوننت‌های قابل‌حمل

یک دهه طراحی ریسپانسیو عمدتاً یعنی media query روی *viewport*. برای هدر و
گرید صفحه خوب کار می‌کند. برای کامپوننت قابل‌استفاده مجدد شکست می‌خورد: همان
کارت در ستون پهن اصلی و سایدبار باریک نباید هر دو منتظر `lg:` روی پنجره
بمانند.

**کوئری کانتینر CSS** این را درست می‌کند. یک عنصر بر اساس اندازه والد خود
استایل می‌گیرد. Tailwind CSS v4 این را به هسته آورده—دیگر به پلاگین
`@tailwindcss/container-queries` نیاز نیست.

## مدل ذهنی دولایه

| لایه | ابزار | سؤالی که جواب می‌دهد |
|------|--------|----------------------|
| پوسته صفحه | `sm:` `md:` `lg:` | *پوسته چیدمان* با دستگاه چگونه عوض شود؟ |
| درون کامپوننت | `@sm:` `@md:` `@lg:` | *این ویجت* با عرض جایگاه چگونه عوض شود؟ |

جمع‌شدن ناوبری، نمایش سایدبار و گرید چندستونه صفحه روی variantهای viewport
می‌مانند. درون کارت، ویجت نظر و کاشی قیمت به variantهای کانتینر می‌روند تا
قابل‌حمل بمانند.

## الگوی حداقلی

```html
<article class="@container">
  <div class="flex flex-col gap-4 @md:flex-row @md:items-center">
    <img class="w-full @md:w-40" src="..." alt="" />
    <div>
      <h3 class="text-lg @md:text-xl">عنوان</h3>
      <p class="text-sm @lg:text-base">خلاصه…</p>
    </div>
  </div>
</article>
```

والد را با `@container` علامت بزنید، بعد روی فرزندان `md:` را با `@md:` عوض
کنید. یادتان باشد: مقیاس بریک‌پوینت کانتینر با viewport فرق دارد (`@md`
معمولاً باریک‌تر از `md` است). اگر توکن‌های طراحی‌تان لازم داشت، با `@theme`
تنظیم کنید.

## چیدمان تو در تو: کانتینر را نام‌گذاری کنید

وقتی کانتینرها تو در تو می‌شوند، جد مشخص را هدف بگیرید:

```html
<div class="@container/main">
  <aside class="@container/sidebar">
    <div class="@md/sidebar:block @md/main:hidden">…</div>
  </aside>
</div>
```

## تله‌هایی که بعدازظهرها را می‌سوزانند

1. **والد بدون اندازه.** فرزند flex بدون عرض واقعی ممکن است برای کوئری
   کانتینر ۰ گزارش دهد. مطمئن شوید کانتینر inline size می‌سازد.
2. **مخفی کردن خود کانتینر.** `display: none` روی `@container` عرض اندازه‌گیری
   را صفر می‌کند—به‌جایش یک wrapper بیرونی را مخفی کنید.
3. **مخلوط بی‌دقت لایه‌ها.** روی یک property، `@md:` را با `md:` «fallback»
   نکنید مگر عمداً هم قانون صفحه و هم جایگاه را می‌خواهید.

## چرا برای سایت‌های جنگو + Tailwind مهم است

partialهای سرورساید (و جابه‌جایی HTMX) همان کامپوننت را در ناحیه‌های مختلف
می‌نشانند. با کوئری کانتینر، وقتی جایگاه عوض می‌شود مرورگر استایل را دوباره
حل می‌کند—بدون propهای `size="compact"` و بدون watcherهای Alpine برای عرض.

ساختار صفحه را با بریک‌پوینت کلاسیک بفرستید. به کامپوننت‌ها یاد دهید به
کانتینرشان احترام بگذارند. این تفکیک، معماری ریسپانسیو پایدار است که
Tailwind v4 بالاخره راحت کرده است.
""",
    },
]
