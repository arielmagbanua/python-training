import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

print('Creating JSON output on spider.js...')
how_many = int(input('How many nodes? '))

cur.execute('''
    SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound
''')

fh = open('spider.js', 'w')
nodes = list()
max_rank = None
min_rank = None

for row in cur:
    nodes.append(row)
    rank = row[2]

    if max_rank is None or max_rank < rank:
        max_rank = rank

    if min_rank is None or min_rank > rank:
        min_rank = rank

    if len(nodes) > how_many:
        break

if max_rank == min_rank or max_rank is None or min_rank is None:
    print('Error - please run sprank.py to compute page rank')
    quit()

fh.write('spiderJson = {"nodes":[\n')

count = 0
map = dict()
ranks = dict()

for row in nodes:
    if count > 0:
        fh.write(',\n')

    # print row
    rank = row[2]
    rank = 19 * ((rank - min_rank) / (max_rank - min_rank))

    fh.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
    fh.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')

    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1

fh.write('],\n')

cur.execute('SELECT DISTINCT from_id, to_id FROM Links')
fh.write('"links":[\n')

count = 0

for row in cur:
    # print row
    if row[0] not in map or row[1] not in map:
        continue

    if count > 0:
        fh.write(',\n')

    rank = ranks[row[0]]

    srank = 19 * ((rank - min_rank) / (max_rank - min_rank))

    fh.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
    count = count + 1

fh.write(']};')
fh.close()
cur.close()

print('Open force.html in a browser to view the visualization')
