import customtkinter as ctk

from PIL import Image



class RecordingView:

    def __init__(self, controller) -> None:
        # pass in the controller
        self.controller = controller

        # set up themes
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # set up frame
        app = ctk.CTk()
        app.geometry("500x500")
        app.title("Voice Recorder")

        # add microphone image
        mic_icon = Image.open("images/microphone.png").convert("RGBA")
        mic_image = ctk.CTkImage(light_image=mic_icon, dark_image=mic_icon, size=(150, 150))

        mic_label = ctk.CTkLabel(master=app, image=mic_image, text="")
        mic_label.pack(pady=40)

        # load play icon
        self.play_icon = Image.open("images/play.png").convert("RGBA")
        self.play_image = ctk.CTkImage(light_image=self.play_icon, dark_image=self.play_icon, size=(40, 40))

        # load stop icon
        self.stop_icon = Image.open("images/stop.png").convert("RGBA")
        self.stop_image = ctk.CTkImage(light_image=self.stop_icon, dark_image=self.stop_icon, size=(40, 40))

        # add record button
        self.record_btn = ctk.CTkButton(master=app, image=self.play_image, text="", width=60, height=60, corner_radius=30, border_width=0, border_color="black", command=self.start_recording)
        self.record_btn.pack()

        # start GUI
        app.mainloop()

    def start_recording(self) -> None:
        self.controller.start_recording()
        self.record_btn.configure(image=self.stop_image, command=self.stop_recording)

    def stop_recording(self) -> None:
        self.controller.stop_recording()
        self.record_btn.configure(image=self.play_image, command=self.start_recording)