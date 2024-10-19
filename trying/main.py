# # Import YOLO from ultralytics
# from ultralytics import YOLO
#
# # Load a YOLOv8 model pre-trained on COCO
# model = YOLO('yolov8n.pt')  # You can choose any YOLOv8 version (yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)
#
# # Train the model on your ataset
# results = model.train(
#     data='./app.yaml',  # Path to the dataset YAML file you created
#     epochs=100,         # Number of epochs for training
#     imgsz=640,          # Image size (default 640, you can change this)
#     batch=16,           # Batch size (adjust based on your system's capacity)
#     workers=4,          # Number of workers for data loading (adjust based on your system)
#     device='cpu'        # Use 'cpu' since you don't have a CUDA-enabled GPU
# )
#
import cv2

# Test displaying a basic color image
image = cv2.imread('train/images/geologic_hazards_mass_wasting_landslides_jpg.rf.44fc1f2aeb9adc149732ef6935552ab3.jpg')  # Use any small image you have
if image is None:
    print("Failed to load image.")
else:
    cv2.imshow('Test Image', image)
    print("Press any key to close the window...")
    cv2.waitKey(0)  # Wait for any key press
    cv2.destroyAllWindows()
