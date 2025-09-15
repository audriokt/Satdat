<<<<<<< HEAD
import os
import re
import subprocess
import whisper

class TranscriptHelper:
    def __init__(self, audio_dir, model_size="base"):
        self.audio_dir = audio_dir
        os.makedirs(audio_dir, exist_ok=True)
        self.model = whisper.load_model(model_size)

    def parse_filename(self, filename):
        match = re.match(r"(\d+)_([a-zA-Z]+)\.mp4", filename)
        return match.groups() if match else (None, None)

    def extract_audio(self, video_path, audio_path):
        command = [
            "ffmpeg", "-y", "-i", video_path,
            "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def transcribe_audio(self, audio_path):
        try:
            result = self.model.transcribe(audio_path)
            return result.get("text", "").strip()
        except Exception as e:
            print(f"❌ Transcription failed: {e}")
=======
import os
import re
import subprocess
import whisper

class TranscriptHelper:
    def __init__(self, audio_dir, model_size="base"):
        self.audio_dir = audio_dir
        os.makedirs(audio_dir, exist_ok=True)
        self.model = whisper.load_model(model_size)

    def parse_filename(self, filename):
        match = re.match(r"(\d+)_([a-zA-Z]+)\.mp4", filename)
        return match.groups() if match else (None, None)

    def extract_audio(self, video_path, audio_path):
        command = [
            "ffmpeg", "-y", "-i", video_path,
            "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def transcribe_audio(self, audio_path):
        try:
            result = self.model.transcribe(audio_path)
            return result.get("text", "").strip()
        except Exception as e:
            print(f"❌ Transcription failed: {e}")
>>>>>>> cf7e4c4243711c8621ae31df9ac4a97d9aadf6cb
            return ""