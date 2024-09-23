def test(str0):
    return ''.join(' ' + char if char.isupper() else char.strip() for char in str0).strip()


