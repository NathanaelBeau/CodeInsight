def test(s):
    return ''.join('{:02x}'.format(ord(c)) for c in s)

