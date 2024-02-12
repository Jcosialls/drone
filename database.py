import sqlite3

connect = sqlite3.connect("test.db")
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS coordonates (id INTTEGER PRIMARY KEY, x INTEGER, y INTEGER, z INTGER, time INTEGER)")

cursor.execute("INSERT INTO coordonates VALUES (2,0,0,0,0)")

x = cursor.execute("SELECT x FROM coordonates")
x.fetchone()
print(f'the x coordonate is : {x}')

connect.commit()

connect.close()