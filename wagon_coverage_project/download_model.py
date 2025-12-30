import os
import shutil
from ultralytics import YOLO

output_path = 'models/yolo/yolov8.pt'

os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Downloading YOLOv8 model...")
try:
    # Use yolov8n.pt (nano model) for downloading from Ultralytics hub
    model = YOLO('yolov8n.pt')  # Downloads the model if not present
    # Move the downloaded model to the desired path
    shutil.move('yolov8n.pt', output_path)
    print(f"Model downloaded and saved to {output_path}")
except Exception as e:
    print(f"Error downloading model: {e}")
    print("Please check your internet connection and try again.")
