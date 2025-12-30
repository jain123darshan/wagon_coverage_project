import cv2
import os

class FrameExtractor:
    def extract_frames(self, video_path, output_dir):
        frames_dir = os.path.join(output_dir, 'frames')
        os.makedirs(frames_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video {video_path}")

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_filename = f"{os.path.basename(video_path).split('.')[0]}_{frame_count}.jpg"
            frame_path = os.path.join(frames_dir, frame_filename)
            cv2.imwrite(frame_path, frame)
            frame_count += 1

        cap.release()
        print(f"Extracted {frame_count} frames from {video_path}")
