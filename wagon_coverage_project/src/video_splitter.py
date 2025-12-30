import cv2
import os
import numpy as np
from src.utils import calculate_optical_flow, detect_gaps, segment_coaches

class VideoSplitter:
    def __init__(self, video_path, output_dir, train_number):
        self.video_path = video_path
        self.output_dir = output_dir
        self.train_number = train_number

    def split_video(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video {self.video_path}")

        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        coaches = segment_coaches(self.video_path)
        coach_videos = []

        for i, (start_frame, end_frame) in enumerate(coaches):
            coach_dir = os.path.join(self.output_dir, f"{self.train_number}_{i+1}")
            os.makedirs(coach_dir, exist_ok=True)
            coach_video_path = os.path.join(coach_dir, f"{self.train_number}_{i+1}.mp4")

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(coach_video_path, fourcc, fps, (width, height))

            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            for frame_num in range(start_frame, end_frame):
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

            out.release()
            coach_videos.append(coach_video_path)

        cap.release()
        return coach_videos
