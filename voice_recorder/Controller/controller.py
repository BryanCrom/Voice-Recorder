import customtkinter as ctk

from voice_recorder.Model.record import Recording
from voice_recorder.View.recording_view import RecordingView

class Controller:
    model: Recording
    view: RecordingView

    def __init__(self, app: ctk.CTk):
        self.app = app
        self.model = Recording()
        self.view = RecordingView(self, self.app)
        self.update()

    def start_recording(self):
        self.model.start_recording()

    def stop_recording(self):
        self.model.stop_recording()

    def update(self):
        if self.model.is_recording:
            samples = self.model.get_samples()
            self.view.update_waveform(samples)
        else:
            self.view.reset_waveform()
        self.app.after(30, self.update)

    def get_elapsed_time(self) -> int:
        return self.model.get_elapsed_time()

    def get_audio(self):
        return self.model.get_audio()
