import requests
import os

url = 'https://github.com/ultralytics/assets/releases/download/v8.0.0/yolov8s.pt'
output_path = 'models/yolo/yolov8.pt'

os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Downloading YOLOv8 model...")
response = requests.get(url, stream=True)
with open(output_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
print(f"Model downloaded to {output_path}")
