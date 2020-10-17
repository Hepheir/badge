import os

from .html import html

def save_at(url, output_file):
    with open(output_file, 'w') as file:
        content = html(url)
        file.write(content)
