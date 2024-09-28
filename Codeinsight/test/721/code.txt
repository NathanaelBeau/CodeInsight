def test(dict0):
    myList = []
    for tup in dict0.items():
        myList.extend(tup)
    return myList
