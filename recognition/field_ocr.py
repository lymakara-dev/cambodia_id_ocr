import cv2

from detection.field_detector import detect_fields
from recognition.ocr import extract_text


def process_fields(image_path):
    image = cv2.imread(image_path)

    detections = detect_fields(image_path)

    results = {}

    for field in detections:
        label = field["label"]

        x1, y1, x2, y2 = field["bbox"]

        crop = image[y1:y2, x1:x2]

        temp_path = f"/tmp/{label}.jpg"

        cv2.imwrite(temp_path, crop)

        ocr_result = extract_text(temp_path)

        if not ocr_result:
            text = ""
        else:
            text = " ".join([
                item["text"]
                for item in ocr_result
            ])          

        results[label] = {
            "text": text,
            "confidence": field["confidence"]
        }

    return results