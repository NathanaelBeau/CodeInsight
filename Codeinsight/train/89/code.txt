def test(lst1):
   dup_items = set()
   uniq_items = []
   for x in lst1:
      if x not in dup_items:
         uniq_items.append(x)
         dup_items.add(x)
   return uniq_items