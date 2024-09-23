df0 = pd.DataFrame({'M': [True, False, True, False], 'N': [False, True, False, True], 'other_column': [100, 200, 300, 400]})
var0 = 'M'
var1 = True
expected_result =  400
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'