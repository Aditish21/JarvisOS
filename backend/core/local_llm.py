import ollama

from memory.memory_manager import (
    get_memory_context
)
from memory.memory_saver import (
    auto_save_memory
)

def ask_ai(prompt):

    memory = get_memory_context(prompt)

    messages = [
        {
            "role": "system",
             "content": f"""
            You are JarvisOS.

            Use the memory below when answering.
            MEMORY:
            {memory}

            If the answer exists in memory, use it.
            Do not say you don't know when the answer is present in memory.
            """
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    response = ollama.chat(
        model="phi3:mini",
        messages=messages
    )
    auto_save_memory(prompt)

    return response["message"]["content"]