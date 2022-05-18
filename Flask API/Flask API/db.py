import sqlite3
import pymysql
# conn = sqlite3.connect("books.sqlite")
conn = pymysql.connect(host= 'sql11.freesqldatabase.com',
database = 'sql11493041',
user= 'sql11493041',
password= 'R3EH8RhAww',
charset = 'utf8mb4',
cursorclass = pymysql.cursors.DictCursor
    
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()