import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fh = codecs.open('where.js', 'w', 'utf-8')
fh.write("myData = [\n")
count = 0

for row in cur:
    data = str(row[1].decode())

    try:
        js = json.loads(str(data))
    except:
        continue

    if not('status' in js and js['status'] == 'OK'):
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    if lat == 0 or lng == 0:
        continue

    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")

    try:
        print(where, lat, lng)

        count = count + 1

        if count > 1:
            fh.write(",\n")

        output = "["+str(lat)+","+str(lng)+", '"+where+"']"

        fh.write(output)
    except:
        continue

fh.write("\n];\n")
cur.close()
fh.close()

print(count, 'records written to where.js')
print('Open where.html to view the data in a browser')

