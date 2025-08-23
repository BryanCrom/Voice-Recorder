from dataclasses import dataclass, field
from scipy.io.wavfile import write

import sounddevice as sd
import os

@dataclass
class Recording:
    fs: int
    duration: int

    filename: str = "untitled.wav"
    folder: str = "recordings"

    def record_audio(self) -> None:
        print(f"Recording for {self.duration} seconds...")
        audio = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        self.save_recording(audio)

    def save_recording(self, audio) -> None:
        self.filename = input("Recording name: ") + ".wav"
        filepath = os.path.join(self.folder, self.filename)
        if os.path.isfile(filepath):
            overwrite = input(f"{self.filename} already exists. Overwrite? (y/n): ")
            if overwrite.lower() == 'n':
                print("Recording not saved.")
                return
        write(filepath, self.fs, audio)
        print(f"Saved Record to {filepath}")

@dataclass
class Recorder:
    recordings : list[Recording] = field(default_factory=list)
    folder: str = "recordings"

    def __post_init__(self) -> None:
        os.makedirs(self.folder, exist_ok=True)
        print(f"Recorder initialized. Recordings will be saved in {self.folder}")

    def new_recording(self) -> None:
        recording = Recording(fs=44100, duration=5)
        recording.record_audio()
        self.recordings.append(recording)


# testing
if __name__ == "__main__":
    rec = Recorder()
    rec.new_recording()