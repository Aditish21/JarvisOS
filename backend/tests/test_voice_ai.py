from audio.recorder import record_audio
from audio.speech_to_text import transcribe
from audio.speak import speak

from core.local_llm import askai


record_audio()

question = transcribe()

print("You Said:", question)

response = askai(question)

print("JarvisOS:", response)

speak(response)