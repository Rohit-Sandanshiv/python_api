import sqlite3
import sys

from db_connection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)
# cursor.execute("""

print(cursor.execute("select * from Consumer").fetchall())
print(cursor.execute("select * from SocialContact").fetchall())
print(cursor.execute("select * from Address").fetchall())
print(cursor.execute("select * from Purchase").fetchall())
print(cursor.execute("select count(*) from Product").fetchall())
print(cursor.execute("select * from counter_table").fetchall())


conn.commit()
conn.close()