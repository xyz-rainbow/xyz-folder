---
name: xyz-folder
description: >
  Autonomous protocol and CLI engine to dynamically organize, categorize, and normalize folders and drives
  into an aesthetic double-bracket and emoji taxonomy ([emoji] [Category]/[emoji] [Subcategory]/).
  Features recursive subfolder styling, zero-data-loss verification, transaction journaling, full rollback/undo,
  one-by-one granular tree inspection, and language-adaptive folder structures.
  Use when the user asks to "organize downloads", "clean my folders", "sort files", "organize drive",
  "ordenar descargas", "clasificar archivos con emojis", "deshacer ordenamiento", or runs /xyz-folder.
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

## 1. Core Principles & Guardrails

1. **Interactive Alignment & Debate First**:
   - The agent **MUST NOT** blindly move files without confirmation.
   - Always scan the target directory, analyze file signatures, detect the user language, and propose a tailored plan.
   - Debate edge cases, exclusions, and custom preferences with the user before touching disk.

2. **One-by-One with Full Tree Protocol ("Uno a Uno con Tree Exhaustivo")**:
   - When organizing or normalizing complex structures, drives, or category trees, **never perform blind mass-renaming**.
   - Proceed strictly **folder by folder ("uno a uno")**.
   - For every target category, execute a deep, granular `tree` inspection to display ALL nested subfolders and files before proposing changes.
   - Always present a clear **"CÓMO ERA" vs "CÓMO QUEDARÍA"** visual comparison.
   - Require explicit user authorization (green light) before touching disk on that specific folder.

3. **Strict Recursive Subfolder Taxonomy (`[emoji] [Carpeta]\`)**:
   - Every single level of subfolder must follow the double-bracket and emoji taxonomy: `[emoji] [Category]/[emoji] [Subcategory]/[emoji] [Sub-subcategory]/...`
   - No orphan flat/raw folders left behind when normalizing a directory tree. Every internal subfolder (e.g., `[📦] [Models]`, `[🤖] [Cline]`, `[🌸] [AnimeJS]`, `[01] [🏛️] [Socrates & Nexus Core]`) receives its explicit `[emoji] [Name]` styling.

4. **Copy-First & Post-Verification Source Purge**:
   - **Always copy first**: The original files remain 100% intact as a live safety backup during the entire transfer and organization process. Never cut/move directly without a verified replica.
   - **Verification before cleanup**: The agent writes files to the new categorized structure and verifies 100% byte integrity against the source.
   - **Source Purge upon 100% Verification**: Once the backup is 100% transferred, organized, and verified byte-by-byte with zero errors, the agent proceeds to eliminate the original files (moving them to the OS Recycle Bin / Trash) to release duplicate disk space and finalize the organization.
   - **Strict Abort on Error**: If even a single file fails verification, the source is left completely untouched.
   - **Collision prevention**: If a file with the same name exists at destination, it is versioned as `filename (1).ext` — never overwritten.

5. **Protected Ecosystem Paths & Binaries**:
   - Video game saves (`Documents/My Games`, `Diablo IV`, `PCSX2`, `Square Enix`, `Need for Speed Heat`, etc.), system shells (`PowerShell`, `WindowsPowerShell`), hardware/SDR configurations (`HDSDR`, `Vital`), and services bound in Windows Registry or system services (`X:\[Tools]`, `SbieSvc.exe`) must be explicitly protected and never altered without authorization.

6. **Windows Shell Lock & Access Denied Resolution**:
   - Windows Explorer shell locks (thumbnail cache, zip associations, `.ShellClassInfo`, `desktop.ini`) often trigger `WinError 5` (Access Denied) or `WinError 32` (File in Use) when deleting large archives or system folders.
   - Implement the safe `rename-truncate-remove` pattern or handle unblocking strategies to guarantee clean deletion of verified originals without leaving ghost files.

7. **Transaction Journaling & Full Rollback**:
   - Every operation writes a `.xyz-folder-manifest.json` transaction log.
   - At any time, the user can cancel progress, revert the entire operation back to original locations (`--undo`), or selectively restore individual files or subfolders (`--restore-filter`).

8. **Safety Backups for Heavy Migrations**:
   - Before running massive file copies or cross-drive tools like `robocopy` / `rsync`, verify destination space, assess disk health (preventing HDD head thrashing), and establish safety backups/snapshots.

9. **Dynamic Language & Taxonomy Localization**:
   - Folder names and emojis adapt to the user natural language:
     - Spanish: `[🎨] [Multimedia]/[🖼️] [Imágenes]`, `[📄] [Documentos]/[📑] [PDFs & Libros]`
     - English: `[🎨] [Media]/[🖼️] [Images]`, `[📄] [Documents]/[📑] [PDFs & Books]`
   - Categories adapt to the actual contents found (e.g., 3D models, audio stems, game mods, research datasets).

10. **Custom Script Synthesis in `.xyz-folder/`**:
    - The bundled `scripts/organize.py` is a **pedagogical baseline reference**, NOT a static rigid executable.
    - For every organization task, the agent **MUST synthesize a dedicated custom script** at `.xyz-folder/organize_session.py` tailored specifically to the files, extensions, exclusions, and language discovered in that session.
    - The script is self-documenting: includes an architectural header summarizing the debate, the exact taxonomy map, pre-flight safety checks, and the OS Recycle Bin integration.

---

## 2. Mandatory Pre-Flight Verification Checklist

Before touching a single file or generating the execution script:
1. **[Disk Space]**: Verify destination capacity with `shutil.disk_usage()`. Ensure available free space exceeds the total batch size by at least 500 MB.
2. **[File Locks]**: Confirm target files are not in use or held by running processes (e.g. IDEs, media players, torrent clients).
3. **[Permissions & Attributes]**: Verify read/write permissions and handle read-only attributes safely.
4. **[Collision Prevention]**: Ensure destination naming logic appends `(1)`, `(2)` to strictly prevent any overwrite.
5. **[Language Alignment]**: Match all directory labels to the user natural language (`[🎨] [Multimedia]` vs `[🎨] [Media]`).
6. **[Transaction Journal]**: Ensure `.xyz-folder/manifest.json` will record every source-destination pair before any file operations.

---

## 3. Agent Execution Protocol (Step-by-Step)

When an AI assistant executes this skill:

### Step 1: Dynamic Discovery & File Signature Analysis
- Never assume hardcoded paths. Detect the user primary folder dynamically via OS standards (Windows User Shell Folders / Linux XDG / macOS).
- Detect the user language (e.g., Spanish or English) to localize all category names.
- Analyze file signatures and extensions. For unknown, extensionless, or exotic files, inspect **magic bytes** (binary headers) to infer their type.

### Step 2: Granular Tree Inspection & "CÓMO ERA vs CÓMO QUEDARÍA" Debate
Before writing code or moving data, advance **one folder at a time**:
1. **Granular Tree Dump**: Run a deep `tree` command displaying every nested subfolder and file.
2. **Recursive Emoji Taxonomy**: Ensure all nested subfolders receive `[emoji] [Carpeta]\`.
3. **Protected Exclusions Check**: Confirm video game saves, application configs, and registry-bound paths are excluded.
4. **Before vs After Visual**: Show the user the exact **"CÓMO ERA" vs "CÓMO QUEDARÍA"** mapping.
- **Wait for explicit user confirmation** before touching disk.

### Step 3: Script Synthesis in `.xyz-folder/organize_session.py`
- Generate an auditable, tailored Python script inside `.xyz-folder/organize_session.py` containing:
  - Header documenting the agreed categories and exclusions.
  - Pre-flight disk space and file lock checks.
  - Copy-verify loop and transaction journaling.
  - Safe removal patterns (`rename-truncate-remove`) and OS Recycle Bin integration.

### Step 4: Staged Copy, Verification & Automated Source Cleanup
- **Copy First**: Copy files to the new categorized structure, keeping original files 100% untouched as a live safety backup.
- **Journal Transaction**: Record every copied pair into `.xyz-folder/manifest.json`.
- **Byte Verification**: Verify that 100% of destination file sizes and checksums match the source.
- **Source Purge upon 100% Verification**:
  - Once 100% of files are verified in the destination with zero errors, proceed to eliminate the original files by sending them to the **OS Recycle Bin / Trash** (or deleting verified originals).
  - This frees up duplicate storage space immediately while preserving a safety recovery window in the OS Recycle Bin and the rollback manifest `.xyz-folder/manifest.json`.
  - If any single file fails transfer or verification, the purge is immediately aborted and the original files remain completely intact.

### Step 5: Adaptive Tree Completion Report
Present the final result with an adaptive visual tree matching the user actual files and language.

### Step 6: Rollback / Undo on Demand
If the user requests to revert ("deshazlo", "undo", "vuelve atrás", "cancela el progreso"):
- **Full Rollback**: `python3 scripts/organize.py --target "/path/to/folder" --undo`
- **Selective Restoration**: `python3 scripts/organize.py --target "/path/to/folder" --restore-filter ".pdf"`

---

## 4. Reference CLI Usage

```bash
# Preview proposed moves without touching files:
python3 scripts/organize.py --target "/path/to/folder" --dry-run

# Organize with explicit language selection:
python3 scripts/organize.py --target "/path/to/folder" --lang es

# Full undo / rollback:
python3 scripts/organize.py --target "/path/to/folder" --undo

# Selective restore:
python3 scripts/organize.py --target "/path/to/folder" --restore-filter "2026"
```

---

## 5. Illustrative Taxonomy Reference

| English (`--lang en`) | Spanish (`--lang es`) | Example Extensions |
| :--- | :--- | :--- |
| `[📦] [Installers]/[💻] [Desktop Apps]` | `[📦] [Instaladores]/[💻] [Programas]` | `.exe`, `.msi`, `.appx`, `.pkg`, `.dmg`, `.deb` |
| `[📦] [Installers]/[📱] [Mobile & Packages]`| `[📦] [Instaladores]/[📱] [Android & APK]` | `.apk`, `.xapk`, `.ipa`, `.jar` |
| `[📄] [Documents]/[📑] [PDFs & Books]` | `[📄] [Documentos]/[📑] [PDFs & Libros]` | `.pdf`, `.epub`, `.mobi`, `.azw3`, `.cbr`, `.cbz` |
| `[📄] [Documents]/[📊] [Office & Sheets]`| `[📄] [Documentos]/[📊] [Ofimática]` | `.docx`, `.doc`, `.xlsx`, `.xls`, `.csv`, `.pptx`|
| `[📄] [Documents]/[📝] [Notes & Text]` | `[📄] [Documentos]/[📝] [Notas & Textos]` | `.txt`, `.md`, `.log`, `.rtf` |
| `[🎨] [Media]/[🖼️] [Images]` | `[🎨] [Multimedia]/[🖼️] [Imágenes]` | `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`, `.gif` |
| `[🎨] [Media]/[🎬] [Videos]` | `[🎨] [Multimedia]/[🎬] [Vídeos]` | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.srt` |
| `[🎨] [Media]/[🎵] [Audio]` | `[🎨] [Multimedia]/[🎵] [Audio]` | `.mp3`, `.flac`, `.wav`, `.m4a`, `.aac`, `.ogg` |
| `[🗜️] [Archives]/[📦] [ZIP & RAR]` | `[🗜️] [Comprimidos]/[📦] [ZIP & RAR]` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.xz` |
| `[🗜️] [Archives]/[💿] [Disk Images & ISOs]`| `[🗜️] [Comprimidos]/[💿] [Imágenes ISO]` | `.iso`, `.img`, `.vhd`, `.torrent` |
| `[💻] [Development & AI]/[🤖] [Models]` | `[💻] [Desarrollo & AI]/[🤖] [Modelos & Pesos]` | `.gguf`, `.safetensors`, `.onnx`, `.pt` |
| `[💻] [Development & AI]/[🐙] [Repos & Code]`| `[💻] [Desarrollo & AI]/[🐙] [Código & Repos]` | `.py`, `.js`, `.ts`, `.rs`, `.go`, `.html` |
| `[💻] [Development & AI]/[🛠️] [Scripts]` | `[💻] [Desarrollo & AI]/[🛠️] [Scripts & Config]`| `.sh`, `.bash`, `.ps1`, `.bat`, `.json`, `.yaml` |
