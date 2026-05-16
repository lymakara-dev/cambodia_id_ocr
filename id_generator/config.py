from pathlib import Path

ROOT = Path(__file__).resolve().parent

WIDTH = 960
HEIGHT = 608

COUNT = 2

RESOURCE_DIR = ROOT / "resources"

FONT_DIR = RESOURCE_DIR / "fonts"

DICT_DIR = RESOURCE_DIR / "dictionaries"

TEMPLATE_DIR = RESOURCE_DIR / "template"

OUTPUT_DIR = ROOT / "output"

OUTPUT_DIR.mkdir(
    exist_ok=True
)

TEMPLATE_IMAGE = (
    TEMPLATE_DIR /
    "id template.png"
)

ANNOTATION_FILE = (
    TEMPLATE_DIR /
    "id_template.txt"
)

LABEL_FILE = (
    OUTPUT_DIR /
    "labels.json"
)