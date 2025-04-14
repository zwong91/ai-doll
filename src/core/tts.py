import subprocess
import os

class TextToSpeech:
    def __init__(self, 
                 backend="espeak",  # 'espeak' 或 'piper'
                 voice="zh+f5",
                 speed=150,    
                 pitch=45,     
                 volume=150,   
                 word_gap=3,
                 piper_model="en_US-lessac-medium.onnx"):
        self.backend = backend
        self.voice = voice
        self.speed = speed
        self.pitch = pitch
        self.volume = volume
        self.word_gap = word_gap
        self.piper_model = piper_model

    def synthesize(self, text, output_file):
        """将文本转换为语音"""
        if self.backend == "espeak":
            self._synthesize_espeak(text, output_file)
        else:
            self._synthesize_piper(text, output_file)

    def _synthesize_espeak(self, text, output_file):
        subprocess.run([
            "espeak-ng",
            "-v", self.voice,
            "-s", str(self.speed),
            "-p", str(self.pitch),
            "-a", str(self.volume),
            "-g", str(self.word_gap),
            "-w", output_file,
            text
        ])

    def _synthesize_piper(self, text, output_file):
        process = subprocess.Popen(
            ["piper", "--model", self.piper_model, "--output_file", output_file],
            stdin=subprocess.PIPE,
            text=True
        )
        process.communicate(input=text)