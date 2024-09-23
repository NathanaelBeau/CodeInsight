def test(var1):
    x = var1 // 2
    y = set([x])
    while x * x != var1:
        x = (x + (var1 // x)) // 2
        if x in y: 
           return False
        y.add(x)
    return True
