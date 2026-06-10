import ollama
import asyncio

from memory.memory_manager import get_memory_context
from memory.memory_saver import auto_save_memory

from agents.router import route_query
from rag.retriever import retrieve_document


async def stream_ai(prompt, stop_flag: dict):

    # -----------------------------
    # ROUTER
    # -----------------------------
    route = route_query(prompt)

    print(f"\n[ROUTE] {route}")

    # -----------------------------
    # PDF ROUTE
    # -----------------------------
    if route == "pdf":

        context = retrieve_document(prompt)

        messages = [
            {
                "role": "system",
                "content": f"""
You are JarvisOS.

Answer using ONLY the PDF context below.

PDF CONTEXT:

{context}

If the answer is not present in the PDF,
say:

"I could not find that information in the document."
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    # -----------------------------
    # MEMORY + GENERAL AI ROUTE
    # -----------------------------
    else:

        memory = get_memory_context(prompt)

        has_memory = (
            memory.strip() != ""
            and "No relevant memory found." not in memory
        )

        memory_section = f"""
MEMORY ABOUT USER:

{memory}

Use memory only if relevant.
""" if has_memory else "No user memory available."

        messages = [
            {
                "role": "system",
                "content": f"""
You are JarvisOS.

{memory_section}

Answer honestly.
Do not invent information.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    # -----------------------------
    # SAVE MEMORY
    # -----------------------------
    if route != "pdf":
        auto_save_memory(prompt)

    # -----------------------------
    # STREAM RESPONSE
    # -----------------------------
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

        chunk = await loop.run_in_executor(
            None,
            get_next_chunk,
            stream
        )

        if chunk is None:
            break

        content = chunk["message"]["content"]

        yield content