import urllib.request

def http(url):
    with urllib.request.urlopen(url) as response:
        return response.read()
