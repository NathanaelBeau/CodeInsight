# Test 2: Using 'bool' method
series = pd.Series([True])
method = "bool"
expected_result =  True
result = test(series, method)
assert result == expected_result, 'Test failed'