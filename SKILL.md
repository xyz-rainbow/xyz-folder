---
name: xyz-folder
description: >
  Autonomous protocol and CLI engine to dynamically organize, categorize, and normalize folders and drives
  into an aesthetic double-bracket and emoji taxonomy ([emoji] [Category]/[emoji] [Subcategory]/).
  Features zero-data-loss verification, collision prevention, transaction journaling, full rollback/undo,
  interactive pre-flight alignment, and language-adaptive folder structures.
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
   - Always scan the target directory, analyze file signatures, detect the user's language, and propose a tailored plan.
   - Debate edge cases, exclusions, and custom preferences with the user before touching disk.

2. **Copy-First & Staged Backup Architecture (Never In-Place Destructive Move)**:
   - **Always copy first**: The original files remain 100% intact as a live safety backup during the entire organization process. Never cut/move directly without a verified replica.
   - **Verification before cleanup**: The agent writes files to the new categorized structure, verifies 100% byte integrity against the source, and reports proof of successful copy.
   - **No deletions without explicit consent**: Original files are NEVER purged automatically. The agent must explicitly ask the user for approval ("luz verde", "visto bueno") before removing any source files.
   - **Collision prevention**: If a file with the same name exists at destination, it is versioned as `filename (1).ext` — never overwritten.

3. **Transaction Journaling & Full Rollback**:
   - Every operation writes a `.xyz-folder-manifest.json` transaction log.
   - At any time, the user can cancel progress, revert the entire operation back to original locations (`--undo`), or selectively restore individual files or subfolders (`--restore-filter`).

4. **Safety Backups for Heavy Migrations**:
   - Before running massive file copies or cross-drive tools like `robocopy` / `rsync`, verify destination space, assess disk health (preventing HDD head thrashing), and establish safety backups/snapshots.

5. **Dynamic Language & Taxonomy Localization**:
   - Folder names and emojis adapt to the user's natural language:
     - Spanish: `[🎨] [Multimedia]/[🖼️] [Imágenes]`, `[📄] [Documentos]/[📑] [PDFs & Libros]`
     - English: `[🎨] [Media]/[🖼️] [Images]`, `[📄] [Documents]/[📑] [PDFs & Books]`
   - Categories adapt to the actual contents found (e.g., 3D models, audio stems, game mods, research datasets).

6. **Custom Script Synthesis in `.xyz-folder/`**:
   - The bundled `scripts/organize.py` is a **pedagogical baseline reference**, NOT a static rigid executable.
   - For every organization task, the agent **MUST synthesize a dedicated custom script** at `.xyz-folder/organize_session.py` tailored specifically to the files, extensions, exclusions, and language discovered in that session.
   - The script is self-documenting: includes an architectural header summarizing the debate, the exact taxonomy map, pre-flight safety checks, and the OS Recycle Bin integration.

---

## 2. Mandatory Pre-Flight Verification Checklist (Check First of All)

Before touching a single file or generating the execution script:
1. **[Disk Space]**: Verify destination capacity with `shutil.disk_usage()`. Ensure available free space exceeds the total batch size by at least 500 MB.
2. **[File Locks]**: Confirm target files are not in use or held by running processes (e.g. IDEs, media players, torrent clients).
3. **[Permissions & Attributes]**: Verify read/write permissions and handle read-only attributes safely.
4. **[Collision Prevention]**: Ensure destination naming logic appends `(1)`, `(2)` to strictly prevent any overwrite.
5. **[Language Alignment]**: Match all directory labels to the user's natural language (`[🎨] [Multimedia]` vs `[🎨] [Media]`).
6. **[Transaction Journal]**: Ensure `.xyz-folder/manifest.json` will record every source-destination pair before any file operations.

---

## 3. Agent Execution Protocol (Step-by-Step)

When an AI assistant executes this skill:

### Step 1: Dynamic Discovery & File Signature Analysis
- Never assume hardcoded paths. Detect the user's primary folder dynamically via OS standards (Windows User Shell Folders / Linux XDG / macOS).
- Detect the user's language (e.g., Spanish or English) to localize all category names.
- Analyze file signatures and extensions. For unknown, extensionless, or exotic files, inspect **magic bytes** (binary headers) to infer their type.

### Step 2: Interactive 3-Point Debate & Alignment Interview
Before writing code or moving data, debate the plan interactively with the user:
1. **Categories & Emojis**: Present the tailored taxonomy proposal adapted to their specific files.
2. **Nesting Depth**: Confirm whether they prefer subcategories (`[Category]/[Subcategory]/`) or a flatter single-tier structure.
3. **Exclusions & Edge Cases**: Ask if any specific folders, project repos, or extensions should be kept intact.
4. **Unknown Files**: If ambiguous files remain, ask the user whether to isolate them in `[📦] [Sin Clasificar]` or leave them untouched in root.
- **Wait for explicit user confirmation** before proceeding.

### Step 3: Script Synthesis in `.xyz-folder/organize_session.py`
- Generate an auditable, tailored Python script inside `.xyz-folder/organize_session.py` containing:
  - Header documenting the agreed categories and exclusions.
  - Pre-flight disk space and file lock checks.
  - Copy-verify loop and transaction journaling.
  - OS Recycle Bin quarantine functions.

### Step 4: Staged Copy, Verification & User Consent Gate
- **Copy First**: Copy files to the new categorized structure, keeping original files 100% untouched as a live safety backup.
- **Journal Transaction**: Record every copied pair into `.xyz-folder/manifest.json`.
- **Byte Verification**: Verify that destination file sizes match source sizes.
- **Explicit Purge Consent Gate**:
  - Present proof of 100% verified copy to the user.
  - Ask: *"Copia 100% verificada. Los originales siguen intactos como backup. ¿Deseas enviarlos a la Papelera de Reciclaje del sistema para validar el orden durante unos días o conservarlos?"*
  - **Only if the user explicitly approves ("luz verde", "visto bueno", "sí")**, move original files to the **OS Recycle Bin / Trash** (never permanent instant deletion), preserving an easy recovery window.

### Step 5: Adaptive Tree Completion Report
Present the final result with an adaptive visual tree matching the user's actual files and language:

```markdown
### Reorganización de <Directorio_Objetivo> Completada 📂

```text
<Directorio_Objetivo>/
├── [🎨] [<Categoría_A>]/
│   ├── [🎬] [<Subcategoría_1>]/   (<N> elementos)
│   └── [🖼️] [<Subcategoría_2>]/   (<N> elementos)
├── [📄] [<Categoría_B>]/
│   └── [📑] [<Subcategoría_3>]/   (<N> elementos)
└── [🗜️] [<Categoría_C>]/
    └── [📦] [<Subcategoría_4>]/   (<N> elementos)
```
*Total organizado: <N> archivos (<Tamaño_Total> reorganizados). Cero pérdida de datos.*
```

### Step 6: Disk & Background Tasks Telemetry (When Applicable)
If a heavy background migration (robocopy/rsync/background worker) is active:

```markdown
### Estado del Disco y Tareas en Segundo Plano 💾

- **Tarea Activa**: `<Identificador o herramienta (e.g., robocopy / rsync / task-xyz)>`
- **Ruta Origen $\rightarrow$ Destino**: `<Origen>` $\rightarrow$ `<Destino>`
- **Volumen & Progreso**: `<Tamaño transferido>` / `<Tamaño total>` (`<Porcentaje>%`)
- **I/O & Rendimiento**: Ancho de banda protegido (evitando saturación de cabezales en discos mecánicos HDD).
- **Espacio Libre en Disco**: `<Espacio libre restante>` en la unidad destino.
```

### Step 7: Rollback / Undo on Demand
If the user requests to revert ("deshazlo", "undo", "vuelve atrás", "cancela el progreso"):
- **Full Rollback**:
  ```bash
  python3 scripts/organize.py --target "/path/to/folder" --undo
  ```
  Every file is restored to its exact original path, and newly created empty folders are cleanly removed.
- **Selective Restoration**:
  ```bash
  python3 scripts/organize.py --target "/path/to/folder" --restore-filter ".pdf"
  ```
  Restores only specific files or extensions while keeping the rest organized.

---

## 3. Reference CLI Usage

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

## 4. Illustrative Taxonomy Reference

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
