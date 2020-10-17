import urllib.request
import ssl

def https(url):
    request_url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request_url, context=context) as response:
        return response.read()
