var0 = 5
var1 = 2
expected_result =  pd.DataFrame(0, index=range(5), columns=range(2))
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'