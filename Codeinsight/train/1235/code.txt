def test(lst0):
    result = []
    for i in range(len(lst0)):
        if i == 0 or lst0[i] != lst0[i - 1]:
            result.append(lst0[i])
    return result