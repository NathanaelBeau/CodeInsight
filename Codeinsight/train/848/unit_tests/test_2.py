df0 = pd.DataFrame({'C': [11, 22, 33, 44, 55], 'D': [66, 77, 88, 99, 111]})
var0 = 3
result1, result2 = test(df0, var0)
assert (result1.values == pd.DataFrame({'C': [11, 22, 33], 'D': [66, 77, 88]}).values).all() and (result2.values == pd.DataFrame({'C': [44, 55], 'D': [99, 111]}).values).all(), 'Test failed'