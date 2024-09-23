import collections
def test(lst0):
    seen = set()
    duplicates = set()
    for item in lst0:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
