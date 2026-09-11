#!/usr/bin/env python3
"""
xyz-folder: Universal Autonomous Directory & Drive Organizer
Classifies messy directories into the strict '[emoji] [Category]/[emoji] [Subcategory]/' architecture.
Zero external dependencies. Python 3 standard library only.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Taxonomy mapping: extension -> (Category, Subcategory)
TAXONOMY: Dict[str, Tuple[str, str]] = {
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
    ".raw": ("[🎨] [Media]", "[🖼️] [Images]"),

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
    ".wma": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".mid": ("[🎨] [Media]", "[🎵] [Audio]"),
    ".midi": ("[🎨] [Media]", "[🎵] [Audio]"),

    # Archives
    ".zip": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".rar": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".7z": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".tar": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".gz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".bz2": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".xz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),
    ".tgz": ("[🗜️] [Archives]", "[📦] [ZIP & RAR]"),

    # Disk Images & Torrents
    ".iso": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".img": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".vhd": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".vhdx": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".torrent": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),

    # Development & AI - Models
    ".gguf": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".safetensors": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".onnx": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".pt": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".pth": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".ckpt": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),

    # Development - Code & Repos
    ".py": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".js": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".ts": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".tsx": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".jsx": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".rs": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".go": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".html": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".htm": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".css": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".scss": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".cpp": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".c": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".h": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".hpp": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".java": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".cs": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".lua": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),

    # Development - Scripts & Config
    ".sh": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".bash": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".ps1": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".bat": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".cmd": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".json": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yaml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".toml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".xml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".ini": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".env": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
}

# Ignored system / temporary files
IGNORED_FILES = {
    "desktop.ini",
    "thumbs.db",
    ".ds_store",
    ".localized",
}

IGNORED_EXTENSIONS = {
    ".tmp",
    ".crdownload",
    ".part",
    ".download",
    ".aria2",
}


def get_default_downloads() -> Path:
    """Detect default Downloads directory across Windows, macOS, and Linux."""
    if sys.platform == "win32":
        # Check Windows User Shell Folders in Registry
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
    """Returns collision-free path appending (1), (2) if needed."""
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
    """Human-readable byte size."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}" if unit != "B" else f"{size} B"
        size /= 1024.0
    return f"{size:.2f} PB"


def organize_directory(
    target_dir: Path,
    dry_run: bool = False,
    auto_confirm: bool = False,
) -> None:
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: Target path '{target_dir}' does not exist or is not a directory.")
        sys.exit(1)

    print(f"\n=======================================================")
    print(f"  xyz-folder: Aesthetic Organizer Engine")
    print(f"  Target: {target_dir}")
    print(f"  Mode:   {'[DRY-RUN PREVIEW]' if dry_run else '[LIVE EXECUTION]'}")
    print(f"=======================================================\n")

    # Discover loose files in target_dir
    planned_moves: List[Tuple[Path, Path, int]] = []

    try:
        entries = list(target_dir.iterdir())
    except PermissionError as e:
        print(f"Permission denied accessing {target_dir}: {e}")
        sys.exit(1)

    for entry in entries:
        # Skip directories
        if entry.is_dir():
            continue

        name_lower = entry.name.lower()
        if name_lower in IGNORED_FILES or entry.suffix.lower() in IGNORED_EXTENSIONS:
            continue

        ext = entry.suffix.lower()
        if ext in TAXONOMY:
            category, subcategory = TAXONOMY[ext]
        else:
            category, subcategory = ("[📦] [Miscellaneous]", "[📁] [Other Files]")

        dest_dir = target_dir / category / subcategory
        dest_file = get_safe_destination(dest_dir, entry.name)
        try:
            size = entry.stat().st_size
        except OSError:
            size = 0
        planned_moves.append((entry, dest_file, size))

    if not planned_moves:
        print("Everything is clean! No loose files found to organize.")
        return

    # Category summaries
    category_counts: Dict[str, int] = {}
    total_bytes = 0
    for src, dst, size in planned_moves:
        cat_pair = f"{dst.parent.parent.name} -> {dst.parent.name}"
        category_counts[cat_pair] = category_counts.get(cat_pair, 0) + 1
        total_bytes += size

    print(f"Found {len(planned_moves)} files to organize ({format_bytes(total_bytes)}):\n")
    for cat_pair, count in sorted(category_counts.items()):
        print(f"  • {cat_pair}: {count} files")

    print("\nProposed Moves:")
    for src, dst, size in planned_moves[:15]:
        print(f"  [+] {src.name} ({format_bytes(size)})")
        print(f"      -> {dst.parent.parent.name}/{dst.parent.name}/{dst.name}")

    if len(planned_moves) > 15:
        print(f"  ... and {len(planned_moves) - 15} more files.")

    if dry_run:
        print("\n[DRY-RUN] No files were moved. Run without --dry-run to apply.")
        return

    if not auto_confirm:
        confirm = input("\nProceed with moving these files? [y/N]: ").strip().lower()
        if confirm not in ("y", "yes"):
            print("Operation aborted by user.")
            return

    # Execute moves atomically
    print("\nExecuting moves...")
    successful_moves = 0
    for src, dst, size in planned_moves:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            successful_moves += 1
        except Exception as e:
            print(f"  [!] Failed to move {src.name}: {e}")

    print(f"\n[DONE] Successfully organized {successful_moves}/{len(planned_moves)} files into aesthetic taxonomy.")


def main():
    parser = argparse.ArgumentParser(
        description="Aesthetic Directory & Drive Organizer with Double-Bracket Emoji Taxonomy.",
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

    args = parser.parse_args()

    if args.target:
        target_path = Path(args.target).resolve()
    else:
        target_path = get_default_downloads()

    organize_directory(
        target_dir=target_path,
        dry_run=args.dry_run,
        auto_confirm=args.auto_confirm,
    )


if __name__ == "__main__":
    main()
