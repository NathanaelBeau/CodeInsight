df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']})
var0 = 'A'
var1 = 'banana'
var2 = 'B'
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'banana', 'bird']})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'