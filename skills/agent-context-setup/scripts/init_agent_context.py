#!/usr/bin/env python3
"""
Agent Context Setup & Scaffolding Tool
Creates a token-efficient, multi-agent control plane (.agent/ and AGENTS.md) in any repository.
Compatible with Cursor, Windsurf, Claude Code, GitHub Copilot, Cline, and Antigravity.
"""

import sys
import os
from pathlib import Path

def scaffold_agent_context(target_root: Path):
    print(f"[*] Bootstrapping Agent Context Architecture in: {target_root.resolve()}")

    # 1. Directory Structure
    dirs = [
        target_root / ".agent" / "rules",
        target_root / ".agent" / "memory" / "domains",
        target_root / ".agent" / "memory" / "decisions",
        target_root / ".agent" / "tasks" / "ready",
        target_root / ".agent" / "tasks" / "claimed",
        target_root / ".agent" / "tasks" / "receipts",
        target_root / ".agent" / "tasks" / "archive",
        target_root / ".agent" / "plans" / "archived",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print(" [+] Directory tree created successfully.")

    # 2. .gitkeep in claimed/
    gitkeep = target_root / ".agent" / "tasks" / "claimed" / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()

    # 3. Create starter AGENTS.md if not exists
    agents_md = target_root / "AGENTS.md"
    if not agents_md.exists():
        agents_content = """# Agent Orchestration & Collaboration Protocol

> **Scope**: Repository-wide standard for autonomous agents and engineers.
> **Mandate**: High-craft architecture with zero token bloat and multi-agent concurrency safety.

---

## 1. Quick System Profile
* **Stack**: Detect and fill your technology stack here.
* **Control Plane**: `.agent/` directory houses all memory, rules, tasks, and receipts.
* **Master Agent Entrypoint**: [`ENTRYPOINT.md`](file:///{entrypoint}) (Read first on every task).

---

## 2. Multi-Agent Auto-Orchestration Protocol
1. **Identify Role**: Backend, Frontend, QA/Reviewer, or Orchestrator.
2. **Context Hydration**: Read `ENTRYPOINT.md` and load ONLY the single domain memory needed (< 1,200 tokens).
3. **Concurrency Control**: Claim ticket by moving: `mv .agent/tasks/ready/T-XYZ.md .agent/tasks/claimed/T-XYZ.<agent-id>.lock`.
4. **Blast-Radius Execution**: Edit ONLY files declared in the ticket's `blast_radius`.
5. **Receipt & Changelog Shift**: Emit proof-of-work receipt in `tasks/receipts/`, append 1-liner to `changelog.md`, and delete `.lock`.

---

## 3. Engineering Non-Negotiables
1. **SOLID & Clean Architecture**: SRP, OCP (provider adapters), LSP, ISP, DIP.
2. **DRY & Modularity**: Zero duplicate logic, composition over inheritance.
3. **Scalability**: Stateless tiers, paginated collection queries (limit <= 100), prevent N+1 queries.
4. **Dynamic Theme Customization**: Zero hardcoded hex/rgb colors; use semantic CSS tokens.
5. **Strict LOC Ceilings**: Files < 250 LOC (frontend) / < 300 LOC (backend), functions < 40 LOC, nesting <= 3.
6. **Zero Inline Styles**: Semantic tokenized styling only.

---

## 4. Primary Developer Commands
```bash
# Add test, build, and lint commands here
```
""".format(entrypoint=str((target_root / ".agent" / "ENTRYPOINT.md").resolve()).replace("\\", "/"))
        agents_md.write_text(agents_content, encoding="utf-8")
        print(" [+] Created root AGENTS.md")

    # 4. Create .agent/ENTRYPOINT.md if not exists
    entrypoint_md = target_root / ".agent" / "ENTRYPOINT.md"
    if not entrypoint_md.exists():
        entrypoint_content = """# Agent Entrypoint & Context Router

> **Token Budget Target**: < 1,200 tokens total context injection per turn.
> **Rule**: DO NOT scan the whole repository. Follow this routing table to hydrate your context.

---

## 1. Context Hydration Decision Matrix
| Task Area | Mandatory Rules | Domain Memory to Read |
| :--- | :--- | :--- |
| **Backend API / DB** | `rules/core.md` + `rules/backend.md` | `memory/domains/<domain>.md` |
| **Frontend UI / Pages** | `rules/core.md` + `rules/frontend.md` | `memory/domains/ui_tokens.md` |
| **QA / Review** | `rules/core.md` + `rules/qa_review.md` | Target receipt in `tasks/receipts/` |
| **Orchestration** | `rules/core.md` | `tasks/board.md` + `changelog.md` |

---

## 2. Fast Claim & Execution Flow
```text
[ tasks/ready/T-XYZ.md ] -> [ Move to tasks/claimed/T-XYZ.<agent-id>.lock ]
                        -> [ Edit blast radius only + test ]
                        -> [ Emit tasks/receipts/T-XYZ-receipt.md ]
                        -> [ Append 1 line to changelog.md + delete .lock ]
```

---

## 3. High-Priority Invariants
* **Frontend**: < 250 LOC per file, 0 inline styles, 0 hardcoded colors.
* **Backend**: < 300 LOC per file, < 40 LOC per function, layer isolation.
"""
        entrypoint_md.write_text(entrypoint_content, encoding="utf-8")
        print(" [+] Created .agent/ENTRYPOINT.md")

    # 5. Create .agent/changelog.md if not exists
    changelog_md = target_root / ".agent" / "changelog.md"
    if not changelog_md.exists():
        changelog_content = """# Project Engineering Changelog

> **Format**: Append-only compressed 1-liners of completed milestones and tasks.
> **Rule**: When a task is verified, append its 1-liner here and delete the active ticket.

---

## Completed Tasks & Milestones
* **Initial Setup**: Scaffolded Agent Context Architecture.
"""
        changelog_md.write_text(changelog_content, encoding="utf-8")
        print(" [+] Created .agent/changelog.md")

    # 6. Create .agent/tasks/board.md if not exists
    board_md = target_root / ".agent" / "tasks" / "board.md"
    if not board_md.exists():
        board_content = """# Active Task Board

> **Active Sprint**: Sprint 1 Initial Foundation
> **Status Summary**: 0 Active Locks | Ready for tickets

---

## 1. Active Task Queue
| Ticket | Scope / Feature | Domain | Blast Radius | Status |
| :--- | :--- | :--- | :--- | :--- |
| `T-001` | Initial System Setup | `core` | `README.md` | ⚪ `READY` |

---

## 2. Active Locks (`tasks/claimed/`)
*Currently no active locks.*
"""
        board_md.write_text(board_content, encoding="utf-8")
        print(" [+] Created .agent/tasks/board.md")

    print("[✔] Agent Context Scaffolding Complete!")

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    scaffold_agent_context(target)
