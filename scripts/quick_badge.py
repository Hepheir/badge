import os

from python.core.download import save_at

from python.acmicpc.net import problem
from python.solved.ac import difficulty, all_dificulties
from python.github.com import user, repository
from python.simpleicons.org import from_cache

from python.simpleicons.org import ARCHIVE

# Example Code
name, link = 'Gmail', 'https://mail.google.com/'

url = from_cache(name, link)
file_path = os.path.join(ARCHIVE, f'{name.lower()}.svg')

save_at(url, file_path)

# Note:
#
# for programming languages, icons provided by simpleicons.org, use 'flat' for the style
