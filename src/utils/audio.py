import sounddevice as sd
import soundfile as sf
import numpy as np

class AudioHandler:
    @staticmethod
    def record(duration=5, sample_rate=16000):
        """录制音频"""
        print("Recording...")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
        sd.wait()
        return audio.flatten()

    @staticmethod
    def save(audio, filename, sample_rate=16000):
        """保存音频"""
        sf.write(filename, audio, sample_rate)

    @staticmethod
    def play(filename):
        """播放音频"""
        data, sr = sf.read(filename)
        sd.play(data, sr)
        sd.wait()
