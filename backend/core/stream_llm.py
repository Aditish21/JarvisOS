import ollama
import asyncio
from memory.memory_manager import get_memory_context
from memory.memory_saver import auto_save_memory

async def stream_ai(prompt, stop_flag: dict):

    memory = get_memory_context(prompt)
    has_memory = "No relevant memory found." not in memory

    # Fix 4: Only reference memory if it actually exists
    memory_section = f"""
MEMORY ABOUT THE USER:
{memory}
Use this memory to answer if relevant.
""" if has_memory else "You have no memory about this user yet."

    messages = [
        {
            "role": "system",
            "content": f"""You are JarvisOS, a helpful personal AI assistant.
{memory_section}
Answer honestly. If you don't know something, say so.
Do not invent or assume information not present in memory."""
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    # Save fact after building prompt (so it's not retrieved in same query)
    auto_save_memory(prompt)

    stream = ollama.chat(
        model="phi3:mini",
        messages=messages,
        stream=True
    )

    loop = asyncio.get_event_loop()

    def get_next_chunk(iterator):
        try:
            return next(iterator)
        except StopIteration:
            return None

    while True:
        if stop_flag.get("stop"):
            break

        chunk = await loop.run_in_executor(None, get_next_chunk, stream)

        if chunk is None:
            break

        content = chunk["message"]["content"]
        yield content