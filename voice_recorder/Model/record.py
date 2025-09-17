import os
import threading
import numpy as np
import soundfile as sf
import sounddevice as sd

from dataclasses import dataclass, field

@dataclass
class Recording:

    is_recording: bool = False
    recording: list = field(default_factory=list)

    def audio_callback(self, indata, frames, time, status) -> None:
        if self.is_recording:
            self.recording.append(indata.copy())

    def record_thread(self) -> None:
        try:
            with sd.InputStream(samplerate=44100, channels=1, callback=self.audio_callback):
                while self.is_recording:
                    sd.sleep(100)
        except Exception as e:
            print(f"Error: {e}")

    def start_recording(self) -> None:
        if self.is_recording:
            print("Recording is already in progress.")
            return

        self.is_recording = True
        self.recording.clear()
        threading.Thread(target=self.record_thread, daemon=True).start()

    def stop_recording(self) -> None:
        if not self.is_recording:
            print("No recording is in progress.")
            return

        self.is_recording = False
        print("Recording stopped.")

        audio = np.concatenate(self.recording, axis=0)
        self.save_recording(audio)

    def save_recording(self, audio) -> None:
        filename = input("Recording name: ") + ".wav"
        filepath = os.path.join("recordings", filename)
        if os.path.isfile(filepath):
            overwrite = input(f"{filename} already exists. Overwrite? (y/n): ")
            if overwrite.lower() == 'n':
                print("Recording not saved.")
                return
        sf.write(filepath, audio, 44100)
        print(f"Saved Record to {filepath}")