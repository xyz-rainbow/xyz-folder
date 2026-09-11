# xyz-folder

**Agent skill & standalone CLI engine for aesthetic directory and drive organization** — classifies messy folders into the clean `[emoji] [Category]/[emoji] [Subcategory]/` architecture with zero data loss.

Works on **Windows, Linux, and macOS**. Zero external dependencies (Python 3 stdlib only).

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-c8ff00?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/skills.sh-xyz--folder-00f0ff?style=flat-square" alt="skills.sh" />
  <img src="https://img.shields.io/badge/npx%20skills%20add-xyz--rainbow%2Fxyz--folder-ff2bd6?style=flat-square" alt="npx skills add" />
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-00ffff?style=flat-square" alt="Platform" />
  <img src="https://img.shields.io/badge/python-3%2B-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python" />
</p>

---

## One-command installation

Install directly into your agent environment using `skills`:

```bash
npx skills add xyz-rainbow/xyz-folder
```

Or globally / non-interactively:

```bash
npx skills add xyz-rainbow/xyz-folder -g -y
```

---

## What it does

- **Aesthetic Double-Bracket Layout**: Organizes loose files into clean `[emoji] [Category]/[emoji] [Subcategory]/` folders.
- **Zero Data Loss Guarantee**: Every file move is verified. If a file with the same name exists at destination, it appends a safe counter (`filename (1).ext`) instead of overwriting.
- **Extensive Taxonomy**: Recognizes 50+ file types across Installers, Documents, Media (Audio/Video/Images), Compressed Archives, and Development/AI (LLM weights, repos, scripts).
- **Safety Pre-flight (Dry-run)**: Preview every planned move before touching a single byte.
- **Cross-Platform**: Automatically locates default Downloads directory across Windows (Registry/User Shell), macOS, and Linux.

---

## Taxonomy Showcase

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

## Standalone CLI Usage

You can also run the organizer script directly without an AI agent:

### 1. Preview changes (Dry-Run):
```bash
python3 scripts/organize.py --dry-run
```

### 2. Organize custom folder:
```bash
python3 scripts/organize.py --target "/path/to/chaotic/folder"
```

### 3. Organize default Downloads folder:
```bash
python3 scripts/organize.py
```

---

## License

MIT © [xyz-rainbow](https://github.com/xyz-rainbow)
