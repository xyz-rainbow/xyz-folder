# xyz-folder

**AI agent skill & standalone CLI engine for aesthetic directory and drive organization** — dynamically organizes, categorizes, and normalizes messy folders into an adaptive emoji taxonomy with zero data loss.

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
- **Copy-First & Live Backup Architecture**: Files are copied and verified byte-by-byte into the new structure while keeping the original files 100% untouched as a live safety backup. The agent never deletes the source without your explicit consent.
- **Full Rollback & Selective Undo**: Every operation writes a `.xyz-folder-manifest.json` transaction log. You can cancel progress, revert everything back to its exact original state (`--undo`), or selectively restore individual files/folders.
- **Safety Checkpoints & Backup Verification**: Automatically checks disk health and available capacity. For large operations or cross-disk migrations (robocopy/rsync), ensures safety checkpoints exist before moving bytes.
- **Aesthetic Double-Bracket Layout & Recursive Subfolders**: Categorizes loose files and nested folders into clean `[emoji] [Category]/[emoji] [Subcategory]/[emoji] [Folder]/` directories with no orphan flat paths left behind.
- **One-by-One with Full Tree Protocol**: Never runs blind mass-renaming. Operates folder by folder, dumping granular trees and presenting "CÓMO ERA" vs "CÓMO QUEDARÍA" before touching disk.
- **Protected Paths & Game Saves**: Keeps game saves (Diablo IV, PCSX2, My Games, etc.), system consoles, and registry-bound binaries 100% protected and untouched.
- **NTFS Compatibility Junctions & Shell Registry Awareness**: Automatically audits Windows `User Shell Folders` and game engine paths (like Cyberpunk 2077 photomode), deploying transparent NTFS junctions (`mklink /J`) to preserve OS shortcuts (`Win + PrtScn`) and game compatibility.
- **Semantic Media Inspection & Contextual Renaming**: Inspects images visually, extracts OCR text, and examines metadata to propose clean kebab-case filenames instead of keeping cryptic UUIDs, camera timestamps, or default generator prefixes.
- **Attribute Remediation & Lock Bypass**: Transparently clears Windows `FILE_ATTRIBUTE_READONLY` attributes and bypasses Explorer preview/thumbnail locks (`rename-truncate-remove`) to eliminate `Access Denied` and `File in Use` errors.
- **Zero Data Loss Guarantee**: Atomic operations with programmatic byte-verification. Destination collisions automatically append safe version counters (`file (1).ext`) — never overwriting.
- **Dynamic Localization**: Automatically detects and speaks your language (Spanish, English, etc.), creating localized folder names (e.g. `[🎨] [Multimedia]/[🖼️] [Imágenes]` or `[🎨] [Media]/[🖼️] [Images]`).

![Architecture](assets/architecture.svg)

![Workflow](assets/workflow.svg)

---

## Adaptive Taxonomy Showcase

> [!NOTE]
> The taxonomy below is an **illustrative reference example**. Categories and emojis dynamically adapt to whatever files are discovered in the target directory.

```text
Directory/
├── [📦] [Installers]/
│   ├── [💻] [Desktop Apps]/
│   └── [📱] [Mobile & Packages]/
├── [📄] [Documents]/
│   ├── [📑] [PDFs & Books]/
│   ├── [📊] [Office & Sheets]/
│   └── [📝] [Notes & Text]/
├── [🎨] [Media]/
│   ├── [🖼️] [Images]/
│   ├── [🎬] [Videos]/
│   └── [🎵] [Audio]/
├── [🗜️] [Archives]/
│   ├── [📦] [ZIP & RAR]/
│   └── [💿] [Disk Images & ISOs]/
└── [💻] [Development & AI]/
    ├── [🤖] [Models & Weights]/
    ├── [🐙] [Repos & Code]/
    └── [🛠️] [Scripts & Config]/
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

> **Note for AI Agents**: `scripts/organize.py` is a baseline reference. Agents are instructed to tailor, extend, or generate custom migration and organization scripts dynamically to best fit the user's specific files, operating system, and storage topology.

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
