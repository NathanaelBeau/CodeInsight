def test(dict0, idx0):
    values_list = list(dict0.values())
    if idx0 < 0 or idx0 >= len(values_list):
        return None
    return values_list[idx0]
