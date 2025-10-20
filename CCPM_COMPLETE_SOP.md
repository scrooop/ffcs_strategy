# CCPM Complete Standard Operating Procedure

**Version:** 2.0
**Last Updated:** 2025-10-20
**Scope:** Complete guide to Claude Code Project Management System

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Prerequisites & Setup](#prerequisites--setup)
3. [Context Management](#context-management)
4. [Core Workflow](#core-workflow)
5. [Parallel Execution](#parallel-execution)
6. [Synchronization & Maintenance](#synchronization--maintenance)
7. [Utility Commands](#utility-commands)
8. [Complete Command Reference](#complete-command-reference)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## System Overview

### What is CCPM?

**Claude Code Project Management (CCPM)** is an integrated project management system that combines:

1. **Context Management** - Living documentation of your project
2. **Requirements Management** - PRDs and structured planning
3. **Task Decomposition** - Automatic epic → task breakdown
4. **GitHub Integration** - Bidirectional issue sync with parent-child relationships
5. **Parallel Execution** - Multi-level parallelism (tasks + streams)
6. **Progress Tracking** - Automated status updates and reporting

### Core Components

```
.claude/
├── context/              # Living project documentation (9 files)
├── prds/                 # Product Requirements Documents
├── epics/                # Implementation epics with tasks
│   └── {epic-name}/
│       ├── epic.md       # Epic overview
│       ├── 1.md          # Task 1
│       ├── 1-analysis.md # Task 1 parallelization analysis
│       ├── updates/      # Progress tracking per task/stream
│       └── execution-status.md
├── agents/               # Specialized agent definitions
├── commands/             # Slash command implementations
├── rules/                # Coordination & operation rules
└── scripts/pm/           # Bash scripts for PM operations
```

### Key Concepts

- **PRD** - Product Requirements Document (what to build)
- **Epic** - Implementation plan (how to build it)
- **Task** - Concrete actionable work item (GitHub sub-issue)
- **Stream** - Parallel work within a task
- **Context** - Project knowledge base for agents

---

## Prerequisites & Setup

### 1. Git & GitHub Setup

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Create GitHub repository (private recommended)
gh auth login
gh repo create [repo name] --private --source=. --remote=origin --push

# Verify setup
git remote -v
gh auth status
```

### 2. CCPM Initialization

```bash
# Initialize CCPM system
/pm:init

# Expected actions:
# - Installs gh CLI (if needed)
# - Authenticates with GitHub
# - Installs gh-sub-issue extension
# - Creates .claude directory structure
# - Creates GitHub labels (epic, task)
# - Verifies CLAUDE.md exists
```

### 3. Context Initialization

```bash
# Create initial project context
/context:create

# Creates 9 context files in .claude/context/:
# - progress.md             # Current status & next steps
# - project-structure.md    # Directory organization
# - tech-context.md         # Dependencies & technologies
# - system-patterns.md      # Architecture & design patterns
# - product-context.md      # Product requirements & users
# - project-brief.md        # Scope, goals, objectives
# - project-overview.md     # High-level feature summary
# - project-vision.md       # Long-term strategic direction
# - project-style-guide.md  # Coding standards & conventions
```

### 4. Verify Setup

```bash
/pm:status        # Should show empty project ready for work
/context:prime    # Should load all 9 context files
```

---

## Context Management

### System Purpose

Context provides **living documentation** that gives AI agents (and humans) comprehensive project understanding without reading the entire codebase.

### The Context Lifecycle

```
Session Start    →  /context:prime     →  Load project understanding
Development Work →  Make changes       →  Code, features, docs
Session End      →  /context:update    →  Capture what changed
```

### Commands

#### `/context:create` - Initialize Context

**When to use:**
- Starting new project
- Adding CCPM to existing project
- Major restructuring requiring fresh baseline

**What it does:**
1. Analyzes project (git, dependencies, code structure)
2. Reads README.md and existing docs
3. Creates 9 comprehensive context files
4. Adds proper frontmatter with timestamps

**Output:** 9 context files in `.claude/context/`

---

#### `/context:prime` - Load Context

**When to use:**
- Starting new development session
- After `/clear` command
- Onboarding new team member
- Agent needs project understanding

**What it does:**
1. Reads context files in priority order:
   - **Priority 1**: project-overview, project-brief, tech-context
   - **Priority 2**: progress, project-structure
   - **Priority 3**: system-patterns, product-context, style-guide, vision
2. Validates frontmatter integrity
3. Checks git status
4. Provides comprehensive summary

**Output:** Summary of loaded context + current project state

---

#### `/context:update` - Update Context

**When to use:**
- End of development session
- After completing major features
- After architectural changes
- Before long breaks (preserve knowledge)

**What it does:**
1. **Detects changes** (git diff, new files, dependencies)
2. **Smart updates** (only files with actual changes):
   - `progress.md` - **Always updated** (recent work, status, next steps)
   - `tech-context.md` - If dependencies changed
   - `project-structure.md` - If directories/files added
   - `system-patterns.md` - If architecture changed
   - Others - Only if relevant changes
3. **Preserves timestamps** (no update if no change)
4. **Incremental versioning** (1.0 → 1.1 for major changes)

**Output:** List of updated files with change summary

---

### Context Best Practices

1. **Prime at session start** - Ensures full understanding
2. **Update at session end** - Captures your work
3. **Update after milestones** - Document major achievements
4. **Don't over-update** - Only update when meaningful changes
5. **Review progress.md regularly** - Keep next steps current

---

## Core Workflow

### Complete Development Cycle

```
1. Requirements  → /pm:prd-new
2. Epic         → /pm:prd-parse
3. Decompose    → /pm:epic-decompose
4. Sync GitHub  → /pm:epic-sync
5. Execute      → /pm:epic-start  (or /pm:issue-start)
6. Track        → /pm:standup, /pm:status
7. Complete     → /pm:issue-sync
8. Merge        → /pm:epic-merge
9. Archive      → /pm:clean
```

---

### Phase 1: Requirements (PRD)

#### `/pm:prd-new <name>`

**Purpose:** Structured brainstorming and requirements capture

**Process:**
1. Interactive Q&A about the feature
2. Gathers problem statement, user stories, requirements
3. Documents success criteria, dependencies, scope
4. Creates `.claude/prds/<name>.md`

**PRD Contents:**
- Executive Summary
- Problem Statement
- User Stories with acceptance criteria
- Functional Requirements
- Non-Functional Requirements
- Success Criteria
- Dependencies & Assumptions
- Out of Scope (critical!)

**Example:**
```bash
/pm:prd-new trade-scanner-batch

# Interactive session:
# Q: What problem does this solve?
# A: Need to scan multiple tickers efficiently...
#
# Q: Who are the users?
# A: Options traders using earnings volatility strategy...
#
# [Creates comprehensive PRD]
```

---

### Phase 2: Epic Creation

#### `/pm:prd-parse <name>`

**Purpose:** Convert requirements into implementation plan

**Process:**
1. Reads PRD from `.claude/prds/<name>.md`
2. Analyzes technical requirements
3. Creates high-level implementation strategy
4. Documents architecture, dependencies, risks
5. Creates `.claude/epics/<name>/epic.md`

**Epic Contents:**
- Implementation approach
- Technical architecture
- Technology choices
- Estimated effort
- Risk assessment
- Blockers & dependencies

---

### Phase 3: Task Decomposition

#### `/pm:epic-decompose <name>`

**Purpose:** Break epic into concrete, actionable tasks

**Process:**
1. Reads epic from `.claude/epics/<name>/epic.md`
2. Identifies logical work units
3. Determines dependencies between tasks
4. Creates numbered task files (1.md, 2.md, etc.)

**Task File Structure:**
```markdown
---
name: Implement batch ticker processing
description: Process multiple tickers with rate limiting
status: open
depends_on: [1]       # Blocked until task 1 completes
estimated_effort: 3h
created: 2025-10-20T14:15:00Z
---

# Task: Implement batch ticker processing

## Description
[Detailed description]

## Acceptance Criteria
- [ ] Process up to 50 tickers per batch
- [ ] Rate limiting: 5 requests/second
- [ ] Error handling for failed tickers
- [ ] Progress bar

## Implementation Notes
[Technical guidance]
```

**Key Fields:**
- `depends_on: []` - Empty = can start immediately
- `depends_on: [1, 2]` - Blocked until tasks 1 & 2 complete
- `status` - open, in_progress, closed
- `estimated_effort` - Time estimate

---

### Phase 4: GitHub Synchronization

#### `/pm:epic-sync <name>`

**Purpose:** Create GitHub issues with parent-child relationships

**Process:**
1. Creates parent **epic issue** on GitHub
2. Creates child **sub-issues** for each task (using gh-sub-issue)
3. Links sub-issues to parent
4. Applies labels (epic, task)
5. Updates local files with GitHub URLs and issue numbers

**GitHub Structure:**
```
Epic Issue #1: Trade Scanner Batch Processing
├── Sub-issue #2: Implement yfinance wrapper
├── Sub-issue #3: Implement batch processing
├── Sub-issue #4: Create ranking algorithm
└── Sub-issue #5: Update GUI
```

**Shortcut:**
```bash
/pm:epic-oneshot <name>
# Equivalent to: epic-decompose + epic-sync
```

---

### Phase 5: Task Execution

Two approaches available:

#### Option A: Automatic Parallel Execution (Recommended)

```bash
/pm:epic-start <name>
```

**What happens:**
1. **Identifies ready tasks** (no unmet dependencies)
2. **Auto-analyzes** each task for parallel streams (if no analysis exists)
3. **Launches multiple tasks** simultaneously (task-level parallelism)
4. **Launches multiple streams** within each task (stream-level parallelism)
5. **Coordinates dependencies** (starts new work as blockers clear)
6. **Consolidates results** (reports to main thread)

**Execution Tree Example:**
```
/pm:epic-start trade-scanner

Round 1: Tasks #2 & #4 ready
├── Task #2 (parallel-worker)
│   ├── Auto-analyze → 2 streams
│   ├── Stream A: yfinance wrapper → agent-2A
│   └── Stream B: Rate limiting → agent-2B
└── Task #4 (parallel-worker)
    ├── Auto-analyze → 1 stream
    └── Stream A: Ranking algo → agent-4A

[3 agents working simultaneously]

Round 2: After #2 completes, Task #3 ready
└── Task #3 (parallel-worker)
    ├── Auto-analyze → 3 streams
    ├── Stream A: Batch executor → agent-3A
    ├── Stream B: Progress tracker → agent-3B
    └── Stream C: Result aggregator → agent-3C (waits for A & B)

[Up to 5 agents working simultaneously across both levels]
```

**Key Feature:** Fully automated, maximum parallelism, minimal manual intervention

---

#### Option B: Manual Single-Task Execution

```bash
/pm:issue-start <issue-number>
```

**What happens:**
1. Fetches issue from GitHub
2. Reads task file
3. Updates status to "in_progress"
4. Launches single agent for this ONE task
5. Creates progress tracking

**When to use:**
- Want control over task sequence
- Testing/debugging specific feature
- Learning the system
- Don't want full parallel execution

---

### Phase 6: Progress Tracking

#### `/pm:next` - Show Available Work

Shows all tasks ready to start (no unmet dependencies)

```
📋 Next Available Tasks
=======================

✅ Ready: #2 - Implement yfinance wrapper
   Epic: trade-scanner

✅ Ready: #4 - Create ranking algorithm
   Epic: trade-scanner
   🔄 Can run in parallel

📊 Summary: 2 tasks ready to start
```

---

#### `/pm:status` - Project Dashboard

Overall view of all PRDs, epics, tasks

```
📊 Project Status
=================

PRDs:
  Backlog: 2
  In Progress: 1
  Completed: 3

Epics:
  trade-scanner (60% complete)
    Tasks: 3/5 closed
  kelly-position-sizer (20% complete)
    Tasks: 1/5 closed
```

---

#### `/pm:standup` - Daily Report

Today's activity, in-progress work, next tasks

```
📅 Daily Standup - 2025-10-20
==============================

📝 Today's Activity:
  • Modified 3 task(s)
  • Updated 1 epic(s)

🔄 Currently In Progress:
  • Issue #2 (trade-scanner) - 75% complete
  • Issue #5 (kelly-position-sizer) - 30% complete

⏭️ Next Available Tasks:
  • #3 - Implement batch processing
  • #6 - Create position size calculator
```

---

#### `/pm:epic-status <name>` - Epic Detail

Progress, tasks, blockers for specific epic

---

#### `/pm:blocked` - Blocked Tasks

All tasks waiting on dependencies with suggestions to unblock

---

### Phase 7: Task Completion

#### `/pm:issue-sync <issue-number>`

**Purpose:** Mark task complete and update GitHub

**Process:**
1. Updates local task status to "closed"
2. Updates epic progress
3. Closes GitHub issue
4. Unblocks dependent tasks
5. Updates task list in parent epic issue

**When to use:** After agent completes task or you manually finish work

---

### Phase 8: Epic Completion & Merge

#### `/pm:epic-merge <name>`

**Purpose:** Merge completed epic back to main branch

**Process:**
1. **Validates completion** (all tasks closed, no uncommitted changes)
2. **Runs tests** (optional but recommended)
3. **Merges to main** with --no-ff (preserves history)
4. **Closes GitHub issues** (epic + all sub-issues)
5. **Cleans up** (removes worktree, deletes branch)
6. **Archives epic** (moves to .claude/epics/archived/)

**When to use:** After ALL tasks in epic are complete

---

### Phase 9: Maintenance

#### `/pm:clean`

**Purpose:** Archive completed work

**Process:**
1. Identifies completed epics (>30 days old)
2. Archives to `.claude/epics/archived/`
3. Cleans up stale progress files
4. Removes execution status from old epics

**Options:**
- `--dry-run` - Show what would be cleaned without doing it

---

## Parallel Execution

### Two Levels of Parallelism

#### Level 1: Task-Level Parallelism (Between Tasks)

Multiple independent **tasks** run simultaneously

**Example:**
```
Epic: Trade Scanner
├── Task #1: Data fetching (no deps) → Runs NOW
├── Task #2: Volatility calc (no deps) → Runs NOW
├── Task #3: Filters (depends on #2) → BLOCKED
└── Task #4: GUI (depends on #1, #2) → BLOCKED
```

Tasks #1 and #2 run in parallel because no dependencies

---

#### Level 2: Stream-Level Parallelism (Within Tasks)

A single **task** broken into parallel work streams

**Example:**
```
Task #1: Data Fetching
├── Stream A: yfinance wrapper → agent-1A
├── Stream B: Rate limiter → agent-1B
└── Stream C: Caching (depends on A & B) → agent-1C
```

Streams A & B run in parallel, C waits

---

### Manual Analysis (Optional)

#### `/pm:issue-analyze <issue-number>`

**Purpose:** Manually identify parallel streams before execution

**When to use:**
- Want to review/customize parallelization strategy
- Complex task needing careful stream decomposition
- Want to edit file assignments

**Process:**
1. Analyzes task requirements
2. Identifies independent work streams
3. Assigns file patterns to each stream
4. Documents dependencies between streams
5. Creates `.claude/epics/<epic>/<issue>-analysis.md`

**Analysis File Example:**
```markdown
---
issue: 2
title: Implement data fetching layer
estimated_hours: 3
parallelization_factor: 2.0
---

# Parallel Work Analysis: Issue #2

## Parallel Streams

### Stream A: yfinance Wrapper
**Scope**: Core API wrapper
**Files**: scripts/data_fetch.py
**Agent Type**: general-purpose
**Can Start**: immediately
**Estimated Hours**: 1.5h
**Dependencies**: none

### Stream B: Rate Limiting
**Scope**: Rate limiter with retry
**Files**: scripts/rate_limiter.py
**Agent Type**: general-purpose
**Can Start**: immediately
**Estimated Hours**: 1.5h
**Dependencies**: none

## Coordination Points
**Shared Files**: None

## Conflict Risk**: Low (separate files)

## Timeline
- With parallelization: 1.5 hours
- Sequential: 3 hours
- Efficiency gain: 50%
```

**Note:** `/pm:epic-start` **auto-analyzes** if analysis doesn't exist. Manual analysis is OPTIONAL.

---

### Coordination System

Agents coordinate through:
1. **File-level isolation** - Different agents work on different files
2. **Git commits** - Agents see each other's work through commits
3. **Progress files** - Each stream updates `.claude/epics/<epic>/updates/<issue>/stream-X.md`
4. **Analysis contract** - Analysis file defines boundaries

**Conflict Resolution:**
- **Same file needed** - Agents serialize access or report conflict
- **Dependencies** - Streams wait for prerequisite streams to complete
- **Errors** - Agent reports issue, continues with other work

---

## Synchronization & Maintenance

### `/pm:sync [epic-name]`

**Purpose:** Bidirectional sync between local files and GitHub issues

**Process:**
1. **Pull from GitHub**
   - Fetch all epic & task issues
   - Check for state changes (closed, reopened)
   - Check for body updates
2. **Update Local**
   - If GitHub newer → update local
   - If GitHub closed → close local
   - Update frontmatter timestamps
3. **Push to GitHub**
   - If local newer → update GitHub
   - If no GitHub issue → create new
   - Update issue body and status
4. **Handle Conflicts**
   - If both changed → ask user (local/github/merge)

**When to use:**
- After working offline
- Before starting new work (ensure sync)
- After manual GitHub edits
- Periodic sync (daily/weekly)

---

### `/pm:import`

**Purpose:** Import existing GitHub issues into CCPM

**Options:**
- `--epic <name>` - Import into specific epic
- `--label <label>` - Import only issues with label
- No args - Import all untracked issues

**Process:**
1. Fetches GitHub issues
2. Identifies untracked (not in .claude/epics/)
3. Categorizes (epic vs task) by labels
4. Creates local structure
5. Sets frontmatter with `imported: true`

**When to use:**
- Migrating existing GitHub project to CCPM
- Importing issues from external sources
- Recovering after manual issue creation

---

### `/pm:epic-refresh <name>`

**Purpose:** Recalculate epic progress from task states

**Process:**
1. Counts closed vs total tasks
2. Calculates progress percentage
3. Updates epic status (backlog/in-progress/completed)
4. Updates GitHub epic task list checkboxes
5. Updates frontmatter timestamps

**When to use:**
- After manually closing tasks
- After bulk task updates
- After `/pm:sync`
- Epic progress seems out of sync

---

## Utility Commands

### `/prompt`

**Purpose:** Execute complex prompts that fail in the input field

**When to use:** Prompt with many `@` references or very long text

**Process:**
1. Write complex prompt in `.claude/commands/prompt.md`
2. Run `/prompt`
3. Command executes the written prompt

---

### `/re-init`

**Purpose:** Update CLAUDE.md with rules from `.claude/CLAUDE.md`

**When to use:**
- After updating .claude/CLAUDE.md
- CLAUDE.md missing or outdated
- Want to sync project-specific rules

---

### `/code-rabbit`

**Purpose:** Process CodeRabbit review comments with context

**Process:**
1. User pastes CodeRabbit comments
2. Claude evaluates each with **codebase context**
3. **Accepts** suggestions that improve quality
4. **Ignores** suggestions that don't apply
5. Applies accepted changes (parallel agents for multiple files)
6. Reports decisions with reasoning

**Decision Framework:**
- Accept: Actual bugs, security issues, logic errors
- Ignore: Style conflicts, inapplicable best practices, false positives

---

### Other Utility Commands

#### `/pm:prd-edit <name>` - Edit existing PRD
#### `/pm:prd-list` - List all PRDs
#### `/pm:prd-status` - Show PRD implementation status
#### `/pm:epic-edit <name>` - Edit epic details
#### `/pm:epic-list` - List all epics
#### `/pm:epic-show <name>` - Display epic and tasks
#### `/pm:epic-close <name>` - Mark epic as complete
#### `/pm:issue-show <num>` - Display issue details
#### `/pm:issue-status <num>` - Check issue status
#### `/pm:issue-close <num>` - Close issue
#### `/pm:issue-reopen <num>` - Reopen closed issue
#### `/pm:issue-edit <num>` - Edit issue details
#### `/pm:search <query>` - Search across all content
#### `/pm:validate` - Check system integrity
#### `/pm:in-progress` - List work currently in progress
#### `/pm:help` - Show help message

---

## Complete Command Reference

### Context Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/context:create` | Initialize context system | Project start, major restructure |
| `/context:prime` | Load project context | Session start, after /clear |
| `/context:update` | Update context files | Session end, after major changes |

### Setup Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:init` | Initialize CCPM system | First time setup |
| `/re-init` | Update CLAUDE.md | After changing .claude/CLAUDE.md |

### PRD Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:prd-new <name>` | Create PRD with brainstorming | Starting new feature |
| `/pm:prd-parse <name>` | Convert PRD to epic | After PRD approval |
| `/pm:prd-list` | List all PRDs | Check what's planned |
| `/pm:prd-edit <name>` | Edit PRD | Update requirements |
| `/pm:prd-status` | PRD implementation status | Track PRD → Epic → Tasks |

### Epic Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:epic-decompose <name>` | Break epic into tasks | After prd-parse |
| `/pm:epic-sync <name>` | Push to GitHub | After decompose |
| `/pm:epic-oneshot <name>` | Decompose + sync | Quick workflow |
| `/pm:epic-start <name>` | **Launch parallel execution** | **Ready to build** |
| `/pm:epic-list` | List all epics | Overview of work |
| `/pm:epic-show <name>` | Show epic details | Review tasks |
| `/pm:epic-status [name]` | Epic progress | Track completion |
| `/pm:epic-refresh <name>` | Recalc progress | After task updates |
| `/pm:epic-close <name>` | Mark complete | All tasks done |
| `/pm:epic-merge <name>` | Merge to main | Epic complete, ready to ship |
| `/pm:epic-edit <name>` | Edit epic | Update details |

### Issue/Task Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:issue-analyze <num>` | Analyze for streams | Before execution (optional) |
| `/pm:issue-start <num>` | Work on single task | Manual task execution |
| `/pm:issue-sync <num>` | Complete task | Task finished |
| `/pm:issue-show <num>` | Show details | Review task |
| `/pm:issue-status <num>` | Check status | Quick status |
| `/pm:issue-close <num>` | Close task | Mark complete |
| `/pm:issue-reopen <num>` | Reopen task | Need more work |
| `/pm:issue-edit <num>` | Edit task | Update details |

### Workflow Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:next` | Show available tasks | Find work to do |
| `/pm:status` | Project dashboard | Overall view |
| `/pm:standup` | Daily report | Morning standup |
| `/pm:blocked` | Show blocked tasks | Identify bottlenecks |
| `/pm:in-progress` | Show active work | See what's running |

### Sync & Import Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:sync [epic]` | Bidirectional sync | After offline work, periodic sync |
| `/pm:import [options]` | Import GitHub issues | Migrating to CCPM |

### Maintenance Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/pm:clean [--dry-run]` | Archive completed | Cleanup old epics |
| `/pm:search <query>` | Search content | Find specific info |
| `/pm:validate` | Check integrity | Debug issues |
| `/pm:help` | Show help | Learn commands |

### Utility Commands
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/prompt` | Execute complex prompt | Prompt too complex for input |
| `/code-rabbit` | Process CodeRabbit reviews | After code review |

---

## Best Practices

### Context Management
1. ✅ **Prime at session start** - Always load context
2. ✅ **Update at session end** - Capture your work
3. ✅ **Update after milestones** - Document achievements
4. ❌ **Don't over-update** - Only when meaningful changes
5. ✅ **Review progress.md** - Keep next steps current

### PRD & Planning
1. ✅ **Thorough brainstorming** - Don't rush PRD creation
2. ✅ **Clear acceptance criteria** - Make requirements testable
3. ✅ **Document out-of-scope** - Prevents scope creep
4. ✅ **Review before parsing** - PRD quality = Epic quality
5. ❌ **Don't skip PRDs** - Even for "small" features

### Task Decomposition
1. ✅ **Keep tasks small** - 1-3 hours ideal
2. ✅ **Clear dependencies** - Accurate `depends_on` enables parallelism
3. ✅ **Atomic acceptance criteria** - Each criterion independently testable
4. ❌ **Don't over-serialize** - Minimize unnecessary dependencies
5. ✅ **Estimate conservatively** - Better to overestimate

### Execution
1. ✅ **Trust /pm:epic-start** - Auto-analysis works well
2. ✅ **Monitor don't micromanage** - Check status periodically
3. ✅ **Let parallelization happen** - Don't force sequential
4. ❌ **Don't manually analyze everything** - Only complex tasks
5. ✅ **Sync tasks when complete** - Keep GitHub updated

### Synchronization
1. ✅ **Sync regularly** - Daily or after major work
2. ✅ **Pull before push** - Avoid conflicts
3. ✅ **Resolve conflicts promptly** - Don't let them accumulate
4. ✅ **Backup before sync** - Safety first
5. ✅ **Validate after sync** - Check nothing broken

### Maintenance
1. ✅ **Clean periodically** - Archive old epics
2. ✅ **Validate system health** - Run /pm:validate monthly
3. ✅ **Refresh epic progress** - After bulk task updates
4. ✅ **Document decisions** - Update context when architecture changes
5. ✅ **Review standups** - Stay aware of project state

---

## Troubleshooting

### Setup Issues

**"Error: No git remote found"**
- Initialize git: `git init`
- Add remote: `git remote add origin <url>`

**"Error: Not authenticated with GitHub"**
- Run: `gh auth login`

**"gh-sub-issue extension not found"**
- Run: `/pm:init` (installs automatically)

**"Warning: Repository not accessible"**
- Verify repo exists: `gh repo view`
- Check write access
- Check authentication: `gh auth status`

---

### Context Issues

**"No context found"**
- Run: `/context:create`

**"Context files corrupted"**
- Check frontmatter format (starts with `---`)
- Re-create: `/context:create` (backup first)

**"Context outdated"**
- Run: `/context:update`

---

### Execution Issues

**"/pm:epic-start does nothing"**
- Check tasks have no unmet dependencies: `/pm:next`
- Verify epic synced to GitHub: `/pm:epic-show <name>`
- Check uncommitted changes: `git status`

**"Too many agents spawned"**
- `/pm:epic-start` is aggressive
- Use `/pm:issue-start <num>` for single tasks
- Edit analysis files to reduce streams

**"Agent conflicts on same file"**
- Expected - agents coordinate through commits
- If real conflict: resolve manually, agents will adapt

---

### Sync Issues

**"Tasks not syncing to GitHub"**
- Check ccpm.config: `cat .claude/ccpm.config`
- Verify auth: `gh auth status`
- Test manually: `gh issue list`

**"GitHub state conflicts with local"**
- Run: `/pm:sync` (handles conflicts)
- Choose: local/github/merge when prompted

**"Issues created in wrong repo"**
- Check `.claude/ccpm.config` GITHUB_REPO value
- Should match your repository

---

### Merge Issues

**"Merge conflicts"**
- Expected when main has changed
- Resolve manually or abort
- See conflict markers (<<<<<<)
- `git add` resolved files, then `git commit`

**"Cannot merge - active agents"**
- Stop agents first (they'll finish their work)
- Wait for consolidation
- Then merge

---

## Recommended Workflows

### Simple Workflow (Most Common)
```bash
# Session Start
/context:prime

# New Feature
/pm:prd-new feature-name          # Interactive brainstorming
/pm:prd-parse feature-name        # Create epic
/pm:epic-oneshot feature-name     # Decompose + sync to GitHub
/pm:epic-start feature-name       # Launch parallel execution

# Monitor
/pm:status                        # Check overall progress
/pm:standup                       # Daily check-in

# Complete
/pm:issue-sync 2                  # As tasks finish
/pm:epic-merge feature-name       # When all tasks done

# Session End
/context:update                   # Capture work
```

**Time:** ~10 min setup, agents do the work

---

### Advanced Workflow (Maximum Control)
```bash
# Session Start
/context:prime

# Planning Phase
/pm:prd-new feature-name
# Edit .claude/prds/feature-name.md if needed

/pm:prd-parse feature-name
# Edit .claude/epics/feature-name/epic.md if needed

/pm:epic-decompose feature-name
# Edit task files if needed

/pm:epic-sync feature-name

# Execution Phase
/pm:issue-analyze 2               # Manual analysis
# Edit analysis if needed
/pm:issue-analyze 3

/pm:epic-start feature-name       # Uses manual analyses

# Monitor closely
/pm:epic-status feature-name
/pm:standup

# Complete
/pm:issue-sync 2
/pm:epic-merge feature-name

# Session End
/context:update
```

**Time:** 30-60 min, full control

---

### Learning Workflow (One Task at a Time)
```bash
# Session Start
/context:prime

# Setup
/pm:prd-new feature-name
/pm:prd-parse feature-name
/pm:epic-oneshot feature-name

# Work on tasks individually
/pm:next                          # See available
/pm:issue-start 2                 # Work on task 2
# ... wait for completion ...
/pm:issue-sync 2                  # Mark complete

/pm:next                          # See next available
/pm:issue-start 3                 # Work on task 3

# When all done
/pm:epic-merge feature-name

# Session End
/context:update
```

**Time:** Hours/days, full understanding

---

## Key Takeaways

1. **Context is foundational** - Prime at start, update at end
2. **Two levels of parallelism** - Between tasks AND within tasks
3. **`/pm:epic-start` is powerful** - Auto-analyzes, launches everything
4. **`/pm:issue-analyze` is optional** - Only for manual control
5. **Sync regularly** - Keep local and GitHub aligned
6. **Trust the system** - Automation works, don't over-control
7. **Monitor don't micromanage** - Check status, let agents work
8. **Archive completed work** - Keep workspace clean

---

## Quick Reference Card

### Daily Commands
```bash
/context:prime              # Start session
/pm:status                  # Check project
/pm:next                    # Find work
/pm:standup                 # Daily report
/context:update             # End session
```

### New Feature Workflow
```bash
/pm:prd-new <name>          # Requirements
/pm:prd-parse <name>        # Epic
/pm:epic-oneshot <name>     # Tasks + GitHub
/pm:epic-start <name>       # BUILD IT
/pm:epic-merge <name>       # Ship it
```

### Maintenance
```bash
/pm:sync                    # Sync with GitHub
/pm:clean                   # Archive old work
/pm:validate                # Check health
```

---

**Bottom line:** CCPM combines context management, structured planning, GitHub integration, and multi-level parallel execution to turn hours of sequential work into minutes of coordinated automation. Use context to maintain knowledge, PRDs to capture requirements, epics to organize work, and parallel execution to maximize speed.
