from . import BASE_URL, LOGO

from ...shields.io import makeurl

RANK_COLORS = {'b': '795548',
               's': '607D8B',
               'g': 'ec9a00',
               'p': '00BFA5',
               'd': '00b4fc',
               'r': 'D81B60'}

RANK_TXT = {'b': 'Bronze',
            's': 'Silver',
            'g': 'Gold',
            'p': 'Platinum',
            'd': 'Diamond',
            'r': 'Ruby'}

TIER_TXT = {'1': 'I',
            '2': 'II',
            '3': 'III',
            '4': 'IV',
            '5': 'V'}

def difficulty(rank:str, tier:int):
    r = rank[0].lower()
    t = str(tier)
    options = [('style', 'flat-square'),
               ('labelColor', 'E0E4E0'),
               ('link', BASE_URL),
               ('link', f'{BASE_URL}/search?query=tier:{r}{t}'),
               ('logo', LOGO)]
    return makeurl('Solved.ac', f'{RANK_TXT[r]} {TIER_TXT[t]}', RANK_COLORS[r], options)
