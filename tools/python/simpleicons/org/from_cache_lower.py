from . import CACHED_COLOR, from_cache

lower_matcher = {}

for logo in CACHED_COLOR:
    lower_matcher[logo.lower()] = logo


def from_cache_lower(logo:str, link:str, name:str='', style='flat-square', logoColorWhite=True):
    logo = lower_matcher[logo.lower()]
    return from_cache(logo, link, name, style, logoColorWhite)
