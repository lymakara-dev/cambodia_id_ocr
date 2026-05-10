from rapidfuzz import process

from database.db import connection


cursor = connection.cursor()

cursor.execute("""
SELECT
    v.id,
    v.name_km,
    v.name_en,

    c.id,
    c.name_km,
    c.name_en

FROM location_village v

JOIN location_commune c
ON v.commune_id = c.id
""")

rows = cursor.fetchall()

villages_en = []
villages_kh = []

village_map_en = {}
village_map_kh = {}

for row in rows:

    village_id = row[0]
    village_kh = row[1]
    village_en = row[2]

    commune_id = row[3]
    commune_kh = row[4]
    commune_en = row[5]

    villages_en.append(
        village_en.upper()
    )

    villages_kh.append(
        village_kh
    )

    data = {
        "id": village_id,

        "village_kh": village_kh,
        "village_en": village_en,

        "commune_id": commune_id,
        "commune_kh": commune_kh,
        "commune_en": commune_en
    }

    village_map_en[
        village_en.upper()
    ] = data

    village_map_kh[
        village_kh
    ] = data


def match_village_en(text):

    text = text.upper()

    result = process.extractOne(
        text,
        villages_en
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": village_map_en[
            matched
        ],
        "score": score
    }


def match_village_kh(text):

    result = process.extractOne(
        text,
        villages_kh
    )

    if result is None:
        return None

    matched, score, _ = result

    return {
        "input": text,
        "matched": village_map_kh[
            matched
        ],
        "score": score
    }