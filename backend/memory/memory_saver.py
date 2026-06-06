import uuid
from memory.vector_store import save_memory
from memory.memory_classifier import is_important

QUESTION_STARTERS = (
    "what", "who", "where", "when", "why", "how",
    "is", "are", "do", "does", "can", "could", "tell me"
)

def is_question(text: str) -> bool:
    text_lower = text.strip().lower()
    return (
        text_lower.endswith("?") or
        text_lower.startswith(QUESTION_STARTERS)
    )

def auto_save_memory(text):
    # Fix 2: Never save questions
    if is_question(text):
        print(f"[SKIPPED - QUESTION] {text}")
        return

    if not is_important(text):
        print(f"[IGNORED] {text}")
        return

    print(f"[SAVED] {text}")
    save_memory(text, str(uuid.uuid4()))