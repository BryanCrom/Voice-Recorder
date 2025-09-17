import customtkinter as ctk
from PIL import Image

class RecordingView:

    def __init__(self, controller) -> None:
        # pass in the controller
        self.controller = controller
        self.initialise_view()

    def initialise_view(self) -> None:
        # set up themes
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # set up frame
        app = ctk.CTk()
        app.geometry("500x500")
        app.title("Voice Recorder")

        # add microphone image
        mic_icon = Image.open("images/microphone.png").convert("RGBA")
        image = ctk.CTkImage(light_image=mic_icon, dark_image=mic_icon, size=(150, 150))

        mic_image = ctk.CTkLabel(master=app, image=image, text="")
        mic_image.pack(pady=40)

        # add record button
        record_btn = ctk.CTkButton(master=app, text="RECORD", command=self.controller.start_recording)
        record_btn.pack(pady=40)

        # add stop record button
        stop_btn = ctk.CTkButton(master=app, text="STOP", command=self.controller.stop_recording)
        stop_btn.pack(pady=40)

        # start GUI
        app.mainloop()