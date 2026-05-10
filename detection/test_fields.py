from ultralytics import YOLO
import cv2

model = YOLO(
    "runs/detect/cambodia_id_fields/weights/best.pt"
)

image = cv2.imread(
    "datasets/cropped_cards/id_0001_crop_0.jpg"
)

results = model.predict(
    image,
    conf=0.01
)

for result in results:

    boxes = result.boxes

    for box in boxes:

        cls_id = int(box.cls[0])

        label = model.names[cls_id]

        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        print(label, confidence)

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

cv2.imshow("fields", image)

cv2.waitKey(0)

cv2.destroyAllWindows()