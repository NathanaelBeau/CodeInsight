# Test 2
series0 = pd.Series([10, 20, 30, 40, 50])
var0 = 40
expected_result =  3
result = test(series0, var0)
assert result == expected_result, 'Test failed'