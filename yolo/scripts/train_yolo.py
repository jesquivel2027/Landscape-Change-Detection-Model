from ultralytics import YOLO

# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")  # Replace with "yolov8s.pt" for better accuracy

# Train the YOLO model
model.train(
    data="./yolo/dataset.yaml",  # Path to dataset configuration
    epochs=50,                  # Number of epochs
    imgsz=640,                  # Image size
    batch=16,                   # Batch size
    save=True                   # Save the best model
)