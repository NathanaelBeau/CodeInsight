import itertools

def test(var0: int) -> list:
    return list(itertools.accumulate(range(var0)))