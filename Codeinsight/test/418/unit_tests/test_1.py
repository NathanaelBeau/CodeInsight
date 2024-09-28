df0 = pd.DataFrame({'B': ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']})
var0 = 'B'
expected_result =  'apple'
result = test(df0, var0)
assert result == expected_result, 'Test failed'