var0 = 'apple'
var1 = pd.Series(['apple', 'banana', 'cherry'])
expected_result =  pd.Series([np.nan, 'banana', 'cherry'])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'