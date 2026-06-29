import sounddevice as sd
import wavio as wv
import numpy as np

def main():
    freq = 44100
    channels = 1
    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    print("Recording... press Enter to stop.")
    with sd.InputStream(samplerate=freq, channels=channels, callback=callback):
        input()  # blocks here until you hit Enter

    audio = np.concatenate(recording, axis=0)
    wv.write("recording.wav", audio, freq, sampwidth=2)
    print("Saved recording.wav")

if __name__ == "__main__":
    main()


