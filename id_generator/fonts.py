from PIL import ImageFont

from config import FONT_DIR


KHMER = str(
    FONT_DIR /
    "khmer.ttf"
)

KHMER_MOUL = str(
    FONT_DIR /
    "khmer_moul.ttf"
)

ENGLISH = str(
    FONT_DIR /
    "english.ttf"
)

OCRB = str(
    FONT_DIR /
    "ocrb.ttf"
)


font_name_kh = ImageFont.truetype(
    KHMER_MOUL,
    24
)

font_kh_big = ImageFont.truetype(
    KHMER,
    23
)

font_kh_small = ImageFont.truetype(
    KHMER,
    21
)

font_en = ImageFont.truetype(
    ENGLISH,
    21
)

font_mrz = ImageFont.truetype(
    OCRB,
    32
)