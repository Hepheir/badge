from .protocol import http, https

def html(url):
    if url.startswith('https://'):
        content = https(url)
        if type(content) is bytes:
            content = content.decode('utf-8')
        return content
    else:
        return http(url)
