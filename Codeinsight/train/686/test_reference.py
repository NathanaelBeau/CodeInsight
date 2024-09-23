def test(str0):
    word_generator = (word for word in str0.split() if not any(char.isdigit() for char in word))
    word_count = sum(1 for _ in word_generator)
    return word_count

