def test(dict0):
    outdict = {}
    for k, v in dict0.items():
        outdict[k.lower()] = v.lower()
    return outdict

