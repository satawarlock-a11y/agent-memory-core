# Technical Specification: Obsidian-Based Agent Memory Pipeline

This document outlines the low-level data flow and markdown parsing logic used by the agent to interface with the local Obsidian memory vault.

---

## 1. Data Flow Architecture

The interaction between the Orchestrator (OpenClaw) and the Obsidian Vault follows a strict I/O loop:

```text
  [User Request] 
        │
        ▼
┌───────────────┐      1. Semantic Lookup      ┌────────────────────────┐
│   OpenClaw    │ ───────────────────────────► │  Obsidian Vault Core   │
│  Orchestrator │ ◄─────────────────────────── │   (Markdown Files)     │
└───────┬───────┘    2. Inject Context/Rules   └────────────────────────┘
        │
        │ 3. Execute Task with Context
        ▼
┌───────────────┐
│  Target LLM   │ ───► [Execution Output]
│   Execution   │ 
└───────┬───────┘
        │
        ▼
┌───────────────┐      4. Extract Experience
│  Reflection   │ ───────────────────────────────────────┐
│     Loop      │                                        ▼
└───────────────┘                        ┌────────────────────────┐
                                         │ Write: episodes/       │
                                         │ Write: reflections/    │
                                         └────────────────────────┘

2. Document Schemas & Metadata Parsing

The Python layer (memory_manager.py) uses regex and YAML parsers to extract cognitive state directly from Markdown frontmatter.
A. Episodic Memory Schema (/episodes/)

Every execution event creates a timestamped file with the following structured metadata:
YAML

---
type: episodic_memory
timestamp: YYYY-MM-DDTHH:MM:SS
tags: [agent_state, session_id, task_type]
status: completed | failed
---
# Episode Title
## Execution Log
[Raw prompts and target agent decisions here]

B. Semantic Concept Schema (/concepts/)

Persistent rules, definitions, and user preferences are stored as evergreen notes. The agent cross-references them using standard Wiki-links:
YAML

---
type: concept_node
category: fact | rule | preference
importance: high
---
# [[User-Preference]]
Details: Prefers concise answers and Python-centric solutions.
Associated Rules: [[System-Constraint]], [[Code-Style]]

3. Context Retrieval & Injection Logic

    Trigger: User sends a request to the agent.

    Scan: The memory manager scans concepts/ and episodes/ to extract matching metadata tags.

    Link Resolution: It follows internal Wiki-links to fetch associated sub-rules or historical context.

    Compilation: The script compiles the final system prompt, combining active user input with historical constraints, before sending it to the LLM backend.
