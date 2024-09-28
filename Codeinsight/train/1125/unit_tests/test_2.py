# Test 3
series0 = pd.Series(['apple', 'banana', 'cherry'])
var0 = 'banana'
expected_result =  1
result = test(series0, var0)
assert result == expected_result, 'Test failed'