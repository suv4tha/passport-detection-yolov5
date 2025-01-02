import csv

# Initialize bbox_dict
bbox_dict = {}

# Path to your CSV file
csv_file_path = r"C:\Users\suvet\Desktop\dataset\yolov5\bounding_boxes.csv"

# Read bounding boxes from CSV and populate bbox_dict
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)  # Use DictReader to handle the header row
    for row in reader:
        image_name = row['image_name']
        xmin = int(row['xmin'])
        ymin = int(row['ymin'])
        xmax = int(row['xmax'])
        ymax = int(row['ymax'])

        # Add to bbox_dict (assuming one bounding box per image for simplicity)
        if image_name not in bbox_dict:
            bbox_dict[image_name] = []
        bbox_dict[image_name].append([xmin, ymin, xmax, ymax])

# Print the final dictionary
print("Finished creating bbox_dict:")
print(bbox_dict)
