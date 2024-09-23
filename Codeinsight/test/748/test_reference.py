def test(dict0: Dict[str, Any], var0: callable):
    return sum(1 for x in dict0.values() if var0(x))

