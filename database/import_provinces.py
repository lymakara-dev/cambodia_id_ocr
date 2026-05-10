from database.db import connection


provinces = [
    ("ភ្នំពេញ", "Phnom Penh"),
    ("បាត់ដំបង", "Battambang"),
    ("សៀមរាប", "Siem Reap")
]

cursor = connection.cursor()

for kh, en in provinces:

    cursor.execute("""
    INSERT INTO provinces (
        name_kh,
        name_en
    )
    VALUES (%s, %s)
    """, (kh, en))

connection.commit()

print(
    "provinces inserted"
)