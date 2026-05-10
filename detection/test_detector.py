from ultralytics import YOLO
import cv2

# load trained model
model = YOLO(
    "runs/detect/cambodia_id_detector/weights/best.pt"
)

# image path
image_path = "datasets/raw/test.jpg"

# read image
image = cv2.imread(image_path)

# run detection
results = model.predict(
    image,
    conf=0.1,
    save=False
)

# loop detections
for result in results:

    boxes = result.boxes

    for box in boxes:

        # confidence
        confidence = float(box.conf[0])

        # class id
        class_id = int(box.cls[0])

        # class name
        class_name = model.names[class_id]

        # coordinates
        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        print("CLASS:", class_name)
        print("CONFIDENCE:", confidence)
        print("BBOX:", [x1, y1, x2, y2])

        # draw rectangle
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # draw label
        cv2.putText(
            image,
            f"{class_name} {confidence:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

# show result
cv2.imshow("Detection", image)

cv2.waitKey(0)

cv2.destroyAllWindows()