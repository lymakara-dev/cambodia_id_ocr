from ultralytics import YOLO

model = YOLO(
    "runs/detect/cambodia_id_fields/weights/best.pt"
)

def detect_fields(image_path):
    results = model.predict(image_path)

    fields = []

    for r in results:
        boxes = r.boxes

        for box in boxes:
            cls_id = int(box.cls[0])

            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            label = model.names[cls_id]

            fields.append({
                "label": label,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2]
            })

    return fields