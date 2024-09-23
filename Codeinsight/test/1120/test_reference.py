def test(var0):
    map_dict = {'K': 10**3, 'M': 10**6, 'B': 10**9}
    if var0[-1].isdigit():
        return float(var0)
    return float(var0[:-1]) * map_dict.get(var0[-1].upper(), 1)

