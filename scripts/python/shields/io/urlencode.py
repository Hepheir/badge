import urllib.parse

def urlencode(x):
    retval = urllib.parse.quote(x)
    retval = retval.replace('-', '--')
    return retval