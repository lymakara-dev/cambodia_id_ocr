from ocr import extract_text

results = extract_text("id.jpeg")

for item in results:
    print(item)