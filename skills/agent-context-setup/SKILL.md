---
name: agent-context-setup
description: >-
  Scaffolds, migrates, or audits a token-efficient multi-agent orchestration architecture
  (.agent/ control plane, root AGENTS.md, scoped rules, bounded-context domain memory,
  task concurrency queue with atomic locks, receipts, and compressed changelog) in any repository.
triggers:
  - "setup agent context"
  - "scaffold agent trackers"
  - "context-setup"
  - "/context-setup"
  - "/agent-context-setup"
globs:
  - "**/*"
compatibility:
  - cursor
  - windsurf
  - claude-code
  - copilot
  - cline
  - antigravity
---

# Skill: Agent Context & Multi-Agent Orchestration Setup

This skill guides any AI agent or engineer in bootstrapping, migrating, or auditing a high-efficiency **Multi-Agent Micro-Context Architecture (MAMCA)** in any software repository. It eliminates token bloat, context dilution, and multi-agent merge collisions while establishing clean architectural boundaries (SOLID, DRY, modularity, dynamic customization).

---

## Target Architecture Blueprint

Every project scaffolded by this skill receives this unified control plane:

```text
<project-root>/
├── AGENTS.md                                # Root orchestration standard & agent protocol (< 100 LOC)
└── .agent/
    ├── ENTRYPOINT.md                        # Context router & hydration matrix (< 50 LOC, ~300 tokens)
    ├── changelog.md                         # Append-only compressed 1-line history
    ├── rules/                               # Scoped rules (Cursor MDC / Glob-activated)
    │   ├── core.md                          # Invariants: SOLID, DRY, LOC limits, API contract
    │   ├── backend.md                       # Scoped to backend/** (language/framework patterns)
    │   ├── frontend.md                      # Scoped to frontend/** (tokens, a11y, ui craft)
    │   └── qa_review.md                     # Scoped to tests, diff verification, receipts
    ├── memory/                              # Bounded-Context Domains (Lazy-Loaded)
    │   ├── system_overview.md               # Stack, ports, auth segments, directory tree
    │   ├── index.md                         # 1-line routing index to domains
    │   ├── domains/                         # Domain memory slices (< 30 LOC each)
    │   └── decisions/                       # Architecture Decision Records (ADRs)
    │       ├── index.md                     # 1-line index of ADR-001...
    │       └── adrs.md                      # Full decision rationale
    ├── tasks/                               # Concurrency Control Plane
    │   ├── board.md                         # Active sprint status & claimed locks
    │   ├── ready/                           # Unclaimed atomic tickets (T-001.md)
    │   ├── claimed/                         # Active agent locks (T-001.<agent_id>.lock)
    │   ├── receipts/                        # Low-token proof-of-work handoff receipts
    │   └── archive/                         # Completed ticket archives
    └── plans/archived/                      # Quarantined legacy monolithic docs (nothing lost)
```

---

## Step-by-Step Execution Workflow

### Step 1: Repository Profiling & Discovery
1. Inspect the root directory: identify package managers (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`), frameworks, and build tools.
2. Locate existing trackers or planning files: search for `TODO.md`, `PLAN.md`, `README.md`, `.cursorrules`, `docs/`, `tasks/`.
3. Check for existing tests and verification commands (`pytest`, `npm test`, `cargo test`).

### Step 2: Directory Scaffolding
Create the directory structure:
```bash
# PowerShell
New-Item -ItemType Directory -Force -Path .agent/rules, .agent/memory/domains, .agent/memory/decisions, .agent/tasks/ready, .agent/tasks/claimed, .agent/tasks/receipts, .agent/tasks/archive, .agent/plans/archived

# Bash / Linux / macOS
mkdir -p .agent/{rules,memory/{domains,decisions},tasks/{ready,claimed,receipts,archive},plans/archived}
```
*(Or run the companion Python script: `python scripts/init_agent_context.py`)*

### Step 3: Author the Root `AGENTS.md`
Generate `AGENTS.md` at the project root customized to the detected stack. It **must** include:
1. **Quick System Profile**: Stack, ports, entrypoint link.
2. **Multi-Agent Auto-Orchestration Protocol**:
   * Step 1: Role Identification (Backend, Frontend, QA, Orchestrator).
   * Step 2: Context Hydration (< 1,200 tokens via `ENTRYPOINT.md`).
   * Step 3: Concurrency Control & Atomic Leases (`mv ready/T-XYZ.md claimed/T-XYZ.<agent-id>.lock`).
   * Step 4: Blast-Radius Execution (strictly declared files only).
   * Step 5: Proof-of-Work Receipt (`tasks/receipts/`) & 1-line Changelog Shift (`changelog.md`).
3. **Engineering Non-Negotiables**:
   * SOLID & Clean Architecture (SRP, OCP, LSP, ISP, DIP).
   * DRY, OOP & Modularity.
   * Scalability & Performance (stateless tier, bounded queries, N+1 prevention).
   * Dynamic Theme Customization (zero hardcoded hex/rgb, semantic design tokens, WCAG contrast).
   * Strict LOC ceilings (< 250 LOC for frontend, < 300 LOC for backend).
   * Zero inline styles.
4. **Primary Developer Commands**: Test, build, lint, and LOC checks.

### Step 4: Author `.agent/ENTRYPOINT.md`
Create the micro-router table mapping task categories directly to mandatory rules and domain memory. Include the 3-step claim diagram and high-priority invariants.

### Step 5: Generate Scoped Rules (`.agent/rules/`)
Create scoped rule files with YAML frontmatter:
* `core.md`: Universal invariants, SOLID, DRY, LOC limits, standard API contract (`{ success, data, message }`).
* `backend.md`: Language/framework specific standards, layering, query scalability, secret masking.
* `frontend.md`: Framework standards, < 250 LOC rule, zero inline styles, dynamic theme tokenization.
* `qa_review.md`: Blast radius diff inspection, verification log capture, receipt format.

### Step 6: Generate Bounded Domain Memory (`.agent/memory/`)
1. Create `system_overview.md` with system architecture, tech stack, and user authentication segments.
2. Create `index.md` listing 1-line links to domain memory slices.
3. Split domain models into small `< 30 LOC` files in `domains/` (e.g. `auth.md`, `catalog.md`, `billing.md`, `ui_tokens.md`).
4. Set up `decisions/index.md` and copy any existing ADRs into `decisions/adrs.md`.

### Step 7: Quarantine Legacy Trackers & Establish Pointers
If the project already has large plans (`TODO.md`, `PLAN.md`, etc.):
1. Move/copy the legacy files into `.agent/plans/archived/`.
2. Replace the legacy files with **compact 5-line pointers** directing future agents to `AGENTS.md` and `.agent/tasks/board.md`.
3. Extract completed historical milestones into 1-line summaries in `.agent/changelog.md`.

### Step 8: Initialize Task Concurrency Queue (`.agent/tasks/`)
1. Create `tasks/board.md` summarizing the active sprint and listing active locks.
2. Break upcoming pending work into atomic task tickets in `tasks/ready/T-XYZ-<slug>.md`.
   * Each ticket must declare: `ticket`, `title`, `domain`, `status: ready`, and `blast_radius: [file1, file2]`.
3. Add a `.gitkeep` in `tasks/claimed/`.
4. If a recent milestone was just completed, generate a baseline proof-of-work receipt in `tasks/receipts/`.

### Step 9: Verification & Token Budget Audit
Run a quick line-count check on `.agent/`:
* Ensure no single active tracker file exceeds 60 lines.
* Verify all internal links use absolute clickable paths (`file:///`).
* Verify that an agent reading `ENTRYPOINT.md` + 1 rule + 1 domain memory + 1 task ticket receives **under 1,200 tokens**.
