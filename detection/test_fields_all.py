from ultralytics import YOLO
import cv2
import os
from pathlib import Path

# create output folder
os.makedirs(
    "datasets/cropped_fields",
    exist_ok=True
)

# load trained field detector
model = YOLO(
    "runs/detect/cambodia_id_fields/weights/best.pt"
)

# supported image extensions
extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png"
]

# collect all cropped card images
image_paths = []

for ext in extensions:
    image_paths.extend(
        Path(
            "datasets/cropped_cards"
        ).glob(ext)
    )

# process all images
for image_path in image_paths:

    print(
        f"\nprocessing: {image_path}"
    )

    # read image
    image = cv2.imread(
        str(image_path)
    )

    if image is None:
        print(
            f"failed to load: {image_path}"
        )
        continue

    # copy for visualization
    visual = image.copy()

    # run field detection
    results = model.predict(
        image,
        conf=0.01,
        save=False
    )

    # image base name
    image_name = image_path.stem

    # loop detection results
    for result in results:

        boxes = result.boxes

        # no detections
        if len(boxes) == 0:

            print(
                "no fields detected"
            )

            continue

        # loop detected fields
        for i, box in enumerate(boxes):

            # class id
            cls_id = int(box.cls[0])

            # field label
            label = model.names[cls_id]

            # confidence
            confidence = float(box.conf[0])

            # coordinates
            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            print(
                f"{label} {confidence:.2f}"
            )

            # draw rectangle
            cv2.rectangle(
                visual,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # draw label
            cv2.putText(
                visual,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # crop field
            crop = image[y1:y2, x1:x2]

            # skip invalid crop
            if crop.size == 0:
                continue

            # create field folder
            field_folder = (
                f"datasets/cropped_fields/{label}"
            )

            os.makedirs(
                field_folder,
                exist_ok=True
            )

            # output filename
            output_path = (
                f"{field_folder}/"
                f"{image_name}_{i}.jpg"
            )

            # save crop
            cv2.imwrite(
                output_path,
                crop
            )

            print(
                f"saved: {output_path}"
            )

    # save visualization image
    visual_path = (
        f"datasets/cropped_fields/"
        f"{image_name}_detected.jpg"
    )

    cv2.imwrite(
        visual_path,
        visual
    )

    print(
        f"saved: {visual_path}"
    )

print(
    "\nall field crops completed"
)