from memory.vector_store import(
    save_memory,
    search_memory
)
save_memory(
    "My favourite language is Python.",
    "1"
)
result=search_memory(
    "What language do I like?"
)
print(result)