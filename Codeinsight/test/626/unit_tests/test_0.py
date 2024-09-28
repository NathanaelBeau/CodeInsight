df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
var0 = 5
expected_result1 = ['B']
result1 = test(df0, var0)
assert result1 == expected_result1, 'Test failed'