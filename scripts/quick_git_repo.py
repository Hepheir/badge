import os

from python.core.download import save_at
from python.github.com import user, repository, ARCHIVE

owner = 'Hepheir'
repo = 'hepheir.github.io'

# url = repository(owner, repo)
# file_path = os.path.join(ARCHIVE, owner, f'{repo}.svg')

url = user(owner)
file_path = os.path.join(ARCHIVE, f'{owner}.svg')

save_at(url, file_path)
