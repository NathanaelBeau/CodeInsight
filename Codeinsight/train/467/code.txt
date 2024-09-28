def test(var0):
    return ''.join(' ' + char if char.isupper() else char.strip() for char in var0).strip()