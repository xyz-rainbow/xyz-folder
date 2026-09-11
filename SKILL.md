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

## 4. Agent Execution Protocol (Universal & Multi-User)

When an AI assistant or agent executes this skill for any user on any platform:

1. **Dynamic Target Discovery (Zero Hardcoded Paths)**:
   - Always discover the user's primary folders dynamically.
   - On Windows: Query Registry `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders` or `$env:USERPROFILE\Downloads`.
   - On Linux: Query `xdg-user-dir DOWNLOAD` or default to `~/Downloads`.
   - On macOS: Default to `~/Downloads`.
   - If an external drive or specific project path is provided, resolve the absolute path and verify existence.

2. **Pre-Flight Dry-Run & Safety Check**:
   - Always inspect files and present the proposed breakdown before moving files if ambiguity exists.
   - **Zero Data Loss Guarantee**: Never overwrite. If a collision occurs at destination, suffix with `(1)`, `(2)`, etc.
   - **No Unconfirmed Deletions**: Never delete unorganized folders or files without explicit confirmation.

3. **Atomic Move & Verification**:
   - Move files atomically.
   - Programmatically verify that source file sizes match destination sizes.
   - Only remove legacy source directories if they are 100% empty.

---

## 5. Standard Reporting & Telemetry Protocol

To maintain universal clarity and executive feedback across agents (Antigravity, Claude Code, Cursor, OpenCode), the agent **MUST** structure its completion messages with the following dedicated report blocks:

### Block A: Completion Tree Report
Emit a visual tree matching the language of the user (e.g., Spanish or English):

```markdown
### Reorganización de <Directorio_Objetivo> Completada 📂

\`\`\`text
<Directorio_Objetivo>/
├── [🎨] [Media]/
│   ├── [🎬] [Videos]/         (<X> elementos)
│   ├── [🎵] [Audio]/          (<X> elementos)
│   └── [🖼️] [Imágenes]/       (<X> elementos)
├── [💻] [Desarrollo & AI]/
│   ├── [🌐] [Web & HTML]/      (<X> elementos)
│   ├── [📝] [Prompts & Specs]/ (<X> elementos)
│   └── [🧩] [Extensiones]/    (<X> elementos)
├── [📄] [Documentos]/
│   ├── [✈️] [Telegram]/       (<X> elementos)
│   ├── [📊] [Ofimática]/      (<X> elementos)
│   └── [📑] [PDFs & Libros]/   (<X> elementos)
├── [📦] [Instaladores]/
│   ├── [🎮] [Mods & Plugins]/ (<X> elementos)
│   └── [📱] [Android & APK]/  (<X> elementos)
└── [🗜️] [Comprimidos]/
    ├── [💾] [Backups]/        (<X> elementos)
    ├── [📁] [Extraídos]/      (<X> elementos)
    └── [📦] [ZIP & RAR]/      (<X> elementos)
\`\`\`
*Total organizado: <N> archivos (<Tamaño_Total> reorganizados). Cero pérdida de datos.*
```

### Block B: Disk & Background Tasks Telemetry
Whenever performing large batch copies, multi-gigabyte moves, or asynchronous operations across drives/partitions, the agent **MUST** include real-time disk status:

```markdown
### Estado del Disco y Tareas en Segundo Plano 💾

- **Tarea Activa**: `<Identificador o herramienta (e.g., robocopy / rsync)>`
- **Ruta Origen $\rightarrow$ Destino**: `<Origen>` $\rightarrow$ `<Destino>`
- **Volumen & Progreso**: `<Tamaño transferido>` / `<Tamaño total>` (`<Porcentaje>%`)
- **I/O & Rendimiento**: Ancho de banda protegido (evitando saturación de cabezales en discos mecánicos).
- **Espacio Libre en Disco**: `<Espacio libre restante>` en la unidad destino.
```

### Block C: Executive Telemetry Footer
End the turn with a concise, parseable notification block:

```text
=== NOTIFY [STORAGE: <STATUS>] ===
- TARGET          : <Ruta organizada>
- ITEMS_ORGANIZED : <N> movidos | 0 fallos
- FREE_SPACE      : <X> GB restantes en unidad
- IMPACT          : Directorio normalizado bajo arquitectura [emoji] [Categoría]
===================================
```

