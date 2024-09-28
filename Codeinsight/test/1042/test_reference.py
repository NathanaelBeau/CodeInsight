def test(lst0):
    seen = set()
    result = []
    for d in lst0:
        if d['id'] not in seen:
            seen.add(d['id'])
            result.append(d)
    return result