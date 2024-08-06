import os
from ultralytics import YOLO

# Define paths
data_yaml_path = '../data.yaml'


# Configuration
conf = {
    'model': 'yolov8x.pt',
    'data': data_yaml_path,
    'epochs': 300,
    'batch_size': 15,
    'img_size': 640,
    'name': 'yolov8x-finetuned'
}

# Create the YOLOv10 model
model = YOLO(conf['model'])

model.train(data=conf['data'], 
            epochs=conf['epochs'], 
            batch=conf['batch_size'], 
            imgsz=conf['img_size'], 
            name = conf['name']
            )

# Save the model
model.save('yolov8x-finetuned.pt')