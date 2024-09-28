# Test 4: Using 'any' method
series = pd.Series([False, True, False])
method = "any"
expected_result =  True
result = test(series, method)
assert result == expected_result, 'Test failed'