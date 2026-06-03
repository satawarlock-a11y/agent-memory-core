# Шаблон Obsidian Web Clipper для memory v3

Дата: 2026-04-14
Статус: draft / practical template

## Коротко

Если ты сохраняешь статьи через Obsidian Web Clipper, лучше сразу писать их не как безымянный кусок текста, а как **raw-source note**, которую потом легко продвинуть в daily/domain/canon.

Главная идея:

- клиппинг = это **сырьё**;
- у него сразу должны быть:
  - ссылка,
  - сайт,
  - автор,
  - дата,
  - статус,
  - место в memory pipeline.

## Что я бы советовала фиксировать сразу

Минимум:

- `type: clipping`
- `status: raw`
- `memory_stage: raw`
- `source_type: article`
- `url`
- `site`
- `author`
- `published`
- `clipped_at`
- `domain`
- `tags`
- `summary_status: pending`

## Практический шаблон

Ниже безопасный базовый шаблон без AI-магии, чтобы он работал стабильно и не ломал сырой слой.

```md
---
type: clipping
status: raw
memory_stage: raw
source_type: article
title: "{{title}}"
url: "{{url}}"
site: "{{site}}"
domain: "{{domain}}"
author: "{{author}}"
published: "{{published|date:\"YYYY-MM-DD\"}}"
clipped_at: "{{date|date:\"YYYY-MM-DD HH:mm\"}}"
words: {{words}}
summary_status: pending
trust: external
tags:
  - clipping
  - raw
  - article
  - inbox
---

# {{title}}

> [!meta]
> Source: [{{site}}]({{url}})
> Author: {{author}}
> Published: {{published|date:"YYYY-MM-DD"}}
> Clipped: {{date|date:"YYYY-MM-DD HH:mm"}}
> Domain: {{domain}}

## Почему сохранил
- 

## Быстрая выжимка
{{description}}

## Highlights
{{highlights}}

## Content
{{content}}
```

## Почему этот шаблон хороший

### 1. Он сразу кладёт статью в правильный слой

Не в “канон”, а в `raw`.

### 2. Он не пытается быть слишком умным

Сначала сохраняем статью хорошо. Потом уже отдельный процесс решает:

- пойдёт ли она в daily summary;
- пойдёт ли в доменную память;
- станет ли частью канона.

### 3. Он дружит с будущей архитектурой V3

Потому что тут уже есть:

- source metadata;
- статус;
- memory stage;
- место для summary;
- место для highlights.

## Что можно добавить потом

Когда базовый поток заработает, можно сделать `v2`-шаблон с дополнительными полями:

- `topic_guess:`
- `project_guess:`
- `relevance_score:`
- `promote_to:`
- `entities:`
- `related:`
- `why_it_matters:`

Но я бы **не ставила это в первый шаблон**. Иначе клиппинг станет слишком умным и слишком хрупким.

## Как я это вижу по фазам

### Сейчас

Использовать простой raw-template сверху.

### Чуть позже

Сделать второй шаблон специально для:

- GitHub repos
- research papers
- Telegram posts/news
- visual references

### Потом

Отдельный post-processing flow:

- clipping -> raw inbox
- raw -> daily digest
- daily -> domain note
- domain -> canon page

## Важная мысль

Web Clipper должен помогать **входящему потоку**, а не пытаться сразу стать “умной памятью”.

То есть:

> Clipper — это хорошая воронка на входе, а не мозг целиком.

## Полезные официальные ссылки

- [Obsidian Web Clipper variables](https://obsidian.md/help/web-clipper/variables)
- [Obsidian Web Clipper filters](https://obsidian.md/help/web-clipper/filters)
- [Obsidian Web Clipper logic](https://help.obsidian.md/web-clipper/logic)
