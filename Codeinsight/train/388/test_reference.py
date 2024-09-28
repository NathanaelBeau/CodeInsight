def test(lst0):
    result = 0
    for num in lst0:
        result = result * (10 ** len(str(num))) + num
    return result
