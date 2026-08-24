import {
  workflow,
  node,
  trigger,
  newCredential,
  ifElse,
  switchCase,
  merge,
  expr,
} from '@n8n/workflow-sdk';

const webhookTrigger = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2.1,
  config: {
    name: 'Webhook',
    parameters: {
      httpMethod: 'POST',
      path: 'portfolio-blog-pipeline',
      responseMode: 'responseNode',
      options: {},
    },
  },
});

const extractWebhookBody = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Extract Webhook Body',
    parameters: {
      mode: 'manual',
      includeOtherFields: false,
      assignments: {
        assignments: [
          { id: 'trigger-source', name: 'trigger_source', value: 'webhook', type: 'string' },
          { id: 'title', name: 'title', value: expr('{{ $json.body.title || "" }}'), type: 'string' },
          { id: 'title-fa', name: 'title_fa', value: expr('{{ $json.body.title_fa || "" }}'), type: 'string' },
          { id: 'content', name: 'content', value: expr('{{ $json.body.content || "" }}'), type: 'string' },
          { id: 'content-fa', name: 'content_fa', value: expr('{{ $json.body.content_fa || "" }}'), type: 'string' },
          { id: 'excerpt', name: 'excerpt', value: expr('{{ $json.body.excerpt || "" }}'), type: 'string' },
          { id: 'excerpt-fa', name: 'excerpt_fa', value: expr('{{ $json.body.excerpt_fa || "" }}'), type: 'string' },
          { id: 'category', name: 'category', value: expr('{{ $json.body.category || "" }}'), type: 'string' },
          { id: 'tags', name: 'tags', value: expr('{{ $json.body.tags || [] }}'), type: 'array' },
          { id: 'status', name: 'status', value: expr('{{ $json.body.status || "draft" }}'), type: 'string' },
          { id: 'author-name', name: 'author_name', value: expr('{{ $json.body.author_name || "Emad" }}'), type: 'string' },
          { id: 'featured-image-url', name: 'featured_image_url', value: expr('{{ $json.body.featured_image_url || "" }}'), type: 'string' },
          { id: 'featured-image-alt', name: 'featured_image_alt', value: expr('{{ $json.body.featured_image_alt || "" }}'), type: 'string' },
          { id: 'featured-image-alt-fa', name: 'featured_image_alt_fa', value: expr('{{ $json.body.featured_image_alt_fa || "" }}'), type: 'string' },
          { id: 'seo-title', name: 'seo_title', value: expr('{{ $json.body.seo_title || "" }}'), type: 'string' },
          { id: 'seo-title-fa', name: 'seo_title_fa', value: expr('{{ $json.body.seo_title_fa || "" }}'), type: 'string' },
          { id: 'seo-description', name: 'seo_description', value: expr('{{ $json.body.seo_description || "" }}'), type: 'string' },
          { id: 'seo-description-fa', name: 'seo_description_fa', value: expr('{{ $json.body.seo_description_fa || "" }}'), type: 'string' },
          { id: 'topic', name: 'topic', value: expr('{{ $json.body.topic || "" }}'), type: 'string' },
        ],
      },
    },
  },
});

const scheduleTrigger = trigger({
  type: 'n8n-nodes-base.scheduleTrigger',
  version: 1.3,
  config: {
    name: 'Daily Schedule',
    parameters: {
      rule: {
        interval: [
          {
            field: 'days',
            daysInterval: 1,
            triggerAtHour: 9,
            triggerAtMinute: 0,
          },
        ],
      },
    },
  },
});

const rssDjango = node({
  type: 'n8n-nodes-base.rssFeedRead',
  version: 1.2,
  config: {
    name: 'RSS Django',
    parameters: {
      url: 'https://www.djangoproject.com/rss/weblog/',
    },
  },
});

const rssLaravel = node({
  type: 'n8n-nodes-base.rssFeedRead',
  version: 1.2,
  config: {
    name: 'RSS Laravel News',
    parameters: {
      url: 'https://laravel-news.com/feed',
    },
  },
});

const rssHackerNews = node({
  type: 'n8n-nodes-base.rssFeedRead',
  version: 1.2,
  config: {
    name: 'RSS Hacker News',
    parameters: {
      url: 'https://hnrss.org/newest?points=80&q=Django+OR+Laravel+OR+Python+OR+HTMX+OR+CSS+OR+JavaScript',
    },
  },
});

const rssWebDev = node({
  type: 'n8n-nodes-base.rssFeedRead',
  version: 1.2,
  config: {
    name: 'RSS Web.dev',
    parameters: {
      url: 'https://web.dev/static/blog/feed.xml',
    },
  },
});

const rssCssTricks = node({
  type: 'n8n-nodes-base.rssFeedRead',
  version: 1.2,
  config: {
    name: 'RSS CSS-Tricks',
    parameters: {
      url: 'https://css-tricks.com/feed/',
    },
  },
});

const mergeFeeds = merge({
  version: 3.2,
  config: {
    name: 'Merge Feeds',
    parameters: {
      mode: 'append',
      numberInputs: 5,
    },
  },
});

const routeWebhookContent = switchCase({
  version: 3.2,
  config: {
    name: 'Route Webhook Content',
    parameters: {
      mode: 'rules',
      rules: {
        values: [
          {
            outputKey: 'bilingual',
            conditions: {
              options: { caseSensitive: true, leftValue: '', typeValidation: 'loose', version: 2 },
              combinator: 'and',
              conditions: [
                { leftValue: expr('{{ $json.title }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
                { leftValue: expr('{{ $json.content }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
                { leftValue: expr('{{ $json.title_fa }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
                { leftValue: expr('{{ $json.content_fa }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
              ],
            },
          },
          {
            outputKey: 'english_only',
            conditions: {
              options: { caseSensitive: true, leftValue: '', typeValidation: 'loose', version: 2 },
              combinator: 'and',
              conditions: [
                { leftValue: expr('{{ $json.title }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
                { leftValue: expr('{{ $json.content }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
              ],
            },
          },
        ],
      },
      options: {
        fallbackOutput: 'extra',
        renameFallbackOutput: 'topic_or_research',
      },
    },
  },
});

const tagWriteModeBilingual = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Tag Write Mode Bilingual',
    parameters: {
      mode: 'manual',
      includeOtherFields: true,
      assignments: {
        assignments: [
          { id: 'write-mode', name: 'write_mode', value: 'bilingual_ready', type: 'string' },
        ],
      },
    },
  },
});

const tagWriteModeAdapt = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Tag Write Mode Adapt',
    parameters: {
      mode: 'manual',
      includeOtherFields: true,
      assignments: {
        assignments: [
          { id: 'write-mode', name: 'write_mode', value: 'adapt_fa', type: 'string' },
        ],
      },
    },
  },
});

const tagWriteModeGenerate = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Tag Write Mode Generate',
    parameters: {
      mode: 'manual',
      includeOtherFields: true,
      assignments: {
        assignments: [
          { id: 'write-mode', name: 'write_mode', value: 'generate_bilingual', type: 'string' },
        ],
      },
    },
  },
});

const normalizeSources = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Normalize Sources',
    parameters: {
      mode: 'manual',
      includeOtherFields: false,
      assignments: {
        assignments: [
          { id: 'trigger-source', name: 'trigger_source', value: 'schedule', type: 'string' },
          { id: 'write-mode', name: 'write_mode', value: 'generate_bilingual', type: 'string' },
          { id: 'source-title', name: 'source_title', value: expr('{{ $json.title || "" }}'), type: 'string' },
          { id: 'source-url', name: 'source_url', value: expr('{{ $json.link || $json.guid || "" }}'), type: 'string' },
          { id: 'source-summary', name: 'source_summary', value: expr('{{ $json.contentSnippet || $json.content || $json.summary || "" }}'), type: 'string' },
          { id: 'source-name', name: 'source_name', value: expr('{{ $json.meta && $json.meta.title ? $json.meta.title : ($json.creator || "RSS") }}'), type: 'string' },
          { id: 'published-at', name: 'published_at', value: expr('{{ $json.isoDate || $json.pubDate || "" }}'), type: 'string' },
          { id: 'topic', name: 'topic', value: expr('{{ $json.title || "" }}'), type: 'string' },
          { id: 'status', name: 'status', value: 'draft', type: 'string' },
          { id: 'author-name', name: 'author_name', value: 'Emad', type: 'string' },
        ],
      },
    },
  },
});

const dedupSeenUrls = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Dedup Seen URLs',
    parameters: {
      resource: 'row',
      operation: 'rowNotExists',
      dataTableId: { __rl: true, mode: 'name', value: 'blog_seen_sources', cachedResultName: 'blog_seen_sources' },
      matchType: 'allConditions',
      filters: {
        conditions: [
          {
            keyName: 'source_url',
            condition: 'eq',
            keyValue: expr('{{ $json.source_url }}'),
          },
        ],
      },
    },
  },
});

const scoreRelevance = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Score Relevance',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: 'const keywords = ["django", "laravel", "php", "python", "htmx", "alpine", "livewire", "postgresql", "orm", "api", "javascript", "css", "html", "tailwind", "accessibility", "performance", "security", "frontend", "backend", "web"];\nconst items = $input.all();\nconst scored = [];\nfor (const item of items) {\n  const data = item.json || {};\n  const url = (data.source_url || "").trim();\n  if (!url) continue;\n  const haystack = [data.source_title, data.source_summary, data.topic, data.source_name].filter(Boolean).join(" ").toLowerCase();\n  let score = 0;\n  for (const keyword of keywords) {\n    if (haystack.includes(keyword)) score += 1;\n  }\n  if (score > 0) scored.push({ json: { ...data, relevance_score: score } });\n}\nreturn scored;',
    },
  },
});

const sortByScore = node({
  type: 'n8n-nodes-base.sort',
  version: 1,
  config: {
    name: 'Sort By Score',
    parameters: {
      type: 'simple',
      sortFieldsUi: {
        sortField: [
          { fieldName: 'relevance_score', order: 'descending' },
        ],
      },
    },
  },
});

const pickBestTopic = node({
  type: 'n8n-nodes-base.limit',
  version: 1,
  config: {
    name: 'Pick Best Topic',
    parameters: {
      maxItems: 1,
    },
  },
});

const writeOriginalPost = node({
  type: '@n8n/n8n-nodes-langchain.openAi',
  version: 2.3,
  config: {
    name: 'Write Original Post',
    executeOnce: true,
    credentials: { openAiApi: newCredential('OpenAI') },
    parameters: {
      resource: 'text',
      operation: 'response',
      modelId: { __rl: true, mode: 'list', value: 'gpt-4o-mini', cachedResultName: 'gpt-4o-mini' },
      simplify: true,
      responses: {
        values: [
          {
            type: 'text',
            role: 'user',
            content: expr('You are a bilingual technical blog writer for a Django/Laravel/web development portfolio. Write ORIGINAL Markdown. Do not copy source text. Include a short Sources section with URLs when research notes exist. Return ONLY valid JSON with keys: title, title_fa, content, content_fa, excerpt, excerpt_fa, category, tags, seo_title, seo_title_fa, seo_description, seo_description_fa, featured_image_alt, featured_image_alt_fa. Persian must be natural technical FA, not a literal translation. Mode: {{ $json.write_mode || "generate_bilingual" }}. Topic: {{ $json.topic || $json.source_title || "" }}. Category hint: {{ $json.category || "" }}. Research title: {{ $json.source_title || "" }}. Research summary: {{ $json.source_summary || "" }}. Research URL: {{ $json.source_url || "" }}. Existing English title: {{ $json.title || "" }}. Existing English content: {{ $json.content || "" }}. If mode is adapt_fa, keep English fields and only create Persian fields. If generate_bilingual, create both languages. tags must be a JSON array of lowercase English strings.'),
          },
        ],
      },
      options: {
        maxTokens: 4096,
        temperature: 0.7,
        textFormat: {
          textOptions: { type: 'json_object' },
        },
      },
    },
  },
});

const parseLlmJson = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Parse LLM JSON',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: 'const upstream = $("Write Original Post").first()?.json || {};\nconst context = $("Tag Write Mode Adapt").first()?.json || $("Tag Write Mode Generate").first()?.json || $("Pick Best Topic").first()?.json || $("Extract Webhook Body").first()?.json || {};\nlet generated = {};\nconst raw = upstream.output || upstream.text || upstream.message || upstream.response || upstream;\nif (typeof raw === "string") {\n  try { generated = JSON.parse(raw); } catch (e) { throw new Error("LLM did not return valid JSON: " + raw); }\n} else if (raw && typeof raw === "object") {\n  generated = raw;\n}\nreturn [{ json: { ...context, ...generated, title: generated.title || context.title || "", content: generated.content || context.content || "", title_fa: generated.title_fa || context.title_fa || "", content_fa: generated.content_fa || context.content_fa || "", excerpt: generated.excerpt || context.excerpt || "", excerpt_fa: generated.excerpt_fa || context.excerpt_fa || "", category: generated.category || context.category || "APIs", tags: generated.tags || context.tags || [], author_name: context.author_name || "Emad", status: context.status || "draft", featured_image_url: context.featured_image_url || "", featured_image_alt: generated.featured_image_alt || context.featured_image_alt || "", featured_image_alt_fa: generated.featured_image_alt_fa || context.featured_image_alt_fa || "", seo_title: generated.seo_title || context.seo_title || "", seo_title_fa: generated.seo_title_fa || context.seo_title_fa || "", seo_description: generated.seo_description || context.seo_description || "", seo_description_fa: generated.seo_description_fa || context.seo_description_fa || "", source_url: context.source_url || "", source_title: context.source_title || "", trigger_source: context.trigger_source || "schedule" } }];',
    },
  },
});

const prepareApiFields = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Prepare API Fields',
    parameters: {
      mode: 'manual',
      includeOtherFields: false,
      assignments: {
        assignments: [
          { id: 'title', name: 'title', value: expr('{{ $json.title }}'), type: 'string' },
          { id: 'title-fa', name: 'title_fa', value: expr('{{ $json.title_fa }}'), type: 'string' },
          { id: 'content', name: 'content', value: expr('{{ $json.content }}'), type: 'string' },
          { id: 'content-fa', name: 'content_fa', value: expr('{{ $json.content_fa }}'), type: 'string' },
          { id: 'excerpt', name: 'excerpt', value: expr('{{ $json.excerpt }}'), type: 'string' },
          { id: 'excerpt-fa', name: 'excerpt_fa', value: expr('{{ $json.excerpt_fa }}'), type: 'string' },
          { id: 'category', name: 'category', value: expr('{{ $json.category }}'), type: 'string' },
          { id: 'tags', name: 'tags', value: expr('{{ $json.tags }}'), type: 'array' },
          { id: 'author-name', name: 'author_name', value: expr('{{ $json.author_name || "Emad" }}'), type: 'string' },
          { id: 'status', name: 'status', value: expr('{{ $json.status || "draft" }}'), type: 'string' },
          { id: 'featured-image-url', name: 'featured_image_url', value: expr('{{ $json.featured_image_url || "" }}'), type: 'string' },
          { id: 'featured-image-alt', name: 'featured_image_alt', value: expr('{{ $json.featured_image_alt || "" }}'), type: 'string' },
          { id: 'featured-image-alt-fa', name: 'featured_image_alt_fa', value: expr('{{ $json.featured_image_alt_fa || "" }}'), type: 'string' },
          { id: 'seo-title', name: 'seo_title', value: expr('{{ $json.seo_title }}'), type: 'string' },
          { id: 'seo-title-fa', name: 'seo_title_fa', value: expr('{{ $json.seo_title_fa }}'), type: 'string' },
          { id: 'seo-description', name: 'seo_description', value: expr('{{ $json.seo_description }}'), type: 'string' },
          { id: 'seo-description-fa', name: 'seo_description_fa', value: expr('{{ $json.seo_description_fa }}'), type: 'string' },
          { id: 'source-url', name: 'source_url', value: expr('{{ $json.source_url || "" }}'), type: 'string' },
          { id: 'source-title', name: 'source_title', value: expr('{{ $json.source_title || "" }}'), type: 'string' },
          { id: 'trigger-source', name: 'trigger_source', value: expr('{{ $json.trigger_source || "schedule" }}'), type: 'string' },
        ],
      },
    },
  },
});

const postDjangoApi = node({
  type: 'n8n-nodes-base.httpRequest',
  version: 4.5,
  config: {
    name: 'POST Django API',
    onError: 'continueErrorOutput',
    retryOnFail: true,
    maxTries: 3,
    waitBetweenTries: 2000,
    credentials: { httpTemplatedCustomAuth: newCredential('Django Blog API Key') },
    parameters: {
      method: 'POST',
      url: 'http://127.0.0.1:8000/api/posts/',
      authentication: 'genericCredentialType',
      genericAuthType: 'httpTemplatedCustomAuth',
      sendBody: true,
      contentType: 'json',
      specifyBody: 'json',
      jsonBody: expr(
        '{{ { title: $json.title, title_fa: $json.title_fa, content: $json.content, content_fa: $json.content_fa, excerpt: $json.excerpt, excerpt_fa: $json.excerpt_fa, category: $json.category, tags: $json.tags, author_name: $json.author_name, status: $json.status, featured_image_url: $json.featured_image_url, featured_image_alt: $json.featured_image_alt, featured_image_alt_fa: $json.featured_image_alt_fa, seo_title: $json.seo_title, seo_title_fa: $json.seo_title_fa, seo_description: $json.seo_description, seo_description_fa: $json.seo_description_fa } }}'
      ),
      options: {
        response: {
          response: {
            fullResponse: false,
            neverError: false,
            responseFormat: 'json',
          },
        },
      },
    },
  },
});

const formatApiError = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Format API Error',
    parameters: {
      mode: 'manual',
      includeOtherFields: false,
      assignments: {
        assignments: [
          { id: 'ok', name: 'ok', value: false, type: 'boolean' },
          { id: 'status', name: 'status', value: expr('{{ $json.error?.status || $json.statusCode || 502 }}'), type: 'number' },
          { id: 'error', name: 'error', value: expr('{{ $json.error?.message || $json.detail || $json }}'), type: 'object' },
          { id: 'trigger-source', name: 'trigger_source', value: expr('{{ $("Prepare API Fields").item.json.trigger_source }}'), type: 'string' },
        ],
      },
    },
  },
});

const hasSourceUrl = ifElse({
  version: 2.2,
  config: {
    name: 'Has Source URL?',
    parameters: {
      conditions: {
        options: { caseSensitive: true, leftValue: '', typeValidation: 'loose', version: 2 },
        combinator: 'and',
        conditions: [
          { leftValue: expr('{{ $("Prepare API Fields").item.json.source_url }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' },
        ],
      },
    },
  },
});

const markSourceSeen = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Mark Source Seen',
    parameters: {
      resource: 'row',
      operation: 'insert',
      dataTableId: { __rl: true, mode: 'name', value: 'blog_seen_sources', cachedResultName: 'blog_seen_sources' },
      columns: {
        mappingMode: 'defineBelow',
        value: {
          source_url: expr('{{ $("Prepare API Fields").item.json.source_url }}'),
          source_title: expr('{{ $("Prepare API Fields").item.json.source_title }}'),
          post_slug: expr('{{ $json.slug }}'),
          processed_at: expr('{{ $now.toISO() }}'),
        },
        schema: [
          { id: 'source_url', displayName: 'source_url', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'source_title', displayName: 'source_title', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'post_slug', displayName: 'post_slug', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'processed_at', displayName: 'processed_at', required: false, defaultMatch: false, display: true, type: 'dateTime', canBeUsedToMatch: true },
        ],
      },
    },
  },
});

const startedByWebhook = ifElse({
  version: 2.2,
  config: {
    name: 'Started By Webhook?',
    parameters: {
      conditions: {
        options: { caseSensitive: true, leftValue: '', typeValidation: 'loose', version: 2 },
        combinator: 'and',
        conditions: [
          { leftValue: expr('{{ $("Extract Webhook Body").isExecuted }}'), operator: { type: 'boolean', operation: 'true' }, rightValue: '' },
        ],
      },
    },
  },
});

const respondCreated = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Respond Created',
    parameters: {
      respondWith: 'json',
      responseBody: expr('{{ $json }}'),
      options: {
        responseCode: 201,
      },
    },
  },
});

const respondApiError = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Respond API Error',
    parameters: {
      respondWith: 'json',
      responseBody: expr('{{ $json }}'),
      options: {
        responseCode: expr('{{ $json.status || 502 }}'),
      },
    },
  },
});

export default workflow('portfolio-blog-content-pipeline', 'Portfolio Blog Content Pipeline')
  .add(webhookTrigger)
  .to(extractWebhookBody)
  .to(routeWebhookContent
    .onCase(0, tagWriteModeBilingual.to(prepareApiFields))
    .onCase(1, tagWriteModeAdapt.to(writeOriginalPost.to(parseLlmJson.to(prepareApiFields))))
    .onCase(2, tagWriteModeGenerate.to(writeOriginalPost.to(parseLlmJson.to(prepareApiFields)))))
  .add(scheduleTrigger)
  .to(rssDjango.to(mergeFeeds.input(0)))
  .add(scheduleTrigger)
  .to(rssLaravel.to(mergeFeeds.input(1)))
  .add(scheduleTrigger)
  .to(rssHackerNews.to(mergeFeeds.input(2)))
  .add(scheduleTrigger)
  .to(rssWebDev.to(mergeFeeds.input(3)))
  .add(scheduleTrigger)
  .to(rssCssTricks.to(mergeFeeds.input(4)))
  .add(mergeFeeds)
  .to(normalizeSources)
  .to(dedupSeenUrls)
  .to(scoreRelevance)
  .to(sortByScore)
  .to(pickBestTopic)
  .to(writeOriginalPost.to(parseLlmJson.to(prepareApiFields)))
  .add(prepareApiFields)
  .to(postDjangoApi
    .onError(formatApiError.to(startedByWebhook.onTrue(respondApiError))))
  .to(hasSourceUrl
    .onTrue(markSourceSeen.to(startedByWebhook.onTrue(respondCreated)))
    .onFalse(startedByWebhook.onTrue(respondCreated)));
