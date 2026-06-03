# agent-memory-core

> **An external, local-first cognitive memory layer designed as a "brain extension" for autonomous AI agents (like OpenClaw), powered by Obsidian Markdown vaults.**

Traditional LLM agents suffer from context-window amnesia. `agent-memory-core` acts as a persistent hippocampus for AI systems. Instead of heavy, complex cloud databases, it uses a local **Obsidian Vault** structure. The agent reads, writes, and cross-links Markdown files, building a human-readable and AI-parseable external cognitive architecture.

![Status](https://img.shields.io/badge/Status-Active-green)
![Type](https://img.shields.io/badge/Architecture-Local--First_Obsidian-blueviolet)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 🧠 Cognitive Vault Structure

The project structures the agent's memory inside Obsidian using native Markdown features (YAML Frontmatter, Wiki-links `[[link]]`, and Tags):

* **`episodes/` (Episodic Memory):** Short-term logs of execution history, prompts, and successful outputs. Allows the agent to remember *what* it just did within the current loop.
* **`concepts/` (Semantic Knowledge Graph):** Permanent rules, user preferences, style guidelines, and LoRA trigger words. 
* **`reflections/` (Self-Criticism Loop):** Post-generation feedback. If an image generation fails or succeeds, the agent logs the experience here to enforce negative/positive constraints in future runs.


┌────────────────────────┐
│  OpenClaw Agent Core   │
└───────────┬────────────┘
│ Read / Write (Python File I/O)
▼
┌────────────────────────┐
│     Obsidian Vault     │ ◄─── Human-in-the-loop can edit
│  (agent-memory-core)   │      rules directly in Markdown!
└─────┬────────────┬─────┘
│            │
▼            ▼
[[Links]]     YAML Metadata ──► (Semantic Search & Filtering)

## ✨ Key Features

* **Zero-Database Overhead:** No Docker or heavy vector DB setups required. Everything runs locally via standard file system operations.
* **Bi-directional Linking:** The agent creates wiki-links between concepts (e.g., linking a specific character `[[Character-A]]` to a proven prompt style `[[Style-Anime]]`).
* **Human-in-the-Loop Friendly:** Because memory is just text files, users can open Obsidian, look at the visual graph of the agent's brain, and manually edit its memory or fix errors.

## 📁 Repository Blueprints

* `scheme.md` — Detailed technical specifications of the file interaction pipeline and context parsing logic.
* `gogo_markmap.md` — The cognitive mapping layout representing how Obsidian folders map to agent states.

## 🛠 Tech Stack

* **Storage:** Markdown / Obsidian Vault Environment
* **Orchestration Interaction:** Python (File I/O, YAML parsing, regex metadata extractors)
* **Target Integration:** OpenClaw / ComfyUI API

---
**Maintainer:** satawarlock-a11y  
**License:** MIT — Open for contributions and forks!
