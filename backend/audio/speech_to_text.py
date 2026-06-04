from faster_whisper import WhisperModel

model = WhisperModel(
    "tiny",
    device="cpu"
)

def transcribe():

    segments, _ = model.transcribe(
        "recording.wav"
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text