from memory.memory_saver import (
    auto_save_memory
)

from memory.memory_manager import (
    get_memory_context
)

auto_save_memory(
    "My name is Aditi."
)

memory = get_memory_context(
    "What is my name?"
)

print(memory)