import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

def record_audio(duration=5, filename="input.mp3", temp_wav="temp.wav"):
    print("Recording... Speak now.")
    fs = 44100  # Sample rate
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(temp_wav, fs, audio)  # Save as WAV

    # Convert to MP3
    sound = AudioSegment.from_wav(temp_wav)
    sound.export(filename, format="mp3")
    os.remove(temp_wav)

    print(f"Recording saved to {filename}")
