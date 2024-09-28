df0 = pd.DataFrame({'A': [5, 6, 3, 4], 'B': [1, 2, 3, 5]})
lst0 = [5, 4]
var0 = "A"
expected_output = pd.DataFrame({'A': [5, 4], 'B': [1, 5]}, index=[0, 3])
assert test(df0, lst0, var0).equals(expected_output), 'Test failed'