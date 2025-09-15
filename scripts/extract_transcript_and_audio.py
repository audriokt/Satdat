<<<<<<< HEAD
"""
This script processes video files to trancript their audio content and saves the results in a CSV file in the following 
format: id, label, transcript in the transcripts directory.
this script also exctrt audio from video files and saves them in the audios directory.
It uses a helper class TranscriptHelper to handle audio extraction and transcription.

"""

import os
import csv
from helpers.transcript_helper import TranscriptHelper

# === Konfigurasi Path ===
VIDEO_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos"
AUDIO_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\audios"
TRANSCRIPT_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\transcripts"
CSV_OUTPUT = os.path.join(TRANSCRIPT_DIR, "video_transcripts.csv")

# === Inisialisasi Helper ===
helper = TranscriptHelper(audio_dir=AUDIO_DIR)

def process_videos():
    os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
    results = []

    for filename in os.listdir(VIDEO_DIR):
        if not filename.endswith(".mp4"):
            continue

        video_path = os.path.join(VIDEO_DIR, filename)
        id_, label = helper.parse_filename(filename)
        if not id_ or not label:
            print(f"Skipping file: {filename}")
            continue

        audio_path = os.path.join(AUDIO_DIR, f"{id_}.wav")
        helper.extract_audio(video_path, audio_path)
        transcript = helper.transcribe_audio(audio_path)

        results.append({"id": id_, "label": label, "transcript": transcript})
        print(f"✅ {filename} → Transcript length: {len(transcript)}")

    with open(CSV_OUTPUT, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "label", "transcript"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n📄 Transkrip selesai → {CSV_OUTPUT}")

if __name__ == "__main__":
=======
"""
This script processes video files to trancript their audio content and saves the results in a CSV file in the following 
format: id, label, transcript in the transcripts directory.
this script also exctrt audio from video files and saves them in the audios directory.
It uses a helper class TranscriptHelper to handle audio extraction and transcription.

"""

import os
import csv
from helpers.transcript_helper import TranscriptHelper

# === Konfigurasi Path ===
VIDEO_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos"
AUDIO_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\audios"
TRANSCRIPT_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\transcripts"
CSV_OUTPUT = os.path.join(TRANSCRIPT_DIR, "video_transcripts.csv")

# === Inisialisasi Helper ===
helper = TranscriptHelper(audio_dir=AUDIO_DIR)

def process_videos():
    os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
    results = []

    for filename in os.listdir(VIDEO_DIR):
        if not filename.endswith(".mp4"):
            continue

        video_path = os.path.join(VIDEO_DIR, filename)
        id_, label = helper.parse_filename(filename)
        if not id_ or not label:
            print(f"Skipping file: {filename}")
            continue

        audio_path = os.path.join(AUDIO_DIR, f"{id_}.wav")
        helper.extract_audio(video_path, audio_path)
        transcript = helper.transcribe_audio(audio_path)

        results.append({"id": id_, "label": label, "transcript": transcript})
        print(f"✅ {filename} → Transcript length: {len(transcript)}")

    with open(CSV_OUTPUT, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "label", "transcript"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n📄 Transkrip selesai → {CSV_OUTPUT}")

if __name__ == "__main__":
>>>>>>> cf7e4c4243711c8621ae31df9ac4a97d9aadf6cb
    process_videos()