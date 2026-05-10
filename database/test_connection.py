from database.db import connection

cursor = connection.cursor()

cursor.execute(
    "SELECT VERSION()"
)

result = cursor.fetchone()

print(result)