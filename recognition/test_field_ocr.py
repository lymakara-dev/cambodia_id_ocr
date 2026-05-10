from pathlib import Path

from recognition.ocr import extract_text

# supported extensions
extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png"
]

# field folders
field_folders = [
    "mrz",
    "id_number",
    "name_en",
    "dob",
    "expiry_date",
    "current_address",
    "appearance"
]

# process each field type
for field in field_folders:

    print(f"\n===== {field} =====")

    folder_path = (
        f"datasets/cropped_fields/{field}"
    )

    image_paths = []

    # collect images
    for ext in extensions:

        image_paths.extend(
            Path(folder_path).glob(ext)
        )

    # OCR every image
    for image_path in image_paths:

        print(f"\nimage: {image_path.name}")

        result = extract_text(
            str(image_path)
        )

        # empty OCR
        if not result:

            print("no text found")

            continue

        # print OCR result
        for item in result:

            text = item["text"]

            confidence = item["confidence"]

            print(
                f"text: {text}"
            )

            print(
                f"confidence: "
                f"{confidence:.2f}"
            )