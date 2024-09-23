def test(str0: str, str1: str) -> list:
    indexes = []
    i = str0.find(str1)
    while i != -1:
        indexes.append(i)
        i = str0.find(str1, i+1)
    return indexes

