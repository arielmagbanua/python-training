import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as Et
import ssl

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
    tree = Et.fromstring(data)

    count_num = 0
    sum_num = 0

    counts = tree.findall('.//count')
    for count in counts:
        sum_num += int(count.text)
        count_num += 1

    print('Count: {}'.format(count_num))
    print('Sum: {}'.format(sum_num))
