# Cambodia ID OCR

Cambodia ID OCR is a computer vision and OCR pipeline for extracting structured information from Cambodia national ID cards.

---

# Pipeline

```text
Image
→ Card Detection
→ Perspective Correction
→ Field Detection
→ OCR
→ MRZ Parsing
→ Checksum Validation
→ JSON Output
```

---

# Features

- Cambodia ID card detection
- Perspective correction
- Field-level detection
- OCR extraction
- MRZ parsing
- MRZ checksum validation
- Structured JSON output
- Khmer and English support

---

# Extracted Fields

```text
photo
id_number
name_kh
name_en
dob
sex
height
birth_address
current_address
issue_date
expiry_date
appearance
mrz
```

---

# Tech Stack

## Backend

- Python 3.10
- FastAPI

## Detection

- YOLOv8
- Ultralytics

## OCR

- PaddleOCR
- PaddlePaddle

## Image Processing

- OpenCV
- NumPy
- Pillow

## Training

- PyTorch
- HuggingFace Transformers
- Albumentations

## Annotation

- Label Studio

---

# Project Structure

```text
cambodia-id-ocr/
│
├── api/
│   └── main.py
│
├── config/
│
├── datasets/
│   ├── raw/
│   └── fields/
│
├── detection/
│   ├── __init__.py
│   └── field_detector.py
│
├── models/
│   └── yolo/
│
├── output/
│
├── parsing/
│   ├── __init__.py
│   └── mrz_parser.py
│
├── preprocessing/
│   ├── __init__.py
│   ├── perspective.py
│   └── image_enhancement.py
│
├── recognition/
│   ├── __init__.py
│   ├── ocr.py
│   ├── field_ocr.py
│   ├── test_fields.py
│   └── test_ocr.py
│
├── services/
│
├── tests/
│
├── training/
│   ├── __init__.py
│   ├── train_detector.py
│   └── train_fields.py
│
├── utils/
│
├── validation/
│   ├── __init__.py
│   └── checksum.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd cambodia-id-ocr
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Ubuntu

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Stable Dependency Versions

```text
Python 3.10.12
NumPy 1.26.4
PaddlePaddle 2.6.2
PaddleOCR 2.7.3
OpenCV 4.6.0.66
```

---

# Dataset Annotation

Recommended annotation tool:

- Label Studio

Export format:

- YOLO

---

# Train Card Detector

```bash
python training/train_detector.py
```

---

# Train Field Detector

```bash
python training/train_fields.py
```

---

# Run OCR Pipeline

```bash
python -m recognition.test_fields
```

---

# MRZ Example

```text
IDKHM1806714117<<<
7505113M3401088KHM<<8
CHHAY<<SETHY<<<<<<<<<<<<<<<<<
```

---

# JSON Output Example

```json
{
  "id_number": "18067141101",
  "name_en": "CHHAY SETHY",
  "dob": "1975-05-11",
  "sex": "M",
  "expiry_date": "2034-01-08",
  "mrz": {
    "raw": [
      "IDKHM1806714117<<<",
      "7505113M3401088KHM<<8",
      "CHHAY<<SETHY<<<<<<<<<<<<<<<<<"
    ],
    "checksum_valid": true
  }
}
```

---

# Future Improvements

- Khmer OCR fine-tuning
- Face matching
- Anti-spoof detection
- GPU inference
- ONNX optimization
- Docker deployment
- Multi-document support

---

# License

MIT