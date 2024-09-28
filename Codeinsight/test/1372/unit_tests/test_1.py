df0 = pd.DataFrame({'C': ['apple', 'banana', 'cherry'], 'D': ['apple', 'banana', 'apple']})
var0 = 'C'
var1 = 'D'
expected_result =  pd.Series([True, True, False])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'