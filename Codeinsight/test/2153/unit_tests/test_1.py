df1 = pd.DataFrame({'B': ['apple', 'banana', 'cherry', 'date', 'fig']})
col1 = 'B'
var1 = 'date'
expected_result =  3
result = test(df1, col1, var1)
assert result == expected_result, 'Test failed'