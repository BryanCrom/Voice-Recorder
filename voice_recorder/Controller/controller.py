from ..Model.record import Recording
from ..View.recording_view import RecordingView

class Controller:
    model: Recording
    view: RecordingView

    def __init__(self):
        self.model = Recording()
        self.view = RecordingView(self)

    def start_recording(self):
        self.model.start_recording()

    def stop_recording(self):
        self.model.stop_recording()