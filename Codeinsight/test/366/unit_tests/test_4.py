# Test 5: Using 'all' method
series = pd.Series([True, True, True])
method = "all"
expected_result =  True
result = test(series, method)
assert result == expected_result, 'Test failed'