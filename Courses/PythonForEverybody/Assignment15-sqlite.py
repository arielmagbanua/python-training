import sqlite3

conn = sqlite3.connect('appdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

# delete all records
cur.execute('DELETE FROM Ages')

cur.execute("INSERT INTO Ages (name, age) VALUES ('Talha', 28)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Francisco', 35)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Kacie', 38)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Elliot', 23)")

rows = cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")\
    .fetchall()

print(rows[0][0])
