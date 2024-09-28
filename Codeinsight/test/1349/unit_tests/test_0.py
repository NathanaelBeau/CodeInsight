df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
var0 = 'A'
expected_result =  6
assert test(df0, var0) == expected_result, 'Test failed'