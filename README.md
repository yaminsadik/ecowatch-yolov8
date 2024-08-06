## Project Overview

This project involves training and fine-tuning a custom object detection model using YOLOv8. The primary goal is to detect illegal dumping, garbage, litter, and other waste-related items from drone footage. The project aims to support sustainable waste management practices by providing an efficient and accurate tool for identifying and managing illegal dumping sites.

## Features
* Custom Object Detection: Train models to detect specific objects relevant to your application.
* Fine-tuned Model: Utilize a YOLOv8{n/s/m/l/x} pre-trained model and fine-tune it with your custom data.
* Versatile Applications: Suitable for a wide range of use cases, including drone footage analysis, security systems, and industrial automation.


## Installation and Setup

1. Clone the repository:
    git clone https://github.com/yaminsadik/ecowatch-yolov8.git

    cd ecowatch-yolov8
    

2. Install the required dependencies:
    pip install -r requirements.txt
    

### Dataset Preparation

To prepare your dataset for training with the YOLOv8 model, organize your data into a structured directory format. A new directory named `datasets` should be created in the root directory, containing three subdirectories: `train`, `valid`, and `test`. Each of these subdirectories should further contain two subdirectories: `images` and `labels`. 

- The `train` directory will hold your training data, with images placed inside the `images` folder and their corresponding annotation files inside the `labels` folder.
- The `valid` directory is for your validation data, structured similarly with images and labels in their respective subdirectories.
- The `test` directory contains your test data, also organized into `images` and `labels` subdirectories.

Each annotation file should correspond to an image file and contain the bounding box coordinates and class labels in YOLO format. This structure ensures that your data is organized for efficient training, validation, and testing, allowing the model to learn effectively and evaluate its performance accurately.


Set up the dataset structure as shown above and update `data.yaml` accordingly.

## Training the Model

To train the model, run the `train.py` script located in the `src` directory.

## Predicting on Images

To perform object detection on a set of images, use the `predict.py` script in the `src` directory.

## Predicting on Videos

To perform object detection on a video, use the `video_pred.py` script in the `src` directory. 

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

