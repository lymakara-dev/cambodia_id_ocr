from rapidfuzz import process

from database.db import connection


cursor = connection.cursor()

cursor.execute("""
SELECT
    c.id,
    c.name_km,
    c.name_en,

    d.id,
    d.name_km,
    d.name_en

FROM location_commune c

JOIN location_district d
ON c.district_id = d.id
""")

rows = cursor.fetchall()

communes_en = []
communes_kh = []

commune_map_en = {}
commune_map_kh = {}

for row in rows:

    commune_id = row[0]
    commune_kh = row[1]
    commune_en = row[2]

    district_id = row[3]
    district_kh = row[4]
    district_en = row[5]

    communes_en.append(
        commune_en.upper()
    )

    communes_kh.append(
        commune_kh
    )

    data = {
        "id": commune_id,

        "commune_kh": commune_kh,
        "commune_en": commune_en,

        "district_id": district_id,
        "district_kh": district_kh,
        "district_en": district_en
    }

    commune_map_en[
        commune_en.upper()
    ] = data

    commune_map_kh[
        commune_kh
    ] = data


def match_commune_en(text):

    text = text.upper()

    result = process.extractOne(
        text,
        communes_en
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": commune_map_en[
            matched
        ],
        "score": score
    }


def match_commune_kh(text):

    result = process.extractOne(
        text,
        communes_kh
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": commune_map_kh[
            matched
        ],
        "score": score
    }