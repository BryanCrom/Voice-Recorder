import customtkinter as ctk

from .Controller.controller import Controller

app = ctk.CTk()
app.geometry("500x500")
app.title("Voice Recorder")
app.resizable(False, False)

Controller(app)

# start GUI
app.mainloop()