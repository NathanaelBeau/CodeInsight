def test(str0: str, str1: str) -> list:
    return [i for i in range(len(str0) - len(str1) + 1) if str0[i:i+len(str1)] == str1]
