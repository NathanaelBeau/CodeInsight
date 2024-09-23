df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
var0 = 1
result1, result2 = test(df0, var0)
assert (result1.values == pd.DataFrame({'X': [10], 'Y': [40]}).values).all() and (result2.values == pd.DataFrame({'X': [20, 30], 'Y': [50, 60]}).values).all(), 'Test failed'