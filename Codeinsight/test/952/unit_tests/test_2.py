df0 = pd.DataFrame({'A': [1, '1', 1.0, '2'], 'B': [4, '5', 5, 5.0]})
var0 = 'A'
expected_result =  3
result = test(df0, var0)
assert result == expected_result, 'Test failed'