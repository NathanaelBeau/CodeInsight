from itertools import compress

def test(lst0, lst1, lst2, lst3, var0) :
    
    reason = [', '.join(compress(var0, x))
              for x in zip(lst0, lst1, lst2, lst3)]
    
    return reason
