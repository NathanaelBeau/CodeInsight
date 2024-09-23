def test(d0):
    return dict(sorted(d0.items(), key=lambda item: item[1], reverse=True))

