def test(str0: str, substring: str) -> list:
    return [i for i in range(len(str0)) if str0.startswith(substring, i)]
