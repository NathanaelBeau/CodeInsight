df0 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
var0 = 'd'
expected_result =  False
result = test(df0, var0)
assert result == expected_result, 'Test failed'