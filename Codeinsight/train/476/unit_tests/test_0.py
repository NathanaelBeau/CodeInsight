# Test 1
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result =  [{'A': 1, 'B': 3}, {'A': 2, 'B': 4}]
result = test(df0)
assert result == expected_result, 'Test failed'