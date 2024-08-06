import os
from ultralytics import YOLO
from pathlib import Path

# Load a pre-trained YOLOv10x model
model_path = '# Path to the model file'
model = YOLO(model_path)

# Define the directory containing the images and the directory to save the results
image_dir = '# Path to the directory containing the images'
output_dir = '# Path to the directory to save the results'

# Create the output directory if it doesn't exist
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Get the list of image files
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Perform object detection on each image and save the results
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    results = model(image_path)

    # Save the result
    output_path = os.path.join(output_dir, f"{Path(image_file).stem}_pred.jpg")
    results[0].save(output_path)

    # Display the result (optional)
    #results[0].show()
