import sounddevice as sd
import wavio as wv
import numpy as np
import os
from openai import OpenAI


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


def transcribe():
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    audio_file = open("recording.wav", "rb")

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file
    )

    print(transcription.text)


if __name__ == "__main__":
    transcribe()
