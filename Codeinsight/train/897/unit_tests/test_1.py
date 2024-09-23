var0 = 'hello'
var1 = pd.Series(['hello', 'world', 'hello'])
expected_result =  pd.Series([np.nan, 'world', np.nan])
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'