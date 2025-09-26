from ..Model.record import Recording
from ..View.recording_view import RecordingView

class Controller:
    model: Recording
    view: RecordingView

    def __init__(self):
        self.model = Recording()
        self.view = RecordingView(self)

        self.callback_line = None
        self.callback_canvas = None
        self.model.callback_line = self.callback_line
        self.model.callback_canvas = self.callback_canvas

    def start_recording(self):
        self.model.start_recording()

    def stop_recording(self):
        self.model.stop_recording()

