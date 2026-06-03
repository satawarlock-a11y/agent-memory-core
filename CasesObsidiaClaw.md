# CasesObsidiaClaw

Дата: 2026-04-17  
Папка: `C:\Progi\VibeProjects\Openclaw\НоваяПамятьV3\`

Фокус: живые кейсы и recurring patterns вокруг `OpenClaw + Obsidian`:
- retrieval sidecars
- sync-safe access
- prompt packaging
- draft-first notes
- git-based continuity
- remote/mobile vault access

Этот файл не про список ссылок ради списка. Он про то, как люди реально собирают vault-as-memory workflows и какие куски архитектуры повторяются снова и снова.

---

## Короткий вывод

1. Obsidian чаще всего выступает как canonical memory / source of truth.
2. Агентный слой почти всегда стараются держать как bridge, а не как скрытый memory blob.
3. Повторяющиеся мосты: MCP, search sidecars, git history, sync-safe access, prompt templates.
4. Люди не хотят dump all notes into model; они хотят slices, drafts, review, promotion to canon.
5. Ваша линия V2/V3 выглядит не как фантазия, а как более зрелая версия того, что уже видно в поле.

---

## Как читать файл

### Tier A — direct OpenClaw + Obsidian
Кейсы, где OpenClaw упомянут прямо.

### Tier B — adjacent patterns
Очень близкий класс систем: Claude / Claude Code / Obsidian / MCP / markdown vault.

### Tier C — recurring practical patterns
Повторяющиеся приёмы, которые стоит считать архитектурным сигналом.

---

## Tier A — direct OpenClaw + Obsidian кейсы

### A1. Obsidian как memory vault для OpenClaw
**Ссылка:** [Best practice for using Obsidian as a “memory vault” for OpenClaw](https://www.reddit.com/r/openclaw/comments/1revaho/best_practice_for_using_obsidian_as_a_memory/)

**Что происходит:**
- Obsidian держат как долгую память;
- OpenClaw читают через retrieval, а не через ручной paste;
- хотят снизить token burn и сохранить continuity.

**Паттерн:** `vault as source of truth` + `retrieval instead of prompt dumping`

---

### A2. OpenClaw как daily companion, Obsidian как живая память
**Ссылка:** [Using OpenClaw as a daily AI companion with Obsidian as its memory](https://www.reddit.com/r/openclaw/comments/1rb49o1/using_openclaw_as_a_daily_ai_companion_with/)

**Что происходит:**
- OpenClaw используют как постоянного daily assistant;
- Obsidian хранит commitments, context, operating notes;
- vault становится рабочей continuity surface.

**Паттерн:** `assistant <-> vault <-> daily life context`

---

### A3. OpenClaw + Obsidian как second brain
**Ссылка:** [Using Obsidian + OpenClaw as my second brain, here’s the setup](https://www.reddit.com/r/openclaw/comments/1rlqfbe/using_obsidian_openclaw_as_my_second_brain_heres/)

**Что происходит:**
- vault связывают с memory layer и search stack;
- хотят, чтобы агент работал с долговременным knowledge layer;
- обсуждают hierarchical memory и retrieval helpers.

**Паттерн:** `vault canon + retrieval helpers + agent context assembly`

---

### A4. Obsidian лечит memory pain у OpenClaw / Claude Code
**Ссылка:** [PROOF: Obsidian solves OpenClaw & Claude Code memory issues](https://www.reddit.com/r/openclaw/comments/1rw4j9f/proof_obsidian_solves_openclaw_claude_code_memory/)

**Что происходит:**
- vault используют как cross-session persistent memory;
- wiki links и connected context помогают continuity;
- memory pain уменьшается через vault-based memory.

**Паттерн:** `vault as shared long-term memory`

---

### A5. OpenClaw + Obsidian через MCP / sync / service layer
**Ссылка:** [OpenClaw and Obsidian](https://www.reddit.com/r/openclaw/comments/1ry8991/openclaw_and_obsidian/)

**Что происходит:**
- vault подключают через MCP server;
- обсуждают read-write access;
- поднимают sync между устройствами и service layer поверх Obsidian.

**Паттерн:** `agent access layer + sync layer + vault as canonical store`

---

### A6. Файловый доступ vs API/CLI vs QMD sidecar
**Ссылка:** [Obsidian integration](https://www.reddit.com/r/openclaw/comments/1sihn5n/obsidian_integration/)

**Что происходит:**
- спорят, давать ли агенту прямой доступ к vault;
- предлагают API / skill layer;
- поднимают QMD sidecar для серьёзного retrieval.

**Паттерн:** `vault API / skill abstraction` + `QMD sidecar for retrieval`

---

### A7. OpenClaw берёт заметки из Obsidian и использует git/log summaries
**Ссылка:** [What are you guys actually using OpenClaw for?](https://www.reddit.com/r/openclaw/comments/1rnyvx3/what_are_you_guys_actually_using_openclaw_for/)

**Что происходит:**
- vault живёт в Obsidian;
- синкается через git;
- OpenClaw тянет latest notes;
- использует git log и делает summary / reminders.

**Паттерн:** `notes -> git history -> agent summary`

---

### A8. obsidian-sync skill для OpenClaw
**Ссылка:** [obsidian-sync — OpenClaw skill](https://openclawai.io/skills/skill/obsidian-sync/)

**Что происходит:**
- sync интеграция оформляется как reusable skill;
- vault и workspace связываются повторяемым механизмом.

**Паттерн:** `workspace <-> sync skill <-> vault`

---

## Tier B — adjacent кейсы

### B1. Obsidian + Claude Desktop + MCP
**Ссылки:**
- [Obsidian knowledgebase + MCP (Claude Desktop)](https://www.reddit.com/r/ObsidianMD/comments/1jwqxeq)
- [Let Claude AI Read/Edit Your Obsidian Files](https://www.reddit.com/r/ObsidianMD/comments/1h2dj7u)

**Что происходит:**
- Claude Desktop как front-end;
- vault остаётся markdown-first;
- MCP даёт read/write/search.

**Почему важно:**
Агент подключается к vault через bridge, а не живёт отдельно.

---

### B2. Sync-safe remote access к vault
**Ссылки:**
- [obsidian-web-mcp: sync-safe MCP server](https://www.reddit.com/r/ObsidianMD/comments/1rwmuiq/obsidianwebmcp_a_syncsafe_mcp_server_that_lets/)
- [I built an MCP server that lets Claude manage my Obsidian vault remotely](https://www.reddit.com/r/ClaudeAI/comments/1q8sxl7/i_built_an_mcp_server_that_lets_claude_manage_my/)
- [How to use Obsidian Sync Effectively and Safely](https://forum.obsidian.md/t/how-to-use-obsidian-sync-effectively-and-safely/80545)

**Что происходит:**
- vault открывают для web/mobile/remote access;
- строят HTTPS / tunnel / sync-safe patterns;
- следят за конфликтами и safety.

**Почему важно:**
Если агент и человек на разных устройствах, нужен bridge, а не сырой файловый доступ.

---

### B3. Agent inside Obsidian
**Ссылка:** [Introduce Claudian, a plugin that embeds Claude Code inside Obsidian](https://www.reddit.com/r/ObsidianMD/comments/1q9y8cx/introduce_claudian_a_plugin_that_embeds_claude/)

**Что происходит:**
- агентная поверхность встраивается прямо в Obsidian sidebar;
- vault становится рабочей сценой агента.

**Почему важно:**
Obsidian начинают воспринимать как operational memory surface, а не только архив.

---

### B4. Persistent markdown vault for Claude Code
**Ссылка:** [Parsidion CC — Persistent Memory for Claude Code via a Markdown Vault](https://www.reddit.com/r/ClaudeCode/comments/1s17c5t/parsidion_cc_persistent_memory_for_claude_code/)

**Что происходит:**
- memory делают через markdown vault;
- данные остаются searchable и human-readable;
- агент и человек видят один и тот же слой истины.

**Почему важно:**
Сильный сигнал в пользу inspectable memory вместо hidden memory blob.

---

### B5. Token-efficient vault access
**Ссылки:**
- [VaultForge — MCP server for Obsidian that cuts token usage 80-95%](https://www.reddit.com/r/ClaudeAI/comments/1rwihrh/vaultforge_mcp_server_for_obsidian_that_cuts/)
- [Is anyone functionally use an MCP with Obsidian?](https://www.reddit.com/r/ObsidianMD/comments/1okyoph/is_anyone_functionally_use_an_mcp_with_obsidian/)

**Что происходит:**
- токеновый перегруз на больших vault;
- нужен умный retrieval / query / indexing;
- dump all notes into model быстро становится плохой идеей.

**Почему важно:**
Подтверждает ставку на `QMD / search / slices / promotion`.

---

### B6. Note synthesis вместо chat sludge
**Ссылки:**
- [Using Obsidian MCP for Note Synthesis](https://www.reddit.com/r/ObsidianMD/comments/1jmlf83)
- [Promptfire](https://forum.obsidian.md/t/new-plugin-promptfire-copy-your-vaults-context-to-any-llm-with-one-hotkey/111088)
- [AI Knowledge Filler](https://forum.obsidian.md/t/ai-knowledge-filler-turn-any-llm-into-a-structured-file-generator-for-obsidian/111443)
- [Smart Templates for Obsidian](https://smartconnections.app/smart-templates/)

**Что происходит:**
- LLM используют для генерации clean markdown artifacts;
- промпты пакуют в шаблоны;
- результат проходит review;
- в canon попадает только то, что прошло отбор.

**Почему важно:**
Это почти ваш `draft-first -> review -> canon`.

---

### B7. Daily notes как intake spine
**Ссылки:**
- [iiz00/obsidian-daily-note-outline](https://github.com/iiz00/obsidian-daily-note-outline)
- [Quick Draft for Obsidian](https://forum.obsidian.md/t/quick-draft-for-obsidian-companion-mobile-app-android-ios/108209)
- [Journal/log workflow – Drafts-like "just start writing"](https://forum.obsidian.md/t/journal-log-workflow-drafts-like-just-start-writing-for-your-daily-notes-ios/18382)
- [Obsidian DailyNotes templates](https://github.com/aseyedia/Obsidian_DailyNotes)

**Что происходит:**
- daily notes становятся intake spine;
- быстрый capture идёт в журнал, а не сразу в canon;
- потом записи выносят в отдельные заметки.

**Почему важно:**
Сначала склад сырья, потом библиотека.

---

## Tier C — recurring practical patterns

### 1. Retrieval sidecars
**Суть:** retrieval нужен как помощник, а не как истина.

**Повторяется:**
- QMD
- Smart Connections
- obsidian-semantic-mcp
- obsidian-mcp-tools

---

### 2. Sync-safe access
**Суть:** vault должен жить на нескольких устройствах, но с понятной консистентностью.

**Повторяется:**
- Obsidian Sync
- Git-based sync
- Working Copy / mobile workflows
- remote MCP / tunnel patterns

---

### 3. Prompt packaging
**Суть:** не хочется вручную лепить простыню текста каждый раз.

**Повторяется:**
- Templater
- Smart Templates
- Promptfire
- custom slash commands / system prompts

---

### 4. Draft-first notes
**Суть:** LLM сначала пишет draft, человек решает судьбу текста.

**Повторяется:**
- generated note drafts
- synthesis notes
- structured file generation
- review before canon

---

### 5. Git-based continuity
**Суть:** git история тоже становится памятью.

**Повторяется:**
- Obsidian Git
- Working Copy
- git log summaries
- version history / diffs

---

### 6. Remote/mobile vault access
**Суть:** люди хотят читать и писать в vault не только с основного ноутбука.

**Повторяется:**
- Obsidian Sync
- Web / tunnel MCP
- mobile companion apps
- remote-safe access patterns

---

## Самые повторяющиеся use cases

### Use case 1 — Vault как canonical memory
agent -> retrieval / bridge -> vault canon

### Use case 2 — Daily companion memory
agent <-> vault <-> daily notes / commitments / project context

### Use case 3 — Research intake -> curated note
web / Telegram / clipper -> raw note -> digest -> curated note

### Use case 4 — Agent reads slices, not whole vault
query -> search helper -> relevant notes -> agent context

### Use case 5 — Agent writes drafts, человек решает promotion
agent output -> draft markdown -> review -> canon / no canon

---

## Что особенно хорошо совпадает с вашей V2/V3

### Сильные совпадения
1. Obsidian/markdown как дом.
2. Retrieval как sidecar, а не truth.
3. Bridge/API/MCP вместо raw access.
4. Draft-first / inspectable artifacts.
5. Hybrid/local search.
6. Continuity через summaries / logs / files.

### Где ваша архитектура глубже рынка
1. Rights-aware memory slices.
2. Domain segmentation (`Telegram / Comfy / visual / user model`).
3. Promotion / publish gates / trust boundaries.

---

## Практический вывод

> Люди уже реально используют Obsidian как дом памяти для OpenClaw и соседних agentic систем, а самого агента подключают к vault через search / MCP / sync / filesystem bridge, а не через закрытый memory backend.

То есть ваша линия — не странная самодеятельность, а вполне правдоподобная эволюция рынка. Просто у вас она собрана аккуратнее и взрослее.

---

## Shortlist ссылок

### Direct OpenClaw + Obsidian
- [Best practice for using Obsidian as a “memory vault” for OpenClaw](https://www.reddit.com/r/openclaw/comments/1revaho/best_practice_for_using_obsidian_as_a_memory/)
- [Using OpenClaw as a daily AI companion with Obsidian as its memory](https://www.reddit.com/r/openclaw/comments/1rb49o1/using_openclaw_as_a_daily_ai_companion_with/)
- [Using Obsidian + OpenClaw as my second brain](https://www.reddit.com/r/openclaw/comments/1rlqfbe/using_obsidian_openclaw_as_my_second_brain_heres/)
- [PROOF: Obsidian solves OpenClaw & Claude Code memory issues](https://www.reddit.com/r/openclaw/comments/1rw4j9f/proof_obsidian_solves_openclaw_claude_code_memory/)
- [OpenClaw and Obsidian](https://www.reddit.com/r/openclaw/comments/1ry8991/openclaw_and_obsidian/)
- [Obsidian integration](https://www.reddit.com/r/openclaw/comments/1sihn5n/obsidian_integration/)
- [What are you guys actually using OpenClaw for?](https://www.reddit.com/r/openclaw/comments/1rnyvx3/what_are_you_guys_actually_using_openclaw_for/)
- [obsidian-sync — OpenClaw skill](https://openclawai.io/skills/skill/obsidian-sync/)

### Adjacent but very useful
- [Obsidian knowledgebase + MCP (Claude Desktop)](https://www.reddit.com/r/ObsidianMD/comments/1jwqxeq)
- [obsidian-web-mcp](https://www.reddit.com/r/ObsidianMD/comments/1rwmuiq/obsidianwebmcp_a_syncsafe_mcp_server_that_lets/)
- [Claudian plugin](https://www.reddit.com/r/ObsidianMD/comments/1q9y8cx/introduce_claudian_a_plugin_that_embeds_claude/)
- [Parsidion CC](https://www.reddit.com/r/ClaudeCode/comments/1s17c5t/parsidion_cc_persistent_memory_for_claude_code/)
- [VaultForge](https://www.reddit.com/r/ClaudeAI/comments/1rwihrh/vaultforge_mcp_server_for_obsidian_that_cuts/)
- [Promptfire](https://forum.obsidian.md/t/new-plugin-promptfire-copy-your-vaults-context-to-any-llm-with-one-hotkey/111088)
- [AI Knowledge Filler](https://forum.obsidian.md/t/ai-knowledge-filler-turn-any-llm-into-a-structured-file-generator-for-obsidian/111443)
- [Smart Templates for Obsidian](https://smartconnections.app/smart-templates/)

---

## Источники

### Official / primary
- https://obsidian.md/help/sync-notes
- https://obsidian.md/help/sync/setup
- https://obsidian.md/help/sync/settings
- https://forum.obsidian.md/t/how-to-use-obsidian-sync-effectively-and-safely/80545
- https://forum.obsidian.md/t/new-plugin-remotely-save/28446
- https://forum.obsidian.md/t/mobile-syncing-vault-with-dropsync-on-android/20714

### OpenClaw direct signal
- https://www.reddit.com/r/openclaw/comments/1revaho/best_practice_for_using_obsidian_as_a_memory/
- https://www.reddit.com/r/openclaw/comments/1rb49o1/using_openclaw_as_a_daily_ai_companion_with/
- https://www.reddit.com/r/openclaw/comments/1rlqfbe/using_obsidian_openclaw_as_my_second_brain_heres/
- https://www.reddit.com/r/openclaw/comments/1rw4j9f/proof_obsidian_solves_openclaw_claude_code_memory/
- https://www.reddit.com/r/openclaw/comments/1ry8991/openclaw_and_obsidian/
- https://www.reddit.com/r/openclaw/comments/1sihn5n/obsidian_integration/
- https://www.reddit.com/r/openclaw/comments/1rnyvx3/what_are_you_guys_actually_using_openclaw_for/
- https://openclawai.io/skills/skill/obsidian-sync/

### Adjacent workflow signal
- https://www.reddit.com/r/ObsidianMD/comments/1jwqxeq
- https://www.reddit.com/r/ObsidianMD/comments/1h2dj7u
- https://www.reddit.com/r/ObsidianMD/comments/1rwmuiq/obsidianwebmcp_a_syncsafe_mcp_server_that_lets/
- https://www.reddit.com/r/ObsidianMD/comments/1q9y8cx/introduce_claudian_a_plugin_that_embeds_claude/
- https://www.reddit.com/r/ClaudeCode/comments/1s17c5t/parsidion_cc_persistent_memory_for_claude_code/
- https://www.reddit.com/r/ClaudeAI/comments/1rwihrh/vaultforge_mcp_server_for_obsidian_that_cuts/
- https://forum.obsidian.md/t/new-plugin-promptfire-copy-your-vaults-context-to-any-llm-with-one-hotkey/111088
- https://forum.obsidian.md/t/ai-knowledge-filler-turn-any-llm-into-a-structured-file-generator-for-obsidian/111443
- https://smartconnections.app/smart-templates/
- https://github.com/jacksteamdev/obsidian-mcp-tools
- https://github.com/aaronsb/obsidian-semantic-mcp
- https://github.com/newtype-01/obsidian-mcp
- https://github.com/Vinzent03/obsidian-git
