def test(var1):
  snot = var1.find('not')
  spoor = var1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    var1 = var1.replace(var1[snot:(spoor+4)], 'good')
    return var1
  else:
    return var1