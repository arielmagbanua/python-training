import sqlite3

# create db connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# drop and create the table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'

fh = open(file_name)

for line in fh:
    if not line.startswith('From: '):
        continue

    # grab the domain name from the email
    domain = line.split()[1].split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

    conn.commit()

query_str = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(query_str):
    print(str(row[0]), row[1])

cur.close()
