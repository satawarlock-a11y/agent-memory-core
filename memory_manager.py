import os
import re
from datetime import datetime

class ObsidianMemoryCore:
    def __init__(self, vault_path: str):
        self.vault_path = vault_path
        self.episodes_path = os.path.join(vault_path, "episodes")
        self.concepts_path = os.path.join(vault_path, "concepts")
        
        # Ensure directory structure exists
        os.makedirs(self.episodes_path, exist_ok=True)
        os.makedirs(self.concepts_path, exist_ok=True)

    def save_episode(self, title: str, prompt: str, outcome: str, tags: list, links: list):
        """Logs a single agent generation episode with YAML frontmatter and Wiki-links"""
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{title.lower().replace(' ', '_')}.md"
        file_path = os.path.join(self.episodes_path, filename)
        
        formatted_tags = ", ".join(tags)
        formatted_links = " ".join([f"[[{link}]]" for link in links])
        
        markdown_content = f"""---
type: episodic_memory
timestamp: {datetime.now().isoformat()}
tags: [{formatted_tags}]
status: completed
---

# Episode: {title}

## Input Prompt
{prompt}

## Workflow Outcome
{outcome}

## Cognitive Connections
Related Concepts: {formatted_links}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content.strip())
        print(f"[MemoryCore] Episode saved to {file_path}")

if __name__ == "__main__":
    # Internal component verification loop
    core = ObsidianMemoryCore(vault_path="./mock_vault")
    core.save_episode(
        title="Anime Character Generation",
        prompt="Masterpiece, 1girl, blue hair, cinematic lighting",
        outcome="Successfully generated via ComfyUI. Hands and face detailing passed validation loop.",
        tags=["sdxl", "illustrious", "success"],
        links=["Character-BlueHair", "Style-Anime"]
    )
