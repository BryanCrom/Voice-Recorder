import time
import threading
import numpy as np
import sounddevice as sd

from dataclasses import dataclass, field

@dataclass
class Recording:

    blocksize: int = 1024
    audio_buffer: np.ndarray = field(default_factory=lambda: np.zeros(1024))
    is_recording: bool = False
    recording: list = field(default_factory=list)
    audio = None
    start_timestamp = None
    elapsed_time = 0

    def audio_callback(self, indata, frames, time, status) -> None:
        if status:
            print(status)
        self.audio_buffer[:] = indata[:, 0]
        if self.is_recording:
            self.recording.append(indata.copy())

    def record_thread(self) -> None:
        try:
            with sd.InputStream(samplerate=44100, channels=1, blocksize=self.blocksize, callback=self.audio_callback):
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
        self.start_timestamp = time.time()
        self.elapsed_time = 0
        self.audio_buffer[:] = 0
        threading.Thread(target=self.record_thread, daemon=True).start()

    def stop_recording(self) -> None:
        if not self.is_recording:
            print("No recording is in progress.")
            return

        self.is_recording = False
        print("Recording stopped.")
        if self.start_timestamp:
            self.elapsed_time = int(time.time() - self.start_timestamp)
            self.start_timestamp = None

        audio = np.concatenate(self.recording, axis=0)
        self.audio = audio

    def get_samples(self):
        return self.audio_buffer

    def update_timer(self):
        if self.is_recording and self.start_timestamp:
            self.elapsed_time = int(time.time() - self.start_timestamp)
        else:
            self.elapsed_time = 0

    def get_elapsed_time(self) -> int:
        self.update_timer()
        return self.elapsed_time

    def get_audio(self):
        return self.audio
