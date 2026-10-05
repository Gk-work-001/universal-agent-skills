# Universal Agent Skills Hub

> **Mission**: A vendor-agnostic, open standard repository for Agentic AI and IDE skills.  
> **Compatibility**: Cursor, Windsurf, Claude Code, GitHub Copilot, Cline / Roo Code, Antigravity, Devin, Aider.

---

## 1. Why Universal Skills?

Modern AI IDEs and autonomous coding agents all rely on prompt engineering, rules, and runbooks—but each tool stores them in a different location (`.cursor/rules/`, `.windsurfrules`, `CLAUDE.md`, `.github/copilot-instructions.md`, `AGENTS.md`).

This repository maintains **pure, platform-agnostic Markdown skills** with structured YAML frontmatter that can be automatically exported or synchronized into **any** agentic environment with a single command.

---

## 2. Repository Layout

```text
universal-agent-skills/
├── skills/
│   └── agent-context-setup/             # Skill #1: Multi-Agent Context Scaffolder
│       ├── SKILL.md                     # Platform-agnostic skill protocol
│       ├── scripts/                     # Standalone Python / shell helpers
│       │   └── init_agent_context.py    # Auto-scaffolding script
│       └── templates/                   # Standard reusable templates
│           ├── core_rules.md.template
│           ├── task_ticket.md.template
│           └── receipt.md.template
├── sync.py                              # Universal exporter CLI for all IDEs
├── .gitignore
└── README.md
```

---

## 3. Skill Catalog

| Skill Name | Scope & Purpose | Slash Command | Compatible Tools |
| :--- | :--- | :--- | :--- |
| **`agent-context-setup`** | Scaffolds a token-efficient multi-agent architecture (`.agent/` control plane, root `AGENTS.md`, scoped rules, domain memory slices, task concurrency queue with atomic locks, receipts, and compressed changelog). | `/context-setup`<br>`/agent-context-setup` | Cursor, Windsurf, Claude Code, Copilot, Cline, Antigravity |

---

## 4. How Skills Are Accessed via Slash (`/`) Across IDEs

Different AI development environments surface skills through different modalities:

### A. Antigravity & Agentic IDEs (Interactive `/` Menu)
* **Automatic Discovery**: Any skill synced to `~/.gemini/config/skills/<skill-name>/` (globally) or `<project>/.agent/skills/` (locally) is automatically mounted into the IDE's interactive slash command autocomplete menu.
* **Available Slash Commands for this repo**:
  * `/agent-context-setup`
  * `/context-setup` *(short alias)*
* **Reloading the UI Cache**: If a skill was added while your IDE window was actively running, the client's slash autocomplete cache must be refreshed:
  1. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>).
  2. Select **`Developer: Reload Window`** (takes ~1-2 seconds).
  3. Type `/` in the chat input — the commands will appear in the dropdown.

### B. Cursor (`@` Symbol & Auto-Activation)
* When exported via `python sync.py --target cursor`, skills are saved as `.cursor/rules/<skill>.mdc`.
* You can reference them explicitly in the chat bar using `@<skill-name>`.
* The AI also auto-attaches the skill whenever you edit matching files or trigger phrases.

### C. Claude Code & Terminal Agents (Natural Language & Memory)
* When exported to `CLAUDE.md`, the agent automatically activates the skill protocol when it detects keywords like `"setup context"`, `"agent context"`, or slash aliases.

### D. Universal Natural Language Trigger
* Regardless of IDE or tool, every skill defines trigger phrases in its YAML frontmatter. You can always activate it in natural language:
  > *"Setup the agent context and trackers in this project using the agent-context-setup skill."*

---

## 5. How to Sync to Any Project

Run `sync.py` pointing to your target project directory:

```bash
# Sync to a specific IDE in a project:
python sync.py --dest /path/to/my-project --target cursor
python sync.py --dest /path/to/my-project --target windsurf
python sync.py --dest /path/to/my-project --target claude
python sync.py --dest /path/to/my-project --target copilot
python sync.py --dest /path/to/my-project --target cline
python sync.py --dest /path/to/my-project --target antigravity

# Sync to all detected IDEs:
python sync.py --dest /path/to/my-project --target all

# List all available skills:
python sync.py --list
```

### Git Submodule Option
To share these skills across all repositories in your organization or team:
```bash
git submodule add https://github.com/Gk-work-001/universal-agent-skills .agent-skills
python .agent-skills/sync.py --target all
```

---

## 6. How to Add New Skills

1. Create a new folder under `skills/<your-skill-name>/`.
2. Add `SKILL.md` with standard YAML frontmatter:
   ```markdown
   ---
   name: your-skill-name
   description: Exact description of what the skill does and when an agent should trigger it.
   triggers: ["trigger phrase 1", "/slash-command"]
   globs: ["**/*"]
   ---

   # Skill Title
   [Step-by-step procedural instructions]
   ```
3. Commit and push to GitHub:
   ```bash
   git add skills/<your-skill-name>
   git commit -m "feat: add <your-skill-name> skill"
   git push origin main
   ```
4. Run `python sync.py` anywhere to deploy the new skill across all your tools.
