"""
extract frames from video files and save them as images in a frames directory.
format of saved images: video_name_frameXXXX.jpg
images that extracted only extract frames with faces in them.

mtcnn is used to detect faces in the frames.
opencv is used to read video files and extract frames.
the purpose of this script is to create dataset for training emotion recognition model.

"""
import os
import cv2
import numpy as np
from datetime import timedelta
from mtcnn import MTCNN
from deepface import DeepFace  # or replace with your own classifier

# === CONFIG ===
VIDEO_FOLDER = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos"
OUTPUT_ROOT = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\frames"
FRAME_INTERVAL = 3  # seconds

detector = MTCNN()

def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frame_times(cap, interval):
    duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    return np.arange(0, duration, interval)

def classify_emotion(face_img):
    try:
        result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except Exception:
        return "unknown"

def extract_faces_and_emotions(video_path, output_root, interval):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamps = get_saving_frame_times(cap, interval)

    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        current_time = frame_id / fps
        if timestamps.size > 0 and current_time >= timestamps[0]:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = detector.detect_faces(rgb_frame)
            for i, face in enumerate(faces):
                if face['confidence'] < 0.95:
                    continue
                x, y, w, h = face['box']
                face_crop = rgb_frame[y:y+h, x:x+w]
                emotion = classify_emotion(face_crop)
                save_dir = os.path.join(output_root, emotion)
                os.makedirs(save_dir, exist_ok=True)
                time_str = format_timedelta(timedelta(seconds=current_time))
                filename = f"{video_name}_{time_str}_face{i}.jpg"
                cv2.imwrite(os.path.join(save_dir, filename), cv2.cvtColor(face_crop, cv2.COLOR_RGB2BGR))
            timestamps = timestamps[1:]
        frame_id += 1
    cap.release()
    print(f"[✓] Processed {video_name}")

def process_video_folder(video_folder, output_root, interval):
    os.makedirs(output_root, exist_ok=True)
    for file in os.listdir(video_folder):
        if file.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            video_path = os.path.join(video_folder, file)
            extract_faces_and_emotions(video_path, output_root, interval)

if __name__ == "__main__":
    process_video_folder(VIDEO_FOLDER, OUTPUT_ROOT, FRAME_INTERVAL)