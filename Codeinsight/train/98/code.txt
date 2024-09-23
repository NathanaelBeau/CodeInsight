def test(var1):
    if (var1<=2):
      return var1
    i = var1 * 2
    factors = [number  for number in range(var1, 1, -1) if number * 2 > var1]
    while True:
        for a in factors:
            if i % a != 0:
                i += var1
                break
            if (a == factors[-1] and i % a == 0):
                return i