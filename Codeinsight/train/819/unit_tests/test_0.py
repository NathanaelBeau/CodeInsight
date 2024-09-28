df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry']})
var0 = r'^a'
var1 = 'A'
expected_result =  pd.DataFrame({'A': ['Apple', 'banana', 'cherry']})
result = test(df0, 'A', var0, var1)
assert result.equals(expected_result), 'Test failed'