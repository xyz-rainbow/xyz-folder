---
name: xyz-folder
description: >
  Autonomous protocol and universal template framework for AI agents to dynamically organize, categorize,
  and normalize folders and drives into an aesthetic double-bracket and emoji taxonomy ([emoji] [Category]/[emoji] [Subcategory]/).
  Features modular domain presets, language auto-adaptation, zero-data-loss verification, transaction journaling,
  full rollback/undo, granular tree inspection, and strict preservation of Git repositories, Windows services, and game saves.
  Use when the user asks to "organize downloads", "clean my folders", "sort files", "organize drive",
  "ordenar descargas", "clasificar archivos con emojis", "deshacer ordenamiento", or runs /xyz-folder.
---

# xyz-folder — Universal Aesthetic Directory & Drive Organizer

An open, non-deterministic cognitive protocol and template framework for AI agents to clean, organize, and classify chaotic directories (Downloads, Desktop, external storage drives, code workspaces, media hubs) into an ultra-clean **double-bracket and emoji taxonomy**:

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

## 1. Core Philosophy: An Adaptive Template, Not a Rigid Dogma

> [!IMPORTANT]
> **Non-Deterministic Heuristic**:
> `xyz-folder` is **NOT a rigid, hardcoded schema**. The categories, emojis, and presets provided in this skill are **modular archetypes and blueprints**. 
> The AI agent **MUST NOT** blindly force a fixed set of folder names. Instead:
> 1. Analyze the user's specific directory contents and file signatures.
> 2. Detect the user's primary language (or requested language) and translate/localize all category names.
> 3. Respect user-specific rules, personal taxonomies, and naming conventions (e.g. numeric ordering `[01] [📂]`, kebab-case, custom emojis).
> 4. Synthesize a bespoke taxonomy proposal derived from the presets, present it for debate, and wait for explicit confirmation.

---

## 2. Universal Principles & Safety Guardrails

1. **Interactive Alignment & Debate First**:
   - The agent **MUST NEVER** blindly move files without confirmation.
   - Scan target directory, analyze signatures, detect user language, and propose a tailored plan.
   - Debate edge cases, exclusions, and custom preferences with the user before touching disk.

2. **One-by-One with Full Tree Protocol ("Uno a Uno con Tree Exhaustivo")**:
   - When organizing complex drives or category trees, **never perform blind mass-renaming**.
   - Proceed strictly **folder by folder ("uno a uno")**.
   - Execute a granular `tree` inspection displaying nested subfolders and files before proposing changes.
   - Always present a clear **"BEFORE vs AFTER" ("CÓMO ERA vs CÓMO QUEDARÍA")** visual comparison.
   - Require explicit user authorization (green light) before touching disk on that specific folder.

3. **Strict Recursive Subfolder Taxonomy (`[emoji] [Category]/[emoji] [Subcategory]/`)**:
   - Internal subfolders follow the double-bracket and emoji taxonomy: `[emoji] [Category]/[emoji] [Subcategory]/[emoji] [Folder]/...`
   - Avoid leaving orphan flat/raw folders behind when normalizing a directory tree.

4. **Copy-First & Post-Verification Source Purge**:
   - **Always copy first on cross-drive migrations**: Original files remain 100% intact as a live safety backup during transfer.
   - **Verification before cleanup**: Verify 100% byte integrity (and checksums for critical files) against the source.
   - **Source Purge upon 100% Verification**: Only after 100% verified with zero errors, eliminate originals (sending to OS Recycle Bin/Trash when possible) to release disk space.
   - **Strict Abort on Error**: If even a single file fails verification, the source is left completely untouched.
   - **Collision prevention**: If a file with the same name exists at destination, version as `filename (1).ext` — never overwrite.

5. **Git Repository Invariance ("Invariabilidad Absoluta de Repositorios Git")**:
   - When organizing code drives or project trees (`[💻] [Projects]`), the agent must **NEVER modify or rename repository root directories** (e.g. `xyz-folder` remains `xyz-folder`, never `[📦] [xyz-folder]`).
   - Never mutate `.git/` directories, branches, commits, or git configurations.
   - Category styling (`[emoji] [Category]`) is strictly applied to **parent container directories** (e.g. `[🚀] [Main-Apps]/xyz-folder`).
   - Run `git status` on representative repositories after container movement to verify zero working tree corruption.

6. **IDE Workspace & Project Link Synchronization**:
   - Moving code containers breaks relative paths in IDE workspace files (e.g. `*.code-workspace`, `.vscode/`, `.idea/`).
   - The agent must proactively locate and update relative path references in workspace files to keep IDE projects working seamlessly.

7. **Windows Services & Deep Registry Executable Locks**:
   - Audit `HKLM\SYSTEM\CurrentControlSet\Services` for active services bound to binaries on secondary drives (e.g. `SbieSvc.exe` in `[Tools]`).
   - If a directory contains an active Windows Service binary, maintain a functional copy or transparent NTFS junction to avoid `WinError 32 (File in Use)` and service crashes.

8. **Protected Ecosystem Paths & Game Engines**:
   - Video game saves (`Documents/My Games`, `Diablo IV`, `PCSX2`, `Square Enix`, `Need for Speed Heat`), system shells (`PowerShell`, `WindowsPowerShell`), and hardware configurations must remain 100% untouched.
   - **User Shell Folders Audit**: Audit `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders` before organizing user directories to detect OS-bound paths (`Screenshots` GUID `{B7BEDE81...}`, `Camera Roll`, `My Pictures`).
   - **Game Engine Hardcoded Paths**: Game engines like Cyberpunk 2077 (REDengine) hardcode screenshot paths (`Pictures\Cyberpunk 2077`). Never rename these paths.
   - **Transparent NTFS Junctions**: When organizing an OS-bound or application-bound folder into emoji taxonomy (e.g. `Screenshots` $\rightarrow$ `[📸] [Screenshots]`), create an NTFS Directory Junction (`mklink /J` / `_winapi.CreateJunction`) at original path so OS shortcuts (`Win + PrtScn`) continue writing seamlessly.

9. **Storage Topology Awareness (Atomic Same-Drive vs Staged Cross-Drive)**:
   - **Same-Drive Moves**: On the same filesystem (NTFS/exFAT), moving directories is an instantaneous atomic pointer update (`[System.IO.Directory]::Move`).
   - **Cross-Drive Migrations (SSD -> HDD)**: Must use Staged Copy-First with strict 100% byte-by-byte integrity verification before purging source.
   - **Anti-Thrashing on Large/Mechanical Drives**: Deep recursive scans (`os.walk`) over huge folder trees (`node_modules`, build artifacts) on HDDs or exFAT cause severe head thrashing and multi-minute freezes. Enforce shallow (depth=1) inspection for top-level category mapping.

10. **Windows Shell Lock, Attribute Remediation & Safe Deletion**:
    - Windows Explorer frequently marks customized folders or directories with `.ShellClassInfo`/`desktop.ini` as `FILE_ATTRIBUTE_READONLY` (`0x1` / `Mode dar---`), throwing `WinError 5 (Access Denied)`.
    - Clear attributes to `FILE_ATTRIBUTE_NORMAL` (`128`) using `ctypes.windll.kernel32.SetFileAttributesW(path, 128)` before `os.rmdir` or `os.remove`.
    - Explorer thumbnail caches, preview handlers, and zip associations trigger `WinError 32 (File in Use)`; use the `rename-truncate-remove` pattern to cleanly bypass locks.

11. **Transaction Journaling & Full Rollback**:
    - Every operation writes a `.xyz-folder-manifest.json` transaction log.
    - At any time, the user can cancel progress, revert the entire operation back to original locations (`--undo`), or selectively restore individual files or subfolders (`--restore-filter`).

12. **Residual Crash Dumps & Sandbox Purging**:
    - Scan for and safely purge stale application crashpad dumps (`.dmp`), Electron runtime caches, and installer extraction temps in root `tmp/` folders when requested, releasing gigabytes of disk space.

13. **Semantic Media Inspection & Contextual Renaming**:
    - Files frequently carry machine-generated, chaotic names: camera timestamps (`Screenshot 2026-05-20...`), random UUIDs/hashes, AI generator prefixes (`Gemini_Generated_Image_...`), or double-extensions.
    - Inspect media visually or examine metadata/headers. Propose clean, descriptive **kebab-case** names (e.g. `synthwave-audio-visualizer-4k.png`) in the comparison table before execution.

14. **Shell Character & Path Escaping Safeguards**:
    - Folders starting with `$` (like `$Temp`) expand to empty string inside double quotes in pwsh. Always use single quotes or escape as ```$Temp``.
    - Folders with brackets like `[📚] [Documentos]` are parsed as regex wildcards by PowerShell cmdlets. Always use `-LiteralPath`.
    - In Python, raw strings ending with a backslash like `r'path\'` cause a syntax error. Use forward slashes `'path/'` or double backslashes.

---

## 3. Modular Presets & Archetypes Library

These presets serve as **battle-tested templates**. The agent should adapt names, translations, and emojis to match the user's files and language.

### Preset A: Developer & Code Workspaces (`[💻] [Projects]`)

| Archetype Container | English Preset | Spanish Preset | Typical Contents |
| :--- | :--- | :--- | :--- |
| **Main Applications** | `[🚀] [Main-Apps]` | `[🚀] [Apps-Principales]` | Production apps, flagship tools, core repos |
| **Secondary & Labs** | `[🧪] [Secondary-Labs]` | `[🧪] [Laboratorios-Secundarios]`| Experimental tools, prototypes, game jam repos |
| **Webs & Extensions** | `[🌐] [Webs-Extensions]` | `[🌐] [Webs-Extensiones]` | Portals, dashboards, browser extensions (`[🧩] [Extensions]`) |
| **AI & Research** | `[🤖] [AI-Research]` | `[🤖] [IA-Investigacion]` | Models, local LLMs, prompt collections, research papers |
| **Hardware & IoT** | `[📟] [Hardware-IoT]` | `[📟] [Hardware-IoT]` | ESP32, microcontrollers, Cardputer, firmware, displays |
| **Animation & Media** | `[🎬] [Animation-Studio]` | `[🎬] [Estudio-Animacion]` | Animation renders, scene clips, 3D/character art |
| **Dev Tools & Scripts**| `[🛠️] [Dev-Tools-Scripts]`| `[🛠️] [Herramientas-Dev]` | Daemons, proxies, ADB scripts, monitoring configs |
| **Backups & Archives** | `[📦] [Backups-Archives]` | `[📦] [Respaldos-Archivos]` | Historical zips, tarballs, older project snapshots |

### Preset B: Master Documents & Knowledge Hub (`[📚] [Documents]`)

| Archetype Container | English Preset | Spanish Preset | Typical Contents |
| :--- | :--- | :--- | :--- |
| **Personal & Identity**| `[👤] [Personal]` | `[👤] [Personal]` | ID templates, healthcare, government, curriculum |
| **Invoices & Finances**| `[🧾] [Invoices]` | `[🧾] [Facturas]` | Receipts, tax documents, accounting spreadsheets |
| **Work & Jobs** | `[💼] [Work]` | `[💼] [Trabajo]` | Client deliverables, employment contracts, meeting notes |
| **Ebooks & Library** | `[📖] [Ebooks]` | `[📖] [Ebooks]` | Calibre library (`metadata.db`), epubs, pdfs, mobi |
| **Hardware & Notes** | `[📟] [Hardware-Docs]` | `[📟] [Cyberdeck]` | Pinouts, datasheets, microcontroller manuals |
| **Exports & Vaults** | `[📦] [Exports]` | `[📦] [Exportaciones]` | SDR databases, browser bookmarks, app settings |
| **Media & Content** | `[📺] [Youtube-Media]` | `[📺] [Youtube]` | Video scripts, content outlines, audio transcripts |
| **AI & Engineering** | `[🤖] [AI-Tools]` | `[🤖] [Herramientas-IA]` | LocalAI configs, MCP server manifests, custom skills |
| **ASCII & Typography** | `[🎨] [Ascii]` | `[🎨] [Ascii]` | ASCII branding, text banners, terminal themes |

### Preset C: Visual & Creative Media Hub (`[🎨] [Media]`)

| Sub-Hub | English Preset | Spanish Preset | Typical Contents |
| :--- | :--- | :--- | :--- |
| **Images** | `[📸] [Screenshots]` | `[📸] [Capturas]` | OS screenshots (NTFS Junction to original path) |
| | `[🖼️] [Wallpapers]` | `[🖼️] [Fondos]` | 4K/10K wallpapers, AI generative art |
| | `[✨] [Brand-Logos]` | `[✨] [Logos-Marca]` | Brand identity, banners, vector suites |
| | `[📱] [App-Icons]` | `[📱] [Iconos-Apps]` | Software icons, UI packs, dock graphics |
| | `[🧊] [3D-Models]` | `[🧊] [Modelos-3D]` | STL, OBJ, 3D printing project files |
| | `[🛒] [Purchases-Gear]`| `[🛒] [Compras-Equipo]` | Hardware receipts, component photos |
| **Videos** | `[🎬] [Captures]` | `[🎬] [Capturas]` | Game Bar clips, desktop screen recordings |
| | `[🧠] [Cognitive-OS]` | `[🧠] [Sistema-Cognitivo]`| Master UI walkthroughs, architectural videos |
| | `[🤖] [AI-Demos]` | `[🤖] [Demos-IA]` | LLM & agent demonstrations |
| | `[💻] [Development]` | `[💻] [Desarrollo]` | Screen recordings of coding sessions |
| | `[✂️] [Editor-Projects]`| `[✂️] [Proyectos-Editor]` | Video editor timelines, clip caches |
| **Music** | `[🎵] [Music]` | `[🎵] [Musica]` | Albums, master FLAC/MP3 collections |
| | `[🎤] [Artists]` | `[🎤] [Artistas]` | Discographies categorized by artist name |
| | `[📻] [Playlists]` | `[📻] [Listas]` | Curated sessions, mix tapes, cover art |
| | `[🔔] [Notifications]` | `[🔔] [Notificaciones]` | System sound effects, UI alert WAV files |

### Preset D: System Tools & Storage Utility Hub (`[🛠️] [Tools]`)

| Archetype Container | English Preset | Spanish Preset | Typical Contents |
| :--- | :--- | :--- | :--- |
| **System Rescue** | `[🔧] [System-Rescue]` | `[🔧] [Rescate-Sistema]` | Disk repair scripts, exFAT watchdog, desktop restorers |
| **USB Imaging** | `[💾] [USB-Flashing]` | `[💾] [Flasheo-USB]` | BalenaEtcher, Rufus, Ventoy ISO burning utilities |
| **Radio & SDR** | `[📻] [SDR-Radio]` | `[📻] [Radio-SDR]` | SDR++, SDRSharp, frequency decoders |
| **Credential Vaults** | `[🔑] [Pass-Exports]` | `[🔑] [Exportaciones-Pass]`| Encrypted password exports, Bitwarden backups |
| **Android Developer** | `[📱] [Android-APK]` | `[📱] [Android-APK]` | APK packages, scrcpy, ADB platform tools |
| **Process Isolation** | `[📦] [Sandboxie]` | `[📦] [Sandboxie]` | Sandboxed browser runners, `SbieSvc.exe` service mirrors |
| **Media Players** | `[🎵] [Music-Players]` | `[🎵] [Reproductores]` | Lightweight audio players (Supersonic, Navidrome clients) |

### Preset E: Server Infrastructure & Homelab (`[🚀] [Homelab]`)

| Archetype Container | English Preset | Spanish Preset | Typical Contents |
| :--- | :--- | :--- | :--- |
| **Kubernetes Cluster** | `[☸️] [K8s-Cluster]` | `[☸️] [Cluster-K8s]` | Pod manifests, debugging pods, `[🧩] [ConfigMaps-Patches]` |
| **Network Storage** | `[💾] [NAS-Storage]` | `[💾] [Almacenamiento-NAS]`| NFS mount scripts, NAS watchdog, SSH diagnostics |
| **Distributed Storage**| `[🐂] [Longhorn-Storage]`| `[🐂] [Storage-Longhorn]`| CSI volumes, CRDs, upgrade disaster plans |
| **Media Automation** | `[🎵] [Music-Pipeline]` | `[🎵] [Pipeline-Musica]` | Beets configs, metadata enrichers, queue workers |
| **Administration** | `[🛠️] [Admin-Scripts]` | `[🛠️] [Scripts-Admin]` | Key decryption, SQL recovery, emergency shell scripts |
| **Cluster Backups** | `[📦] [Backups]` | `[📦] [Backups]` | Snapshot tars, database dumps |
| **Ephemeral Scratch** | `[🧪] [Scratch]` | `[🧪] [Borradores]` | Temporary test manifests, staging YAMLs |

---

## 4. Mandatory Pre-Flight Verification Checklist

Before touching a single file or generating the execution script:
1. **[Disk Space]**: Verify destination capacity with `shutil.disk_usage()`. Ensure available free space exceeds the total batch size by at least 500 MB.
2. **[File & Service Locks]**: Confirm files are not locked by active processes, IDEs, or Windows Services (`HKLM\SYSTEM\CurrentControlSet\Services`).
3. **[Permissions & Attributes]**: Clear `FILE_ATTRIBUTE_READONLY` (`128`) on Windows to prevent `Access Denied`.
4. **[Collision Prevention]**: Ensure destination naming logic appends `(1)`, `(2)` to strictly prevent any overwrite.
5. **[Language Alignment]**: Detect prompt and system language; translate all category names accordingly.
6. **[Transaction Journal]**: Ensure `.xyz-folder/manifest.json` will record every source-destination pair before any file operations.

---

## 5. Agent Execution Protocol (Step-by-Step)

When an AI assistant executes this skill:

### Step 1: Dynamic Discovery & Context Analysis
- Detect the user's primary language from prompts and system locale.
- Scan the directory structure (using shallow scans on large drives).
- Identify file types, domains (e.g. code, documents, media, system utilities), and detect active Git repos.

### Step 2: Bespoke Taxonomy Synthesis & Alignment Debate
- Select and combine relevant archetypes from the presets library.
- Adapt category labels to the user's language and project terminology.
- Present a clear **"CÓMO ERA" vs "CÓMO QUEDARÍA"** visual comparison table.
- **Wait for user feedback and confirmation** before moving any files.

### Step 3: Execution (Same-Drive Pointer Moves vs Cross-Drive Copy-First)
- **Same Drive**: Use atomic directory renames (`[System.IO.Directory]::Move` in PowerShell / `os.rename` in Python).
- **Cross-Drive**: Synthesize `.xyz-folder/organize_session.py`, copy first, verify byte-by-byte, and only purge originals after 100% verification.
- **Git Repos**: Move repo parent directories without touching repo folder names, `.git/`, branches, or commits.
- **IDE Workspaces**: Update relative path links in `*.code-workspace` files.

### Step 4: Verification & Reporting
- Verify Git repository status with `git status`.
- Present the final organized tree report to the user.

### Step 5: Rollback on Demand
If the user requests to undo ("deshazlo", "undo", "vuelve atrás"):
- Revert operations using `.xyz-folder/manifest.json`:
  `python3 scripts/organize.py --target "/path/to/folder" --undo`
