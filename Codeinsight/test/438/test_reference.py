def test(var0, dct0):
    queue = [dct0]
    while queue:
        current_dict = queue.pop(0)
        if var0 in current_dict:
            return current_dict[var0]
        for value in current_dict.values():
            if isinstance(value, dict):
                queue.append(value)
    return None
