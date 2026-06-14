from automation.app_control import (
    open_chrome, open_vscode, open_notepad, open_calculator
)
from automation.file_control import (
    open_downloads, open_desktop,
    open_documents, open_pictures,
    create_folder, create_file
)
from automation.system_control import (
    get_battery,
    get_ram,
    get_cpu,
    take_screenshot
)

def run_pc_command(query):
    q = query.lower().strip()

    # Apps
    if "chrome" in q:          return open_chrome()      or "Opening Chrome"
    if "vscode" in q or "vs code" in q: return open_vscode() or "Opening VS Code"
    if "notepad" in q:         return open_notepad()     or "Opening Notepad"
    if "calculator" in q:      return open_calculator()  or "Opening Calculator"

    # Folders
    if "downloads" in q:       return open_downloads()
    if "desktop" in q:         return open_desktop()
    if "documents" in q:       return open_documents()
    if "pictures" in q:        return open_pictures()

    # File system
    if "create folder" in q:
        name = q.replace("create folder", "").strip()
        return create_folder(name)

    if "create file" in q:
        name = q.replace("create file", "").strip()
        return create_file(name)
    #system control
    
    if "battery" in query:
        return get_battery()

    if "ram" in query:
        return get_ram()

    if "cpu" in query:
        return get_cpu()

    if "screenshot" in query:
        return take_screenshot()

    return None