# passport-detection-yolov5
A YOLOv5-based model for detecting and localizing passports in images. Trained on a custom dataset with augmented images, it achieves high accuracy under varying angles, lighting, and backgrounds. Ideal for automated document verification and identity management
# Passport Detection with YOLOv5

This repository contains a project that focuses on **Passport Detection** using the YOLOv5 object detection framework. The goal is to identify passports in images and classify them accurately. This project uses a custom dataset of passport images for training and testing.

---

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [License](#license)

---

## Overview

This project utilizes the YOLOv5 framework to detect passports in images. YOLOv5 is a popular object detection model that provides fast and accurate results. The model has been trained on a custom dataset and fine-tuned to perform well on passport detection tasks.

---

## Installation

To get started with the project, clone the repository and install the necessary dependencies:

git clone https://github.com/suv4tha/passport-detection-yolov5.git
cd passport-detection-yolov5
Then, install the required Python packages:

pip install -r requirements.txt

Usage
Once the setup is complete, you can start using the model for inference or training. Here’s how you can run the detection on a sample image:

Detection
Ensure you have a trained model or weights in the weights/ directory.
Run the detection script:
bash
Copy code
python detect.py --weights path_to_weights --source path_to_image
Replace path_to_weights with the location of your trained model weights and path_to_image with the image you want to process.

Training
To train the model on your own dataset, run the following command:

bash
Copy code
python train.py --data data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --batch-size 16 --epochs 100
This will start training the model on your dataset, which is specified in data.yaml.

Dataset
The dataset used in this project consists of images of passports collected from various sources. You can customize the dataset by replacing the current dataset with your own images.

Model Training
To train the model, you can adjust the hyperparameters such as batch size, learning rate, and the number of epochs. The training process is automated and will generate model weights that can be used for inference.

You can monitor the training process using the built-in logger to track metrics like loss, precision, recall, and mAP.

Results
Once the model is trained, you can visualize the detection results by running the detection script with any test image or video.
License
MIT License

Copyright (c) 2025 suv4tha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
