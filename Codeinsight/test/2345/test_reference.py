def test(var0):
    char_count = {}
    for char in var0:
        char_count[char] = char_count.get(char, 0) + 1
    return sum(1 for count in char_count.values() if count > 1)
