#!/usr/bin/env python3
"""
xyz-folder: Baseline Reference Organizer & Rollback Engine.

NOTE FOR AI AGENTS:
This script is a reference baseline implementation. Agents should adapt, customize,
or generate tailored scripts dynamically depending on the user's specific files,
subfolder requirements, language, and operating environment.

Features:
- Dual-bracket & emoji taxonomy architecture.
- Transaction journaling via .xyz-folder-manifest.json.
- One-command full rollback (--undo) and selective restoration (--restore-filter).
- Multi-language taxonomy (English / Spanish / Auto).
- Collision prevention via version suffixing (e.g. 'file (1).ext').
- Zero external dependencies (Python 3 stdlib only).
"""

import argparse
import json
import locale
import os
import shutil
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

MANIFEST_FILENAME = ".xyz-folder-manifest.json"

# English Taxonomy
TAXONOMY_EN: Dict[str, Tuple[str, str]] = {
    # Installers & Packages
    ".exe": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".msi": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".appx": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".msix": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".pkg": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".dmg": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".deb": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".rpm": ("[📦] [Installers]", "[💻] [Desktop Apps]"),
    ".apk": ("[📦] [Installers]", "[📱] [Mobile & Packages]"),
    ".xapk": ("[📦] [Installers]", "[📱] [Mobile & Packages]"),
    ".ipa": ("[📦] [Installers]", "[📱] [Mobile & Packages]"),
    ".jar": ("[📦] [Installers]", "[📱] [Mobile & Packages]"),

    # Documents & Books
    ".pdf": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".epub": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".mobi": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".azw": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".azw3": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".cbr": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".cbz": ("[📄] [Documents]", "[📑] [PDFs & Books]"),
    ".djvu": ("[📄] [Documents]", "[📑] [PDFs & Books]"),

    # Office & Sheets
    ".docx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".doc": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".xlsx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".xls": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".csv": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".pptx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".ppt": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".odt": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".ods": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".odp": ("[📄] [Documents]", "[📊] [Office & Sheets]"),

    # Notes & Text
    ".txt": ("[📄] [Documents]", "[📝] [Notes & Text]"),
    ".md": ("[📄] [Documents]", "[📝] [Notes & Text]"),
    ".log": ("[📄] [Documents]", "[📝] [Notes & Text]"),
    ".rtf": ("[📄] [Documents]", "[📝] [Notes & Text]"),

    # Media - Images
    ".png": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".jpg": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".jpeg": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".webp": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".svg": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".gif": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".psd": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".ai": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".ico": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".bmp": ("[🎨] [Media]", "[🖼️] [Images]"),
    ".tiff": ("[🎨] [Media]", "[🖼️] [Images]"),

    # Media - Videos
    ".mp4": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".mkv": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".avi": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".mov": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".webm": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".flv": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".wmv": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".srt": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".vtt": ("[🎨] [Media]", "[🎬] [Videos]"),

    # Media - Audio
    ".mp3": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".flac": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".wav": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".m4a": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".aac": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".ogg": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".opus": ("[🎨] [Media]", "[🎵] [Audio]"),

    # Archives
    ".zip": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".rar": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".7z": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".tar": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".gz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".bz2": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".xz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".tgz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".iso": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".img": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".torrent": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),

    # Development & AI
    ".gguf": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".safetensors": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".onnx": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".pt": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".pth": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".py": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".js": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".ts": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".tsx": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".rs": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".go": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".html": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".css": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".sh": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".ps1": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".json": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yaml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".toml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
}

# Spanish Taxonomy
TAXONOMY_ES: Dict[str, Tuple[str, str]] = {
    # Instaladores y Paquetes
    ".exe": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".msi": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".appx": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".msix": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".pkg": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".dmg": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".deb": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".rpm": ("[📦] [Instaladores]", "[💻] [Programas]"),
    ".apk": ("[📦] [Instaladores]", "[📱] [Android & APK]"),
    ".xapk": ("[📦] [Instaladores]", "[📱] [Android & APK]"),
    ".ipa": ("[📦] [Instaladores]", "[📱] [Android & APK]"),
    ".jar": ("[📦] [Instaladores]", "[🎮] [Mods & Plugins]"),

    # Documentos y Libros
    ".pdf": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".epub": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".mobi": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".azw": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".azw3": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".cbr": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),
    ".cbz": ("[📄] [Documentos]", "[📑] [PDFs & Libros]"),

    # Ofimática
    ".docx": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".doc": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".xlsx": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".xls": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".csv": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".pptx": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".ppt": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".odt": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".ods": ("[📄] [Documentos]", "[📊] [Ofimática]"),
    ".eml": ("[📄] [Documentos]", "[📊] [Ofimática]"),

    # Notas y Texto
    ".txt": ("[📄] [Documentos]", "[📝] [Notas & Textos]"),
    ".md": ("[📄] [Documentos]", "[📝] [Notas & Textos]"),
    ".log": ("[📄] [Documentos]", "[📝] [Notas & Textos]"),
    ".rtf": ("[📄] [Documentos]", "[📝] [Notas & Textos]"),

    # Multimedia - Imágenes
    ".png": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".jpg": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".jpeg": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".webp": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".svg": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".gif": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".psd": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".ai": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),
    ".ico": ("[🎨] [Multimedia]", "[🖼️] [Imágenes]"),

    # Multimedia - Vídeos
    ".mp4": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),
    ".mkv": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),
    ".avi": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),
    ".mov": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),
    ".webm": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),
    ".srt": ("[🎨] [Multimedia]", "[🎬] [Vídeos]"),

    # Multimedia - Audio
    ".mp3": ("[🎨] [Multimedia]", "[🎵] [Audio]"),
    ".flac": ("[🎨] [Multimedia]", "[🎵] [Audio]"),
    ".wav": ("[🎨] [Multimedia]", "[🎵] [Audio]"),
    ".m4a": ("[🎨] [Multimedia]", "[🎵] [Audio]"),
    ".aac": ("[🎨] [Multimedia]", "[🎵] [Audio]"),
    ".ogg": ("[🎨] [Multimedia]", "[🎵] [Audio]"),

    # Comprimidos
    ".zip": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".rar": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".7z": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".tar": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".gz": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".bz2": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".xz": ("[🗜️] [Comprimidos]", "[📦] [ZIP & RAR]"),
    ".iso": ("[🗜️] [Comprimidos]", "[💿] [Imágenes ISO]"),
    ".torrent": ("[🗜️] [Comprimidos]", "[💿] [Torrents]"),

    # Desarrollo y AI
    ".gguf": ("[💻] [Desarrollo & AI]", "[🤖] [Modelos & Pesos]"),
    ".safetensors": ("[💻] [Desarrollo & AI]", "[🤖] [Modelos & Pesos]"),
    ".py": ("[💻] [Desarrollo & AI]", "[🐙] [Código & Repos]"),
    ".js": ("[💻] [Desarrollo & AI]", "[🐙] [Código & Repos]"),
    ".ts": ("[💻] [Desarrollo & AI]", "[🐙] [Código & Repos]"),
    ".html": ("[💻] [Desarrollo & AI]", "[🐙] [Código & Repos]"),
    ".css": ("[💻] [Desarrollo & AI]", "[🐙] [Código & Repos]"),
    ".sh": ("[💻] [Desarrollo & AI]", "[🛠️] [Scripts & Config]"),
    ".ps1": ("[💻] [Desarrollo & AI]", "[🛠️] [Scripts & Config]"),
    ".json": ("[💻] [Desarrollo & AI]", "[🛠️] [Scripts & Config]"),
    ".yaml": ("[💻] [Desarrollo & AI]", "[🛠️] [Scripts & Config]"),
    ".yml": ("[💻] [Desarrollo & AI]", "[🛠️] [Scripts & Config]"),
}

IGNORED_FILES = {"desktop.ini", "thumbs.db", ".ds_store", ".localized", MANIFEST_FILENAME}
IGNORED_EXTENSIONS = {".tmp", ".crdownload", ".part", ".download", ".aria2"}


def detect_language() -> str:
    """Auto-detect system language."""
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.lower().startswith("es"):
            return "es"
    except Exception:
        pass
    return "en"


def get_default_downloads() -> Path:
    """Detect default Downloads directory across OS."""
    if sys.platform == "win32":
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
            )
            val, _ = winreg.QueryValueEx(key, "{374DE290-123F-4565-9164-39C4925E467B}")
            expanded = os.path.expandvars(val)
            if os.path.isdir(expanded):
                return Path(expanded)
        except Exception:
            pass
    return Path.home() / "Downloads"


def get_safe_destination(dest_dir: Path, filename: str) -> Path:
    """Returns a collision-free path by suffixing (1), (2) if file exists."""
    candidate = dest_dir / filename
    if not candidate.exists():
        return candidate

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1
    while candidate.exists():
        candidate = dest_dir / f"{stem} ({counter}){suffix}"
        counter += 1
    return candidate


def format_bytes(size: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}" if unit != "B" else f"{size} B"
        size /= 1024.0
    return f"{size:.2f} PB"


def execute_rollback(target_dir: Path, filter_pattern: Optional[str] = None) -> None:
    """Reverses operations recorded in .xyz-folder-manifest.json."""
    manifest_path = target_dir / MANIFEST_FILENAME
    if not manifest_path.exists():
        print(f"Error: No rollback manifest found at {manifest_path}")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    moves = data.get("moves", [])
    if not moves:
        print("Manifest is empty. Nothing to restore.")
        return

    print(f"\n=======================================================")
    print(f"  xyz-folder: Rollback Engine")
    print(f"  Target: {target_dir}")
    print(f"  Entries in Manifest: {len(moves)}")
    if filter_pattern:
        print(f"  Selective Filter: '{filter_pattern}'")
    print(f"=======================================================\n")

    restored_count = 0
    remaining_moves = []

    for entry in reversed(moves):
        src = Path(entry["src"])
        dst = Path(entry["dst"])

        if filter_pattern and filter_pattern.lower() not in dst.name.lower():
            remaining_moves.append(entry)
            continue

        if not dst.exists():
            print(f"  [!] Missing destination file: {dst.name} (skipped)")
            remaining_moves.append(entry)
            continue

        try:
            src.parent.mkdir(parents=True, exist_ok=True)
            safe_target = get_safe_destination(src.parent, src.name)
            shutil.move(str(dst), str(safe_target))
            restored_count += 1
            print(f"  [⏪] Restored: {dst.name} -> {safe_target.name}")

            # Clean empty parent directory if left empty
            parent = dst.parent
            while parent != target_dir and parent.exists():
                try:
                    if not any(parent.iterdir()):
                        parent.rmdir()
                        parent = parent.parent
                    else:
                        break
                except OSError:
                    break
        except Exception as e:
            print(f"  [!] Failed to restore {dst.name}: {e}")
            remaining_moves.append(entry)

    print(f"\n[DONE] Restored {restored_count} files to original positions.")

    if not remaining_moves:
        try:
            manifest_path.unlink()
            print("Rollback complete. Manifest cleaned up.")
        except OSError:
            pass
    else:
        data["moves"] = list(reversed(remaining_moves))
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Manifest updated. {len(remaining_moves)} entries remaining.")


def organize_directory(
    target_dir: Path,
    lang: str = "auto",
    dry_run: bool = False,
    auto_confirm: bool = False,
) -> None:
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: Target path '{target_dir}' does not exist or is not a directory.")
        sys.exit(1)

    selected_lang = detect_language() if lang == "auto" else lang
    taxonomy = TAXONOMY_ES if selected_lang == "es" else TAXONOMY_EN

    print(f"\n=======================================================")
    print(f"  xyz-folder: Adaptive Organizer Engine")
    print(f"  Target:   {target_dir}")
    print(f"  Language: {selected_lang.upper()}")
    print(f"  Mode:     {'[DRY-RUN PREVIEW]' if dry_run else '[LIVE EXECUTION]'}")
    print(f"=======================================================\n")

    planned_moves: List[Tuple[Path, Path, int]] = []

    try:
        entries = list(target_dir.iterdir())
    except PermissionError as e:
        print(f"Permission denied accessing {target_dir}: {e}")
        sys.exit(1)

    for entry in entries:
        if entry.is_dir():
            continue

        name_lower = entry.name.lower()
        if name_lower in IGNORED_FILES or entry.suffix.lower() in IGNORED_EXTENSIONS:
            continue

        ext = entry.suffix.lower()
        if ext in taxonomy:
            category, subcategory = taxonomy[ext]
        else:
            category, subcategory = (
                ("[📦] [Miscelánea]", "[📁] [Otros]") if selected_lang == "es"
                else ("[📦] [Miscellaneous]", "[📁] [Other Files]")
            )

        dest_dir = target_dir / category / subcategory
        dest_file = get_safe_destination(dest_dir, entry.name)
        try:
            size = entry.stat().st_size
        except OSError:
            size = 0
        planned_moves.append((entry, dest_file, size))

    if not planned_moves:
        print("Everything is organized! No loose files found.")
        return

    category_counts: Dict[str, int] = {}
    total_bytes = 0
    for src, dst, size in planned_moves:
        cat_pair = f"{dst.parent.parent.name} -> {dst.parent.name}"
        category_counts[cat_pair] = category_counts.get(cat_pair, 0) + 1
        total_bytes += size

    print(f"Found {len(planned_moves)} files to organize ({format_bytes(total_bytes)}):\n")
    for cat_pair, count in sorted(category_counts.items()):
        print(f"  • {cat_pair}: {count} files")

    print("\nProposed Moves (Sample):")
    for src, dst, size in planned_moves[:15]:
        print(f"  [+] {src.name} ({format_bytes(size)})")
        print(f"      -> {dst.parent.parent.name}/{dst.parent.name}/{dst.name}")

    if len(planned_moves) > 15:
        print(f"  ... and {len(planned_moves) - 15} more files.")

    if dry_run:
        print("\n[DRY-RUN] No files were moved. Run without --dry-run to apply.")
        return

    if not auto_confirm:
        prompt_text = "\n¿Deseas proceder con la organización de estos archivos? [y/N]: " if selected_lang == "es" else "\nProceed with moving these files? [y/N]: "
        confirm = input(prompt_text).strip().lower()
        if confirm not in ("y", "yes", "s", "si", "sí"):
            print("Operation aborted by user.")
            return

    # Execute moves atomically and journal into manifest
    print("\nExecuting moves...")
    manifest_entries = []
    successful_moves = 0

    for src, dst, size in planned_moves:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            manifest_entries.append({
                "src": str(src),
                "dst": str(dst),
                "size": size,
            })
            successful_moves += 1
        except Exception as e:
            print(f"  [!] Failed to move {src.name}: {e}")

    # Write transaction manifest for rollback support
    manifest_path = target_dir / MANIFEST_FILENAME
    existing_manifest = {"timestamp": time.time(), "moves": []}
    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                existing_manifest = json.load(f)
        except Exception:
            pass

    existing_manifest["moves"].extend(manifest_entries)
    existing_manifest["last_updated"] = time.time()

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(existing_manifest, f, indent=2, ensure_ascii=False)

    print(f"\n[DONE] Successfully organized {successful_moves}/{len(planned_moves)} files.")
    print(f"[JOURNAL] Rollback transaction saved to {manifest_path.name}")
    print(f"         Run 'python organize.py --undo' at any time to restore.")


def main():
    parser = argparse.ArgumentParser(
        description="Aesthetic Directory & Drive Organizer with Dynamic Emoji Taxonomy & Rollback Support.",
    )
    parser.add_argument(
        "-t", "--target",
        type=str,
        default=None,
        help="Target directory to organize (defaults to user Downloads folder)",
    )
    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Simulate moves and display plan without modifying any files",
    )
    parser.add_argument(
        "-y", "--yes",
        dest="auto_confirm",
        action="store_true",
        help="Automatically confirm and apply changes without prompting",
    )
    parser.add_argument(
        "--lang",
        choices=["auto", "en", "es"],
        default="auto",
        help="Language for category taxonomy ('auto', 'es', or 'en')",
    )
    parser.add_argument(
        "-u", "--undo",
        action="store_true",
        help="Rollback previous organization using .xyz-folder-manifest.json",
    )
    parser.add_argument(
        "--restore-filter",
        type=str,
        default=None,
        help="Selectively restore only files matching this substring/extension",
    )

    args = parser.parse_args()

    target_path = Path(args.target).resolve() if args.target else get_default_downloads()

    if args.undo or args.restore_filter:
        execute_rollback(target_dir=target_path, filter_pattern=args.restore_filter)
    else:
        organize_directory(
            target_dir=target_path,
            lang=args.lang,
            dry_run=args.dry_run,
            auto_confirm=args.auto_confirm,
        )


if __name__ == "__main__":
    main()
