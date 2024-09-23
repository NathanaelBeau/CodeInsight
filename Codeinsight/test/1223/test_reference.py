import itertools

def test(*lst0: List[Any]):
    max_length = max(map(len, lst0))
    result = []
    for combo in itertools.product(*lst0):
        temp = list(itertools.islice(itertools.cycle(combo), max_length))
        result.append(temp)
    return result
