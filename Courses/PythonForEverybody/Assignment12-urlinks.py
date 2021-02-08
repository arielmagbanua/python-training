import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl


def print_url(url_print):
    print('Receiving: {}'.format(url_print))


def open_url(url_to_open):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # print('Opening: ' + url_to_open)

    html = urllib.request.urlopen(url_to_open, context=ctx).read()
    return BeautifulSoup(html, 'html.parser')


url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for _ in range(count):
    # follow the url
    new_soup = open_url(url)
    new_tags = new_soup('a')
    url = new_tags[position - 1].get('href', None)
    print_url(url)


