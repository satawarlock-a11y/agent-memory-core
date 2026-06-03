Markdown

# Technical Specification: Obsidian-Based Agent Memory Pipeline

This document outlines the low-level data flow and markdown parsing logic used by the agent to interface with the local Obsidian memory vault.

---

## 1. Data Flow Architecture

The interaction between the OpenClaw Orchestrator, ComfyUI, and the Obsidian Vault follows a strict I/O loop:

```text
  [User Request] 
        │
        ▼
┌───────────────┐      1. Semantic Lookup      ┌────────────────────────┐
│   OpenClaw    │ ───────────────────────────► │  Obsidian Vault Core   │
│  Orchestrator │ ◄─────────────────────────── │   (Markdown Files)     │
└───────┬───────┘    2. Inject Context/Rules   └────────────────────────┘
        │
        │ 3. Dispatch Optimized Prompt
        ▼
┌───────────────┐
│    ComfyUI    │ ───► [Qwen-VL Vision Feedback]
│   Pipeline    │ ◄─── (Validates Output)
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

Every generation event creates a timestamped file with the following structured metadata:
YAML

---
type: episodic_memory
timestamp: YYYY-MM-DDTHH:MM:SS
tags: [model_name, workflow_status, prompt_type]
status: completed | failed
---
# Episode Title
## Execution Log
[Raw prompts and ComfyUI seed parameters here]

B. Semantic Concept Schema (/concepts/)

Persistent rules, character references, and artistic constraints are stored as evergreen notes. The agent cross-references them using standard Wiki-links:
YAML

---
type: concept_node
category: character | style | constraint
importance: high
---
# [[Character-Name]]
Features: Blue eyes, tactical gear.
Associated Styles: [[Style-Cyberpunk]], [[Style-Grit]]

3. Context Retrieval & Injection Logic

    Trigger: User sends a prompt: "Generate a picture of Character-A in a cyberpunk city."

    Scan: The memory manager scans concepts/ for Character-A.md.

    Link Resolution: It follows the internal Wiki-links [[Style-Cyberpunk]] inside that file to fetch associated style tags and negative prompts.

    Compilation: The script compiles the final system prompt for OpenClaw, combining active user input with historical constraints before hitting the ComfyUI API.
