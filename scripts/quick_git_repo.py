import os

from python.core.download import save_at
from python.github.com import user, repository, ARCHIVE

ROOT = os.path.dirname(os.path.dirname(__file__))

owner = 'Hepheir'
repo = 'Blog-Posts'

if repo:
    url = repository(owner, repo)
    file_path = os.path.join(ROOT, ARCHIVE, owner, f'{repo}.svg')
else:
    url = user(owner)
    file_path = os.path.join(ROOT, ARCHIVE, f'{owner}.svg')

save_at(url, file_path)
