def test(lst0, lst1):
    return [' '.join(word for word in s.split() if word not in lst1) for s in lst0]
