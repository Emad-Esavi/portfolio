# Portfolio

A bilingual (English / Persian) personal portfolio and blog built with Django. Manage your profile, projects, experience, services, certificates, and blog posts from the Django admin — no code changes required for day-to-day content updates.

The blog also exposes a private REST API for automation tools (n8n, scripts, CI) so you can create and update posts programmatically, including bilingual content.

## Features

- **Portfolio pages** — Home, About, Projects (with detail pages and galleries), Services, Certificates, and Contact
- **Blog** — Categories, tags, search, featured posts, RSS feed, and draft/published workflow
- **Bilingual UI** — English and Persian with RTL support via `django-modeltranslation`
- **Blog REST API** — Authenticated CRUD for posts (used by n8n and other automation)
- **n8n content pipeline** — Scheduled RSS ingestion + LLM writing, or webhook-triggered post creation
- **Contact form** — Email notifications queued via Celery + Redis, sent over SMTP with rate limiting
- **Modern frontend** — Tailwind CSS 4, DaisyUI, HTMX, and live browser reload in development
- **SEO** — Sitemap, robots.txt, and per-page SEO fields on profile and posts

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Backend | Django 6, PostgreSQL, Django REST Framework |
| Frontend | Tailwind CSS 4, DaisyUI, HTMX |
| i18n | django-modeltranslation, Django locale |
| Email | Gmail SMTP (via `.env`), Celery + Redis queue |
| Automation | n8n (workflow in `n8n-workflows/`) |

## Prerequisites

- Python 3.12+
- Node.js 18+ and npm
- PostgreSQL 14+ (local, Docker, or Windows host from WSL2)
- Redis 6+ (for contact-form email queue)
- Git
- **Optional:** n8n (for automated blog content pipeline) and an OpenAI API key

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

Edit `.env` with your database, SMTP, Redis, and API key settings:

```env
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=change-me
DB_HOST=localhost
DB_PORT=5432

REDIS_URL=redis://127.0.0.1:6379/0

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-gmail@gmail.com

# Required for /api/ — generate with:
#   python -c "import secrets; print(secrets.token_urlsafe(32))"
BLOG_API_KEY=your-secret-api-key
```


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

### 6. Start Redis, web server, and Celery worker

Make sure Redis is running locally:

```bash
redis-server
# or: docker run -p 6379:6379 redis
```

Start the Django app and Celery worker together with Honcho:

```bash
honcho start
```

Or run them in separate terminals:

```bash
python manage.py runserver
celery -A portfolio worker --loglevel=info
```

In another terminal (for CSS hot reload):

```bash
cd theme/static_src && npm run dev
# or: python manage.py tailwind start
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and the admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Blog REST API

Private JSON API for creating and managing blog posts. All endpoints require the `X-API-Key` header matching `BLOG_API_KEY` in `.env`. If the key is unset, every request returns `401`.

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/posts/` | List all posts |
| `POST` | `/api/posts/` | Create a post |
| `GET` | `/api/posts/{slug}/` | Retrieve a post |
| `PATCH` | `/api/posts/{slug}/` | Partial update (PUT is disabled) |
| `DELETE` | `/api/posts/{slug}/` | Delete a post |

Rate limits: 30 write requests/min, 60 read requests/min (authenticated).

### Example: create a post

```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_BLOG_API_KEY" \
  -d '{
    "title": "Hello from the API",
    "title_fa": "سلام از API",
    "content": "# Hello\n\nMarkdown body.",
    "content_fa": "# سلام\n\nمتن مارک‌داون.",
    "excerpt": "Short summary",
    "category": "django",
    "tags": ["python", "django", "api"],
    "status": "draft",
    "author_name": "Emad",
    "featured_image_url": "https://example.com/cover.jpg",
    "seo_title": "Hello from the API",
    "seo_description": "A post created via the REST API."
  }'
```

**Field notes:**

- `title` and `content` are required; `slug` is auto-generated from the title if omitted
- `category` and `tags` are strings — categories/tags are created automatically if they do not exist
- `featured_image_url` must be `http://` or `https://` (local `ImageField` uploads remain admin-only)
- Persian fields (`title_fa`, `content_fa`, etc.) are optional and stored via modeltranslation
- `status` is `draft` or `published`; publishing sets `published_at` automatically

## n8n Blog Content Pipeline

The workflow definition lives in `n8n-workflows/portfolio-blog-content-pipeline.ts` (n8n Workflow SDK). It connects RSS feeds and/or a webhook to the Django Blog API.

### What it does

**Daily schedule (9:00 AM):**

1. Reads RSS feeds (Django, Laravel News, Hacker News, web.dev, CSS-Tricks)
2. Deduplicates URLs via an n8n Data Table (`blog_seen_sources`)
3. Scores items by web-dev keyword relevance
4. Uses OpenAI to write an original bilingual Markdown post
5. `POST`s the draft to `/api/posts/`

**Webhook trigger (`POST /webhook/portfolio-blog-pipeline`):**

| Payload | Behavior |
| --- | --- |
| Full bilingual content (`title`, `content`, `title_fa`, `content_fa`) | Posts directly to the API |
| English only (`title`, `content`) | LLM generates Persian, then posts |
| Topic / research fields only | LLM generates both languages, then posts |

### Setup

1. Run n8n locally (default: [http://localhost:5678](http://localhost:5678))
2. Import or deploy the workflow from `n8n-workflows/portfolio-blog-content-pipeline.ts`
3. Create credentials in n8n:
   - **OpenAI** — for the "Write Original Post" node
   - **Django Blog API Key** — HTTP Header Auth with `X-API-Key: YOUR_BLOG_API_KEY`
4. Create a Data Table named `blog_seen_sources` with columns: `source_url`, `source_title`, `post_slug`, `processed_at`
5. Ensure Django is running and `BLOG_API_KEY` matches the n8n credential
6. Update the `POST Django API` node URL if your server is not `http://127.0.0.1:8000`


## Content Management

After logging into the admin, add your content in this order:

1. **Profile** — Name, bio, photo, resume, social links, and SEO fields
2. **Skills** — Technologies shown on project and about pages
3. **Projects** — Portfolio items with thumbnails, galleries, and status filters
4. **Experience** — Work history timeline
5. **Services** — Offerings with icons and descriptions
6. **Certificates** — Credentials and course completions
7. **Blog posts** — Articles with categories, tags, and featured flags (or via the REST API / n8n)

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
├── blog/
│   ├── api/           # REST API (views, serializers, auth, throttling)
│   ├── management/    # Management commands (seed_blog, etc.)
│   └── templates/     # Blog page templates
├── core/              # Portfolio app (profile, projects, contact, …)
├── n8n-workflows/     # n8n Workflow SDK definitions
├── theme/             # Tailwind theme and base templates
├── portfolio/         # Django project settings and URLs
├── templates/         # Shared templates (robots.txt, UI components, …)
├── locale/            # Compiled translation files
├── scripts/           # Utility scripts (translations, PostgreSQL setup)
├── manage.py
└── requirements.txt
```



## License

This project is provided as-is for personal and portfolio use.
