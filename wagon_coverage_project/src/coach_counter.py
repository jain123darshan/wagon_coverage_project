import cv2
import numpy as np
from src.utils import calculate_optical_flow, detect_gaps

class CoachCounter:
    def count_coaches(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video {video_path}")

        prev_frame = None
        coach_count = 0
        gap_detected = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if prev_frame is not None:
                flow = calculate_optical_flow(prev_frame, frame)
                gaps = detect_gaps(flow)
                if np.any(gaps) and not gap_detected:
                    coach_count += 1
                    gap_detected = True
                elif not np.any(gaps):
                    gap_detected = False

            prev_frame = frame

        cap.release()
        return coach_count
