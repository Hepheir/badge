import os

from .html import html

def save_at(url, output_file):
    dirname = os.path.dirname(output_file)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(output_file, 'w') as file:
        content = html(url)
        file.write(content)
