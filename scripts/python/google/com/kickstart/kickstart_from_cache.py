from . import LOGO, CACHED_KICKSTART_ROUND_ID

from ....shields.io import makeurl

def kickstart_from_cache(round_title:str):
    round_id = CACHED_KICKSTART_ROUND_ID[round_title]
    options = [('style', 'flat-square'),
               ('labelColor', '757575'),
               ('link', 'https://codingcompetitions.withgoogle.com/kickstart/'),
               ('link', f'https://codingcompetitions.withgoogle.com/kickstart/round/{round_id}'),
               ('logo', LOGO)]
    return makeurl('Kick Start', round_title, 'd7d7d7', options)
