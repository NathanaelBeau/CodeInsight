def test(str0):
    if len(str0) <= 1:
        return str0
    mid = len(str0) // 2
    left_half = str0[:mid]
    right_half = str0[mid:]
    return test(right_half) + test(left_half)

