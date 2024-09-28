def test(str0):
    return [x.strip().lower() for x in str0.split("\n") if x.strip()]
