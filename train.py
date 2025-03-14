from ultralytics import YOLO

model = YOLO("yolov8n.pt") # pass any model type
model.train(epochs=5)
