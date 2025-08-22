from typing import List
from dataclasses import dataclass, field

import sounddevice as sd
from scipy.io.wavfile import write
import os

@dataclass
class Recording:
    fs: int  # Sampling frequency
    duration: int

    filename: str = "untitled.wav"
    folder: str = "recordings"

    def record_audio(self) -> None:
        print(f"Recording for {self.duration} seconds...")
        recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        self.filename = input("Recording name: ") + ".wav"
        filepath = os.path.join(self.folder, self.filename)
        if os.path.isfile(filepath):
            overwrite = input(f"{self.filename} already exists. Overwrite? (y/n): ")
            if overwrite.lower() == 'n':
                print("Recording not saved.")
                return
            elif overwrite.lower() == 'y':
                write(filepath, self.fs, recording)
                print(f"Saved recording to {filepath}")

@dataclass
class Recorder:
    recordings : List[Recording] = field(default_factory=List)
    folder: str = "recordings"

    def __post_init__(self) -> None:
        os.makedirs(self.folder, exist_ok=True)
        print(f"Recorder initialized. Recordings will be saved in {self.folder}")



if __name__ == "__main__":
    rec = Recording(fs=44100, duration=5)
    rec.record_audio()
    print("Recording completed.")