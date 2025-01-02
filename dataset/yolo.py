import os
from PIL import Image

# Function to convert bounding box annotations to YOLO format
def convert_to_yolo_format(image_path, bbox_list, label_dir):
    # Open the image to get its dimensions
    with Image.open(image_path) as img:
        image_width, image_height = img.size  # Get image width and height

    # Initialize an empty list to store YOLO annotations
    yolo_annotations = []

    # Loop through each bounding box
    for bbox in bbox_list:
        xmin, ymin, xmax, ymax = bbox  # Unpack bounding box coordinates

        # Calculate center_x, center_y, width, height (normalized by image dimensions)
        center_x = (xmin + xmax) / 2.0 / image_width
        center_y = (ymin + ymax) / 2.0 / image_height
        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height

        # YOLO format: "class_id center_x center_y width height"
        # Class ID for passport is 0 (since there's only one class)
        yolo_annotations.append(f"0 {center_x} {center_y} {width} {height}")

    # Save annotations to a text file in the labels directory (with same name as the image)
    label_file = os.path.join(label_dir, os.path.basename(image_path).replace(".jpg", ".txt"))
    with open(label_file, "w") as f:
        f.write("\n".join(yolo_annotations))

# Function to process a directory of images and generate corresponding labels
def process_images(image_dir, label_dir, bbox_dict):
    # Ensure the label directory exists
    os.makedirs(label_dir, exist_ok=True)

    # Count for files processed
    processed_files_count = 0

    # Iterate over each image in the directory
    for image_name in os.listdir(image_dir):
        if image_name.endswith(".jpg"):  # Process only JPG images
            image_path = os.path.join(image_dir, image_name)

            # Get the bounding box annotations for the image from the dictionary
            bbox_list = bbox_dict.get(image_name, [])
            if bbox_list:
                # Convert to YOLO format and save the annotation
                print(f"Processing {image_name}...")
                convert_to_yolo_format(image_path, bbox_list, label_dir)
                processed_files_count += 1
            else:
                print(f"No bounding box data for {image_name}")

    return processed_files_count

# Example of bounding boxes (replace with your own data)
bbox_dict = {
    "image1.jpg": [[50, 30, 250, 200], [300, 150, 500, 350]],
    "image2.jpg": [[60, 40, 270, 210], [320, 170, 510, 360]],
    # Add more images and their corresponding bounding boxes here
}

# Directories for images and labels
train_image_dir = r"C:\Users\suvet\Desktop\dataset\yolov5\bio_augmented\images\train"
train_label_dir = r"C:\Users\suvet\Desktop\dataset\yolov5\bio_augmented\labels\train"
val_image_dir = r"C:\Users\suvet\Desktop\dataset\yolov5\bio_augmented\images\val"
val_label_dir = r"C:\Users\suvet\Desktop\dataset\yolov5\bio_augmented\labels\val"

# Process training and validation images
train_processed_count = process_images(train_image_dir, train_label_dir, bbox_dict)
val_processed_count = process_images(val_image_dir, val_label_dir, bbox_dict)

# Final confirmation print statement
print(f"Finished processing:")
print(f"- {train_processed_count} training images processed.")
print(f"- {val_processed_count} validation images processed.")

if train_processed_count == 0 and val_processed_count == 0:
    print("No images were processed. Please check the bounding box data or image files.")
else:
    print("Processing complete. Check the labels directories for .txt files.")
