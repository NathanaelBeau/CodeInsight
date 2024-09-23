def test(lst0):
    stack = [lst0]
    flat_list = []
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            flat_list.append(current)
    return flat_list