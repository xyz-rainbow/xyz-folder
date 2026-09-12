# xyz-folder

**Autonomous protocol & universal template framework for aesthetic directory and drive organization** — dynamically organizes, categorizes, and normalizes messy folders into an adaptive emoji taxonomy with single-word root containers and zero data loss.

Works on **Windows, Linux, and macOS**. Zero external dependencies (Python 3 stdlib only).

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-c8ff00?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/skills.sh-xyz--folder-00f0ff?style=flat-square" alt="skills.sh" />
  <img src="https://img.shields.io/badge/npx%20skills%20add-xyz--rainbow%2Fxyz--folder-ff2bd6?style=flat-square" alt="npx skills add" />
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-00ffff?style=flat-square" alt="Platform" />
  <img src="https://img.shields.io/badge/python-3%2B-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python" />
</p>

![Banner](assets/banner.svg)

---

## One-command installation

Install directly into your agent environment using `skills`:

```bash
npx skills add xyz-rainbow/xyz-folder
```

Or via direct GitHub URL:

```bash
npx skills add https://github.com/xyz-rainbow/xyz-folder
```

Global, non-interactive install:

```bash
npx skills add xyz-rainbow/xyz-folder -g -y
```

---

## Key Capabilities

- **Interactive Alignment First**: The agent will never blindly scramble your files. It scans signatures, asks clarifying questions, debates proposed categories with you, and waits for your confirmation.
- **Granular Multi-Phase Execution & Checkpoint Confirmations**: Partitions large reorganizations into bite-sized sequential phases (Purge Duplicates -> De-nest Bridge Folders -> Provision Skeleton -> Domain Migrations -> File Deduplication -> Zero-Orphan Audit). Each phase is explicitly presented, reviewed, and approved with checkpoints before touching disk.
- **Single-Word Root Categories**: Root containers strictly enforce a single, concise word (`[Estudios]`, `[Salud]`, `[Pension]`, `[Identidad]`, `[Trabajo]`, `[Facturas]`, `[Legal]`, `[Apuntes]`, `[Otros]`) eliminating visual clutter and hyphenated monstrosities. Subcategories also prioritize single-word names.
- **Module Nesting Architecture**: Eliminates root fragmentation by neatly grouping creative notes (`Ascii`, `Youtube`) inside `[Apuntes]` / `[Notes]`, and peripheral vaults (`Ebooks`, `Backups`, `Hardware`) inside `[Otros]` / `[Other]`.
- **Cognitive Template & Non-Deterministic Framework**: Not a rigid schema. The agent dynamically derives a tailored taxonomy from modular archetypes, adapting to your specific workflow domain and files.
- **Dynamic Language & Culture Auto-Alignment**: Automatically detects and adapts to your language (English, Spanish, German, French, Japanese, etc.), translating all category names and aligning semantic emojis.
- **Copy-First & Live Backup Architecture**: Cross-drive migrations copy first and verify byte-by-byte before purging the source. Same-drive work is an atomic directory move. The agent never deletes a "duplicate" without a content hash in the plan.
- **Full Rollback & Selective Undo**: Every operation writes `.xyz-folder/manifest.json`. You can cancel progress, revert everything (`--undo`), or restore a subset (`--restore-filter`). Legacy `.xyz-folder-manifest.json` is still accepted.
- **Git Repository & Workspace Invariance**: Preserves active Git repositories (`.git/`) and code projects 100% untouched. Repo folder names, commit history, and branches remain invariant while parent containers are organized and IDE workspace files (`*.code-workspace`) are automatically updated.
- **Windows Service Registry Lock Protection**: Audits `HKLM\SYSTEM\CurrentControlSet\Services` to guarantee that executables linked to active Windows background services (e.g. `SbieSvc.exe`) are preserved without process locks or crashes.
- **Storage Topology & Anti-Thrashing Engine**: Distinguishes between same-drive atomic pointer updates and cross-drive staged copy-first migrations. Enforces shallow scans on large or mechanical HDDs to eliminate head thrashing and multi-minute freezes.
- **Aesthetic Double-Bracket Layout & Recursive Subfolders**: Categorizes loose files and nested folders into clean `[emoji] [Category]/[emoji] [Subcategory]/[emoji] [Folder]/` directories with no orphan flat paths left behind.
- **One-by-One with Full Tree Protocol**: Never runs blind mass-renaming. Operates folder by folder, dumping granular trees and presenting "CÓMO ERA" vs "CÓMO QUEDARÍA" before touching disk.
- **Protected Paths & Game Saves**: Keeps game saves (Diablo IV, PCSX2, My Games, etc.), system consoles, and registry-bound binaries 100% protected and untouched.
- **NTFS Compatibility Junctions & Shell Registry Awareness**: Automatically audits Windows `User Shell Folders` and game engine paths (like Cyberpunk 2077 photomode), deploying transparent NTFS junctions (`mklink /J`) to preserve OS shortcuts (`Win + PrtScn`) and game compatibility.
- **Semantic Media Inspection & Contextual Renaming**: Inspects images visually, extracts OCR text, and examines metadata to propose clean kebab-case filenames instead of keeping cryptic UUIDs, camera timestamps, or default generator prefixes.
- **Attribute Remediation & Lock Bypass**: Transparently clears Windows `FILE_ATTRIBUTE_READONLY` attributes and bypasses Explorer preview/thumbnail locks (`rename-truncate-remove`) to eliminate `Access Denied` and `File in Use` errors.
- **Zero Data Loss Guarantee**: Atomic operations with programmatic byte-verification. Destination collisions automatically append safe version counters (`file (1).ext`) — never overwriting.
- **Inventory Coverage & User-Named Roots**: Every depth-1 child must appear in the plan. User-named principals stay as roots; presets fill subfolders. Unsorted buckets (`Otros`, `Random`, `Downloads`) get their own pass.
- **Open-the-File Renaming**: Generic names (`Untitled document`, numeric hashes) are classified by content, not filename. Identity documents are not given scenic names.

![Architecture](assets/architecture.svg)

![Workflow](assets/workflow.svg)

---

## Naming Syntax Formats Catalog

Before touching disk, the agent asks you to select your preferred naming syntax:

| Format | Syntax Pattern | Example Root Directory | Best For |
| :--- | :--- | :--- | :--- |
| **Format A** | `[emoji] [Nombre]` | `[🪪] [Identidad]` | Visual aesthetic layout, high contrast icon-first |
| **Format B** | `[00]-[Nombre]` | `[01]-[Identidad]` | Deterministic file manager sorting without emojis |
| **Format C** | `[00]-[Nombre] [Emoji]` | `[01]-[Personal] [👤]` | **(Recommended)** Combines OS file sorting with visual clarity |
| **Format D** | `[Emoji]-[Nombre] [00]` | `[🪪]-[Identidad] [01]` | Visual categorization with trailing index tags |
| **Format E** | `[00]-[Nombre] [ASCII]` | `[01]-[Personal] [*]` | Terminal-focused environments, legacy shells, retro ASCII |

### Gravity-Based `[00]` Sorting Hierarchy

- **`[00]-[09]` (Vital Core)**: Identity documents, personal cards, social security benefits, official state resolutions.
- **`[10]-[19]` (Health & Mind)**: Medical diagnostics, psychiatric records, cognitive architectures, therapy.
- **`[20]-[29]` (Career & Study)**: Academic institutes, professional CVs, employment contracts, invoices.
- **`[30]-[39]` (Legal Defense)**: Police reports, incident evidence logs, court complaints, vehicle registries.
- **`[40]-[49]` (AI & Knowledge)**: Local AI models, agent skills, prompts, study notes (`[Apuntes]` nesting `[Ascii]` & `[Youtube]`).
- **`[50]-[99]` (Vaults & Storage)**: Auxiliary stores, Calibre libraries (`[Ebooks]`), `[Backups]`, `[Hardware]`, `[Otros]`.

---

## Modular Presets & Archetypes Library

> [!NOTE]
> These presets are **modular archetypes and inspiration templates**, not hardcoded schemas. The AI agent evaluates your directory and assembles a customized taxonomy matching your language and rules.

### 1. Developer Workspaces & Code Repositories (`[💻] [Projects]`)

```text
Target Projects/
├── [🚀] [Apps]/                  # Core production applications, tools, CLI engines
├── [🧪] [Labs]/                  # Experimental prototypes, labs, game jam projects
├── [🌐] [Webs]/                  # Portals, dashboards, browser extensions ([🧩] [Extensions])
├── [🤖] [AI]/                    # Local LLMs, model weights, prompt vaults, research papers
├── [📟] [Hardware]/              # Embedded, ESP32, Cardputer, firmware, pinout docs
├── [🎬] [Animation]/             # Creative production, renders, scene clips, 3D character art
├── [🛠️] [Tools]/                 # Proxies, monitoring daemons, ADB helpers, sysadmin scripts
└── [📦] [Backups]/               # Historical zips, snapshots, legacy project forks
```

### 2. Master Documents & Knowledge Hub (`[📚] [Documents]`)

```text
Documents Hub/
├── [🪪] [Identity]/              # National IDs, passports, driver licenses, family records
├── [🏛️] [Pension]/               # Social security, retirement, disability/orphan benefits
├── [📑] [Disability]/            # Disability determinations, welfare resolution cards
├── [🏥] [Health]/                # Medical summaries, hospital reports, clinical tests
├── [🧠] [Cognitive]/             # Psychological evaluations, neurodivergence assessments
├── [🎓] [Studies]/               # Academic institutes, coursework, assignments (EAC), exams
├── [📄] [Curriculum]/            # Resumes, CV versions, cover letters, portfolios
├── [💼] [Work]/                  # Client contracts, employment agreements, deliverables
├── [🧾] [Invoices]/              # Taxes, receipts, accounting spreadsheets, bills
├── [👮] [Legal]/                 # Police reports, court documents, incident logs
├── [🤖] [AI]/                    # Agent configurations, MCP manifests, custom prompts
├── [📝] [Notes]/                 # Notes & scripts; nests [🎨] [Ascii] and [📺] [Youtube]
│   ├── [🎨] [Ascii]/
│   └── [📺] [Youtube]/
└── [📂] [Other]/                 # Staging & vaults; nests [📖] [Ebooks], [📦] [Backups], [📟] [Hardware]
    ├── [📖] [Ebooks]/
    ├── [📦] [Backups]/
    └── [📟] [Hardware]/
```

### 3. Visual & Creative Media Hub (`[🎨] [Media]`)

```text
Media Hub/
├── [📸] [Screenshots]/            # Screen captures (NTFS Junction to original system path)
├── [🖼️] [Wallpapers]/             # Curated 4K/10K wallpapers, AI generative artwork
├── [✨] [Logos]/                  # Logos, vector banners, visual brand identities
├── [📱] [Icons]/                  # Software icons, UI packs, dock iconography
├── [🧊] [Models]/                 # 3D printable models (STL, OBJ, CAD files)
├── [🎬] [Captures]/               # Game Bar video recordings, desktop captures
├── [🧠] [Cognitive]/              # Walkthroughs, architectural system recordings
├── [🎵] [Music]/                  # Master audio library, FLAC & MP3 discographies
├── [🎤] [Artists]/                # Music collections classified by artist name
└── [🔔] [Alerts]/                 # System sound effects, alert audio samples
```

### 4. System Tools & Utility Storage (`[🛠️] [Tools]`)

```text
Tools Hub/
├── [🔧] [Rescue]/                 # Drive repair, exFAT watchdog, desktop restorers
├── [💾] [Imaging]/                # OS imaging, Rufus, BalenaEtcher, Ventoy utilities
├── [📻] [Radio]/                  # Software Defined Radio suites (SDR++, SDRSharp)
├── [🔑] [Vaults]/                 # Encrypted credential vaults, Bitwarden backups
├── [📱] [Android]/                # Mobile packages, APKs, ADB platform tools
└── [📦] [Sandbox]/                # Application isolation runtimes, service mirrors
```

### 5. Server Infrastructure & Homelab (`[🚀] [Homelab]`)

```text
Homelab Hub/
├── [☸️] [K8s]/                    # Pod manifests, debugging pods, [🧩] [ConfigMaps]
├── [💾] [NAS]/                    # Network storage mount scripts, NAS watchdogs
├── [🐂] [Longhorn]/               # Distributed CSI storage, disaster recovery plans
├── [🎵] [Pipeline]/               # Tagging workers, Beets configs, queue automations
├── [🛠️] [Scripts]/                # SQL helpers, decrypt tools, emergency scripts
└── [📦] [Backups]/                # Snapshot archives, volume backups, database dumps
```

---

## Standalone CLI Engine

The bundled `scripts/organize.py` serves as a reference engine and can be executed standalone:

### 1. Preview changes (Dry-Run):
```bash
python3 scripts/organize.py --dry-run
```

### 2. Organize custom folder with language selection:
```bash
# Spanish categories:
python3 scripts/organize.py --target "/path/to/folder" --lang es

# English categories:
python3 scripts/organize.py --target "/path/to/folder" --lang en
```

### 3. Full Rollback (Undo entire operation):
```bash
python3 scripts/organize.py --target "/path/to/folder" --undo
```

### 4. Selective Restoration (Restore specific files or patterns):
```bash
python3 scripts/organize.py --target "/path/to/folder" --restore-filter ".pdf"
```

---

## GitHub topics

`ai-agent-skill` `skills-sh` `npx-skills-add` `agent-skills` `folder-organizer` `directory-organizer` `file-organizer` `zero-data-loss` `windows` `linux` `macos` `python`

---

## Sponsor this project

If this skill helps keep your workspace, downloads, and storage clean:

- [Buy Me a Coffee](https://buymeacoffee.com/xyzclouds)
- [Ko-fi](https://ko-fi.com/xyzclouds)
- [Patreon](https://patreon.com/xyzclouds)
- [PayPal](https://paypal.me/rainbowkolors)

---

## License

MIT © [xyz-rainbow](https://github.com/xyz-rainbow). See [LICENSE](LICENSE).
