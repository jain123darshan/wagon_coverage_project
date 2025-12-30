import cv2
from ultralytics import YOLO

def test_yolo_model():
    # Load the model
    model_path = 'models/yolo/yolov8.pt'
    model = YOLO(model_path)

    # Load a sample image
    sample_image_path = 'data/coaches/12309_2/frames/12309_2_0.jpg'
    image = cv2.imread(sample_image_path)

    if image is None:
        print(f"Could not load image from {sample_image_path}")
        return

    print("Running inference on sample image...")

    # Run inference
    results = model(image)

    # Print results
    print("Detection results:")
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                cls = int(box.cls.item())
                conf = box.conf.item()
                class_name = model.names[cls]
                print(f"Detected: {class_name} with confidence {conf:.2f}")

    print("Model test completed successfully!")

if __name__ == "__main__":
    test_yolo_model()
