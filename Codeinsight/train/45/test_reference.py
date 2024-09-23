def test(lst1):
     fst   = lst1[0]
     snd   = lst1[1]
     lst1[0]  = snd
     lst1[1]  = fst  
     return lst1
