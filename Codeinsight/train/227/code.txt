def test(lst1,var1):

      for idx, elt in enumerate( reversed( lst1 ) ):
           if elt >= var1:
               return len( lst1 ) - idx - 1