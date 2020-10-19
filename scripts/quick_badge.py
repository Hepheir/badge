import os

from python.core.download import save_at

from python.acmicpc.net import problem
from python.solved.ac import difficulty, all_dificulties
from python.github.com import user, repository
from python.simpleicons.org import from_cache, from_cache_lower

from python.simpleicons.org import ARCHIVE

# Example Code
name, link = 'github', 'https://hepheir.github.io/'

url = from_cache_lower(name, link, 'Dev Blog')
file_path = os.path.join('svg/util/blog', f'hepheir.svg')

save_at(url, file_path)

# Note:
#
# for programming languages, icons provided by simpleicons.org, use 'flat' for the style
