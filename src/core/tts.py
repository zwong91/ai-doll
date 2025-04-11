import subprocess

class TextToSpeech:
    def __init__(self, 
                 voice="zh+f5",
                 speed=130,    # 语速
                 pitch=55,     # 音高
                 volume=150,   # 音量
                 word_gap=3):  # 单词间隙
        self.voice = voice
        self.speed = speed
        self.pitch = pitch
        self.volume = volume
        self.word_gap = word_gap

    def synthesize(self, text, output_file):
        """将文本转换为语音"""
        subprocess.run([
            "espeak-ng",
            "-v", self.voice,   # 声音
            "-s", str(self.speed),    # 语速
            "-p", str(self.pitch),    # 音高
            "-a", str(self.volume),   # 音量
            "-g", str(self.word_gap), # 单词间隙
            "-w", output_file,
            text
        ])