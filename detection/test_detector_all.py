from ultralytics import YOLO
import cv2
import os
from pathlib import Path

# output folder
os.makedirs(
    "datasets/cropped_cards",
    exist_ok=True
)

# load model
model = YOLO(
    "runs/detect/cambodia_id_detector/weights/best.pt"
)

# supported extensions
extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png"
]

# collect image paths
image_paths = []

for ext in extensions:
    image_paths.extend(
        Path("datasets/raw").glob(ext)
    )

# process all images
for image_path in image_paths:

    print(f"processing: {image_path}")

    # read image
    image = cv2.imread(
        str(image_path)
    )

    # detect card
    results = model.predict(
        image,
        conf=0.1,
        save=False
    )

    # loop detections
    for i, result in enumerate(results):

        boxes = result.boxes

        for j, box in enumerate(boxes):

            # coordinates
            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            # crop card
            crop = image[y1:y2, x1:x2]

            # filename
            filename = (
                image_path.stem
            )

            # output path
            output_path = (
                f"datasets/cropped_cards/"
                f"{filename}_crop_{j}.jpg"
            )

            # save crop
            cv2.imwrite(
                output_path,
                crop
            )

            print(
                f"saved: {output_path}"
            )