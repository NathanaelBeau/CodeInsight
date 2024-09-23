def test(d: dict) -> list:
    keys = ['key1', 'key2']
    return [dict((k, d[k][i]) for k in keys) for i in range(len(d['key1']))]
