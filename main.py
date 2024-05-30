import tkinter as tk
from tkinter import ttk
import pyttsx3

speech_engine = pyttsx3.init()

voices = speech_engine.getProperty('voices')
voice_options = {voice.name: voice.id for voice in voices}

def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    volume = volume_slider.get() / 100
    rate = rate_slider.get()
    voice_name = voice_combo.get()
    speech_engine.setProperty('volume', volume)
    speech_engine.setProperty('rate', rate)
    speech_engine.setProperty('voice', voice_options[voice_name])
    speech_engine.say(text)
    speech_engine.runAndWait()
    print("Your Text:", text)
    print("Volume Level:", volume)
    print("Rate of Speech:", rate)
    print("Voice:", voice_name)

root = tk.Tk()
root.title("Text to Speech")

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(pady=5)

volume_label = tk.Label(root, text="Volume")
volume_label.pack()
volume_slider = ttk.Scale(root, from_=0, to=100, orient='horizontal')
volume_slider.set(100)
volume_slider.pack(pady=5)

rate_label = tk.Label(root, text="Rate of Speech (Words per Minute)")
rate_label.pack()
rate_slider = ttk.Scale(root, from_=50, to=300, orient='horizontal')
rate_slider.set(200)
rate_slider.pack(pady=5)

voice_label = tk.Label(root, text="Voice")
voice_label.pack()
voice_combo = ttk.Combobox(root, values=list(voice_options.keys()))
voice_combo.set(list(voice_options.keys())[0])
voice_combo.pack(pady=5)

root.mainloop()
