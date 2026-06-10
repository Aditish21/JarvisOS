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


def route_query(query):

    query = query.lower()

    for keyword in MEMORY_KEYWORDS:
        if keyword in query:
            return "memory"

    for keyword in PDF_KEYWORDS:
        if keyword in query:
            return "pdf"

    return "general"