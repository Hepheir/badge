from ...shields.io import makeurl

def repository(owner:str, repository:str):
    options = [('style', 'flat-square'),
               ('labelColor', '181717'),
               ('logo', 'Github'),
               ('link', f'https://github.com/{owner}'),
               ('link', f'https://github.com/{owner}/{repository}')]
    return makeurl(owner, repository, 'dbdbdb', options)
