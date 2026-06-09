from rag.document_store import collection

data = collection.get()

print(
    "Total Documents:",
    len(data["documents"])
)