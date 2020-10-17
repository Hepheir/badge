import urllib.parse

from . import urlencode

BASE_URL = 'https://img.shields.io/badge/'

def makeurl(label='', message='', color='', options=[tuple, ...]):
    sub_url = '-'.join(map(urlencode,(label, message, color)))
    query = urllib.parse.urlencode(options)
    return BASE_URL + sub_url + '?' + query