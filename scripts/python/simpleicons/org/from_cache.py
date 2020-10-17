from . import CACHED_COLOR_LOWER

from ...shields.io import makeurl

def from_cache(name, link, style='flat-square', logoColorWhite=True):
    color = CACHED_COLOR_LOWER[name]
    options = [('style', style),
               ('labelColor', color),
               ('logo', name),
               ('link', link),
               ('logoColor', 'FAFAFA')]
    return makeurl('', name, color, options)
