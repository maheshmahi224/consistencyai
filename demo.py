import pygame
import numpy as np
import tkinter as tk

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2)

# Function to generate and play sound
def play_sound(frequency):
    sample_rate = 44100
    duration = 0.5  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Generate sine wave sound
    wave = (4096 * np.sin(2 * np.pi * frequency * t)).astype(np.int16)
    
    # Convert to 2D array for stereo output
    stereo_wave = np.column_stack((wave, wave))  
    
    sound = pygame.sndarray.make_sound(stereo_wave)
    sound.play()

# Define piano keys and their frequencies
keys = {
    'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13,
    'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392.00,
    'G#': 415.30, 'A': 440.00, 'A#': 466.16, 'B': 493.88,
    'C2': 523.25
}

# Create the main window
root = tk.Tk()
root.title("🎹 Virtual Piano")

# Styling for white and black keys
white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C2']
black_keys = ['C#', 'D#', 'F#', 'G#', 'A#']

# Create piano keys
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Add white keys
for note in white_keys:
    btn = tk.Button(frame, text=note, width=6, height=3, bg="white", fg="black",
                    command=lambda f=keys[note]: play_sound(f))
    btn.pack(side=tk.LEFT)

# Add black keys (positioned above white keys)
for note in black_keys:
    btn = tk.Button(frame, text=note, width=4, height=2, bg="black", fg="white",
                    command=lambda f=keys[note]: play_sound(f))
    btn.place(in_=frame, relx=(white_keys.index(note[0]) + 0.7) / len(white_keys), rely=0.2)

root.mainloop()
