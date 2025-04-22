# Records audio from microphone and saves it to a file

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import os
from datetime import datetime

fs = 16000  # Sample rate
recording = []
is_recording = True

def record_callback(indata, frames, time, status):
    if status:
        print(status)
    if is_recording:
        recording.append(indata.copy())

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"data/conversation_{timestamp}.wav"

stream = sd.InputStream(samplerate=fs, channels=1, callback=record_callback)

print("Recording... Press ENTER to stop.")
stream.start()

input()
is_recording = False
stream.stop()
stream.close()

# Combine and save
audio_data = np.concatenate(recording, axis=0)
write(filename, fs, audio_data)
print(f"Recording stopped.")
print(f"Audio saved to {filename}.")

