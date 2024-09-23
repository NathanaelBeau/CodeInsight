df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
var0 = 2
result1, result2 = test(df0, var0)
assert (result1.values == pd.DataFrame({'A': [1, 2], 'B': [5, 6]}).values).all() and (result2.values == pd.DataFrame({'A': [3, 4], 'B': [7, 8]}).values).all(), 'Test failed'