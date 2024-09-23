def test(lst1):
    lst1.sort()
    if len(lst1) % 2 == 0:
      return lst1[int(len(lst1)/2)-1]
    else:
      return lst1[int(len(lst1)/2)]
