def test(myDict: dict, var0: any) -> dict:
    return dict(filter(lambda item: item[1] != var0, myDict.items()))
