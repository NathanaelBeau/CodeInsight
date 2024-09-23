def test(var1,var2):
     return math.sqrt(sum([(x1-x2)**2 for x1,x2 in zip(var1,var2)]))
