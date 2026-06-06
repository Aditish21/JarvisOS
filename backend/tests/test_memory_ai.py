from memory.vector_store import save_memory
from memory.memory_manager import get_memory_context
from core.local_llm import ask_ai

save_memory(
    "My name is Aditi.",
    "1"
)

memory = get_memory_context(
    "What is my name?"
)

print("MEMORY FOUND:")
print(memory)

response = ask_ai(
    "What is my name?"
)

print("\nAI RESPONSE:")
print(response)