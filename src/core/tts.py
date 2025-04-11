import subprocess

class TextToSpeech:
    def __init__(self, voice="zh"):
        self.voice = voice

    def synthesize(self, text, output_file):
        """将文本转换为语音"""
        subprocess.run(["espeak-ng", "-v", self.voice, "-w", output_file, text])
