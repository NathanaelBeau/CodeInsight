df0 = pd.DataFrame({'A': ['apple', 'banana', 'apple', 'orange', 'apple'], 'B': [1, 2, 3, 4, 5]})
var0 = 'A'
var1 = 'B'
expected_result =  pd.Series([1, 2, 4], index=['apple', 'banana', 'orange'], name='B')
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'