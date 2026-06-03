# Что менять в текущем vault

Дата: 2026-04-13
Статус: practical migration note

## Коротко

Текущий vault **не надо перестраивать целиком**.

Правильный путь:

> добавить новый каркас памяти рядом с существующим, а потом постепенно подтягивать важное.

Это как не сносить дом, чтобы провести электричество: сначала ставим щиток, подписываем автоматы, потом аккуратно разводим линии.

## Что добавить сразу

Минимальный набор:

1. `SESSION-STATE.md` или рабочий аналог в понятном месте.
2. `ADR/` — решения.
3. `Known_Bad/` — что пробовали и почему не сработало.
4. `Daily/` или согласованный daily слой.
5. `Inbox/Raw/` для входящих статей, Telegram-ссылок, заметок.
6. `Index/MOC` страницы по главным доменам:
   - Echo;
   - OpenClaw;
   - Telegram;
   - Comfy;
   - Visual Taste;
   - Creator/VTuber/blog;
   - Memory Architecture.
7. Минимальные Properties:
   - `type`;
   - `status`;
   - `domain`;
   - `source`;
   - `created`;
   - `updated`;
   - `trust` или `confidence` только где нужно.

## Что не трогать сейчас

- Не переименовывать весь vault.
- Не переносить дневники пачкой.
- Не переписывать старые статьи в новую структуру автоматически.
- Не ломать текущие папки Obsidian.
- Не делать граф обязательной формой хранения.
- Не переносить truth в QMD/vector DB/Graphiti/Cognee/OpenViking.

## Что переносить позже

После фаз 0–2:

- важные memory-статьи из `Clippings`;
- лучшие материалы из `НоваяПамять`;
- документы V2 как архив/appendix;
- user style/emotional docs в curated Echo style memory;
- Comfy workflows и визуальные эталоны;
- Telegram/raw intake history.

## Что оставить архивом

- `НоваяПамятьV2` — архив исследования и предыдущей архитектуры.
- `НоваяПамять` — reference-полка старых материалов.
- старые clipping-файлы — raw/source layer, не canon автоматически.

## Болезненность миграции

| Зона | Болезненность | Почему |
|---|---:|---|
| Добавить SESSION-STATE / ADR / Known_Bad | низкая | новые папки/файлы, старое не ломают |
| Ввести Properties для новых файлов | низкая | не надо править весь vault сразу |
| Сделать MOC/index pages | низкая-средняя | надо руками выбрать главные входы |
| Подключить QMD/hybrid retrieval | средняя | нужна индексация и policy, но canon не мигрирует |
| Telegram intake | средняя | нужны права, безопасность, parsing, daily digest |
| Comfy/visual memory | средняя | надо придумать карточки и gold/negative folders |
| Graph layer | высокая | только после чистых связей и stable retrieval |
| OpenViking/MemOS/agent backend | высокая | может изменить runtime-модель, только через adapter |

## Какие папки уже можно использовать

- `C:\Progi\openfolder_openclaw\openvault\Память\`
- `C:\Progi\openfolder_openclaw\openvault\Память\Настройки памяти\`
- `C:\Progi\openfolder_openclaw\openvault\Патчинг (ПК)\`
- `C:\Progi\openfolder_openclaw\openvault\Проекты\`
- `C:\Progi\openfolder_openclaw\openvault\Информация_и_Гайды\Общение\`
- будущие доменные папки под Telegram/Comfy/Visual — после согласования структуры.

## Какие лучше не ломать

- дневники;
- личные заметки;
- существующие project docs;
- старые clippings;
- runtime/config папки OpenClaw;
- всё, что уже является source of truth проекта.

## Принцип миграции

1. Новые данные пишем уже по v3-правилам.
2. Старые данные не трогаем пачкой.
3. Если старый файл часто нужен — делаем curated summary или index link.
4. Если старый файл конфликтует с новым решением — пишем ADR/Known_Bad.
5. Инструменты подключаем через adapter.
6. Canon остаётся в `.md`.

## Что будет первым реальным шагом внедрения

После утверждения Roadmap:

1. создать минимальный `SESSION-STATE.md`;
2. завести `ADR/` и `Known_Bad/`;
3. выбрать место для `Inbox/Raw`;
4. сделать 3–5 MOC/index pages;
5. подключить/проверить retrieval policy;
6. только потом двигаться к Telegram intake.
