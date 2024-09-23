var0 = 3
var1 = 3
expected_result =  pd.DataFrame(0, index=range(3), columns=range(3))
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'