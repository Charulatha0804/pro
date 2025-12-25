import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration=3600, fs=44100):
    print("Recording started...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("Recording saved.")