def test(var1, var2):
  chars = list(var1)
  results = []
  for c in itertools.product(chars, repeat = var2):
    results.append(c)
  return results
