def test(words: list) -> bool:
    return all([word.isupper() for word in words])

