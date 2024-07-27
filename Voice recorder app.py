import tkinter as tk
from tkinter import messagebox, Toplevel
import pyaudio
import threading
import time

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")
        self.root.configure(bg='#050f28')
        self.root.geometry("500x500")

        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.filename_base = "recorded_audio"
        self.counter = 1
        self.frames = []

        self.is_recording = False
        self.is_paused = False
        self.is_gif_running = True
        self.elapsed_time = 0
        self.pause_start_time = 0

        self.p = pyaudio.PyAudio()

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Press the button to start recording:", bg='#050f28', fg='white', font=("Helvetica", 16))
        self.info_label.pack(pady=20)

        self.mic_button = tk.Button(self.root, text="Start", command=self.start_recording, bg='#8DECB4', fg='black', font=("Helvetica", 16), width=12, height=2, borderwidth=0)
        self.mic_button.pack(pady=20)
        self.mic_button.config(relief="groove", borderwidth=2)

        self.status_label = tk.Label(self.root, text="", bg='#050f28', fg='white', font=("Helvetica", 14))
        self.status_label.pack(pady=20)

        self.show_recordings_button = tk.Button(self.root, text="Show Recordings", command=self.show_recordings, bg='orange', font=("Helvetica", 14))
        self.show_recordings_button.pack(pady=20)

    def start_recording(self):
        self.is_recording = True
        self.is_paused = False
        self.is_gif_running = True
        self.mic_button.config(bg='#15F5BA', text="Recording", state=tk.DISABLED)
        self.status_label.config(text="Recording...")

        self.start_time = time.time()
        self.elapsed_time = 0
        self.frames = []
        threading.Thread(target=self.record_audio).start()

        self.control_window = Toplevel(self.root)
        self.control_window.title("Recording Controls")
        self.control_window.geometry("400x300")
        self.control_window.configure(bg='#050f28')

        self.pause_resume_button = tk.Button(self.control_window, text="Pause Recording", command=self.toggle_pause_resume, bg='#37B7C3', font=("Helvetica", 14))
        self.pause_resume_button.pack(pady=20)

        self.stop_button = tk.Button(self.control_window, text="Stop Recording", command=self.stop_recording, bg='red', font=("Helvetica", 14))
        self.stop_button.pack(pady=20)

        self.timer_label = tk.Label(self.control_window, text="Timer: 0 seconds", bg='#050f28', fg='white', font=("Helvetica", 16))
        self.timer_label.pack(pady=20)

        self.update_timer()

        # Load and display the GIF
        self.display_gif()

    def display_gif(self):
        gif_path = "gif.gif"
        self.gif_image = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.gif_image)]

        self.gif_label = tk.Label(self.control_window, bg='#050f28')
        self.gif_label.pack(pady=10)
        self.update_gif(0)

    def update_gif(self, frame_index):
        if self.is_gif_running:
            frame = self.gif_frames[frame_index]
            self.gif_label.config(image=frame)
            frame_index = (frame_index + 1) % len(self.gif_frames)
        self.control_window.after(100, self.update_gif, frame_index)

    def stop_recording(self):
        self.is_recording = False
        self.is_paused = False
        self.is_gif_running = False
        self.mic_button.config(bg='#8DECB4', text="Start", state=tk.NORMAL)
        self.status_label.config(text="Recording stopped.")

        # Save recorded frames to a WAV file
        if self.frames:
            filename = f"{self.filename_base}_{self.counter}.wav"
            wf = wave.open(filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            self.counter += 1

        # Clean
