def test(lst0):
    return max(range(len(lst0)), key=lambda index: lst0[index]['size'])

