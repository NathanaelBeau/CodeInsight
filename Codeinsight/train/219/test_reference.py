def test(lst1):
    res = []
    for elt in lst1:
       if elt not in res: 
          res.append(elt)
    return res
