from ...shields.io import makeurl

def user(name:str):
    options = [('style', 'flat-square'),
               ('labelColor', '181717'),
               ('logo', 'Github'),
               ('link', f'https://github.com/'),
               ('link', f'https://github.com/{name}')]
    return makeurl('', name, '181717', options)
