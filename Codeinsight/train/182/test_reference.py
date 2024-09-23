def test(lst1):
     m   = sum(lst1) / len(lst1)
     std = math.sqrt( sum( (elt-m)**2 for elt in lst1)/len(lst1)) 
     return  [ (elt-m)/std for elt in lst1]
