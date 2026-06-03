# Memory Tools Catalog — рабочий справочник OpenClaw

Updated: 2026-04-17  
Folder: `C:\Progi\VibeProjects\Openclaw\НоваяПамятьV3\`  
Visual maps: `MemoryTools_Map_All_Zones.excalidraw` *(главная большая карта всех инструментов по зонам)*  `MemoryTools_Map.excalidraw` *(старый обзор)*  `MemoryTools_Map_V3_Selected.excalidraw` *(устаревшая decision-map, не основная)*

Design note: главная карта оформлена как atlas/poster: широкие glass-cards, статус-шильдик справа, краткая польза под названием, RU+EN заголовки зон, локальный HarmoniaSansProCyr font slot.

## Зачем этот файл

Это **не презентация** и **не NotebookLM-пакет**. Это рабочий каталог memory-инструментов: чтобы быстро понять, что где лежит в зоопарке памяти, кто локальный/open-source, кто SaaS-heavy, кто просто retrieval, а кто реально memory backend.

Простая аналогия: если OpenClaw — это кибер-город, то:

- **Vault / Markdown** — архив и библиотека города.
- **Retrieval / indexing** — метро и поисковые дроны.
- **Agent memory backend** — долгосрочная память жителей-агентов.
- **Graph / Memory OS** — карта связей и городская нервная система.
- **MCP bridges** — шлюзы между районами.
- **Evals** — камеры контроля качества: не врёт ли память и не забывает ли важное.

---

## Быстрый вердикт

### Core local OSS / стоит смотреть в первую очередь

| Инструмент | Почему интересен |
|---|---|
| **Obsidian + Markdown canon** | человекочитаемый source of truth, легко чинить руками |
| **QMD** | локальный hybrid retrieval по Markdown-корпусу |
| **memvid** | serverless/single-file memory: один переносимый артефакт, BM25 + vector |
| **keep** | reflective memory для заметок/файлов, есть OpenClaw-интеграционный вайб |
| **Basic Memory** | local-first Markdown knowledge graph + MCP |
| **Mimir** | локальный memory bank + semantic vector search по файлам |
| **DiffMem** | git-based temporal memory: история, diffs, auditability |
| **agentmemory** | persistent memory именно для coding agents, hooks + BM25/vector + MCP |
| **MCP Memory Service** | общий MCP backend памяти для разных клиентов |
| **MemPalace** | spatial memory palace: wings/rooms/drawers + KG + MCP tools |
| **Memori** | agent-native structured persistent state |
| **Memobase** | долгий user profile / context API |
| **Mem0** | универсальный baseline memory layer, много интеграций |
| **OpenMemory** | local-first memory OS/backend с traces/explainability |
| **MemMachine** | инженерный split: episodic graph DB + profile SQL |
| **MemU** | proactive/always-on memory framework |
| **ALMA-memory** | learning memory: стратегии, anti-patterns, outcomes |
| **EverOS / EverMemOS** | umbrella memory OS: EverCore + HyperMem + benchmarks |
| **Graphiti** | temporal KG для агентной памяти |
| **Cognee** | graph + vector knowledge engine, local mode |
| **LightRAG / GraphRAG** | graph-augmented retrieval baseline |
| **Aegis Memory** | governance/security/trust hierarchy для памяти |

### Watch / mixed model / смотреть осторожно

| Инструмент | Почему осторожно |
|---|---|
| **Honcho** | open/self-host путь есть, но managed/API слой заметный |
| **memphora-sdk** | похоже на platform/service SDK, local-first не главный характер |
| **MemoryKit** | имя мутное, есть несколько кандидатов |
| **Always On Memory Agent** | больше 24/7 runtime, чем универсальный memory backend |
| **Open Brain / OB1** | личная brain-инфраструктура, но надо проверять canonical repo/license |
| **Smart Connections** | полезный Obsidian semantic слой, но есть вопросы license drift |
| **Zep** | сильный temporal KG/backend, но cloud/product слой выражен |
| **Letta** | stateful agent platform, не “чистая память” |

### Omit from local-core / adjacent / historical

| Инструмент | Почему не core |
|---|---|
| **Vault-AI** | старый cloud/OpenAI/Pinecone-style long-term memory app |
| **Fastio / cloud persistent storage** | cloud persistence, не local-first memory core |
| **Gemini/OpenAI embeddings** | полезные API-слои, но не локальный memory backend |
| **LangMem** | завязан на LangGraph/LangChain; полезно как reference, не обязательно тащить |

---

## Корзины архитектуры

| Корзина | Смысл | Типичный вопрос |
|---|---|---|
| **Vault / canonical memory** | где живёт человекочитаемая правда | “Где лежит знание, если агент умер?” |
| **Retrieval / indexing** | как быстро найти нужный кусок | “Как вытащить контекст без ручной охоты?” |
| **Continuity / coding-agent memory** | как не потерять нить между сессиями | “Что агент должен помнить завтра?” |
| **Agent-native backend** | память как backend/API для агентов | “Куда агент пишет факты и события?” |
| **Profile / user memory** | долгий профиль пользователя/персоны | “Что система знает про человека?” |
| **Memory OS / orchestration** | update/retrieve/reflect/schedule | “Кто управляет жизненным циклом памяти?” |
| **Graph / temporal / hypergraph** | связи, история, multi-hop reasoning | “Как связаны факты и как они менялись?” |
| **MCP / bridge / service** | общий шлюз памяти для клиентов | “Как дать память разным агентам?” |
| **Eval / benchmark** | проверка recall/галлюцинаций/качества | “Память вообще работает или красиво врёт?” |
| **Cloud / SaaS-heavy** | полезно, но не local-first core | “Где риск lock-in?” |
| **Ambiguous / needs verification** | мутные имена/несколько реп | “Что именно мы имеем в виду?” |

---

## Master catalog

> `Local` = можно запускать локально или self-host.  
> `OSS` = исходники/лицензия доступны или заявлены.  
> `SaaS risk`: Low / Med / High / Unknown.  
> `Verdict`: core / watch / adjacent / omit / idea / verify.

| # | Инструмент | Корзина | Local / OSS | SaaS risk | Что это такое | Чем отличается | Вердикт | Ссылка |
|---:|---|---|---|---|---|---|---|---|
| 1 | Obsidian + Markdown canon | Vault / canonical memory | Local / OSS-ish app ecosystem | Low | Главный человекочитаемый источник правды в `.md` | Если всё сломалось, знания всё равно открываются текстом | core | [Obsidian](https://obsidian.md/) |
| 2 | WikiLinks / MOCs / Daily notes | Vault architecture | Local | Low | Система связей, входных страниц и дневного слоя | Навигационный скелет vault | core | [MOC forum](https://forum.obsidian.md/t/a-case-for-mocs/2418) |
| 3 | Obsidian Properties | Metadata | Local | Low | YAML/properties поверх заметок | Минимальная структурность без базы данных | core | [docs](https://obsidian.md/help/properties) |
| 4 | Obsidian Bases | Database view over Markdown | Local | Low | Табличные представления поверх `.md` | Можно смотреть vault как lightweight DB | core | [docs](https://obsidian.md/help/bases) |
| 5 | SESSION-STATE.md / hot RAM | Continuity | Local / own pattern | Low | Горячее состояние текущей работы | Не память навсегда, а “что сейчас на столе” | idea/core pattern | local pattern |
| 6 | ADR / Known_Bad | Governance / negative memory | Local / own pattern | Low | Решения, запреты, антипаттерны | Память не только “что делать”, но и “куда не лезть” | core pattern | local pattern |
| 7 | QMD | Retrieval / indexing | Local / OSS | Low | Локальный поиск по Markdown/docs, hybrid query | Поисковый движок, не memory backend | core | [GitHub](https://github.com/tobi/qmd) |
| 8 | BM25 / lexical search | Retrieval primitive | Local primitive | Low | Точный поиск по словам | Ловит имена, код, точные термины лучше вектора | core primitive | [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) |
| 9 | Hybrid search: BM25 + vector + rerank | Retrieval architecture | Local possible | Low-Med | Комбинация точного и смыслового поиска | Базовая архитектура нормального recall | core pattern | local research |
| 10 | Local embeddings | Retrieval primitive | Local | Low | Локальный смысловой поиск | Сохраняет privacy, но требует моделей/ресурсов | core | [MTEB](https://huggingface.co/spaces/mteb/leaderboard) |
| 11 | Qwen embeddings | Embeddings | Local/API possible | Low-Med | Мультиязычные embeddings RU/EN | Хороший кандидат для русско-английского vault | verify | [Qwen3 Embedding](https://qwenlm.github.io/blog/qwen3-embedding/) |
| 12 | Gemini API embeddings | API embeddings | API | High | API semantic retrieval | Качество без локальной модели, но cloud | adjacent | [docs](https://ai.google.dev/gemini-api/docs/embeddings) |
| 13 | OpenAI embeddings | API embeddings | API | High | API embeddings для RAG | Quality-first, но не local-first | adjacent | [docs](https://developers.openai.com/api/docs/guides/embeddings) |
| 14 | Vector DB / vector index | Retrieval storage | Local possible | Low-Med | Индекс embeddings/similarity | Инфраструктурный слой, не память сам по себе | core layer | [LanceDB](https://github.com/lancedb/lancedb) |
| 15 | LCM / Lossless Claw | Continuity / compaction | Local / OSS | Low-Med | Сохранять смысл при compaction | Интересен как “не потерять мысль при сжатии” | watch | [GitHub](https://github.com/Martian-Engineering/lossless-claw) |
| 16 | ClawMem | Agent memory / hybrid RAG | Local / OSS | Low-Med | On-device memory layer для Claude Code/OpenClaw | Близко к нашему домену, но надо тестить качество | watch | [GitHub](https://github.com/yoloshii/ClawMem) |
| 17 | OpenViking | Context DB / context FS | Local/OSS likely | Med | Унификация context/resources/skills/memory | Больше context filesystem, чем точечная память | watch later | [GitHub](https://github.com/volcengine/OpenViking) |
| 18 | Karpathy / LLM Wiki pattern | Wiki memory concept | Local pattern | Low | Raw → compiled wiki | Сильный паттерн: агент компилирует свою энциклопедию | idea | [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| 19 | LLM Wiki v2 / agentmemory gist | Wiki refinement | Local pattern | Low | Расширение LLM Wiki pattern | Не путать с repo `rohitg00/agentmemory` | idea | [gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) |
| 20 | llm-wiki-kit | Wiki compiler | Local/OSS | Low-Med | Wiki из PDFs/URLs/YouTube | Может быть ingest/compiler, не backend памяти | verify | [GitHub](https://github.com/iamsashank09/llm-wiki-kit) |
| 21 | SwarmVault | Wiki/compiler | Local-first/OSS | Low-Med | Raw research → Markdown wiki + graph + search | Похож на pipeline для исследовательского vault | watch | [GitHub](https://github.com/swarmclawai/swarmvault) |
| 22 | Knowledge Vault | Obsidian+Claude workflow | Local pattern | Low | Personal knowledge system на markdown+skills | Reference для workflow, не продукт | idea | [gist](https://gist.github.com/naushadzaman/164e85ec3557dc70392249e548b423e9) |
| 23 | Basic Memory | Vault-first / KG / MCP | Local / AGPL-3.0 | Med | Local-first knowledge graph на Markdown | “Дом знаний” с graph/MCP, не просто поиск | core/watch | [GitHub](https://github.com/basicmachines-co/basic-memory) |
| 24 | Claudesidian | Obsidian starter | Local / OSS | Low | Шаблон vault под Claude/agents | Полезен как стартовая структура | idea | [GitHub](https://github.com/heyitsnoah/claudesidian) |
| 25 | Obsidian Memory MCP | MCP / vault bridge | Local / OSS | Low-Med | AI memories as Markdown files | MCP-мост, где память = заметки | watch | [GitHub](https://github.com/YuNaga224/obsidian-memory-mcp) |
| 26 | Obsidian MCP Plugin | MCP / vault bridge | Local / OSS | Low-Med | LLM ↔ Obsidian через MCP | Plugin-side bridge, проверить стабильность | verify | [GitHub](https://github.com/jlevere/obsidian-mcp-plugin) |
| 27 | Obsidian local LLM hub | Obsidian AI overlay | Local / OSS | Low-Med | Локальный чат/RAG/workflows внутри Obsidian | UI/assistant слой над vault | watch later | [GitHub](https://github.com/takeshy/obsidian-local-llm-hub) |
| 28 | RSSidian | Intake / RSS → Markdown | Local / OSS | Low | Ингест RSS в Markdown | Память начинается с intake, не только recall | idea | [GitHub](https://github.com/pedramamini/RSSidian) |
| 29 | Graphify | Graph / codebase understanding | Local / MIT signal | Low | Folder/code/docs/PDFs → queryable KG | Больше repo-understanding, чем generic memory | watch/core graph | [site](https://graphify.net/) |
| 30 | Graphiti | Graph / temporal memory | Local / OSS | Med | Temporal KG для AI agents | Граф с историей изменений, не static KG | core graph | [GitHub](https://github.com/getzep/graphiti) |
| 31 | Cognee | Graph / hybrid retrieval | Local / OSS | Med | Knowledge engine: graph + vector + ingestion | Больше pipeline/engine, чем простой RAG | core/watch | [GitHub](https://github.com/topoteretes/cognee) |
| 32 | LightRAG | Graph / RAG engine | Local / MIT | Low-Med | Быстрый graph-augmented RAG | RAG engine, не memory OS | core baseline | [GitHub](https://github.com/HKUDS/LightRAG) |
| 33 | GraphRAG | Graph / RAG baseline | Local / MIT | Low-Med | Graph-based retrieval over datasets | Классический baseline для сложного discovery | core baseline | [Microsoft](https://microsoft.github.io/graphrag/) |
| 34 | Mem0 | Agent memory backend | Local/self-host / Apache-2.0 | Med | Universal memory layer for AI agents | Самый baseline-кандидат для сравнения backend-памяти | core/watch | [GitHub](https://github.com/mem0ai/mem0) |
| 35 | Zep | Graph-backed backend | CE/self-host + cloud | High-Med | Session/user memory + temporal KG | Сильная платформа, но cloud/product уклон | watch | [GitHub](https://github.com/getzep/zep) |
| 36 | Letta | Stateful agent platform | Local / Apache-2.0 | Med | Stateful agents with memory blocks | Это agent runtime/platform, не просто memory store | watch | [GitHub](https://github.com/letta-ai/letta) |
| 37 | LangMem | Framework memory tools | Local in LangGraph stack | Med | Memory tools для LangGraph/LangChain | Полезно, если идём в LangGraph; иначе не core | adjacent | [GitHub](https://github.com/langchain-ai/langmem) |
| 38 | MemOS | Memory OS / orchestration | Local / Apache signal | Low-Med | Memory OS for LLM/agent systems | Не путать с MemoryOS; broader system-level OS | core/watch | [GitHub](https://github.com/MemTensor/MemOS) |
| 39 | MemMachine | Agent backend / system | Local / Apache-2.0 | Low-Med | Episodic + profile memory via REST/Python/MCP | Чёткий split: graph episodic + SQL profile | core/watch | [GitHub](https://github.com/MemMachine/MemMachine) |
| 40 | ByteRover CLI / Cipher | Coding-agent memory | Local/OSS | Med | Portable memory layer для coding agents | Memory as CLI/coding workflow layer | watch | [GitHub](https://github.com/campfirein/byterover-cli) |
| 41 | MemU | Proactive memory framework | Local/self-host / Apache-2.0 | Med | 24/7 proactive memory, multimodal → hierarchy | “Память как файловая система + always-on” | core/watch | [GitHub](https://github.com/NevaMind-AI/memU) |
| 42 | OpenMemory | Local memory OS/backend | Local / Apache-2.0 | Low-Med | Local persistent memory store / Memory OS | Explainable traces, SQLite/Docker, local-first | core | [GitHub](https://github.com/CaviraOSS/OpenMemory) |
| 43 | OpenLethe / Lethe | Persistent memory layer | Local/OSS | Unknown | Persistent memory для agents | Нужно перепроверить активность/роль | verify | [GitHub](https://github.com/openlethe/lethe) |
| 44 | Hindsight | Memory OS / learning memory | Local / MIT | Med | Retain / recall / reflect memory banks | Biomimetic memory banks, learning via reflection | core/watch | [GitHub](https://github.com/vectorize-io/hindsight) |
| 45 | Mengram | Human-like memory | Local/OSS | Unknown | Semantic/episodic/procedural memory | Learning from failures / human-memory vibe | verify | [GitHub](https://github.com/alibaizhanov/mengram) |
| 46 | Hipocampus | Lifecycle / memory harness | Local/OSS | Unknown | 3-tier memory, compaction tree, hybrid search | Hippocampus-style lifecycle framing | verify | [GitHub](https://github.com/kevin-hs-sohn/hipocampus) |
| 47 | MemAware benchmark | Eval / benchmark | Unknown | Unknown | Проверяет memory awareness | Benchmark, не memory engine | eval/verify | [GitHub](https://github.com/kevin-hs-sohn/memaware) |
| 48 | GBrain | Brain/context repo | Local/OSS | Unknown | Экспериментальная brain/memory система | Adjacent personal brain reference | verify | [GitHub](https://github.com/garrytan/gbrain) |
| 49 | Dependency-Free Memory Palace / MemPalace concept | Concept | Local pattern | Low | Memory palace без зависимостей | Не путать с official MemPalace repo | idea | [gist](https://gist.github.com/jrswab/f230d2576bbdf899a56693285e7e0453) |
| 50 | Aether | Unknown / memory candidate | OSS? | Unknown | Ранее not verified, найден публичный repo | Требует отдельной проверки роли | verify | [GitHub](https://github.com/S-HARI-S/Aether) |
| 51 | Fastio / cloud persistent storage | Cloud persistence | Cloud | High | Cloud storage, locks, RAG search | Не local-first core | omit | [article](https://fast.io/resources/openclaw-persistent-storage/) |
| 52 | Smart Connections | Obsidian semantic retrieval | Local possible / license caution | Med | Semantic search/chat-with-notes в Obsidian | UI discovery layer внутри vault | watch | [GitHub](https://github.com/brianpetro/obsidian-smart-connections) |
| 53 | Tezcat | Obsidian remembrance agent | Local/OSS | Unknown | Memory assist во время письма | Похоже на “напоминалку смысла”, не backend | adjacent | [GitHub](https://github.com/mmargenot/tezcat) |
| 54 | Second Brain AI agent | Markdown → vector → agent | Local/OSS | Low-Med | Мост markdown-корпуса к agent workflow | Reference pipeline для second brain | idea/watch | [GitHub](https://github.com/flepied/second-brain-agent) |
| 55 | Obsidian MCP Server | MCP / vault bridge | Local/OSS | Low-Med | Agent ↔ Obsidian через MCP | Ещё один vault bridge candidate | watch | [GitHub](https://github.com/newtype-01/obsidian-mcp) |
| 56 | Smart Composer | Obsidian copilot | Local/API mix | Med | Note-native copilot + semantic search | UX слой написания/редактирования заметок | watch | [GitHub](https://github.com/glowingjade/obsidian-smart-composer) |
| 57 | Local LLM Helper | Obsidian local utility | Local/OSS | Low | Chat/processing/semantic search | Лёгкий pragmatic plugin | watch | [GitHub](https://github.com/manimohans/obsidian-local-llm-helper) |
| 58 | Perplexed | Research / citations | Local/API mix | Med | Reference-driven generation with citations | Research intake, не долгосрочная память | adjacent | [GitHub](https://github.com/lossless-group/perplexed-plugin) |
| 59 | Memento MCP | MCP / persistent memory | Local/OSS | Low-Med | Long-term memory + KG + MCP | Хороший reference для MCP memory | watch | [GitHub](https://github.com/gannonh/memento-mcp) |
| 60 | Smart Connect | Local bridge | Local/OSS | Low-Med | Notes/tools/chat bridge | Агентские руки к локальным данным | watch | [GitHub](https://github.com/brianpetro/smart-connect) |
| 61 | ReMe | Agent memory kit | Local/OSS | Low-Med | File-based + vector memory, compaction, recall | Practical kit, не тяжёлая OS | watch | [GitHub](https://github.com/agentscope-ai/ReMe) |
| 62 | Mnemosyne | Coding continuity / orchestration | Local/OSS | Unknown | Persistent memory/orchestration for coding agents | Больше orchestration, чем vault memory | watch | [GitHub](https://github.com/rand/mnemosyne) |
| 63 | DiffMem | Git-based memory | Local/OSS | Low | Markdown + Git history + BM25 | Версионность и temporal depth через Git | core/watch | [GitHub](https://github.com/Growth-Kinetics/DiffMem) |
| 64 | In Memoria | Coding assistant memory infra | Local / MIT | Low | MCP, project blueprints, work context routing | Codebase intelligence + routing to files | core/watch | [GitHub](https://github.com/pi22by7/In-Memoria) |
| 65 | Mem4AI | Multi-level memory library | Local/OSS | Unknown | user/session/agent memory baseline | Лёгкий baseline без тяжёлой OS | watch | [GitHub](https://github.com/unclecode/mem4ai) |
| 66 | SimpleMem | Lifelong / compression | Local/OSS | Unknown | continuity/compression candidate | Semantic compression angle | watch/verify | [GitHub](https://github.com/aiming-lab/SimpleMem) |
| 67 | HMLR | Governance / memory architecture | Local/OSS described | Med | Living memory, conflict resolution, policy reasoning | Policy/adversarial/multi-hop акцент | watch | [GitHub](https://github.com/Sean-V-Dev/HMLR-Agentic-AI-Memory-System) |
| 68 | WeKnora | Knowledge orchestration | Local/OSS | Med | memory-aware retrieval/orchestration | Больше knowledge orchestration, чем память | adjacent/watch | [GitHub](https://github.com/Tencent/WeKnora) |
| 69 | GoodAI LTM | Long-term memory / benchmark | Local/OSS | Low | Long-term memory for agents | Хороший LTM/eval reference | watch/eval | [GitHub](https://github.com/GoodAI/goodai-ltm) |
| 70 | memora | Profile / temporal memory | Local likely / Apache-2.0 | Med | Human-memory-like temporal recall | Agent identity + timestamped recall | watch | [GitHub](https://github.com/ELZAI/memora) |
| 71 | memvid | File-native / single-file memory | Local / MIT | Low | Serverless memory in one `.mv2` file, BM25 + vector + timeline | “Память в коробке”: portable, zero-infra | core | [GitHub](https://github.com/Olow304/memvid) / [docs](https://docs.memvid.com/) |
| 72 | keep | Vault/file-native reflective memory | Local / OSS claimed | Low | Конспектирует, индексирует и связывает notes/files | Reflective note/file memory, близко к OpenClaw | core | [GitHub](https://github.com/keepnotes-ai/keep) / [docs](https://docs.keepnotes.ai/guides/openclaw/) |
| 73 | Memori | Agent-native backend | Local/self-host / Apache-2.0 | Med | Execution + conversation → structured persistent state | Сильнее в “agent state fabric”, чем profile-only | core/watch | [GitHub](https://github.com/MemoriLabs/Memori) |
| 74 | Memobase | Profile / user memory | Self-host / Apache-2.0 | Med | Long-term user profile + context API | “Досье пользователя”, не общий vault | core/watch | [GitHub](https://github.com/memodb-io/memobase) |
| 75 | MCP Memory Service | MCP / service backend | Local / MIT signal | Med | MCP memory backend для Claude/Cursor/многих tools | Transport/service layer для общей памяти | core | [GitHub](https://github.com/doobidoo/mcp-memory-service) |
| 76 | Mimir | File-native + retrieval + orchestration | Local / MIT + terms | Low | Memory bank + semantic vector search for local files | Похоже на local shared memory bank | core | [GitHub](https://github.com/orneryd/Mimir) |
| 77 | agentmemory | Coding-agent continuity | Local / Apache-2.0 | Low-Med | Persistent memory for coding agents, hooks, BM25+vector, MCP | Repo-инструмент, не gist-паттерн | core | [GitHub](https://github.com/rohitg00/agentmemory) |
| 78 | MemPalace official | Spatial memory / MCP / KG | Local / MIT signal | Low | Memory palace: wings/rooms/halls/drawers + KG + MCP | Opinionated spatial recall model | core/watch | [GitHub](https://github.com/MemPalace/mempalace) / [site](https://mempalaceofficial.com/) |
| 79 | EverOS / EverMemOS | Memory OS / orchestration | Local / Apache-2.0 | Low-Med | Umbrella stack: EverCore + HyperMem + benchmarks | Не один backend, а research/OS stack | core/watch | [GitHub](https://github.com/EverMind-AI/EverOS) |
| 80 | EverCore | Memory OS core | Local / Apache-2.0 | Low-Med | Core long-term memory OS внутри EverOS | Ядро, не graph feature | core component | [EverOS](https://github.com/EverMind-AI/EverOS) |
| 81 | HyperMem | Graph / hypergraph memory | Local / Apache-2.0 | Low-Med | Hypergraph memory architecture в EverOS | Гиперграфовый слой связей | core component | [EverOS](https://github.com/EverMind-AI/EverOS) |
| 82 | MemoryOS | Memory OS / personalized agents | Local / Apache-2.0 | Med | Storage/update/retrieval/generation for personalized agents | Отдельный проект, не MemOS | watch/core | [GitHub](https://github.com/BAI-LAB/MemoryOS) |
| 83 | ALMA-memory | Learning/profile memory | Local / MIT | Low-Med | Learns strategies, anti-patterns, outcomes | Память про “что сработало/провалилось” | core/watch | [GitHub](https://github.com/RBKunnela/ALMA-memory) |
| 84 | Honcho | Stateful agent backend | Self-host + managed / license verify | Med-High | Sessions, peers, working representations | Peer/stateful design, не простой store | watch | [GitHub](https://github.com/plastic-labs/honcho) |
| 85 | memphora-sdk | SDK / service layer | OSS MIT signal / local unclear | Med-High | Persistent memory SDK/platform family | Похоже на platform SDK, не pure local engine | watch | [GitHub](https://github.com/Memphora/memphora-sdk) |
| 86 | MemoryKit | Agent memory backend candidate | OSS-looking / unclear | Med | Persistent memory layer for agents | Мутное имя, несколько проектов | ambiguous/watch | [GitHub](https://github.com/0j/memorykit) |
| 87 | Aegis Memory | Governance / security memory | Local / Apache-2.0 signal | Low-Med | Trust hierarchy, integrity, audit vibe | Не просто хранит, а управляет доверием | watch/core if governance | [GitHub](https://github.com/quantifylabs/aegis-memory) |
| 88 | Open Brain / OB1 | Personal brain infra | Local-ish / license unclear | Low-Med | Database + AI gateway + chat/channel + memory | Brain infrastructure, не memory backend only | watch | [GitHub](https://github.com/NateBJones-Projects/OB1) |
| 89 | MARM-Systems | MCP / multi-agent memory | Local / MIT | Med | Universal MCP server for persistent multi-agent memory | MCP-first memory transport | watch/core bridge | [GitHub](https://github.com/Lyellr88/MARM-Systems) |
| 90 | Vault-AI | Cloud-heavy historical app | OSS / OpenAI+Pinecone-era | High | ChatGPT with long-term memory style app | Исторический пример, не local-first core | omit/adjacent | [GitHub](https://github.com/pashpashpash/vault-ai) |
| 91 | Always On Memory Agent | Continuity / 24/7 runtime | Local likely / MIT signal | Med | Always-on agent runtime with persistent memory | Runtime/worker, не generic backend | watch | [GitHub](https://github.com/mxyhi/always-on-memory-agent) |
| 92 | Hippocampus-memory-mcp | MCP / lifecycle memory | Local / verify | Low-Med | MCP server with consolidation/forgetting/retrieval | Applied hippocampus-inspired MCP server | watch | [PyPI](https://pypi.org/project/hippocampus-memory-mcp/) |
| 93 | hippocampus.md | Protocol / lifecycle memory | Partial/unknown | Med | Context lifecycle protocol, sparse indexing | Spec/protocol layer, не product-first repo | adjacent/verify | [site](https://hippocampus.md/) |
| 94 | HaluMem | Eval / hallucination benchmark | Local/OSS likely | Low-Med | Benchmark for memory-induced hallucination | Проверяет, когда память заставляет врать | eval | [GitHub](https://github.com/MemTensor/HaluMem) |
| 95 | GoodAI LTM Benchmark | Eval / benchmark | Local/OSS | Low | Benchmark for long-term memory/continual learning | General LTM benchmark | eval | [GitHub](https://github.com/GoodAI/goodai-ltm-benchmark) |
| 96 | EverMemBench | Eval / benchmark | Local / Apache-2.0 | Low | Benchmark suite внутри EverOS | Встроенная оценка memory quality | eval | [EverOS](https://github.com/EverMind-AI/EverOS) |
| 97 | EvoAgentBench | Eval / agent evolution | Local / Apache-2.0 | Low | Self-evolution evaluation внутри EverOS | Больше agent evolution, чем pure memory recall | eval/adjacent | [EverOS](https://github.com/EverMind-AI/EverOS) |

---

## Как отличать похожие инструменты

### memvid vs Basic Memory

- **memvid** — “память в одном переносимом контейнере”: single-file `.mv2`, hybrid search, timeline.
- **Basic Memory** — “дом знаний”: Markdown + knowledge graph + MCP.

Если грубо: `memvid` — флешка с быстрым индексом, `Basic Memory` — библиотека с полками и связями.

### keep vs Smart Connections

- **keep** — reflective memory layer: конспектирует, индексирует, связывает notes/files, ближе к OpenClaw-memory.
- **Smart Connections** — Obsidian UI/discovery слой: semantic search и связанные заметки внутри vault.

`keep` больше про память как слой, `Smart Connections` больше про навигацию и поиск.

### Mimir vs QMD

- **QMD** — search/retrieval engine по Markdown.
- **Mimir** — memory bank с local file indexing, shared memories и orchestration vibe.

`QMD` — поисковая собака. `Mimir` — маленький архивариус с картотекой.

### DiffMem vs agentmemory

- **DiffMem** — Git/diff/time-based memory: история изменений как источник recall.
- **agentmemory** — coding-agent memory: hooks, working memory, BM25/vector, MCP.

`DiffMem` помнит “как менялось”, `agentmemory` помнит “что агенту нужно продолжать”.

### Memori vs Memobase

- **Memori** — structured state из диалогов и действий агента.
- **Memobase** — долгий user profile/context API.

`Memori` — состояние агента, `Memobase` — досье пользователя.

### Honcho vs Mem0

- **Mem0** — универсальный baseline memory layer.
- **Honcho** — stateful peer/session backend с managed/service уклоном.

`Mem0` проще сравнивать и пилотировать, `Honcho` интереснее как система отношений/состояний.

### MemOS vs MemoryOS

- **MemOS** — проект `MemTensor/MemOS`, broader memory OS для LLM/agent systems.
- **MemoryOS** — отдельный проект `BAI-LAB/MemoryOS`, personalized agents, academic/research vibe.

Их нельзя склеивать. Название похоже, но это разные звери.

### EverOS vs MemoryOS

- **EverOS** — umbrella stack: EverCore + HyperMem + EverMemBench + use-cases.
- **MemoryOS** — focused memory OS для personalized agents.

`EverOS` — набор лабораторий в одном корпусе. `MemoryOS` — отдельная операционка памяти.

### Graphiti vs GraphRAG

- **Graphiti** — temporal knowledge graph for agents, relationships change over time.
- **GraphRAG** — graph-augmented retrieval over datasets.

`Graphiti` больше про живую историю агента, `GraphRAG` — про структурированный поиск по данным.

### Cognee vs LightRAG

- **Cognee** — broader knowledge engine: graph + vector + ingestion pipelines.
- **LightRAG** — быстрый RAG engine с graph extraction.

`Cognee` — фабрика знаний. `LightRAG` — быстрый retrieval-мотор.

### MCP Memory Service vs MARM-Systems

- **MCP Memory Service** — generic MCP memory backend для разных clients.
- **MARM-Systems** — MCP-first hub for persistent multi-agent memory/context sharing.

Оба bridge/service, но MARM сильнее заявлен как multi-agent transport.

### MemPalace concept vs MemPalace official

- **Dependency-Free Memory Palace gist** — идея/паттерн.
- **MemPalace official repo** — отдельный инструмент с spatial hierarchy, KG, MCP tools.

Не путать “философию дворца памяти” и конкретный проект.

### Vault-AI vs local-first tools

- **Vault-AI** — хороший исторический ориентир старой волны: OpenAI/Pinecone-style memory app.
- **local-first stack** — Markdown/vault/local retrieval/self-host backends.

Vault-AI можно держать как музейный экспонат: полезно посмотреть, но не строить на нём V3.

---

## Что потенциально тащить в OpenClaw V3 как слои

### Минимальный локальный каркас

1. **Obsidian/Markdown canon** — источник правды.
2. **QMD + BM25/vector/rerank** — retrieval слой.
3. **SESSION-STATE + ADR/Known_Bad** — hot memory + governance.
4. **MCP bridge** — чтобы агенты могли читать/писать контролируемо.
5. **Eval notes/benchmarks** — чтобы проверять качество recall.

### Экспериментальные кандидаты

| Слой | Кандидаты |
|---|---|
| File-native memory | `memvid`, `keep`, `Mimir`, `MemPalace` |
| Coding continuity | `agentmemory`, `DiffMem`, `In Memoria`, `ByteRover` |
| Agent backend | `Memori`, `Mem0`, `OpenMemory`, `MemMachine` |
| Profile memory | `Memobase`, `ALMA-memory`, `Memora` |
| Graph layer | `Graphiti`, `Cognee`, `LightRAG`, `GraphRAG` |
| Memory OS | `EverOS`, `MemOS`, `MemoryOS`, `Hindsight` |
| MCP service | `MCP Memory Service`, `MARM-Systems`, `Memento MCP` |
| Evals | `GoodAI LTM Benchmark`, `HaluMem`, `EverMemBench`, `MemAware` |

---

## Ссылки-источники для текущего расширения

Primary/project links used in this pass:

- [memvid](https://github.com/Olow304/memvid), [docs](https://docs.memvid.com/)
- [keep](https://github.com/keepnotes-ai/keep), [OpenClaw guide](https://docs.keepnotes.ai/guides/openclaw/)
- [Memori](https://github.com/MemoriLabs/Memori)
- [Memobase](https://github.com/memodb-io/memobase)
- [MCP Memory Service](https://github.com/doobidoo/mcp-memory-service)
- [Mimir](https://github.com/orneryd/Mimir)
- [agentmemory](https://github.com/rohitg00/agentmemory)
- [MemPalace](https://github.com/MemPalace/mempalace), [site](https://mempalaceofficial.com/)
- [EverOS](https://github.com/EverMind-AI/EverOS), [docs](https://docs.evermind.ai/)
- [MemoryOS](https://github.com/BAI-LAB/MemoryOS)
- [ALMA-memory](https://github.com/RBKunnela/ALMA-memory)
- [Honcho](https://github.com/plastic-labs/honcho), [docs](https://docs.honcho.dev/)
- [memphora-sdk](https://github.com/Memphora/memphora-sdk)
- [MemoryKit candidate](https://github.com/0j/memorykit)
- [Aegis Memory](https://github.com/quantifylabs/aegis-memory)
- [OB1](https://github.com/NateBJones-Projects/OB1)
- [MARM-Systems](https://github.com/Lyellr88/MARM-Systems)
- [Vault-AI](https://github.com/pashpashpash/vault-ai)
- [Always On Memory Agent](https://github.com/mxyhi/always-on-memory-agent)
- [Graphiti](https://github.com/getzep/graphiti)
- [Cognee](https://github.com/topoteretes/cognee)
- [LightRAG](https://github.com/HKUDS/LightRAG)
- [GraphRAG](https://microsoft.github.io/graphrag/)
- [HaluMem](https://github.com/MemTensor/HaluMem)
- [GoodAI LTM Benchmark](https://github.com/GoodAI/goodai-ltm-benchmark)

---

## Примечание по точности

Каталог — рабочий, а не юридическая экспертиза лицензий. Где лицензия/локальность не была уверенно подтверждена, стоит метка `verify`, `watch` или `ambiguous`. Перед реальным внедрением любого инструмента нужно отдельно проверить:

- актуальную лицензию;
- свежесть репозитория;
- self-host путь;
- зависимости от cloud/API;
- наличие MCP/CLI/SDK;
- насколько хорошо он ложится в OpenClaw V3.

