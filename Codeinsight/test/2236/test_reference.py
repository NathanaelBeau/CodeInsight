def test(str0):
    return [list(map(int, str0.split(',')[i:i+2])) for i in range(0, len(str0.split(',')), 2)]

