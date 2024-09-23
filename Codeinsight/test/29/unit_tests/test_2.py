df0 = pd.DataFrame({'X': [11, 12, 13, 14], 'Y': [21, 22, 23, 24]})
lst0 = [13, 14]
var0 = "X"
expected_output = pd.DataFrame({'X': [13, 14], 'Y': [23, 24]}, index=[2, 3])
assert test(df0, lst0, var0).equals(expected_output), 'Test failed'