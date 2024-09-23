def test(var0):
    chars_to_remove = "!@#$"
    return ''.join([char for char in var0 if char not in chars_to_remove])

