from rapidfuzz import process

from database.db import connection


cursor = connection.cursor()

cursor.execute("""
SELECT
    d.id,
    d.name_km,
    d.name_en,
    p.id,
    p.name_km,
    p.name_en
FROM location_district d
JOIN location_province p
ON d.province_id = p.id
""")

rows = cursor.fetchall()

districts_en = []
districts_kh = []

district_map_en = {}
district_map_kh = {}

for row in rows:

    district_id = row[0]
    district_kh = row[1]
    district_en = row[2]

    province_id = row[3]
    province_kh = row[4]
    province_en = row[5]

    districts_en.append(
        district_en.upper()
    )

    districts_kh.append(
        district_kh
    )

    data = {
        "id": district_id,

        "district_kh": district_kh,
        "district_en": district_en,

        "province_id": province_id,
        "province_kh": province_kh,
        "province_en": province_en
    }

    district_map_en[
        district_en.upper()
    ] = data

    district_map_kh[
        district_kh
    ] = data


def match_district_en(text):

    text = text.upper()

    result = process.extractOne(
        text,
        districts_en
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": district_map_en[
            matched
        ],
        "score": score
    }


def match_district_kh(text):

    result = process.extractOne(
        text,
        districts_kh
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": district_map_kh[
            matched
        ],
        "score": score
    }