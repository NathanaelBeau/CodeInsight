def test(var0):
    unique_chars = []
    for char in var0:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)