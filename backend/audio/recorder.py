import sounddevice as sd
from scipy.io.wavfile import write

def record_audio():

    fs = 44100
    seconds = 15

    print("Recording...")

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1
    )

    sd.wait()

    write(
        "recording.wav",
        fs,
        recording
    )

    print("Saved recording.wav")