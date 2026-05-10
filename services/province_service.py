from rapidfuzz import process

from database.db import connection


cursor = connection.cursor()

cursor.execute("""
SELECT
    id,
    name_km,
    name_en
FROM location_province
""")

rows = cursor.fetchall()

provinces_en = []
provinces_kh = []

province_map_en = {}
province_map_kh = {}

for row in rows:

    province_id = row[0]
    kh = row[1]
    en = row[2]

    provinces_en.append(
        en.upper()
    )

    provinces_kh.append(
        kh
    )

    province_map_en[
        en.upper()
    ] = {
        "id": province_id,
        "kh": kh,
        "en": en
    }

    province_map_kh[
        kh
    ] = {
        "id": province_id,
        "kh": kh,
        "en": en
    }


def match_province_en(text):

    text = text.upper()

    result = process.extractOne(
        text,
        provinces_en
    )

    if result is None:
        return None

    matched, score, _ = result

    province = province_map_en[
        matched
    ]

    return {
        "input": text,
        "matched": province,
        "score": score
    }


def match_province_kh(text):

    result = process.extractOne(
        text,
        provinces_kh
    )

    if result is None:
        return None

    matched, score, _ = result

    province = province_map_kh[
        matched
    ]

    return {
        "input": text,
        "matched": province,
        "score": score
    }