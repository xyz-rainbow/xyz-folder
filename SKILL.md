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

2. **Zero Data Loss Guarantee**:
   - Files are moved atomically and verified byte-for-byte.
   - **Collision prevention**: If a file with the same name already exists at the destination, it is safely versioned as `filename (1).ext` — never overwritten.
   - **No deletions without explicit consent**: Old folders are only removed if 100% empty after move verification.

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

6. **Reference Script Notice**:
   - The bundled `scripts/organize.py` is a **baseline reference engine**.
   - Agents are instructed to tailor, extend, or generate custom migration and organization scripts dynamically to best fit the user's specific files, operating system, and storage topology.

---

## 2. Agent Execution Protocol (Step-by-Step)

When an AI assistant executes this skill:

### Step 1: Dynamic Discovery & Language Detection
- Never assume hardcoded paths. Detect the user's primary folder dynamically:
  - Windows: Query Registry `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders` or `$env:USERPROFILE\Downloads`.
  - Linux: Query `xdg-user-dir DOWNLOAD` or default to `~/Downloads`.
  - macOS: Default to `~/Downloads`.
  - Custom drives or projects: Resolve absolute path and verify existence.
- Detect the user's conversational language (e.g., Spanish or English) to align category naming.

### Step 2: Pre-Flight Scan & Alignment Interview
- Inspect loose files and scan extensions.
- Present a dry-run preview with file counts and byte sizes.
- **Ask clarifying questions**:
  - *"He detectado archivos multimedia, instaladores y documentos. ¿Prefieres agrupar los instaladores móviles (.apk) juntos o separados de los de PC?"*
  - *"¿Hay carpetas o proyectos específicos que prefieras excluir de la reorganización?"*
- Wait for user confirmation / green light before executing.

### Step 3: Safety Checkpoints & Backup Verification
- For small local sorts: proceed with atomic moves and manifest journaling.
- For large multi-gigabyte or cross-volume migrations (robocopy, rsync, external HDDs):
  - Check destination volume capacity and verify disk health.
  - Create a safety backup/checkpoint if modifying critical directories.
  - Guard disk I/O (avoid concurrent reads/writes on single spinning HDDs).

### Step 4: Atomic Execution & Journaling
- Write moves into `.xyz-folder-manifest.json` in the target directory:
  ```json
  {
    "timestamp": 1789123456.0,
    "target": "/path/to/folder",
    "moves": [
      {
        "src": "/path/to/folder/invoice.pdf",
        "dst": "/path/to/folder/[📄] [Documentos]/[📑] [PDFs]/invoice.pdf",
        "size": 1048576
      }
    ]
  }
  ```
- Move files atomically. Suffix collisions with `(1)`, `(2)`.

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
