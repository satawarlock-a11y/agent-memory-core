# Memory Tools V2 — Activity Status Pass

Updated: 2026-05-20  
Source base: `C:\Progi\VibeProjects\Openclaw\НоваяПамятьV3\MemoryTools_Catalog_V2_Merged_2026-05-20.md`

This file is a maintenance-status pass over the **V2 merged additions**.

Status meanings:
- **ACTIVE** — recent commit/release/issues/docs movement suggests the project is currently alive.
- **STALE / ABANDONED** — public code/release signal looks quiet enough to treat the project as risky.
- **UNCERTAIN** — mixed signal, ambiguous canonical repo, or too little evidence.

Important note:
- Dates and repo metadata are **facts**.
- The final status label is an **inference** from those facts.

---

## 1) Actively developing / alive now

| Project | Evidence | Confidence |
|---|---|---|
| **LycheeMemory** | open-sourced 2026-03-23; commits on 2026-05-13 | High |
| **Remnic** | commits on 2026-05-19 and 2026-05-20 | High |
| **neo4j-labs/agent-memory** | commits on 2026-05-18 | High |
| **neo4j-labs/create-context-graph** | commits on 2026-05-19; v0.12.0 release prep | High |
| **TiMEM** | commits on 2026-04-07; very early-stage but still moving | Medium |
| **KektorDB** | commits on 2026-05-11 and 2026-05-17 | High |
| **superlocalmemory** | commit 2026-05-18; issue activity 2026-05-16 | High |
| **total-agent-memory** | commit + release on 2026-05-20 | High |
| **Engram** | commit 2026-05-20; release 2026-05-18 | High |
| **nocturne_memory** | commit 2026-05-15; release 2026-05-14 | High |
| **MegaMemory** | commit + release on 2026-05-03; issue updated 2026-05-10 | Med-High |
| **krusch-context-mcp** | commit 2026-05-20 | Medium |
| **agora-code** | commit 2026-04-09; issue updated 2026-04-04 | Medium |
| **mimirs** | commit 2026-04-29 | Medium |
| **codebase-memory-mcp** | commit 2026-05-19; release 2026-05-04 | High |
| **openclaw-basic-memory** | release + commit on 2026-05-05 | High |
| **ClawXMemory** | commit 2026-04-15; repo updated 2026-05-08 | Med-High |
| **graph-memory** | commit 2026-04-07; repo updated 2026-05-19 | Medium |
| **obsidian-vault-mcp** | commit 2026-05-19 | High |
| **mcpvault** | commit 2026-04-16; repo updated 2026-05-20 | High |
| **obsidian-remote-mcp** | commit 2026-05-15 | High |
| **Obsidian_FolderBridge** | commit 2026-04-08; repo updated 2026-05-20 | Med-High |
| **TurboVault** | commit 2026-05-19 | High |
| **obsidian-graph** | commit 2026-05-13 | High |
| **commonplace** | release v0.6.0 on 2026-05-16; commit same day | High |
| **dory** | commit 2026-05-12 | High |
| **frozo-vault-mem** | commit 2026-05-20 | High |
| **contextual-memory-architecture** | commit 2026-05-14 | Med-High |
| **sovereign-memory** | commit 2026-05-19 | High |
| **onebrain** | commit 2026-05-20 | High |
| **mind-mem** | commit 2026-05-20 | High |
| **Agent Recall** | repo/site updated 2026-04-23 | Med-High |
| **CtxVault** | repos updated 2026-05-18 and 2026-05-20 | High |
| **Hive Memory** | repos updated 2026-05-04 and 2026-05-13 | Medium |
| **Recall** | repo updated 2026-05-14 | High |
| **Bossa** | package released 2026-03-07; launch signal 2026-03-17 | Med-High |
| **Wire Memory** | repo updated 2026-05-19 | High |
| **LoCoMo** | repo updated 2026-05-20 | High |
| **LongMemEval** | repo updated 2026-05-20 | High |
| **AMA-Bench** | repo updated 2026-05-07 | High |
| **Mem-Gallery** | repo updated 2026-05-18 | High |
| **BEAM** | repo updated 2026-05-20 | High |

---

## 2) Stale / abandoned / risky due to silence

| Project | Evidence | Confidence |
|---|---|---|
| **GraphZep** | commits stop at 2025-08-24; only a handful of commits | High |
| **agentic-memory** | commit 2026-03-08; release 2026-02-23; no later strong movement | Medium |
| **codex-mem** | commit + release both on 2026-03-07; no later visible movement | Medium |
| **Agent Replay** | initial commit 2026-02-20; no releases; no later visible movement | Medium |
| **letta-obsidian** | latest commit 2026-02-11; repo updated later but code looks quiet | Medium |
| **gigabrain** | last meaningful commit 2025-01-18; project explicitly marked discontinued / archived by org signal | High |

---

## 3) Uncertain / gray zone

| Project | Why uncertain | Confidence |
|---|---|---|
| **Redis Agent Memory Server** | docs live; last visible code signal around 2026-02-26; maybe maintained, but code freshness is not strong | Medium |
| **MemoryGraph** | docs exist and repo looks real, but code signal is quiet since 2026-02-12 | Medium |
| **Sediment** | good architecture signal, but code movement looks quiet since 2026-02-14 | Medium |
| **obsidian-web-mcp** | initial release 2026-03-17, repo updated later; not enough code churn yet to call robustly active | Medium |
| **pebble** | commit 2026-05-05 but thin signal overall, no release cadence | Low-Med |
| **Memory Store** | name is too generic; multiple candidate repos; canonical project unclear | Medium |
| **Parsidion CC** | community signal exists, but canonical public repo is unclear | Low-Med |

---

## 4) Short practical read

### Strongest ACTIVE cluster
If you only want the clearly breathing ones from the added V2 pool, the strongest cluster is:
- LycheeMemory
- Remnic
- neo4j-labs/agent-memory
- neo4j-labs/create-context-graph
- KektorDB
- superlocalmemory
- total-agent-memory
- Engram
- codebase-memory-mcp
- obsidian-vault-mcp
- mcpvault
- obsidian-remote-mcp
- TurboVault
- commonplace
- dory
- frozo-vault-mem
- onebrain
- mind-mem

### Strongest STALE warnings
These are the ones I would mark as risky if you care about ongoing maintenance:
- GraphZep
- agentic-memory
- codex-mem
- Agent Replay
- letta-obsidian
- gigabrain

### Gray-zone caution
Promising, but I would verify before depending on them:
- Redis Agent Memory Server
- MemoryGraph
- Sediment
- obsidian-web-mcp
- pebble
- Memory Store
- Parsidion CC

---

## 5) Source notes

This pass used the evidence returned by 5 parallel scouts over:
- GitHub repo metadata
- latest commit signals
- release cadence
- archive/discontinued flags
- issue/update hints
- a small amount of official docs/community corroboration where repo identity was ambiguous

This is not a full maintainer-health audit. It is a practical current-signal maintenance pass.
