def test(str0):
    switched_str = []
    for i in range(0, len(str0) - 1, 2):
        switched_str.append(str0[i+1])
        switched_str.append(str0[i])
    if len(str0) % 2:
        switched_str.append(str0[-1])
    return ''.join(switched_str)
