import cv2
import os
import numpy as np

class ColorValidator:
    def validate_colors(self, frames_dir):
        colors = []
        for frame_file in os.listdir(frames_dir):
            if frame_file.endswith('.jpg'):
                frame_path = os.path.join(frames_dir, frame_file)
                image = cv2.imread(frame_path)
                # Extract dominant color (simple average)
                avg_color = np.mean(image, axis=(0, 1))
                colors.append(avg_color)

        # Check consistency (simple std dev check)
        if len(colors) > 1:
            color_std = np.std(colors, axis=0)
            if np.any(color_std > 50):  # Threshold for inconsistency
                print(f"Color inconsistency detected in {frames_dir}")
            else:
                print(f"Colors are consistent in {frames_dir}")
        else:
            print(f"Only one frame in {frames_dir}, skipping color validation")
