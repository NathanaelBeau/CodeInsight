def test(str0):
    return dict(x.split('=') for x in str0.split())

