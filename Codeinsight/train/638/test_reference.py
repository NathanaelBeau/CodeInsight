def test(lst0):
    lst0.sort()  
    lst0.sort(key=len, reverse=True)  
    return lst0