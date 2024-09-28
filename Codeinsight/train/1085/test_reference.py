def test(lst0):
    seen = set()
    new_lst = []
    for triple in lst0:
        first = triple[0]
        if first in seen:
            continue
        seen.add(first)
        new_lst.append(triple)
    return new_lst
