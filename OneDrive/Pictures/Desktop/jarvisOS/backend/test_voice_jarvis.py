from audio.recorder import record_audio
from audio.speech_to_text import transcribe
from audio.speak import speak
record_audio()
question = transcribe()
print("You said:", question)
speak(f"You said {question}")