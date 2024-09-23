# Test 1
series0 = pd.Series(['a', 'b', 'c', 'd', 'e'])
var0 = 'c'
expected_result =  2
result = test(series0, var0)
assert result == expected_result, 'Test failed'