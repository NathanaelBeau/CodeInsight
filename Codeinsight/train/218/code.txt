def test(lst1,lst2):
    return sum(a*b for (a,b) in zip(lst1,lst2))