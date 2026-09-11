---
name: xyz-folder
description: >
  Autonomous protocol and CLI engine to organize, categorize, and normalize folders and drives
  into the strict double-bracket and emoji aesthetic architecture ([emoji] [Category]/[emoji] [Subcategory]/).
  Features zero-data-loss verification, collision prevention, file-signature taxonomy, and pre-flight dry-run inspection.
  Use when the user asks to "organize downloads", "clean my folders", "sort files", "organize drive",
  "ordenar descargas", "clasificar archivos con emojis", or runs /xyz-folder.
---

# xyz-folder — Aesthetic Directory & Drive Organizer

A universal agent skill and standalone CLI engine that cleans, organizes, and classifies chaotic directories (Downloads, Desktop, external storage drives, project folders) into an ultra-clean **double-bracket and emoji taxonomy**:

```text
Target Directory/
├── [📦] [Installers]/
│   ├── [💻] [Desktop Apps]/
│   └── [📱] [Mobile & Packages]/
├── [📄] [Documents]/
│   ├── [📑] [PDFs & Books]/
│   └── [📊] [Office & Sheets]/
├── [🎨] [Media]/
│   ├── [🖼️] [Images]/
│   ├── [🎬] [Videos]/
│   └── [🎵] [Audio]/
├── [🗜️] [Archives]/
│   ├── [📦] [ZIP & RAR]/
│   └── [💿] [Disk Images & ISOs]/
└── [💻] [Development & AI]/
    ├── [🤖] [Models & Weights]/
    └── [🐙] [Repos & Code]/
```

Works out of the box on **Windows, Linux, and macOS**. Zero external dependencies (Python 3 standard library only).

---

## 1. Core Principles

1. **Zero Data Loss Guarantee**:
   - Files are moved atomically and verified.
   - **Collision prevention**: If a file with the same name already exists at the destination, it is safely versioned as `filename (1).ext` — never overwritten.
   - **No deletions without explicit consent**: Temporary or duplicate cleaning requires explicit user confirmation.
2. **Strict Dual-Bracket Architecture**:
   - Categories always follow `[emoji] [Category]`.
   - Subcategories follow `[emoji] [Subcategory]`.
   - Preserves system and existing already-bracketed directories without breaking them.
3. **Pre-flight Dry-Run by Default**:
   - Always supports simulating operations first (`--dry-run`) to review proposed moves before touching disk.

---

## 2. Quick Execution

Resolve the skill directory as the folder that contains this `SKILL.md` (works for `npx skills add`, `~/.agents/skills/`, or local installs).

### Dry-run (Inspect proposed moves):
```bash
python3 scripts/organize.py --target "/path/to/folder" --dry-run
```

### Organize default user Downloads:
```bash
python3 scripts/organize.py
```

### Organize a specific path with confirmation:
```bash
python3 scripts/organize.py --target "/path/to/folder"
```

---

## 3. Taxonomy & File Mappings

| Category | Subcategory | Typical Extensions |
| :--- | :--- | :--- |
| `[📦] [Installers]` | `[💻] [Desktop Apps]` | `.exe`, `.msi`, `.appx`, `.msix`, `.pkg`, `.dmg`, `.deb`, `.rpm` |
| `[📦] [Installers]` | `[📱] [Mobile & Packages]` | `.apk`, `.xapk`, `.ipa`, `.jar` |
| `[📄] [Documents]` | `[📑] [PDFs & Books]` | `.pdf`, `.epub`, `.mobi`, `.azw3`, `.cbr`, `.cbz` |
| `[📄] [Documents]` | `[📊] [Office & Sheets]` | `.docx`, `.doc`, `.xlsx`, `.xls`, `.csv`, `.pptx`, `.ppt` |
| `[📄] [Documents]` | `[📝] [Notes & Text]` | `.txt`, `.md`, `.log`, `.rtf` |
| `[🎨] [Media]` | `[🖼️] [Images]` | `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`, `.gif`, `.psd`, `.ai` |
| `[🎨] [Media]` | `[🎬] [Videos]` | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.flv`, `.srt` |
| `[🎨] [Media]` | `[🎵] [Audio]` | `.mp3`, `.flac`, `.wav`, `.m4a`, `.aac`, `.ogg`, `.opus` |
| `[🗜️] [Archives]` | `[📦] [ZIP & RAR]` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz` |
| `[🗜️] [Archives]` | `[💿] [Disk Images & ISOs]`| `.iso`, `.img`, `.vhd`, `.vhdx`, `.bin`, `.torrent` |
| `[💻] [Development & AI]` | `[🤖] [Models & Weights]`| `.gguf`, `.safetensors`, `.onnx`, `.pt`, `.pth`, `.bin` |
| `[💻] [Development & AI]` | `[🐙] [Repos & Code]` | `.py`, `.js`, `.ts`, `.rs`, `.go`, `.html`, `.css`, `.cpp`, `.c` |
| `[💻] [Development & AI]` | `[🛠️] [Scripts & Config]`| `.sh`, `.bash`, `.ps1`, `.bat`, `.cmd`, `.json`, `.yaml`, `.yml`, `.env` |

---

## 4. Agent Guidelines

When an AI assistant executes this skill:
1. **Identify the target**: If no path is specified, ask or locate the user's primary Downloads folder.
2. **Run a Dry-Run first**: Present the category count and proposed plan to the user.
3. **Execute atomically**: Move files cleanly, handle duplicates with suffix counters, and report total files organized and space reorganized.
