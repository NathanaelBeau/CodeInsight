def test(str0: bytes):
    return str0.decode('utf8')[::-1].encode('utf8')

