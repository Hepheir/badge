import os

from python.core.download import save_at
from python.github.com import user, repository, ARCHIVE

owner = 'DGU-DAI-Lab'
repo = 'giwa-damage-detector-demo'

url = repository(owner, repo)
file_path = os.path.join(ARCHIVE, owner, f'{repo}.svg')

save_at(url, file_path)
