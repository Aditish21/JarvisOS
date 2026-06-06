from memory.vector_store import search_memory

def get_memory_context(query):
    documents = search_memory(query)

    if not documents:
        return "No relevant memory found."

    return "\n".join(f"- {doc}" for doc in documents)