import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    results = None

    try:
        results = json.loads(data)
    except:
        results = None

    if not results or 'status' not in results or results['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id = results['results'][0]['place_id']
    print('Place id {}'.format(place_id))
