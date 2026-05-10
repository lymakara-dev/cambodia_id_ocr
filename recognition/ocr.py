from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    show_log=False
)


def extract_text(image_path):
    results = ocr.ocr(image_path)

    output = []

    if results is None:
        return output

    for result in results:

        if result is None:
            continue

        for line in result:

            if line is None:
                continue

            text = line[1][0]
            confidence = line[1][1]

            output.append({
                "text": text,
                "confidence": float(confidence)
            })

    return output