from faster_whisper import WhisperModel

class SpeechToText:
    def __init__(self, model_size="tiny", device="cpu", compute_type="int8"):
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe(self, audio_file, language="zh"):
        """将音频转换为文本"""
        segments, _ = self.model.transcribe(audio_file, language=language)
        return " ".join([segment.text for segment in segments])
