# Portfolio

A bilingual (English / Persian) personal portfolio and blog built with Django. Manage your profile, projects, experience, services, certificates, and blog posts from the Django admin — no code changes required for day-to-day content updates.

## Features

- **Portfolio pages** — Home, About, Projects (with detail pages and galleries), Services, Certificates, and Contact
- **Blog** — Categories, tags, search, featured posts, RSS feed, and draft/published workflow
- **Bilingual UI** — English and Persian with RTL support via `django-modeltranslation`
- **Contact form** — Email notifications over SMTP with rate limiting
- **Modern frontend** — Tailwind CSS 4, DaisyUI, HTMX, and live browser reload in development
- **SEO** — Sitemap, robots.txt, and per-page SEO fields on profile and posts

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Backend | Django 6, SQLite |
| Frontend | Tailwind CSS 4, DaisyUI, HTMX |
| i18n | django-modeltranslation, Django locale |
| Email | Gmail SMTP (via `.env`) |

## Prerequisites

- Python 3.12+
- Node.js 18+ and npm
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/portfolio.git
cd portfolio
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your SMTP credentials if you want the contact form to send email:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-gmail@gmail.com
```

> **Note:** Never commit `.env`. It is already listed in `.gitignore`.

### 4. Install frontend dependencies

```bash
cd theme/static_src
npm install
npm run build
cd ../..
```

Or use the Django Tailwind integration:

```bash
python manage.py tailwind install
python manage.py tailwind build
```

### 5. Run database migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Start the development server

In one terminal:

```bash
python manage.py runserver
```

In a second terminal (for CSS hot reload):

```bash
cd theme/static_src && npm run dev
# or: python manage.py tailwind start
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and the admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Content Management

After logging into the admin, add your content in this order:

1. **Profile** — Name, bio, photo, resume, social links, and SEO fields
2. **Skills** — Technologies shown on project and about pages
3. **Projects** — Portfolio items with thumbnails, galleries, and status filters
4. **Experience** — Work history timeline
5. **Services** — Offerings with icons and descriptions
6. **Certificates** — Credentials and course completions
7. **Blog posts** — Articles with categories, tags, and featured flags

All translatable fields support English and Persian from the admin.

## Translations

UI strings are compiled with a custom script (no GNU gettext required):

```bash
python scripts/build_translations.py
```

Locale files live in `locale/`.

## Project Structure

```
portfolio/
├── blog/              # Blog app (posts, categories, tags, RSS)
├── core/              # Portfolio app (profile, projects, contact, …)
├── theme/             # Tailwind theme and base templates
├── portfolio/         # Django project settings and URLs
├── templates/         # Shared templates (robots.txt, etc.)
├── locale/            # Compiled translation files
├── scripts/           # Utility scripts
├── manage.py
└── requirements.txt
```



## License

This project is provided as-is for personal and portfolio use.
