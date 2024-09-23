import itertools
def test(lst0):
    stack = [([], lst0)]
    results = []

    while stack:
        path, lists = stack.pop()
        if not lists:
            results.append(tuple(path))
        else:
            for item in lists[0]:
                stack.append((path + [item], lists[1:]))

    return results

