def test(var0):
    punctuation = ".,!?;:"
    result = []
    skip = False
    for i, char in enumerate(var0):
        if char in punctuation and i > 0 and var0[i-1] == ' ':
            result.pop()  # remove the space
        result.append(char)
    return ''.join(result)
