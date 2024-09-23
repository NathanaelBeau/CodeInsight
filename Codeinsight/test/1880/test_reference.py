def test(myDict: dict, var0: any) -> dict:
    return {key: value for key, value in myDict.items() if value != var0}

