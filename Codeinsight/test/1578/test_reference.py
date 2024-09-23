def test(dict0: Dict[str, str]):
    return {k.lower(): v.lower() for k, v in dict0.items()}

