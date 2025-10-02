import customtkinter as ctk
import tkinter as tk
import soundfile as sf

from PIL import Image
from tkinter import filedialog



class RecordingView:

    def __init__(self, controller, app) -> None:

        self.app = app

        # set up main app window
        self.width = 600
        self.height = 200

        # pass in the controller
        self.controller = controller

        # set up themes
        ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light")
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # add microphone image
        mic_icon = Image.open("images/microphone.png").convert("RGBA")
        mic_image = ctk.CTkImage(light_image=mic_icon, dark_image=mic_icon, size=(150, 150))

        mic_label = ctk.CTkLabel(master=app, image=mic_image, text="")
        mic_label.pack(pady=20)

        # load play icon
        self.play_icon = Image.open("images/play.png").convert("RGBA")
        self.play_image = ctk.CTkImage(light_image=self.play_icon, dark_image=self.play_icon, size=(40, 40))

        # load stop icon
        self.stop_icon = Image.open("images/stop.png").convert("RGBA")
        self.stop_image = ctk.CTkImage(light_image=self.stop_icon, dark_image=self.stop_icon, size=(40, 40))

        #add timer label
        self.timer_label = ctk.CTkLabel(master=app, text="00:00", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # add record button
        self.record_btn = ctk.CTkButton(master=app, image=self.play_image, text="", width=60, height=60, corner_radius=30, border_width=0, border_color="black", command=self.start_recording)
        self.record_btn.pack()

        # add canvas for waveform
        self.canvas = tk.Canvas(master=app, width=self.width, height=self.height, bg="#ebebeb", highlightthickness=0)
        self.canvas.pack()

        self.line = self.canvas.create_line(0, self.height // 2, self.width, self.height // 2, fill="red")

        self.update_timer()

    def start_recording(self) -> None:
        self.controller.start_recording()
        self.record_btn.configure(image=self.stop_image, command=self.stop_recording)

    def stop_recording(self) -> None:
        self.controller.stop_recording()
        file_path = filedialog.asksaveasfilename(
            title="recording",
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")],
        )

        if file_path:
            audio = self.controller.get_audio()
            sf.write(file_path, audio, 44100)
        else:
            print("Save operation cancelled.")
        self.record_btn.configure(image=self.play_image, command=self.start_recording)

    def update_waveform(self, samples):
        self.canvas.delete(self.line)

        h = self.height // 2
        x_scale = self.width / len(samples)
        points = []
        for i, s in enumerate(samples):
            x = i * x_scale
            y = h - (s * h)
            points.append((x, y))

        flat_points = [coord for xy in points for coord in xy]
        self.line = self.canvas.create_line(flat_points, fill="red")

    def update_timer(self):
        elapsed = self.controller.get_elapsed_time()
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")

        self.app.after(1000, self.update_timer)