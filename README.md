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

| Skill Name | Scope & Purpose | Compatible Tools |
| :--- | :--- | :--- |
| **`agent-context-setup`** | Scaffolds a token-efficient multi-agent architecture (`.agent/` control plane, root `AGENTS.md`, scoped rules, domain memory slices, task concurrency queue with atomic locks, receipts, and compressed changelog). | Cursor, Windsurf, Claude Code, Copilot, Cline, Antigravity |

---

## 4. How to Sync to Any Project

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
git submodule add https://github.com/<your-username>/universal-agent-skills .agent-skills
python .agent-skills/sync.py --target all
```

---

## 5. How to Add New Skills

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
