import sqlite3

how_many = int(input("How many to dump? "))

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, sender FROM Senders')
senders = dict()
for message_row in cur:
    senders[message_row[0]] = message_row[1]

cur.execute('SELECT id, subject FROM Subjects')
subjects = dict()

for message_row in cur:
    subjects[message_row[0]] = message_row[1]


cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
messages = dict()
for message_row in cur:
    messages[message_row[0]] = (message_row[1], message_row[2], message_row[3], message_row[4])

print("Loaded messages=", len(messages), "subjects=", len(subjects), "senders=", len(senders))

send_counts = dict()
send_orgs = dict()

for (message_id, message) in list(messages.items()):
    sender = message[1]
    send_counts[sender] = send_counts.get(sender, 0) + 1

    pieces = senders[sender].split("@")

    if len(pieces) != 2:
        continue

    dns = pieces[1]
    send_orgs[dns] = send_orgs.get(dns, 0) + 1

print('')
print('Top', how_many, 'Email list participants')

x = sorted(send_counts, key=send_counts.get, reverse=True)
for k in x[:how_many]:
    print(senders[k], send_counts[k])

    if send_counts[k] < 10:
        break

print('')
print('Top', how_many, 'Email list organizations')

x = sorted(send_orgs, key=send_orgs.get, reverse=True)
for k in x[:how_many]:
    print(k, send_orgs[k])

    if send_orgs[k] < 10:
        break
