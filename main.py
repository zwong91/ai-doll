import argparse
import tempfile
import os
from src.core.stt import SpeechToText
from src.core.tts import TextToSpeech
from src.core.llm import LLMClient
from src.utils.audio import AudioHandler
from src.config.config import Config

class VoiceAssistant:
    def __init__(self, config: Config):
        self.config = config
        self.stt = SpeechToText(config.whisper_model, config.whisper_device, config.whisper_compute_type)
        self.tts = TextToSpeech(config.tts_voice)
        self.llm = LLMClient(config.llm_url, config.llm_model)
        self.audio = AudioHandler()

    def process_conversation(self):
        """处理实时对话"""
        audio = self.audio.record(self.config.record_duration, self.config.sample_rate)
        
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_input:
            self.audio.save(audio, temp_input.name, self.config.sample_rate)
            text = self.stt.transcribe(temp_input.name)
            print(f"You said: {text}")

            response = self.llm.get_response(text)
            print(f"AI response: {response}")

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_output:
                self.tts.synthesize(response, temp_output.name)
                self.audio.play(temp_output.name)
                os.unlink(temp_output.name)
            os.unlink(temp_input.name)

    def process_audio_file(self, audio_file_path):
        """处理音频文件"""
        text = self.stt.transcribe(audio_file_path)
        print(f"Audio content: {text}")

        response = self.llm.get_response(text)
        print(f"AI response: {response}")

        output_dir = os.path.dirname(audio_file_path)
        output_file = os.path.join(output_dir, "response.wav")
        self.tts.synthesize(response, output_file)
        print(f"Response saved to: {output_file}")
        self.audio.play(output_file)

def main():
    parser = argparse.ArgumentParser(description='Voice Assistant')
    parser.add_argument('--file', '-f', help='Path to input audio file')
    parser.add_argument('--interactive', '-i', action='store_true', help='Run in interactive mode')
    args = parser.parse_args()

    config = Config()
    assistant = VoiceAssistant(config)

    if args.file:
        assistant.process_audio_file(args.file)
    elif args.interactive:
        while True:
            try:
                assistant.process_conversation()
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error occurred: {e}")
    else:
        print("Please specify either --file or --interactive mode")

if __name__ == "__main__":
    main()
