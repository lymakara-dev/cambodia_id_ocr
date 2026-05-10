import pymysql


connection = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root@123",
    database="data_dev",
    charset="utf8mb4"
)