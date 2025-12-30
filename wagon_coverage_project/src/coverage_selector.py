import os
import cv2
import numpy as np

class CoverageSelector:
    def select_coverage_frames(self, frames_dir):
        frames = []
        for frame_file in sorted(os.listdir(frames_dir)):
            if frame_file.endswith('.jpg'):
                frames.append(os.path.join(frames_dir, frame_file))

        # Simple selection: select every nth frame for coverage
        n = max(1, len(frames) // 10)  # Select up to 10 frames per coach
        selected = frames[::n]
        return selected
