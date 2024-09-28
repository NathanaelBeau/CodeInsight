def test(str0):
    words = str0.split()
    result = []

    for word in words:
        if not word.isdigit():
            result.append(word)

    return ' '.join(result)