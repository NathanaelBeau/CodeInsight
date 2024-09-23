def test(lst0):
    return {p: {'id': p, 'position': ind} for ind, p in enumerate(lst0)}
