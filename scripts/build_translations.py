#!/usr/bin/env python3
"""Generate and compile Django locale files without GNU gettext installed."""

from __future__ import annotations

import polib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_DIR = BASE_DIR / "locale"

HEADER = {
    "Project-Id-Version": "portfolio",
    "Report-Msgid-Bugs-To": "",
    "POT-Creation-Date": "2026-08-12 00:00+0000",
    "PO-Revision-Date": "2026-08-12 00:00+0000",
    "Last-Translator": "",
    "MIME-Version": "1.0",
    "Content-Type": "text/plain; charset=UTF-8",
    "Content-Transfer-Encoding": "8bit",
}

# msgid -> fa translation (None means use msgid as-is for en catalog)
TRANSLATIONS: dict[str, str | None] = {
    # Settings / language names
    "English": "انگلیسی",
    "Persian": "فارسی",
    # Navigation
    "Home": "خانه",
    "Projects": "پروژه‌ها",
    "Certificates": "گواهینامه‌ها",
    "Blog": "وبلاگ",
    "About": "درباره من",
    "Services": "خدمات",
    "Contact": "تماس",
    "All": "همه",
    "Featured": "ویژه",
    "Search": "جستجو",
    "Clear": "پاک کردن",
    "Present": "اکنون",
    "Author": "نویسنده",
    "Tags": "برچسب‌ها",
    "Close": "بستن",
    # Hero
    "Hello, I'm": "سلام، من",
    "Your Name": "نام شما",
    "Backend Developer": "توسعه‌دهنده بک‌اند",
    "Welcome to my portfolio. Please create your profile from the Django admin panel to customize this section.": (
        "به نمونه‌کار من خوش آمدید. لطفاً پروفایل خود را از پنل مدیریت جنگو ایجاد کنید تا این بخش را سفارشی کنید."
    ),
    "View Projects": "مشاهده پروژه‌ها",
    "Download CV": "دانلود رزومه",
    "Contact Me": "تماس با من",
    # 404
    "Page Not Found": "صفحه پیدا نشد",
    "Error 404": "خطای ۴۰۴",
    "Page not found": "صفحه پیدا نشد",
    "The page you were looking for could not be found.": (
        "صفحه‌ای که به دنبال آن بودید پیدا نشد."
    ),
    "This route doesn't exist — or it moved. Head home, or browse the projects instead.": (
        "این مسیر وجود ندارد — یا جابه‌جا شده است. به خانه برگردید یا پروژه‌ها را مرور کنید."
    ),
    "Back to Home": "بازگشت به خانه",

    # About
    "Introduction": "معرفی",
    "About Me": "درباره من",
    "A quick introduction about who I am and what I enjoy building.": (
        "معرفی کوتاهی از اینکه من کی هستم و چه چیزهایی دوست دارم بسازم."
    ),
    "I'm a passionate backend developer who enjoys building scalable web applications, REST APIs, and clean software architecture using modern technologies.": (
        "من یک توسعه‌دهنده بک‌اند پرانرژی هستم که از ساخت برنامه‌های وب مقیاس‌پذیر، REST API و معماری نرم‌افزار تمیز با فناوری‌های مدرن لذت می‌برم."
    ),
    "This section will automatically display your personal introduction after you create your profile in the Django admin panel.": (
        "این بخش پس از ایجاد پروفایل در پنل مدیریت جنگو، به‌طور خودکار معرفی شخصی شما را نمایش می‌دهد."
    ),
    "I enjoy designing scalable backend systems, building REST APIs, optimizing databases, and creating clean, maintainable software. My goal is to build applications that are fast, secure, and easy to maintain.": (
        "من از طراحی سیستم‌های بک‌اند مقیاس‌پذیر، ساخت REST API، بهینه‌سازی پایگاه داده و ایجاد نرم‌افزار تمیز و قابل نگهداری لذت می‌برم. هدف من ساخت برنامه‌هایی است که سریع، امن و آسان برای نگهداری باشند."
    ),
    "Years Experience": "سال تجربه",
    "Projects Delivered": "پروژه تحویل‌شده",
    "APIs Shipped": "API منتشرشده",
    "Client Focus": "تمرکز بر مشتری",
    "Learn More About Me": "بیشتر درباره من",
    "Learn more about my background, skills, and professional journey.": (
        "بیشتر درباره پیشینه، مهارت‌ها و مسیر حرفه‌ای من بدانید."
    ),
    "A closer look at who I am, what I build, and the path that brought me here.": (
        "نگاهی نزدیک‌تر به اینکه من کی هستم، چه می‌سازم و مسیری که مرا به اینجا رسانده."
    ),
    "Quick Facts": "اطلاعات سریع",
    "Add location, email, and phone in your profile to show them here.": (
        "برای نمایش در اینجا، موقعیت، ایمیل و تلفن را در پروفایل خود اضافه کنید."
    ),
    "Profile Photo": "عکس پروفایل",
    "Skills & Tools": "مهارت‌ها و ابزارها",
    "Technologies I use to design, build, and ship reliable software.": (
        "فناوری‌هایی که برای طراحی، ساخت و تحویل نرم‌افزار قابل اعتماد استفاده می‌کنم."
    ),
    "Experience Snapshot": "نگاهی به تجربه",
    "A condensed look at recent roles. Full timeline lives on the home page.": (
        "نگاهی فشرده به نقش‌های اخیر. خط زمانی کامل در صفحه اصلی است."
    ),
    "View Full Timeline": "مشاهده خط زمانی کامل",
    "Building scalable Django applications, REST APIs, and modern backend architectures with a focus on performance and maintainability.": (
        "ساخت برنامه‌های جنگو مقیاس‌پذیر، REST API و معماری‌های بک‌اند مدرن با تمرکز بر عملکرد و قابلیت نگهداری."
    ),
    "Developed APIs, optimized databases, integrated third-party services, and collaborated with frontend developers on production applications.": (
        "توسعه API، بهینه‌سازی پایگاه داده، یکپارچه‌سازی سرویس‌های شخص ثالث و همکاری با توسعه‌دهندگان فرانت‌اند در برنامه‌های تولیدی."
    ),
    # Projects
    "Selected Work": "کارهای منتخب",
    "Featured Projects": "پروژه‌های ویژه",
    "A selection of projects showcasing my experience in backend development, APIs, and modern web technologies.": (
        "مجموعه‌ای از پروژه‌ها که تجربه من در توسعه بک‌اند، API و فناوری‌های وب مدرن را نشان می‌دهد."
    ),
    "View All Projects": "مشاهده همه پروژه‌ها",
    "Portfolio": "نمونه‌کار",
    "A curated collection of applications, APIs, and experiments I've built with modern backend technologies.": (
        "مجموعه‌ای گزیده از برنامه‌ها، APIها و آزمایش‌هایی که با فناوری‌های بک‌اند مدرن ساخته‌ام."
    ),
    "Browse featured and completed projects spanning backend systems, APIs, and modern web applications.": (
        "مرور پروژه‌های ویژه و تکمیل‌شده در سیستم‌های بک‌اند، API و برنامه‌های وب مدرن."
    ),
    "No projects yet": "هنوز پروژه‌ای وجود ندارد",
    "No projects match this filter. Try another status or view all projects.": (
        "هیچ پروژه‌ای با این فیلتر مطابقت ندارد. وضعیت دیگری را امتحان کنید یا همه پروژه‌ها را ببینید."
    ),
    "Projects will appear here once they are added in the Django admin.": (
        "پس از افزودن در پنل مدیریت جنگو، پروژه‌ها در اینجا نمایش داده می‌شوند."
    ),
    "Overview": "نمای کلی",
    "Gallery": "گالری",
    "Project Screenshots": "تصاویر پروژه",
    "More Work": "کارهای بیشتر",
    "Related Projects": "پروژه‌های مرتبط",
    "Next Step": "گام بعدی",
    "Have a similar idea?": "ایده مشابهی دارید؟",
    "Let's talk about how we can build something reliable, scalable, and thoughtfully designed.": (
        "بیایید درباره ساخت چیزی قابل اعتماد، مقیاس‌پذیر و با طراحی دقیق صحبت کنیم."
    ),
    "Live Demo": "نمایش زنده",
    "Discuss a Similar Project": "گفتگو درباره پروژه مشابه",
    "Image preview": "پیش‌نمایش تصویر",
    # Tech stack
    "Capabilities": "توانمندی‌ها",
    "Tech Stack": "فناوری‌ها",
    "Technologies and tools I use to build scalable, secure, and modern web applications.": (
        "فناوری‌ها و ابزارهایی که برای ساخت برنامه‌های وب مقیاس‌پذیر، امن و مدرن استفاده می‌کنم."
    ),
    # Experience
    "Career": "مسیر شغلی",
    "Experience": "تجربه",
    "My professional journey and the milestones that have shaped my career.": (
        "مسیر حرفه‌ای من و نقاط عطفی که شکل‌دهنده مسیر شغلی‌ام بوده‌اند."
    ),
    # Services
    "What I Offer": "آنچه ارائه می‌دهم",
    "Helping businesses build reliable, scalable, and high-performance web applications.": (
        "کمک به کسب‌وکارها برای ساخت برنامه‌های وب قابل اعتماد، مقیاس‌پذیر و پرعملکرد."
    ),
    "Backend Development": "توسعه بک‌اند",
    "Designing secure, scalable, and maintainable backend systems using Django and modern development practices.": (
        "طراحی سیستم‌های بک‌اند امن، مقیاس‌پذیر و قابل نگهداری با جنگو و شیوه‌های توسعه مدرن."
    ),
    "REST API Development": "توسعه REST API",
    "Building fast, secure, and well-documented APIs for web applications, mobile apps, and third-party integrations.": (
        "ساخت APIهای سریع، امن و مستند برای برنامه‌های وب، موبایل و یکپارچه‌سازی با سرویس‌های شخص ثالث."
    ),
    "Database Design": "طراحی پایگاه داده",
    "Creating efficient database schemas, optimizing queries, and ensuring data integrity for long-term scalability.": (
        "ایجاد طرح‌های پایگاه داده کارآمد، بهینه‌سازی پرس‌وجوها و تضمین یکپارچگی داده برای مقیاس‌پذیری بلندمدت."
    ),
    "View All Services": "مشاهده همه خدمات",
    "Backend development, REST APIs, and database design services for reliable, scalable web applications.": (
        "خدمات توسعه بک‌اند، REST API و طراحی پایگاه داده برای برنامه‌های وب قابل اعتماد و مقیاس‌پذیر."
    ),
    "Process": "فرآیند",
    "How I Work": "نحوه کار من",
    "A clear, collaborative process from discovery to delivery.": (
        "فرآیندی شفاف و مشارکتی از کشف نیاز تا تحویل."
    ),
    "Discover": "کشف",
    "Understand goals, constraints, and success metrics for your product or API.": (
        "درک اهداف، محدودیت‌ها و معیارهای موفقیت برای محصول یا API شما."
    ),
    "Design": "طراحی",
    "Shape architecture, data models, and interfaces that stay maintainable as you grow.": (
        "شکل‌دهی معماری، مدل داده و رابط‌هایی که با رشد شما قابل نگهداری بمانند."
    ),
    "Build": "ساخت",
    "Implement with clean code, tests, and iterative feedback so quality stays high.": (
        "پیاده‌سازی با کد تمیز، تست و بازخورد تکراری تا کیفیت بالا بماند."
    ),
    "Deliver": "تحویل",
    "Ship, document, and hand over systems that are ready for production and future work.": (
        "تحویل، مستندسازی و واگذاری سیستم‌هایی که برای تولید و کارهای آینده آماده‌اند."
    ),
    "Ready to start?": "آماده شروع هستید؟",
    "Let's build something solid": "بیایید چیز محکمی بسازیم",
    "Tell me about your project and I'll help you choose the right approach for backend, APIs, or data.": (
        "درباره پروژه‌تان بگویید تا در انتخاب رویکرد مناسب برای بک‌اند، API یا داده کمکتان کنم."
    ),
    # Certificates
    "Credentials": "مدارک",
    "Verified credentials and courses that shaped my engineering craft.": (
        "مدارک و دوره‌های تأییدشده‌ای که مهندسی من را شکل داده‌اند."
    ),
    "View All Certificates": "مشاهده همه گواهینامه‌ها",
    "No certificates yet": "هنوز گواهینامه‌ای وجود ندارد",
    "Certificates will appear here once they are added in the Django admin.": (
        "پس از افزودن در پنل مدیریت جنگو، گواهینامه‌ها در اینجا نمایش داده می‌شوند."
    ),
    "View credential": "مشاهده مدرک",
    "View certificate": "مشاهده گواهینامه",
    "View certificate image": "مشاهده تصویر گواهینامه",
    "Copy credential ID": "کپی شناسه مدرک",
    "Credential ID copied": "شناسه مدرک کپی شد",
    # Blog
    "Writing": "نوشته‌ها",
    "Latest from the Blog": "تازه‌ترین مطالب وبلاگ",
    "Recent articles and notes on backend development, APIs, and building reliable systems.": (
        "مقالات و یادداشت‌های اخیر درباره توسعه بک‌اند، API و ساخت سیستم‌های قابل اعتماد."
    ),
    "View All Posts": "مشاهده همه مطالب",
    "Articles, notes, and write-ups on backend development, APIs, and building reliable systems.": (
        "مقالات، یادداشت‌ها و نوشته‌ها درباره توسعه بک‌اند، API و ساخت سیستم‌های قابل اعتماد."
    ),
    "Search posts": "جستجوی مطالب",
    "Highlights": "برجسته‌ها",
    "Featured Posts": "مطالب ویژه",
    "No posts yet": "هنوز مطلبی وجود ندارد",
    "No posts match your search. Try a different query.": (
        "هیچ مطلبی با جستجوی شما مطابقت ندارد. عبارت دیگری را امتحان کنید."
    ),
    "No published posts in this filter yet.": "هنوز مطلب منتشرشده‌ای در این فیلتر وجود ندارد.",
    "Posts will appear here once they are published in the Django admin.": (
        "پس از انتشار در پنل مدیریت جنگو، مطالب در اینجا نمایش داده می‌شوند."
    ),
    "RSS Feed": "فید RSS",
    "Blog RSS Feed": "فید RSS وبلاگ",
    "Breadcrumb": "مسیر صفحه",
    "Search articles…": "جستجوی مقالات…",
    "Read More": "ادامه مطلب",
    "This post is a draft and is only visible to staff.": (
        "این مطلب پیش‌نویس است و فقط برای کارکنان قابل مشاهده است."
    ),
    "Keep Reading": "ادامه مطالعه",
    "Related Posts": "مطالب مرتبط",
    "More Writing": "نوشته‌های بیشتر",
    "Explore the full blog": "کاوش در کل وبلاگ",
    "Browse more articles on backend systems, APIs, and building reliable products.": (
        "مقالات بیشتری درباره سیستم‌های بک‌اند، API و ساخت محصولات قابل اعتماد بخوانید."
    ),
    "All Posts": "همه مطالب",
    "Share": "اشتراک‌ گذاری",
    "Pass this post along on Telegram, WhatsApp, or copy the link.": (
        "این مطلب را در تلگرام، واتساپ به اشتراک بگذارید یا لینک را کپی کنید."
    ),
    "Telegram": "تلگرام",
    "WhatsApp": "واتساپ",
    "Copy link": "کپی لینک",
    "Link copied": "لینک کپی شد",
    "Copied": "کپی شد",
    "Portfolio Blog": "وبلاگ نمونه‌کار",
    "Latest articles and notes from the portfolio blog.": (
        "تازه‌ترین مقالات و یادداشت‌های وبلاگ نمونه‌کار."
    ),
    "Posts filed under %(category)s.": "مطالب دسته‌بندی‌شده در %(category)s.",
    "Posts tagged with %(tag)s.": "مطالب با برچسب %(tag)s.",
    # Contact
    "Let's Work Together": "بیایید با هم کار کنیم",
    "Have a project in mind or just want to say hello? I'd love to hear from you.": (
        "پروژه‌ای در ذهن دارید یا فقط می‌خواهید سلام کنید؟ خوشحال می‌شوم از شما بشنوم."
    ),
    "Get in Touch": "در تماس باشید",
    "Whether you're looking for a backend developer, need help building an API, or want to discuss a new project, feel free to reach out.": (
        "چه به دنبال توسعه‌دهنده بک‌اند باشید، به ساخت API نیاز داشته باشید یا بخواهید درباره پروژه جدیدی صحبت کنید، با خیال راحت تماس بگیرید."
    ),
    "Email": "ایمیل",
    "Phone": "تلفن",
    "Location": "موقعیت",
    "Social": "شبکه‌های اجتماعی",
    "Get in touch about backend development, APIs, or a new project collaboration.": (
        "برای توسعه بک‌اند، API یا همکاری در پروژه جدید با من تماس بگیرید."
    ),
    "FAQ": "سوالات متداول",
    "Common Questions": "پرسش‌های رایج",
    "How quickly do you respond?": "چقدر سریع پاسخ می‌دهید؟",
    "I typically reply within 1–2 business days. For urgent project inquiries, include deadlines in your message so I can prioritize accordingly.": (
        "معمولاً ظرف ۱ تا ۲ روز کاری پاسخ می‌دهم. برای درخواست‌های فوری، مهلت‌ها را در پیام ذکر کنید تا اولویت‌بندی کنم."
    ),
    "What kind of projects do you take on?": "چه نوع پروژه‌هایی می‌پذیرید؟",
    "Backend systems, REST APIs, Django and Laravel applications, database design, and integrations. I also build personal websites and shop websites, and can connect your custom frontend to a Laravel or Django backend. I'm happy to discuss both greenfield builds and improvements to existing products.": (
        "سیستم‌های بک‌اند، REST API، برنامه‌های جنگو و لاراول، طراحی پایگاه داده و یکپارچه‌سازی. همچنین وب‌سایت شخصی و فروشگاهی می‌سازم و می‌توانم فرانت‌اند اختصاصی شما را به بک‌اند لاراول یا جنگو متصل کنم. خوشحال می‌شوم هم درباره پروژه‌های جدید و هم بهبود محصولات موجود صحبت کنم."
    ),
    "Do you work remotely?": "آیا از راه دور کار می‌کنید؟",
    "Yes — I collaborate remotely with clients worldwide, using clear async communication and regular check-ins.": (
        "بله — با مشتریان در سراسر جهان از راه دور همکاری می‌کنم، با ارتباط شفاف ناهمزمان و جلسات منظم."
    ),
    # Footer
    "Crafting reliable backend systems and refined digital experiences.": (
        "ساخت سیستم‌های بک‌اند قابل اعتماد و تجربه‌های دیجیتال باکیفیت."
    ),
    "Navigate": "پیمایش",
    "Connect": "ارتباط",
    "Get in touch": "تماس بگیرید",
    "All rights reserved.": "تمامی حقوق محفوظ است.",
    # UI / a11y
    "Toggle color theme": "تغییر تم رنگ",
    "Toggle theme": "تغییر تم",
    "Select language": "انتخاب زبان",
    "Languages": "زبان‌ها",
    "Open navigation menu": "باز کردن منوی ناوبری",
    "Mobile navigation": "ناوبری موبایل",
    "Close navigation menu": "بستن منوی ناوبری",
    "Pagination": "صفحه‌بندی",
    "Previous": "قبلی",
    "Next": "بعدی",
    # Model choices
    "Completed": "تکمیل‌شده",
    "In Progress": "در حال انجام",
    "Planned": "برنامه‌ریزی‌شده",
    # Contact form (existing)
    "Full Name": "نام کامل",
    "Email Address": "آدرس ایمیل",
    "Subject": "موضوع",
    "Company": "شرکت",
    "Message": "پیام",
    "Website": "وب‌سایت",
    "Please enter your name.": "لطفاً نام خود را وارد کنید.",
    "Name must be at most 150 characters.": "نام باید حداکثر ۱۵۰ کاراکتر باشد.",
    "Please enter your email address.": "لطفاً آدرس ایمیل خود را وارد کنید.",
    "Enter a valid email address.": "یک آدرس ایمیل معتبر وارد کنید.",
    "Subject must be at most 200 characters.": "موضوع باید حداکثر ۲۰۰ کاراکتر باشد.",
    "Company must be at most 150 characters.": "نام شرکت باید حداکثر ۱۵۰ کاراکتر باشد.",
    "Phone must be at most 30 characters.": "شماره تلفن باید حداکثر ۳۰ کاراکتر باشد.",
    "Please enter a message.": "لطفاً پیام خود را وارد کنید.",
    "Message must be at least 10 characters.": "پیام باید حداقل ۱۰ کاراکتر باشد.",
    "Message must be at most 5000 characters.": "پیام باید حداکثر ۵۰۰۰ کاراکتر باشد.",
    "Too many messages. Please wait an hour before trying again.": (
        "پیام‌های زیادی ارسال شده است. لطفاً یک ساعت صبر کنید و دوباره تلاش کنید."
    ),
    "Thank you! Your message has been sent.": "متشکرم! پیام شما ارسال شد.",
    "I'll get back to you as soon as I can.": "در اسرع وقت با شما تماس خواهم گرفت.",
    "Please correct the errors below.": "لطفاً خطاهای زیر را برطرف کنید.",
    "Send Message": "ارسال پیام",
    "John Doe": "علی رضایی",
    "Acme Inc. (optional)": "شرکت نمونه (اختیاری)",
    "+1 555 000 0000 (optional)": "+۹۸ ۹۱۲ ۰۰۰ ۰۰۰ (اختیاری)",
    "Project Inquiry": "استعلام پروژه",
    "Tell me about your project...": "درباره پروژه‌تان بگویید...",
}

PLURAL_TRANSLATIONS: dict[tuple[str, str], tuple[str, str]] = {
    ("%(minutes)s min read", "%(minutes)s min read"): (
        "%(minutes)s دقیقه مطالعه",
        "%(minutes)s دقیقه مطالعه",
    ),
    ("%(views)s view", "%(views)s views"): (
        "%(views)s بازدید",
        "%(views)s بازدید",
    ),
    (
        '%(counter)s result for “%(search_query)s”',
        '%(counter)s results for “%(search_query)s”',
    ): (
        '%(counter)s نتیجه برای «%(search_query)s»',
        '%(counter)s نتیجه برای «%(search_query)s»',
    ),
}


def build_po(language: str, plural_forms: str) -> polib.POFile:
    po = polib.POFile()
    po.metadata = {
        **HEADER,
        "Language-Team": language,
        "Language": language,
        "Plural-Forms": plural_forms,
    }

    for msgid, fa_text in sorted(TRANSLATIONS.items(), key=lambda item: item[0].lower()):
        entry = polib.POEntry(msgid=msgid)
        if language == "fa":
            entry.msgstr = fa_text or msgid
        else:
            entry.msgstr = msgid
        po.append(entry)

    for (msgid, msgid_plural), (fa_s, fa_p) in PLURAL_TRANSLATIONS.items():
        entry = polib.POEntry(msgid=msgid, msgid_plural=msgid_plural)
        if language == "fa":
            entry.msgstr_plural = {0: fa_s, 1: fa_p}
        else:
            entry.msgstr_plural = {0: msgid, 1: msgid_plural}
        po.append(entry)

    # Singular blocktrans entries
    blocktrans_singular = {
        "Search: %(search_query)s": "جستجو: %(search_query)s",
        "View screenshot %(n)s": "مشاهده تصویر %(n)s",
        "View %(title)s certificate from %(issuer)s": (
            "مشاهده گواهینامه %(title)s از %(issuer)s"
        ),
    }
    for msgid, fa_text in blocktrans_singular.items():
        entry = polib.POEntry(msgid=msgid)
        entry.msgstr = fa_text if language == "fa" else msgid
        po.append(entry)

    return po


def main() -> None:
    configs = [
        ("en", "nplurals=2; plural=(n != 1);"),
        ("fa", "nplurals=2; plural=(n > 1);"),
    ]
    for lang, plural_forms in configs:
        po = build_po(lang, plural_forms)
        po_path = LOCALE_DIR / lang / "LC_MESSAGES" / "django.po"
        mo_path = LOCALE_DIR / lang / "LC_MESSAGES" / "django.mo"
        po_path.parent.mkdir(parents=True, exist_ok=True)
        po.save(str(po_path))
        po.save_as_mofile(str(mo_path))
        print(f"Wrote {po_path} ({len(po)} entries)")
        print(f"Compiled {mo_path}")


if __name__ == "__main__":
    main()
