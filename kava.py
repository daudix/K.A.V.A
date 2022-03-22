#!/usr/bin/python
import pyaudio
import numpy as np
import subprocess

# Select mode

print("\n[Select mode:] \n\nLight: Set keyboard brightness to 50% & visualising louder sounds\n\nDark: Keyboard is off until microphone will hear sounds\n")
modeselect = input("(l)ight or (d)ark: ")

# Number of data points to read at a time
CHUNK = 2**10

# Time seolution of the recording device (Hz)
RATE = 44100

# Start the PyAudio class
p=pyaudio.PyAudio()

# Uses the default input device
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)


while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2

    v = int(100*peak/2**10)

    # Just printing the value of v to improve this piece of shi... code

    print(v)


    # Light

    if modeselect == "l":
        subprocess.run(f"kbdlight set {v}", shell=True)

    # Dark (Future feature)

    if modeselect == "d":
        subprocess.run(f"kbdlight set {v}", shell=True)

stream.stop_stream()
stream.close()
p.terminate()
