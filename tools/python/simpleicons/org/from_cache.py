from . import CACHED_COLOR

from ...shields.io import makeurl

def from_cache(logo:str, link:str, name:str='', style='flat-square', logoColorWhite=True):
    if not name:
        name = logo
    color = CACHED_COLOR[logo]
    options = [('style', style),
               ('labelColor', color),
               ('logo', logo),
               ('link', link),
               ('logoColor', 'FAFAFA')]
    return makeurl('', name, color, options)
