---
name: xyz-folder
description: >
  Autonomous protocol and universal template framework for AI agents to dynamically organize, categorize,
  and normalize folders and drives into an aesthetic taxonomy with single-word root categories, module nesting
  (Ascii/Youtube into Apuntes; Ebooks/Backups/Hardware into Otros), gravity-based numeric ordering ([00]-[Nombre] [Emoji]),
  syntax format catalogs, dynamic self-adaptation, and anti-repetition icon rules.
  Features zero-data-loss verification, transaction journaling, full rollback/undo, and strict preservation of Git repos and game saves.
  Use when the user asks to "organize downloads", "clean my folders", "sort files", "organize drive",
  "ordenar descargas", "clasificar archivos con emojis", "deshacer ordenamiento", or runs /xyz-folder.
---

# xyz-folder — Universal Aesthetic Directory & Drive Organizer

An open, non-deterministic cognitive protocol and template framework for AI agents to clean, organize, and classify chaotic directories (Downloads, Desktop, external storage drives, code workspaces, media hubs) into an ultra-clean **customizable taxonomy with gravity-based ordering and visual iconography**:

```text
Target Directory/
├── [01]-[Identidad] [🪪]/
│   ├── [01]-[Titular] [👤]/
│   └── [02]-[Familia] [👩]/
├── [02]-[Pension] [🏛️]/
│   ├── [01]-[Orfandad] [📜]/
│   └── [02]-[Formularios] [📋]/
├── [03]-[Discapacidad] [📑]/
├── [04]-[Salud] [🏥]/
├── [05]-[Cognitivo] [🧠]/
├── [06]-[Estudios] [🎓]/
├── [07]-[Curriculum] [📄]/
├── [08]-[Trabajo] [💼]/
├── [09]-[Facturas] [🧾]/
├── [10]-[Legal] [👮]/
├── [11]-[AI] [🤖]/
├── [12]-[Apuntes] [📝]/
│   ├── [01]-[Ascii] [🎨]/
│   └── [02]-[Youtube] [📺]/
└── [13]-[Otros] [📂]/
    ├── [01]-[Ebooks] [📖]/
    ├── [02]-[Backups] [📦]/
    └── [03]-[Hardware] [📟]/
```

Works out of the box on **Windows, Linux, and macOS**. Zero external dependencies (Python 3 standard library only).

---

## 1. Core Philosophy: Dynamic Self-Adaptation & Evolutionary Memory

> [!IMPORTANT]
> **Dynamic Self-Adaptation Principle ("Principio de Auto-Adaptación Continua")**:
> `xyz-folder` is **NOT a frozen script or rigid schema**. It is a **living cognitive framework**.
> The AI agent **MUST continuously adapt and enrich this skill** whenever the user introduces:
> 1. A new naming requirement, syntax style, or numeric convention.
> 2. Specific domain rules, nesting patterns, or priority hierarchies.
> 3. Additional emojis, ASCII symbols, or localization languages.
> The agent **must proactively persist new requirements into the skill documentation and scripts**, ensuring evolutionary memory across sessions.
>
> **Adaptive Heuristics**:
> 1. Analyze the target directory contents, volume, and file signatures.
> 2. Detect the user's language and translate all category labels naturally.
> 3. **Prompt the user to select their preferred Naming Syntax Format** before moving any files.
> 4. If the user names principal categories, those names **are the root containers**. Presets fill **subfolders** under them.
> 5. **Single-Word Root Categories**: Root containers strictly prefer a single, concise word (`[Estudios]`, `[Salud]`, `[Pension]`, `[Identidad]`, `[Trabajo]`). Avoid compound or hyphenated root names.
> 6. **Module Nesting Architecture**: Group specific creative notes (`Ascii`, `Youtube`) under `[Apuntes]` / `[Notes]`, and secondary or auxiliary stores (`Ebooks`, `Backups`, `Hardware`) under `[Otros]` / `[Other]` rather than spawning fragmented root containers.
> 7. **Anti-Repetition Rule**: Never repeat the exact same emoji or ASCII icon within the same folder level.
> 8. **Semantic Equivalence Rule ("Random" = "Otros")**: `Random` and `Otros` are conceptually identical. Always maintain and prefer `[Otros]`. Never maintain a separate `Random` root; route and distribute all unsorted or random files into their proper domains, and auxiliary miscellany into `[Otros]`.
> 9. **Terminal Gravity Rule ("[Otros] is ALWAYS the Last Number")**: `[Otros]` acts as the ultimate residual storage sink. By strict rule, **`[Otros]` MUST ALWAYS occupy the highest / final index of the numeric hierarchy** (e.g. `[14]-[Otros] [📂]` or `[99]-[Otros] [📂]`). Specific domain categories (like `Multimedia`) must precede it.
> 10. **Mandatory Visual Comparison Table ("Tabla Visual CÓMO ERA vs CÓMO QUEDARÍA")**: Before executing any disk modifications, file moves, or renames, the agent **MUST ALWAYS render an interactive Markdown comparison table** detailing `Ubicación Actual (CÓMO ERA)`, `Destino Canónico (CÓMO QUEDARÍA)`, and `Justificación y Función`. Execution requires explicit user confirmation via `ask_question`.
> 11. **Exhaustive File-by-File Content Inspection ("Protocolo de Auditoría Anatómica 1 a 1")**: Never assume or classify a file solely by its filename or extension. The agent MUST open and parse the internal data streams (PyMuPDF/`fitz` for PDFs, `zipfile` + `xml.etree.ElementTree` for DOCX/ODT, native text reader for markdown/yaml/json/txt) to extract actual headers, titles, and paragraphs.
> 12. **Strict Cryptographic Deduplication & Recycle Bin Safety ("Regla de Purgado Criptográfico en Papelera")**: A file is ONLY classified as a duplicate if BOTH its exact byte length and full cryptographic hash (SHA-256) match 100% with the canonical original (`sz_orig == sz_dupl and h_orig == h_dupl`). Permanent destructive deletions are strictly prohibited for duplicates; all purged duplicates or corrupt files MUST be moved to the OS Recycle Bin (`[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(..., 'SendToRecycleBin')` on Windows) to guarantee complete reversibility.
> 13. **Corrupt & Zero-Byte Artifact Elimination**: Detect and purge unrecoverable 0-byte files resulting from interrupted network downloads or crash dumps (e.g. `tmp*.mp4`), verifying size = 0 and empty SHA-256 hash `e3b0c442...` before recycling.
> 14. **Canonical Chronological Standardization ("Estandarización Mensual Canónica")**: In periodic or monthly series (e.g., invoices, monthly reports), enforce uniform canonical naming `[00]-[Mes] [Emoji]` (e.g. `[02]-[Febrero] [❄️]`, `[06]-[Junio] [☀️]`, `[11]-[Originales] [📄]`). Prohibit hybrid schemes (`06-2026` mixed with `[02]-[Febrero]`). If parallel split folders exist for the same period (e.g. PDFs in one folder and HTMLs in another), merge them into a single canonical month folder.
> 15. **Subdirectory Key Promotion Rule ("Regla de Promoción de Subdirectorios Clave")**: When high-value functional domains (such as `Chats` or `Credenciales`) are buried inside general parent folders (like `Notas`), promote them to canonical top-level subdirectories under their parent domain (`[03]-[Chats] [💬]`, `[04]-[Credenciales] [🔐]`).
> 16. **Semantic Special Asset Routing ("Rutas Semánticas de Activos Especiales")**:
>     - *Bóvedas y Credenciales*: Passwords, PGP keys, 2FA codes, proxy lists (`HTTPS/SOCKS5`) $\rightarrow$ `[Personal]\[Credenciales] [🔐]`.
>     - *Guiones y Producción Audiovisual*: Video scripts, research notes for videos $\rightarrow$ `[Apuntes]\[Youtube] [📺]`.
>     - *Lírica y Música*: Song lyrics (`Letras_De_Canciones.docx`) $\rightarrow$ `[Multimedia]\[Musica] [🎵]` along with the master audio tracks.
>     - *Administración de Sistemas*: OS command references, Linux setup manuals $\rightarrow$ `[Apuntes]\[Tecnicos] [💻]` (never in AI prompts or Gems).
>     - *Contenedores Intencionales*: Empty folders with confirmed future intent (e.g. `[04]-[Borradores] [🧪]`) are preserved.
> 17. **Multi-Phase & Sub-Phase Architecture with Visual Mermaid Flowcharts ("Arquitectura de Fases y Sub-Fases con Diagramas de Flujo Mermaid")**:
>     - Complex mass migrations and database integrations must be partitioned into major Phases (`Fase 1`, `Fase 2`...) and granular, confirmable Sub-Phases (`Sub-Fase 1.1`, `Sub-Fase 1.2`...).
>     - The agent **MUST ALWAYS render an interactive Mermaid flowchart (`flowchart LR` or `flowchart TD`)** mapping the raw source files/folders to the canonical destination hierarchy, illustrating data flows, deduplication volumes, and routing targets before execution.
> 18. **Quality-First Cryptographic Deduplication ("Criterio de Calidad ante Duplicados Criptográficos")**:
>     - When duplicate candidates are detected:
>       - Verify **BOTH exact byte length and cryptographic hash (`hashlib.sha256()`)**.
>       - **If 100% identical**: Preserve the existing canonical version that features the standardized, cleanest naming convention; completely omit the duplicate candidate from being copied or moved, avoiding clutter or artificial `(1)` collisions.
>       - **If differing in size or hash**: Inspect internal data, metadata completeness (e.g. richer Calibre `.opf` tags), higher image resolution, or date modified to select and preserve the superior, most complete version.
> 19. **Multi-Root Intelligent Routing for Drive Architectures ("Enrutamiento Multi-Raíz Inteligente")**:
>     - When managing structured drives (e.g., `A:\`), avoid polluting the primary document container (`[📚] [Documentos]`) with massive executables, raw emulators, ROMs, or multi-gigabyte monolithic archives.
>     - Route specialized payloads directly to dedicated root-level drive categories:
>       - `A:\[🎵] [Music]`: Original artist productions, studio albums, stems, and multitracks (`[⚡] [XYZ-Productions]\`).
>       - `A:\[🎮] [Games]`: Console emulators, system firmwares (`.PUP`, Switch `.keys`), GPU drivers.
>       - `A:\[📱] [Android-APK]`: Standalone Android APK packages and mobile tools.
>       - `A:\[🛠️] [Tools]`: Portable USB utilities, hardware flashing, diagnostics suites.
>       - `A:\[📦] [Backups]`: Monolithic server archives (e.g., `external-drive.zip`).


---

## 2. Naming Syntax Formats Catalog (Catálogo de Nomenclaturas)

Before performing any directory organization or file movement, the agent **MUST present this catalog to the user and request which naming format to apply**:

| Format ID | Syntax Pattern | Example Root Directory | Best Suited For |
| :--- | :--- | :--- | :--- |
| **Format A** *(Classic Double-Bracket)* | `[emoji] [Nombre]` | `[🪪] [Identidad]` | Visual aesthetic layout, high contrast, clean icon-first reading. |
| **Format B** *(Pure Numeric Gravity)* | `[00]-[Nombre]` | `[01]-[Identidad]` | Strict deterministic file-manager sorting, minimal, no emojis. |
| **Format C** *(Gravity + Trailing Emoji)* | `[00]-[Nombre] [Emoji]` | `[01]-[Personal] [👤]` | **(Recommended)** Combines OS file sorting with visual clarity. |
| **Format D** *(Emoji-First + Numeric)* | `[Emoji]-[Nombre] [00]` | `[🪪]-[Identidad] [01]` | Visual categorization with trailing index tags. |
| **Format E** *(Retro ASCII Icon)* | `[00]-[Nombre] [ASCII]` | `[01]-[Personal] [*]` | Terminal-focused environments, legacy shells, ASCII aesthetics. |

---

## 3. Gravity & Priority System (`[00]` Numeric Sorting Hierarchy)

When using numeric formatting (`[00]-[Nombre] ...`), indices are assigned according to **critical gravity, survival priority, and functional dependence** rather than arbitrary alphabetical order:

| Numeric Band | Priority Tier | Domain Scope | Representative Categories |
| :--- | :--- | :--- | :--- |
| **`[00]` - `[09]`** | **Tier 1: Vital Core & Legal Identity** | Non-transferable legal existence, survival benefits, official state resolutions. | `[01]-[Identidad] [🪪]`, `[02]-[Pension] [🏛️]`, `[03]-[Discapacidad] [📑]` |
| **`[10]` - `[19]`** | **Tier 2: Health, Biology & Mind** | Medical diagnostics, psychiatric records, cognitive architectures, therapy. | `[04]-[Salud] [🏥]`, `[05]-[Cognitivo] [🧠]` |
| **`[20]` - `[29]`** | **Tier 3: Education, Career & Finance** | Academic institutes, professional certifications, employment contracts, bills. | `[06]-[Estudios] [🎓]`, `[07]-[Curriculum] [📄]`, `[08]-[Trabajo] [💼]`, `[09]-[Facturas] [🧾]` |
| **`[30]` - `[39]`** | **Tier 4: Legal Defense & Enforcement** | Police reports, incident evidence logs, court complaints, vehicle registries. | `[10]-[Legal] [👮]` |
| **`[40]` - `[49]`** | **Tier 5: Cognition, AI & Knowledge** | Local AI models, agent skills, prompts, study notes, video scripts, ASCII art. | `[11]-[AI] [🤖]`, `[12]-[Apuntes] [📝]` *(anida Ascii y Youtube)* |
| **`[50]` - `[99]`** | **Tier 6: Storage, Media & Terminal Vault** | Media suites, Calibre ebook libraries, historical backups, hardware specs, terminal residual sink. | `[13]-[Multimedia] [🎬]` *(anida Fotos, Musica, Videos, Graficos)*, `[14]-[Otros] [📂]` *(anida Ebooks, Backups y Hardware; **SIEMPRE el último número**)* |

---

## 4. Giant Catalog of Emojis and ASCII Icons (Catálogo Universal)

> [!CAUTION]
> **Anti-Repetition Rule ("Regla de Unicidad Visual en el Mismo Directorio")**:
> **NEVER repeat the same emoji or ASCII icon across sibling folders in the same directory level.**
> If `[01]-[Identidad]` uses `[🪪]`, no sibling folder under the same parent may use `[🪪]`. Subfolders must choose a distinct semantic icon (e.g. `[👤]`, `[👩]`, `[👨]`).

### 4.1 Emojis Master Table

| Icon | Unicode Name | Category / Context | Recommended Folder Names | When to Avoid |
| :---: | :--- | :--- | :--- | :--- |
| `🪪` | Identification Card | Official identity, national IDs, passports, driver licenses | `[Identidad]`, `[DNI]`, `[ID-Vault]` | General notes, receipts |
| `👤` | Bust in Silhouette | Personal documents, primary user, single identity | `[Personal]`, `[Titular]`, `[Perfil]` | Companies, teams |
| `👩` | Woman | Family member, maternal records, female profile | `[Familiar]`, `[Madre]`, `[Titular]` | Generic tech folders |
| `🏛️` | Classical Building | Government bodies, Social Security, INSS, public pensions | `[Pension]`, `[INSS]`, `[Administracion]` | Private businesses |
| `📑` | Bookmark Tabs | Official resolutions, disability degrees, administrative files | `[Discapacidad]`, `[Resoluciones]` | Music or media |
| `🏥` | Hospital | Medical records, clinical summaries, hospital discharges | `[Salud]`, `[Hospital]`, `[Clinica]` | General sports |
| `🩺` | Stethoscope | Medical diagnostics, physical exams, imaging, tests | `[Diagnosticos]`, `[Resonancia]`, `[Pruebas]` | Office paperwork |
| `💊` | Pill | Medication, psychiatry, pharmacology, prescriptions | `[Psiquiatria]`, `[Farmacia]`, `[Tratamientos]` | Hardware, software |
| `🧠` | Brain | Neurodivergence, psychology, cognitive OS, AutismOS | `[Cognitivo]`, `[Psicologia]`, `[Neurologia]` | Routine finances |
| `🧩` | Puzzle Piece | Cognitive frameworks, modules, extensions, integrations | `[Marco]`, `[Consciencia]`, `[Extensiones]` | Random unsorted files |
| `🎓` | Graduation Cap | Academic institutions, universities, institutes, courses | `[Estudios]`, `[IOC]`, `[Universidad]` | Work contracts |
| `📄` | Page Facing Up | Curriculum vitae, official forms, loose documents | `[Curriculum]`, `[CV]`, `[Documentos]` | Media audio/video |
| `💼` | Briefcase | Active employment, clients, enterprise projects, labor | `[Trabajo]`, `[Empleo]`, `[Proyectos]` | Academic homework |
| `🧾` | Receipt | Invoices, receipts, tax returns, accounting spreadsheets | `[Facturas]`, `[Recibos]`, `[Contabilidad]` | Identity cards |
| `👮` | Police Officer | Police complaints, formal denunciations, court/notary | `[Legal]`, `[Policia]`, `[Mossos]` | Normal civil notes |
| `🚨` | Rotating Light | Urgent reports, incident logs, emergency evidence | `[Denuncia]`, `[Urgente]`, `[Incidentes]` | Routine backups |
| `🚗` | Automobile | Vehicle records, DGT registration, driver licenses | `[DGT]`, `[Vehiculos]`, `[Trafico]` | Non-vehicle taxes |
| `🤖` | Robot Face | AI assistants, MCP servers, LLM prompts, agent skills | `[AI]`, `[Modelos]`, `[Agentes]` | Standard web scripts |
| `💎` | Gem Stone | Master prompts, custom GPTs, Gemini Gems, gold configs | `[Gems]`, `[Prompts-Maestros]` | Generic text files |
| `⚡` | High Voltage | Energy, electricity invoices, high-speed automations | `[Electricidad]`, `[Suministros]`, `[Scripts]` | Physical paper files |
| `📝` | Memo / Pencil | Study notes, general memos, drafts, research summaries | `[Apuntes]`, `[Notas]`, `[Borradores]` | Identity archives |
| `🎨` | Artist Palette | ASCII art, graphic design, branding, vector illustrations | `[Ascii]`, `[Diseno]`, `[Creativo]` | Spreadsheets |
| `📺` | Television | YouTube scripts, video production, video assets | `[Youtube]`, `[Media-Content]` | Audio-only tracks |
| `🎬` | Clapper Board | Video studio, video captures, rendered movies | `[Videos]`, `[Capturas]`, `[Animacion]` | Static images |
| `🖼️` | Framed Picture | High-resolution photography, wallpapers, visual assets | `[Fotos]`, `[Imagenes]`, `[Fondos]` | Code or text logs |
| `🎵` | Musical Note | Master music, discographies, soundtracks | `[Musica]`, `[Audio]`, `[Soundtracks]` | Voice notes/podcasts |
| `🎙️` | Studio Microphone | Voice recordings, podcast master audio, audio notes | `[Audios]`, `[Grabaciones]`, `[Entrevistas]` | Written books |
| `📖` | Open Book | Calibre library, EPUBs, eBooks, literature | `[Ebooks]`, `[Biblioteca]`, `[Lectura]` | Short cheat sheets |
| `📘` | Blue Book | Dedicated book, technical manuals, monographs | `[AutismOS]`, `[Monografias]`, `[Manuales]` | Commercial invoices |
| `📦` | Package / Box | Archives, backups, Google Takeout, compressed vaults | `[Backups]`, `[Exports]`, `[Paquetes]` | Single text notes |
| `🗜️` | Clamp / Compress | ZIP, RAR, 7Z, tarballs, compressed data | `[Comprimidos]`, `[Archivos-ZIP]` | Raw loose photos |
| `📟` | Pager / Device | Microcontrollers, ESP32, Cardputer, hardware datasheets | `[Hardware]`, `[Cyberdeck]`, `[Dispositivos]` | Web applications |
| `📱` | Mobile Phone | Android APKs, mobile apps, mobile firmware | `[Android]`, `[Mobile]`, `[M5-CYD]` | Desktop x86 binaries |
| `💻` | Laptop Computer | General software, coding repos, desktop applications | `[Programas]`, `[Desarrollo]`, `[SMX]` | Physical hardware |
| `💾` | Floppy Disk | Disk images, ROMs, USB flashing tools, firmwares | `[Flasheo]`, `[ISOs]`, `[Imagenes-Disco]` | Cloud bookmarks |
| `💿` | Optical Disc | ISO files, game discs, software distributions | `[ISOs]`, `[CD-ROM]`, `[Instaladores]` | Small scripts |
| `🔑` | Key | Passwords, credential exports, Bitwarden backups, SSH | `[Claves]`, `[Seguridad]`, `[Credenciales]` | Public documents |
| `🌐` | Globe | Websites, web extensions, portals, domains | `[Webs]`, `[Portales]`, `[Internet]` | Local offline files |
| `🛠️` | Hammer and Wrench | System utilities, dev tools, diagnostic scripts | `[Herramientas]`, `[Tools]`, `[Scripts]` | Pure text essays |
| `🔧` | Wrench | System rescue, disk recovery, repair batch scripts | `[Rescate]`, `[Mantenimiento]` | Media players |
| `🔬` | Microscope | Forensic investigation, scientific analysis, lab tests | `[Investigacion]`, `[Ciencia]`, `[Forense]` | Administrative forms |
| `🎮` | Video Game | Game mods, game saves, emulation profiles | `[Mods]`, `[Juegos]`, `[Emulacion]` | Serious tax files |
| `🏢` | Office Building | Community of owners, building administration, real estate | `[Comunidad]`, `[Inmuebles]`, `[Edificio]` | Personal healthcare |
| `🛒` | Shopping Cart | Hardware purchases, gear receipts, purchase warranties | `[Compras]`, `[Equipamiento]`, `[Garantias]` | Doctor summaries |
| `🤝` | Handshake | Social agreements, labor insertion, partnerships | `[SIL]`, `[Convenios]`, `[Asociaciones]` | Unilateral complaints|
| `📂` | File Folder | Master storage, residual archives, miscellaneous vault | `[Otros]`, `[Almacen]`, `[Miscelanea]` | Specific identity IDs|

### 4.2 ASCII Icons Master Table (Retro / Terminal Mode)

| ASCII Tag | Name | Aesthetic Context | Example Usage |
| :---: | :--- | :--- | :--- |
| `[*]` | Asterisk / Star | Core identity, primary focal entity, flagship module | `[01]-[Personal] [*]` |
| `[#]` | Hash / Root | System infrastructure, root admin, base configs | `[00]-[Sistema] [#]` |
| `[!]` | Exclamation | Legal urgency, critical warnings, active police actions | `[10]-[Legal] [!]` |
| `[+]` | Plus / Health | Healthcare, medical reports, pharmacology, additions | `[04]-[Salud] [+]` |
| `[~]` | Tilde / Wave | Audio, music, voice frequencies, fluctuating signals | `[05]-[Audio] [~]` |
| `[$]` | Dollar / Currency | Financial invoices, accounting, taxes, bank records | `[09]-[Facturas] [$]` |
| `[@]` | At-Sign | Communications, email archives, identity profiles | `[01]-[Identidad] [@]` |
| `[>]` | Pointer / Run | Executables, deployment scripts, active pipelines | `[11]-[Scripts] [>]` |
| `[o]` | Ring / Node | General subfolder, standard container, document bundle | `[02]-[Notas] [o]` |
| `[x]` | Cross / Archive | Backups, historical snapshots, obsolete records | `[13]-[Backups] [x]` |
| `[//]` | Double Slash | Coding repositories, dev workspaces, source code | `[08]-[Codigo] [//]` |
| `[::]` | Scope / Namespace | Educational modules, curriculum, academic courses | `[06]-[Estudios] [::]` |
| `[<>]` | Tag / Markup | Web development, templates, HTML/JSON assets | `[08]-[Webs] [<>]` |

---

## 5. Universal Principles & Safety Guardrails

1. **Interactive Alignment & Debate First**:
   - The agent **MUST NEVER** blindly move files without confirmation.
   - Scan target directory, analyze signatures, detect user language, and propose a tailored plan.
   - Debate edge cases, exclusions, and custom preferences with the user before touching disk.

2. **Pre-Flight Syntax Alignment**:
   - Always present the **Naming Syntax Formats Catalog** and obtain the user's explicit choice (e.g. Format C: `[00]-[Nombre] [Emoji]`).

3. **One-by-One with Full Tree Protocol ("Uno a Uno con Tree Exhaustivo")**:
   - Never perform blind mass-renaming.
   - Proceed strictly **folder by folder ("uno a uno")**.
   - Execute a granular `tree` inspection displaying nested subfolders and files before proposing changes.
   - Always present a clear **"BEFORE vs AFTER" ("CÓMO ERA vs CÓMO QUEDARÍA")** visual comparison.
   - Require explicit user authorization (green light) before touching disk on that specific folder.

4. **Single-Word Category Rule ("Regla de Palabra Única en Categorías Principales")**:
   - Principal / root category containers MUST strictly prefer a single, concise word inside the brackets: `[Nombre]` (e.g., `[Estudios]`, `[Salud]`, `[Pension]`, `[Identidad]`, `[Trabajo]`, `[Facturas]`, `[Legal]`, `[Apuntes]`, `[Otros]`).
   - Avoid compound or hyphenated category names at the root level (`[Estudios-IOC]`, `[Informes-Medicos]`).
   - Subcategories also prioritize single words, allowing compound names only when technical precision demands it.

5. **Module Nesting Architecture ("Arquitectura de Anidación de Módulos Específicos")**:
   - **Notes & Content (`[📝] [Apuntes]` / `[Notes]`)**: Anida obligatoriamente `[Ascii]` y `[Youtube]` como subdirectorios.
   - **Storage Vaults (`[📂] [Otros]` / `[Other]`)**: Anida obligatoriamente `[Ebooks]` (Calibre), `[Backups]` y `[Hardware]`.

6. **Granular Multi-Phase Phasing with Step-by-Step Checkpoints**:
   - Complex reorganizations are partitioned into sequential, verified phases (Purge Duplicates $\rightarrow$ De-nest Bridge Folders $\rightarrow$ Provision Skeleton $\rightarrow$ Domain Migrations $\rightarrow$ File Deduplication $\rightarrow$ Zero-Orphan Audit).
   - Each phase is confirmed individually with the user before proceeding.

7. **Copy-First & Post-Verification Source Purge**:
   - Cross-drive moves use Staged Copy-First with byte-by-byte SHA-256 verification before purging source.
   - Same-drive moves are atomic pointer updates (`[System.IO.Directory]::Move` / `os.rename`).
   - Destination collisions append `(1)`, `(2)` — never overwrite.
   - File duplicate deletions strictly require SHA-256 hash proof recorded in the plan.

8. **Git Repository Invariance**:
   - Never modify `.git/`, branches, commits, or repo root names. Style only parent containers.

9. **Open the File — Names Lie**:
   - Classify by inspecting contents, headers, text, or visual images, not deceptive raw filenames (`Untitled document`, camera hashes).

10. **Transaction Journaling & Full Rollback**:
    - Every action records source $\rightarrow$ destination in `.xyz-folder/manifest.json`.
    - Run `python3 scripts/organize.py --target "/path" --undo` for instant full rollback.

11. **Anatomical 1-to-1 Content Inspection**:
    - Never assume contents from names. Open real streams: PyMuPDF (`fitz`) for PDF text layers, `zipfile` + `xml.etree.ElementTree` for DOCX/ODT word documents, native reader for TXT/MD/JSON/YAML.

12. **Strict Cryptographic Deduplication & OS Recycle Bin**:
    - Deduplication strictly requires a 100% match in BOTH byte length and cryptographic hash (`hashlib.sha256()`).
    - Destructive permanent unlinks (`os.remove` / `rm -rf`) are strictly prohibited for duplicate files.
    - All recycled files MUST be routed to the OS Recycle Bin (`[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(..., 'SendToRecycleBin')` on Windows) to allow instantaneous human recovery.

13. **Chronological Series Normalization**:
    - In periodic monthly series (accounting, bills), enforce uniform format: `[00]-[Mes] [Emoji]` (`[02]-[Febrero] [❄️]`, `[06]-[Junio] [☀️]`, `[11]-[Originales] [📄]`).
    - Merge split folders of the same month (e.g. PDFs in one folder, HTMLs in another) into one single canonical month container.

14. **Subdirectory Key Promotion & Special Asset Routing**:
    - High-value domains buried inside generic folders (e.g. `Chats` or `Credenciales` inside `Notas`) MUST be promoted to first-level canonical subdirectories (`[03]-[Chats] [💬]`, `[04]-[Credenciales] [🔐]`).
    - Consolidate credentials in `[Credenciales]`, video scripts in `[Youtube]`, song lyrics in `[Musica]`, and OS system administration manuals in `[Tecnicos]`. Preserve intentionally empty containers (e.g. `[Borradores]`).

---

## 6. Mandatory Pre-Flight Verification Checklist

Before touching a single file or generating the execution script:
1. **[Disk Space]**: Verify capacity (`shutil.disk_usage()`).
2. **[Syntax Format Chosen]**: Confirm user preference from the Naming Syntax Catalog (e.g. `[00]-[Nombre] [Emoji]`).
3. **[Single-Word Root Compliance]**: Verify root categories use exactly one word.
4. **[Module Nesting Compliance]**: Verify Ascii/Youtube $\subset$ Apuntes; Ebooks/Backups/Hardware $\subset$ Otros.
5. **[Anti-Repetition Audit]**: Verify zero duplicate emojis or ASCII icons across sibling folders in the same directory.
6. **[Multi-Phase Segmentation]**: Confirm plan is split into sequential checkpointed phases (Fases A a F).
7. **[1-to-1 Content Verification]**: Confirm actual text and byte hashes before proposing moves or purges.
8. **[Recycle Bin Safety]**: Verify deletion commands route to OS Recycle Bin, never permanent hard unlink.
9. **[Transaction Journal]**: Ensure `.xyz-folder/manifest.json` is initialized.

---

## 7. Agent Execution Protocol (Step-by-Step)

1. **Discovery & Context**: Inspect depth-1 inventory, detect language, identify Git repos.
2. **Interactive Alignment**: Present the Naming Syntax Catalog, Gravity Hierarchy, and proposed visual Before vs After.
3. **Phase-by-Phase Execution**: Execute each phase only after receiving explicit user confirmation.
4. **Verification & Report**: Check zero orphan files, confirm Git status, display final aesthetic tree.
5. **Rollback Ready**: Stand by with `.xyz-folder/manifest.json` for on-demand rollback.
