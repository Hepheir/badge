import os

from python.core.download import save_at

from python.acmicpc.net import problem
from python.solved.ac import difficulty, all_dificulties
from python.github.com import user, repository
from python.simpleicons.org import from_cache, from_cache_lower

from python.simpleicons.org import ARCHIVE

ROOT = os.path.dirname(os.path.dirname(__file__))

# Example Code
name, link = 'react', 'https://ko.reactjs.org/'

url = from_cache_lower(name, link)
file_path = os.path.join(ROOT, ARCHIVE, name+'.svg')

save_at(url, file_path)

# Note:
#
# for programming languages, icons provided by simpleicons.org, use 'flat' for the style
