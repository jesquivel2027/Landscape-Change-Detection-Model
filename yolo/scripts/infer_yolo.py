from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("./yolo/models/best.pt")  # Replace with your trained weights

# Perform inference on test images
results = model.predict(
    source="./data/test/images",  # Path to test images
    save=True,                    # Save predictions
    conf=0.5                      # Confidence threshold
)

# Print results
print(results)