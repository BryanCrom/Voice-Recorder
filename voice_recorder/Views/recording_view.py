import tkinter as tk
import customtkinter as ctk

class RecordingView:

    def __init__(self, controller):
        # pass in the controller
        self.controller = controller

        # set up themes
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # set up frame
        self.app = ctk.CTk()
        self.app.geometry("400x300")
        self.app.title("Voice Recorder")

        # add record button
        self.record_btn = ctk.CTkButton(self.app, text="RECORD", command=controller.start_recording)
        self.record_btn.pack(pady = 40)

        # start GUI
        self.app.mainloop()