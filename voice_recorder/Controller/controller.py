from ..Model.record import Recorder
from ..View.recording_view import RecordingView

class Controller:
    model: Recorder
    view: RecordingView

    def __init__(self):
        self.model = Recorder()
        self.view = RecordingView(self)

    def start_recording(self):
        self.model.new_recording()