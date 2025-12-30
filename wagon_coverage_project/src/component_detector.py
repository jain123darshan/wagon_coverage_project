import cv2
import os
import numpy as np
from ultralytics import YOLO

class ComponentDetector:
    def __init__(self):
        # Load YOLOv8 model directly from ultralytics hub
        self.model = YOLO('yolov8n.pt')  # Use nano model for better performance

    def detect_components(self, frames_path, output_path):
        os.makedirs(output_path, exist_ok=True)
        for frame_file in os.listdir(frames_path):
            if frame_file.endswith('.jpg'):
                frame_path = os.path.join(frames_path, frame_file)
                image = cv2.imread(frame_path)
                annotated_image = self.detect_components_yolo(image)
                output_file = os.path.join(output_path, frame_file)
                cv2.imwrite(output_file, annotated_image)

    def detect_components_yolo(self, image):
        # Run YOLOv8 inference
        results = self.model(image)

        # Process results
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Get class and confidence
                    cls = int(box.cls.item())
                    conf = box.conf.item()
                    class_name = self.model.names[cls]

                    # Draw bounding box
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Label with class name and confidence
                    label = f"{class_name}: {conf:.2f}"
                    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image
