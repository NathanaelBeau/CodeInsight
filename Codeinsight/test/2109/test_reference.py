def test(d: dict, var0: str, var1: str) -> bool:
    return {var0, var1}.issubset(d.keys())

