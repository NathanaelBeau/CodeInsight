var0 = 2
var1 = 5
expected_result =  pd.DataFrame(0, index=range(2), columns=range(5))
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'