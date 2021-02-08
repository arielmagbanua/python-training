import urllib.request
import urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    url = input('Enter location: ')
    if len(url) < 1:
        break

    print('Retrieving {}'.format(url))
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    json_data = json.loads(data)
    comments = json_data['comments']

    total_count = 0
    comment_count = 0

    for comment in comments:
        count = int(comment.get('count', '0'))
        total_count += count
        comment_count += 1

    print('Count: {}'.format(comment_count))
    print('Sum: {}'.format(total_count))
