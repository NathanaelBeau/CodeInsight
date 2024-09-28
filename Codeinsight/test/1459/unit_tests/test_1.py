df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
var0 = 'B'
expected_result =  33
assert test(df0, var0) == expected_result, 'Test failed'