def test(str0):
    txt = l = []
    for t in str0.split():
        try:
            l.append(float(t))
        except ValueError:
            pass
    return txt

