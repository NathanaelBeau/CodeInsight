def test(str0):
    reversed_chars = [char for char in str0]
    reversed_chars.reverse()
    return ''.join(reversed_chars)
