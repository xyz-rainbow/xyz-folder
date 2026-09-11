# xyz-folder

**Autonomous protocol & universal template framework for aesthetic directory and drive organization** — dynamically organizes, categorizes, and normalizes messy folders into an adaptive emoji taxonomy with zero data loss.

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
- **Cognitive Template & Non-Deterministic Framework**: Not a rigid schema. The agent dynamically derives a tailored taxonomy from modular archetypes, adapting to your specific workflow domain and files.
- **Dynamic Language & Culture Auto-Alignment**: Automatically detects and adapts to your language (English, Spanish, German, French, Japanese, etc.), translating all category names and aligning semantic emojis.
- **Copy-First & Live Backup Architecture**: Files are copied and verified byte-by-byte into the new structure while keeping original files 100% untouched as a live safety backup. The agent never deletes the source without your explicit consent.
- **Full Rollback & Selective Undo**: Every operation writes a `.xyz-folder-manifest.json` transaction log. You can cancel progress, revert everything back to its exact original state (`--undo`), or selectively restore individual files/folders.
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

![Architecture](assets/architecture.svg)

![Workflow](assets/workflow.svg)

---

## Modular Presets & Archetypes Library

> [!NOTE]
> These presets are **modular archetypes and inspiration templates**, not hardcoded schemas. The AI agent evaluates your directory and assembles a customized taxonomy matching your language and rules.

### 1. Developer Workspaces & Code Repositories (`[💻] [Projects]`)

```text
Target Projects/
├── [🚀] [Main-Apps]/              # Core production applications, tools, CLI engines
├── [🧪] [Secondary-Labs]/         # Experimental prototypes, labs, game jam projects
├── [🌐] [Webs-Extensions]/        # Portals, dashboards, browser extensions ([🧩] [Extensions])
├── [🤖] [AI-Research]/            # Local LLMs, model weights, prompt vaults, research papers
├── [📟] [Hardware-IoT]/           # Embedded, ESP32, Cardputer, firmware, pinout docs
├── [🎬] [Animation-Studio]/       # Creative production, renders, scene clips, 3D character art
├── [🛠️] [Dev-Tools-Scripts]/      # Proxies, monitoring daemons, ADB helpers, sysadmin scripts
└── [📦] [Backups-Archives]/       # Historical zips, snapshots, legacy project forks
```

### 2. Master Documents & Knowledge Hub (`[📚] [Documents]`)

```text
Documents Hub/
├── [👤] [Personal]/               # Identification, medical, administrative, resumes
├── [🧾] [Invoices]/               # Taxes, receipts, accounting spreadsheets, bills
├── [💼] [Work]/                   # Client contracts, deliverables, enterprise projects
├── [📖] [Ebooks]/                 # Calibre library (metadata.db), EPUB, MOBI, PDF readers
├── [📟] [Hardware-Docs]/          # Datasheets, schematics, microcontroller manuals
├── [📦] [Exports]/                # Bookmarks, database dumps, application exports
├── [📺] [Media-Content]/          # Video scripts, presentation outlines, transcripts
├── [🤖] [AI-Tools]/               # Agent configurations, MCP manifests, custom prompts
└── [🎨] [Ascii]/                  # ASCII art collections, brand assets, retro themes
```

### 3. Visual & Creative Media Hub (`[🎨] [Media]`)

```text
Media Hub/
├── [📸] [Screenshots]/            # Screen captures (NTFS Junction to original system path)
├── [🖼️] [Wallpapers]/             # Curated 4K/10K wallpapers, AI generative artwork
├── [✨] [Brand-Logos]/             # Logos, vector banners, visual brand identities
├── [📱] [App-Icons]/              # Software icons, UI packs, dock iconography
├── [🧊] [3D-Models]/              # 3D printable models (STL, OBJ, CAD files)
├── [🎬] [Captures]/               # Game Bar video recordings, desktop captures
├── [🧠] [Cognitive-OS]/           # Walkthroughs, architectural system recordings
├── [🎵] [Music]/                  # Master audio library, FLAC & MP3 discographies
├── [🎤] [Artists]/                # Music collections classified by artist name
└── [🔔] [Notifications]/          # System sound effects, alert audio samples
```

### 4. System Tools & Utility Storage (`[🛠️] [Tools]`)

```text
Tools Hub/
├── [🔧] [System-Rescue]/          # Drive repair, exFAT watchdog, desktop restorers
├── [💾] [USB-Flashing]/           # OS imaging, Rufus, BalenaEtcher, Ventoy utilities
├── [📻] [SDR-Radio]/              # Software Defined Radio suites (SDR++, SDRSharp)
├── [🔑] [Pass-Exports]/           # Encrypted credential vaults, Bitwarden backups
├── [📱] [Android-APK]/            # Mobile packages, APKs, ADB platform tools
└── [📦] [Sandboxie]/              # Application isolation runtimes, service mirrors
```

### 5. Server Infrastructure & Homelab (`[🚀] [Homelab]`)

```text
Homelab Hub/
├── [☸️] [K8s-Cluster]/             # Pod manifests, debugging pods, [🧩] [ConfigMaps-Patches]
├── [💾] [NAS-Storage]/            # Network storage mount scripts, NAS watchdogs
├── [🐂] [Longhorn-Storage]/       # Distributed CSI storage, disaster recovery plans
├── [🎵] [Music-Pipeline]/         # Tagging workers, Beets configs, queue automations
├── [🛠️] [Admin-Scripts]/          # SQL helpers, decrypt tools, emergency scripts
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
