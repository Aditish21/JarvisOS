MEMORY_KEYWORDS = [
    "my name",
    "who am i",
    "what is my name",
    "my favorite",
    "my favourite",
    "my project",
    "what do i like"
]

PDF_KEYWORDS = [
    "silhouette",
    "clustering",
    "chapter",
    "document",
    "pdf",
    "notes",
    "according to the pdf"
]
AUTOMATION_KEYWORDS = [
    "open downloads", "open desktop", "open documents", "open pictures",
    "open chrome", "open vscode", "open notepad", "open calculator",
    "create folder", "create file",
    "open vs code", "open browser", "battery",
    "battery status",
    "battery percentage",

    "ram",
    "ram usage",
    "memory usage",
    "RAM","RAM USAGE"

    "cpu",
    "cpu usage",
    "processor usage",
    "CPU"

    "screenshot",
    "take screenshot",
    "capture screen",
    "screen capture"
    "Screenshot","Capture Screenshot","Take screenshot"
]

def route_query(query):

    query = query.lower()

    for keyword in AUTOMATION_KEYWORDS:
        if keyword in query:
            print(f"[ROUTE] automation (matched: '{keyword}')")
            return "automation"

    for keyword in MEMORY_KEYWORDS:
        if keyword in query:
            return "memory"

    for keyword in PDF_KEYWORDS:
        if keyword in query:
            return "pdf"

    return "general"