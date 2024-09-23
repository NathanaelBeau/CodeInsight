def test(str0):
    return dict((k.strip(), int(v.strip())) for k, v in (p.split('-') for p in str0.split(',')))



