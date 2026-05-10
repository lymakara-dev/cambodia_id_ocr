import json

from rapidfuzz import process


with open(
    "data/dictionaries/provinces.json",
    "r",
    encoding="utf-8"
) as f:

    provinces = json.load(f)


# english list
province_en = [
    p["en"].upper()
    for p in provinces
]

# khmer list
province_kh = [
    p["kh"]
    for p in provinces
]


def match_province_en(text):

    text = text.upper()

    result = process.extractOne(
        text,
        province_en
    )

    if result is None:
        return None

    matched, score, index = result

    return {
        "input": text,
        "matched": matched,
        "kh": provinces[index]["kh"],
        "score": score
    }


def match_province_kh(text):

    result = process.extractOne(
        text,
        province_kh
    )

    if result is None:
        return None

    matched, score, index = result

    return {
        "input": text,
        "matched": matched,
        "en": provinces[index]["en"],
        "score": score
    }