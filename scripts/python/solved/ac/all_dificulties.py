from .difficulty import difficulty

def all_dificulties() -> iter:
    for rank in 'bsgpdr':
        for tier in '12345':
            yield difficulty(rank, tier)
