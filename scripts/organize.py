#!/usr/bin/env python3
"""
========================================================================================
xyz-folder: Baseline Reference Architecture & Dynamic Script Template
========================================================================================

GUÍA ARQUITECTÓNICA PARA AGENTES DE IA (AI AGENT IMPLEMENTATION GUIDE):
----------------------------------------------------------------------------------------
ESTE SCRIPT ES UNA GUÍA Y PLANTILLA BASE DE REFERENCIA, NO UNA CAJA NEGRA RÍGIDA.
Cuando un agente de IA ejecuta la skill 'xyz-folder', DEBE:
1. Escanear primero el directorio del usuario para analizar qué extensiones reales existen.
2. Si los archivos del usuario son estándar, puede ejecutar este script adaptando parámetros.
3. Si el usuario tiene extensiones especializadas (e.g., modelos 3D .stl/.obj, audio stems,
   datasets de machine learning, ROMs de emulación, libros de calibre, etc.), el agente
   DEBE GENERAR O ADAPTAR este script dinámicamente inyectando las categorías exactas
   que encajen con el contexto del usuario.
4. NUNCA forzar categorías vacías en el árbol visual si el usuario no tiene esos archivos.

========================================================================================
CHECKLIST DE VERIFICACIÓN OBLIGATORIA (LO PRIMERO DE TODO ANTES DE TOCAR UN BYTE):
========================================================================================
[✓] 1. DISK CAPACITY: Verificar espacio libre con shutil.disk_usage() en disco destino.
[✓] 2. FILE LOCKS: Verificar que ningún archivo esté en uso por aplicaciones activas.
[✓] 3. COLLISION PREVENTION: Generar sufijos automáticos (1), (2) para nunca sobreescribir.
[✓] 4. LANGUAGE MATCH: Ajustar el idioma de las carpetas al del usuario (ES / EN).
[✓] 5. DRY-RUN PREVIEW: Mostrar un desglose previo y esperar confirmación del usuario.
[✓] 6. MANIFEST JOURNAL: Guardar .xyz-folder/manifest.json para permitir rollback inmediato.
========================================================================================
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

MANIFEST_DIRNAME = ".xyz-folder"
MANIFEST_FILENAME = "manifest.json"
LEGACY_MANIFEST_FILENAME = ".xyz-folder-manifest.json"


def resolve_manifest_path(target_dir: Path, for_write: bool = False) -> Path:
    """Canonical journal is .xyz-folder/manifest.json; undo still reads the legacy root file."""
    canonical = target_dir / MANIFEST_DIRNAME / MANIFEST_FILENAME
    legacy = target_dir / LEGACY_MANIFEST_FILENAME
    if for_write:
        canonical.parent.mkdir(parents=True, exist_ok=True)
        return canonical
    if canonical.exists():
        return canonical
    if legacy.exists():
        return legacy
    return canonical

# ======================================================================================
# SECCIÓN 1: TAXONOMÍAS DE REFERENCIA (ADAPTABLES POR EL AGENTE)
# ======================================================================================
# El agente puede y debe añadir o modificar este diccionario según los archivos reales
# que descubra en el escaneo del directorio. Por ejemplo:
#   ".stl": ("[🎨] [Diseño 3D]", "[🖨️] [Modelos STL]")
#   ".nes": ("[🎮] [Retro & Emulación]", "[🕹️] [Nintendo NES]")
#   ".fasta": ("[🔬] [Bioinformática]", "[🧬] [Secuencias]")

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

    # Office & Sheets
    ".docx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".doc": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".xlsx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".xls": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".csv": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".pptx": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".ppt": ("[📄] [Documents]", "[📊] [Office & Sheets]"),
    ".odt": ("[📄] [Documents]", "[📊] [Office & Sheets]"),

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

    # Media - Videos
    ".mp4": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".mkv": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".avi": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".mov": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".webm": ("[🎨] [Media]", "[🎬] [Videos]"),
    ".srt": ("[🎨] [Media]", "[🎬] [Videos]"),

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
    ".iso": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),
    ".torrent": ("[🗜️] [Archives]", "[💿] [Disk Images & ISOs]"),

    # Development & AI
    ".gguf": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".safetensors": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".onnx": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".pt": ("[💻] [Development & AI]", "[🤖] [Models & Weights]"),
    ".py": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".js": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".ts": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".rs": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".go": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".html": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".css": ("[💻] [Development & AI]", "[🐙] [Repos & Code]"),
    ".sh": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".ps1": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".json": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yaml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
    ".yml": ("[💻] [Development & AI]", "[🛠️] [Scripts & Config]"),
}

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

# Archivos del sistema ignorados para no romper el entorno
IGNORED_FILES = {"desktop.ini", "thumbs.db", ".ds_store", ".localized", LEGACY_MANIFEST_FILENAME}
IGNORED_EXTENSIONS = {".tmp", ".crdownload", ".part", ".download", ".aria2"}


# ======================================================================================
# SECCIÓN 2: VERIFICACIONES CRÍTICAS PREVIAS (PRE-FLIGHT CHECKS)
# ======================================================================================

def verify_disk_space(target_dir: Path, required_bytes: int) -> bool:
    """Verifica que haya suficiente espacio libre en la unidad destino."""
    try:
        total, used, free = shutil.disk_usage(str(target_dir))
        # Exigir al menos el espacio requerido + 500 MB de margen de seguridad
        safety_margin = 500 * 1024 * 1024
        if free < (required_bytes + safety_margin):
            print(f"[ERROR DE SEGURIDAD] Espacio insuficiente en disco.")
            print(f"  Disponible: {format_bytes(free)} | Requerido: {format_bytes(required_bytes + safety_margin)}")
            return False
        return True
    except Exception as e:
        print(f"[AVISO] No se pudo verificar el espacio en disco: {e}")
        return True


def detect_language() -> str:
    """Detecta el idioma del entorno del usuario."""
    try:
        lang, _ = locale.getdefaultlocale()
        if lang and lang.lower().startswith("es"):
            return "es"
    except Exception:
        pass
    return "en"


def get_default_downloads() -> Path:
    """Descubre dinámicamente la carpeta de Descargas según el SO."""
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
    """
    GARANTÍA DE CERO PÉRDIDA: Previene colisiones.
    Si 'archivo.ext' ya existe, genera 'archivo (1).ext', 'archivo (2).ext', etc.
    """
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


# ======================================================================================
# SECCIÓN 3: MOTOR DE ROLLBACK Y RESTAURACIÓN SELECTIVA
# ======================================================================================

def execute_rollback(target_dir: Path, filter_pattern: Optional[str] = None) -> None:
    """
    Deshace las operaciones registradas en el manifest.
    Si se especifica filter_pattern, restaura únicamente los archivos que coincidan.
    """
    manifest_path = resolve_manifest_path(target_dir, for_write=False)
    if not manifest_path.exists():
        print(f"Error: No se encontró el registro de transacciones en: {manifest_path}")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    moves = data.get("moves", [])
    if not moves:
        print("El manifest está vacío. No hay archivos para restaurar.")
        return

    print(f"\n=======================================================")
    print(f"  xyz-folder: Motor de Rollback & Restauración")
    print(f"  Directorio: {target_dir}")
    print(f"  Movimientos en historial: {len(moves)}")
    if filter_pattern:
        print(f"  Filtro selectivo activo: '{filter_pattern}'")
    print(f"=======================================================\n")

    restored_count = 0
    remaining_moves = []

    # Revertir en orden inverso (los últimos primero)
    for entry in reversed(moves):
        src = Path(entry["src"])
        dst = Path(entry["dst"])

        if filter_pattern and filter_pattern.lower() not in dst.name.lower():
            remaining_moves.append(entry)
            continue

        if not dst.exists():
            print(f"  [!] Archivo destino no encontrado: {dst.name} (ignorado)")
            remaining_moves.append(entry)
            continue

        try:
            src.parent.mkdir(parents=True, exist_ok=True)
            safe_target = get_safe_destination(src.parent, src.name)
            shutil.move(str(dst), str(safe_target))
            restored_count += 1
            print(f"  [⏪] Restaurado: {dst.name} -> {safe_target.name}")

            # Limpiar carpetas creadas si quedaron vacías
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
            print(f"  [!] Error al restaurar {dst.name}: {e}")
            remaining_moves.append(entry)

    print(f"\n[FINALIZADO] Se restauraron {restored_count} archivos a su ubicación previa.")

    if not remaining_moves:
        try:
            manifest_path.unlink()
            print("Rollback completo concluido. Archivo manifest limpiado.")
        except OSError:
            pass
    else:
        data["moves"] = list(reversed(remaining_moves))
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Manifest actualizado. Restan {len(remaining_moves)} entradas pendientes.")


# ======================================================================================
# SECCIÓN 4: MOTOR DE ORGANIZACIÓN ATÓMICA
# ======================================================================================

def organize_directory(
    target_dir: Path,
    lang: str = "auto",
    dry_run: bool = False,
    auto_confirm: bool = False,
) -> None:
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: La ruta '{target_dir}' no existe o no es un directorio.")
        sys.exit(1)

    selected_lang = detect_language() if lang == "auto" else lang
    taxonomy = TAXONOMY_ES if selected_lang == "es" else TAXONOMY_EN

    print(f"\n=======================================================")
    print(f"  xyz-folder: Motor Adaptable de Organización")
    print(f"  Directorio: {target_dir}")
    print(f"  Idioma:     {selected_lang.upper()}")
    print(f"  Modo:       {'[SIMULACIÓN / DRY-RUN]' if dry_run else '[EJECUCIÓN REAL]'}")
    print(f"=======================================================\n")

    planned_moves: List[Tuple[Path, Path, int]] = []

    try:
        entries = list(target_dir.iterdir())
    except PermissionError as e:
        print(f"Permiso denegado al acceder a {target_dir}: {e}")
        sys.exit(1)

    total_bytes_needed = 0

    for entry in entries:
        # Preservar carpetas existentes para no crear anidaciones indeseadas
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
        total_bytes_needed += size

    if not planned_moves:
        print("Todo en orden. No se encontraron archivos sueltos para clasificar.")
        return

    # Comprobación de seguridad de espacio
    if not verify_disk_space(target_dir, total_bytes_needed):
        sys.exit(1)

    category_counts: Dict[str, int] = {}
    for src, dst, size in planned_moves:
        cat_pair = f"{dst.parent.parent.name} -> {dst.parent.name}"
        category_counts[cat_pair] = category_counts.get(cat_pair, 0) + 1

    print(f"Se encontraron {len(planned_moves)} archivos ({format_bytes(total_bytes_needed)}):\n")
    for cat_pair, count in sorted(category_counts.items()):
        print(f"  • {cat_pair}: {count} archivos")

    print("\nPropuesta de movimientos (Muestra inicial):")
    for src, dst, size in planned_moves[:15]:
        print(f"  [+] {src.name} ({format_bytes(size)})")
        print(f"      -> {dst.parent.parent.name}/{dst.parent.name}/{dst.name}")

    if len(planned_moves) > 15:
        print(f"  ... y {len(planned_moves) - 15} archivos más.")

    if dry_run:
        print("\n[DRY-RUN] Simulación completa. No se modificó ningún archivo.")
        print("Ejecuta sin '--dry-run' para aplicar los cambios.")
        return

    if not auto_confirm:
        prompt_text = (
            "\n¿Confirmas proceder con la organización de estos archivos? [y/N]: "
            if selected_lang == "es"
            else "\nProceed with moving these files? [y/N]: "
        )
        confirm = input(prompt_text).strip().lower()
        if confirm not in ("y", "yes", "s", "si", "sí"):
            print("Operación cancelada por el usuario.")
            return

    # Ejecución atómica y registro en el manifest
    print("\nEjecutando movimientos atómicos...")
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
            print(f"  [!] Fallo al mover {src.name}: {e}")

    # Guardar manifest transaccional (canonical path; merge legacy if present)
    existing_manifest = {"timestamp": time.time(), "moves": []}
    read_path = resolve_manifest_path(target_dir, for_write=False)
    if read_path.exists():
        try:
            with open(read_path, "r", encoding="utf-8") as f:
                existing_manifest = json.load(f)
        except Exception:
            pass
    manifest_path = resolve_manifest_path(target_dir, for_write=True)

    existing_manifest["moves"].extend(manifest_entries)
    existing_manifest["last_updated"] = time.time()

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(existing_manifest, f, indent=2, ensure_ascii=False)

    print(f"\n[ÉXITO] Se organizaron {successful_moves}/{len(planned_moves)} archivos.")
    print(f"[JOURNAL] Registro transaccional guardado en: {manifest_path.name}")
    print(f"          Ejecuta 'python organize.py --undo' en cualquier momento para deshacer.")


def main():
    parser = argparse.ArgumentParser(
        description="Organizador de Directorios y Unidades con Taxonomía Emoji Adaptable y Soporte de Rollback.",
    )
    parser.add_argument(
        "-t", "--target",
        type=str,
        default=None,
        help="Directorio objetivo (por defecto: Descargas del usuario)",
    )
    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Simula los movimientos sin modificar archivos en disco",
    )
    parser.add_argument(
        "-y", "--yes",
        dest="auto_confirm",
        action="store_true",
        help="Confirma automáticamente la ejecución sin solicitar confirmación interactiva",
    )
    parser.add_argument(
        "--lang",
        choices=["auto", "en", "es"],
        default="auto",
        help="Idioma de las carpetas generadas ('auto', 'es', o 'en')",
    )
    parser.add_argument(
        "-u", "--undo",
        action="store_true",
        help="Deshace la reorganización previa usando el archivo manifest",
    )
    parser.add_argument(
        "--restore-filter",
        type=str,
        default=None,
        help="Restaura selectivamente solo los archivos que contengan este texto o extensión",
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
