import cv2
import os
import numpy as np

class ComponentDetector:
    def __init__(self):
        pass  # No model needed for OpenCV contour detection

    def detect_components(self, frames_path, output_path):
        os.makedirs(output_path, exist_ok=True)
        for frame_file in os.listdir(frames_path):
            if frame_file.endswith('.jpg'):
                frame_path = os.path.join(frames_path, frame_file)
                image = cv2.imread(frame_path)
                annotated_image = self.detect_doors_opencv(image)
                output_file = os.path.join(output_path, frame_file)
                cv2.imwrite(output_file, annotated_image)

    def detect_doors_opencv(self, image):
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # Edge detection
        edges = cv2.Canny(blurred, 50, 150)
        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Filter contours that could be doors (rectangular shapes)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Minimum area threshold
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w) / h
                if 0.5 < aspect_ratio < 2.0:  # Aspect ratio for doors
                    # Draw bounding box
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Label as door
                    cv2.putText(image, 'Door', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return image
