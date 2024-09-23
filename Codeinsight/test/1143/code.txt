def test(str0):
    return dict((n, int(v)) for n, v in (a.split('=') for a in str0.split()))
