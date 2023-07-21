import numpy as np
import librosa
import matplotlib.pyplot as plt

# Define a function to plot the waveform
def plot_waveform(audio, title):
    plt.figure(figsize=(14, 5))
    plt.plot(audio)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

# Load the original audio
PATH = "data/pigeons-flying-6351.mp3" 
original_audio, sample_rate = librosa.load(PATH)

# Plot the audio waveform
plot_waveform(original_audio, "Waveform of Original Audio")

# Reduce the aduio speed
speed_factor = 0.5
augmented_audio = librosa.effects.time_stretch(original_audio, rate = speed_factor)

# Plot the augment audio waveform
plot_waveform(augmented_audio, "Waveform of Augmented Audio")

# Play the audio
from IPython.display import Audio
Audio(data=augmented_audio, rate=sample_rate)