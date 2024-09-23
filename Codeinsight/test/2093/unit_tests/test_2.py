df0 = pd.DataFrame({'A': ['apple', 'apple', 'apple', 'orange'], 'B': ['red', 'red', 'green', 'orange']})
var0 = 'A'
var1 = 'B'
expected_result =  pd.Series(['red', 'orange'], index=['apple', 'orange'], name='B')
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'