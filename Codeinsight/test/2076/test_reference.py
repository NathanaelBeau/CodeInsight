def test(lst0):
    for item in lst0[:]:
        count = lst0.count(item)
        if count > 1:
            for _ in range(count-1):
                lst0.remove(item)
    lst0.sort()
    return lst0
