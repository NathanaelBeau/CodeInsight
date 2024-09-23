def test(var1):
  length = len(var1)

  if length > 2:
    if var1[-3:] == 'ing':
      var1 += 'ly'
    else:
      var1 += 'ing'

  return var1
