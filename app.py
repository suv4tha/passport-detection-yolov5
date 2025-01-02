import torch
import gradio as gr
from PIL import Image
import numpy as np

# Specify the path to your locally saved trained model
model_path = 'runs/train/exp/weights/best.pt'  # Adjust this path as per your model's location

# Load the model from the local path
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)  # Load the custom model

# Define the function to make predictions
def predict(image):
    # Convert input image to PIL and numpy array format if necessary
    img = np.array(image)

    # Perform inference using the model
    results = model(img)  # Model predicts the objects in the image

    # Extract the bounding boxes, labels, and confidences
    results.render()  # Render the results (draw bounding boxes on the image)

    # Return the image with predictions and any other useful information (like labels and confidence)
    return Image.fromarray(results.imgs[0])  # Returning the image with detected passports

# Create a Gradio interface
iface = gr.Interface(
    fn=predict,  # Function to call when the user uploads an image
    inputs=gr.Image(type="pil"),  # The input is an image in PIL format
    outputs=gr.Image(type="pil"),  # Output will be an image (with bounding boxes drawn)
    title="Passport Detection",  # Title of the interface
    description="<h2>Passport Detection Model</h2><p>Upload an image to detect and localize passports in it. This uses a YOLOv5 model trained on a custom passport dataset.</p><p style='text-align: center; font-size: 14px; color: #888;'>Built by Suvetha Oudearadjou</p>",  # Description with footer
    theme="huggingface",  # Use Huggingface theme for a sleek, colorful interface
    allow_flagging="never",  # Disable the flagging option
    live=True  # Optional: Update results live as the user uploads images
)

# Launch the interface
iface.launch()
