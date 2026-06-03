# Roadmap памяти v3

Дата: 2026-04-13
Статус: draft после `01` и `02`; презентации делать только после утверждения

## Короткая практическая суть

Roadmap упрощён до фаз. Не стартуем с графов и тяжёлых memory OS.

Главная линия:

```text
правила -> markdown-основа -> поиск -> continuity -> Telegram -> Comfy/visual -> Эхо+сестрички -> graph/advanced
```

## Roadmap по фазам

| Фаза | Цель | Что вводим | Инструмент / подход | Что не делаем | Критерий готовности |
|---|---|---|---|---|---|
| Фаза 0 — зафиксировать правила | не дать памяти разъехаться до старта | L0 governance: source of truth, rights, promotion, draft-first | свои md-правила: README, SESSION-STATE skeleton, ADR/Known_Bad policy | QMD/graph/agent backend | понятно, кто куда пишет и что является правдой |
| Фаза 1 — живая markdown-основа | чтобы любая новая информация имела место | raw inbox, daily notes, curated pages, wiki links, Properties/Bases | Obsidian + markdown + templates | сложные memory SDKs | новые заметки можно раскладывать без хаоса |
| Фаза 2 — поиск и retrieval | чтобы память быстро находилась | QMD, BM25+vector hybrid, local embeddings pilot, retrieval policy | QMD + adapter + local embeddings test set | граф как core | Эхо может найти нужные заметки без заливки всего vault в prompt |
| Фаза 3 — continuity и librarian | чтобы контекст жил между сессиями и не тух | SESSION-STATE discipline, daily summaries, nightly librarian, LCM/ClawMem pilot | сначала свои summaries, потом пилот LCM/ClawMem | полный OpenViking/MemOS | долгая задача восстанавливается по state+summary+retrieval |
| Фаза 4 — Telegram intake и новости | сделать Telegram дверью в память | intake bot, сортировка ссылок/статей, daily digest, draft posts | свой Telegram adapter; RSSidian как reference | автопубликация без подтверждения | новость из Telegram попадает в raw, digest и нужный домен |
| Фаза 5 — Comfy / visual / taste memory | помнить результаты, вкус и визуальные эталоны | Comfy run cards, artifact cards, gold/negative folders, scoring 1–10 | свои markdown cards; later image embeddings | сложный multimodal graph с первого дня | можно объяснить, почему картинка 8/10 или 3/10 |
| Фаза 6 — Эхо и сестрички | Эхо как локальный Джарвис, подагенты как ограниченные сестрички | memory slices, rights, bridges, emotional mode memory, safe action ladder | свой rights-aware orchestrator; Letta/Mem0/ByteRover pilots later | дать подагентам весь vault | Админша/кодер/Comfy-агент видят только свой срез |
| Фаза 7 — graph/agent-native advanced layer | добавлять сложную умность только на устойчивый фундамент | Graphify/Graphiti/Cognee/LightRAG/OpenViking/MemMachine experiments | derived sidecars through adapters | переписать canon под граф | граф даёт пользу на реальных вопросах, а не просто красивую картинку |

## Как понять “закончили фазу — идём дальше”

Можно идти дальше, если:

1. фаза даёт практическую пользу;
2. есть понятный файл/папка/процесс;
3. Эхо или агент может этим пользоваться;
4. человек может открыть `.md` и понять смысл;
5. нет зависимости, которая при обновлении ломает весь мозг.

Фазы можно частично пересекать, но **не надо строить фазу 7, если фазы 0–2 ещё не живые**.

## Что берём от ключевых направлений

### От Karpathy / LLM Wiki

Берём сразу:

- raw → curated;
- compiled wiki pages;
- index pages;
- links между знаниями;
- maintenance loop.

Это входит в фазы 0–1.

### От QMD / retrieval

Берём на фазе 2:

- поиск по vault;
- retrieval перед ответом;
- hybrid search принцип;
- QMD как helper, не truth.

### От LCM / ClawMem

Проверяем на фазе 3:

- continuity;
- compaction resilience;
- runtime memory;
- MCP/hook integration.

Не делаем их единственным мозгом.

### От OpenViking

Пока берём только идею:

- context layers;
- hierarchical context delivery;
- resources/skills/memory как управляемые контексты.

Полный OpenViking — только фаза 7, если реально нужен dispatcher.

### От Mem0/Zep/Letta/MemMachine/ByteRover

Берём как рынок и future pilots:

- agent-native memory;
- user/profile/episodic/procedural memory;
- coding-agent memory;
- evaluation ideas.

Но core Эхо сначала строится через markdown canon + rights + retrieval.

## Что объяснять в будущих презентациях

По каждой фазе потом сделать отдельную презентацию:

- главная мысль;
- лёгкое объяснение;
- технический слой;
- схема;
- инструменты;
- почему выбрали;
- что не вводим;
- критерий готовности.

Стиль: лёгкий дневной cyberpunk 2077, не сухая методичка.
