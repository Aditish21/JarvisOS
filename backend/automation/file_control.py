import os
import ctypes
import subprocess
from ctypes import windll, wintypes
from pathlib import Path

# Windows Known Folder GUIDs
# These are stable across ALL Windows versions and OneDrive configurations
KNOWN_FOLDERS = {
    "downloads":  "{374DE290-123F-4565-9164-39C4925E467B}",
    "desktop":    "{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}",
    "documents":  "{FDD39AD0-238F-46AF-ADB4-6C85480369C7}",
    "pictures":   "{33E28130-4E1E-4676-835A-98395C3BC3BB}",
    "music":      "{4BD8D571-6D19-48D3-BE97-422220080E43}",
    "videos":     "{18989B1D-99B5-455B-841C-AB7C74E4DDFC}",
    "downloads":  "{374DE290-123F-4565-9164-39C4925E467B}",
}

def get_windows_folder(folder_name: str) -> str:
    """
    Uses Win32 SHGetKnownFolderPath to get the REAL path.
    Works on all Windows versions, OneDrive, custom locations.
    """
    guid = KNOWN_FOLDERS.get(folder_name.lower())
    if not guid:
        raise ValueError(f"Unknown folder: {folder_name}")

   

    try:
        result = subprocess.run(
            [
                "powershell", "-NoProfile", "-Command",
                f"[System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::{folder_name.capitalize()})"
            ],
            capture_output=True, text=True, timeout=5
        )
        ps_path = result.stdout.strip()
        if ps_path and os.path.exists(ps_path):
            return ps_path
    except Exception:
        pass

    # Downloads is NOT in SpecialFolder enum — use registry directly
    if folder_name.lower() == "downloads":
        try:
            result = subprocess.run(
                [
                    "powershell", "-NoProfile", "-Command",
                    "(New-Object -ComObject Shell.Application)"
                    ".NameSpace('shell:Downloads').Self.Path"
                ],
                capture_output=True, text=True, timeout=5
            )
            ps_path = result.stdout.strip()
            if ps_path and os.path.exists(ps_path):
                return ps_path
        except Exception:
            pass

    # Final fallback — construct manually
    home = Path.home()
    fallback = home / folder_name.capitalize()
    return str(fallback)


def open_folder(folder_name: str) -> str:
    """Opens any Windows known folder reliably."""
    try:
        path = get_windows_folder(folder_name)
        subprocess.Popen(f'explorer "{path}"')   # explorer never raises, even on edge cases
        return f"Opening {folder_name.capitalize()}: {path}"
    except Exception as e:
        return f"Could not open {folder_name}: {str(e)}"


# ── Public functions ──────────────────────────────────────────

def open_downloads():
    return open_folder("downloads")

def open_desktop():
    return open_folder("desktop")

def open_documents():
    return open_folder("documents")

def open_pictures():
    return open_folder("pictures")


def create_folder(folder_name: str) -> str:
    """Creates folder on the REAL Desktop path."""
    try:
        desktop = get_windows_folder("desktop")
        path = os.path.join(desktop, folder_name)
        os.makedirs(path, exist_ok=True)
        return f"Folder '{folder_name}' created on Desktop"
    except Exception as e:
        return f"Could not create folder: {str(e)}"


def create_file(file_name: str) -> str:
    """Creates file on the REAL Desktop path."""
    try:
        desktop = get_windows_folder("desktop")
        path = os.path.join(desktop, file_name)
        with open(path, "w") as f:
            f.write("")
        return f"File '{file_name}' created on Desktop"
    except Exception as e:
        return f"Could not create file: {str(e)}"