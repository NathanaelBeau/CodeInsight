def test(arr0, arr1):
    for i in arr1:
        if i in arr0:
            arr0.remove(i)
    return arr0

