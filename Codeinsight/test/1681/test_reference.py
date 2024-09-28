def test(str0):
    words = []
    word_start = 0

    for i, char in enumerate(str0):
        if char == " " or i == len(str0) - 1:
            if i == len(str0) - 1:
                words.append(str0[word_start:i+1])
            else:
                words.append(str0[word_start:i])
            word_start = i + 1

    return words
