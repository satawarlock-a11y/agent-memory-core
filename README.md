# agent-memory-core

> **An open-source, local-first cognitive memory layer designed as a "brain extension" for autonomous LLM agents (like OpenClaw), powered by Obsidian Markdown vaults.**

Traditional LLM agents suffer from context-window amnesia. `agent-memory-core` acts as a persistent hippocampus for AI systems. Instead of heavy, complex cloud databases, it uses a local **Obsidian Vault** structure. The agent reads, writes, and cross-links Markdown files, building a human-readable and AI-parseable external cognitive architecture.

![Status](https://img.shields.io/badge/Status-Active-green)
![Type](https://img.shields.io/badge/Architecture-Local--First_Obsidian-blueviolet)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 🧠 Cognitive Vault Structure

The project structures the agent's memory inside Obsidian using native Markdown features (YAML Frontmatter, Wiki-links `[[link]]`, and Tags):

* **`episodes/` (Episodic Memory):** Short-term logs of execution history, user prompts, and raw agent decisions. Allows the agent to remember *what* it just did within the current session.
* **`concepts/` (Semantic Knowledge Graph):** Permanent rules, user preferences, long-term facts, and behavioral constraints forming the agent's permanent "personality".
* **`reflections/` (Self-Criticism Loop):** Post-execution feedback. The agent logs its own performance scores here to enforce negative/positive constraints in future runs.

┌────────────────────────┐
│   LLM / Agent Core     │
│      (OpenClaw)        │
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

* **Zero-Database Overhead:** No Docker or heavy vector DB setups required. Everything runs locally via standard file system operations and markdown parsing.
* **Bi-directional Linking:** The agent creates wiki-links between concepts (e.g., linking a specific task `[[Task-12]]` to a proven core rule `[[System-Constraint]]`).
* **Human-in-the-Loop Friendly:** Because memory is just text files, users can open Obsidian, look at the visual graph of the agent's brain, and manually edit its memory or fix errors.

## 📁 Repository Structure

* `memory_manager.py` — Core Python module handling file I/O, YAML parsing, and automated memory creation.
* `scheme.md` — Detailed technical specifications of the file interaction pipeline and context parsing logic.
* `LICENSE` — MIT Open Source License.

## 🛠 Tech Stack

* **Storage Environment:** Obsidian Vault / Markdown File System
* **Core Logic:** Python 3.x (YAML parsing, regex metadata extractors)
* **Orchestration Target:** OpenClaw Ecosystem / Generic AI Agent Pipelines

---
**Maintainer:** satawarlock-a11y  
**License:** MIT — Open for contributions and forks!
