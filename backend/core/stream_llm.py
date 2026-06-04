import ollama
async def stream_ai(prompt, stop_flag: dict):
    import asyncio
    stream = ollama.chat(
        model = "tinyllama",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
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
            
        # Run blocking next() in thread so WebSocket can receive messages
        chunk = await loop.run_in_executor(None, get_next_chunk, stream)
        
        if chunk is None:
            break
            
        content = chunk["message"]["content"]
        yield content