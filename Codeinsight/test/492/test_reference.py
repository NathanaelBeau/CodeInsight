def test(str0):
    try:
        return int(str0)
    except ValueError:
        return None