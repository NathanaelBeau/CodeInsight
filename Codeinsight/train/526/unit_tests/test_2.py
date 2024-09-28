# Test 3
df0 = pd.DataFrame({'M': [10.5, 11.5], 'N': [12.5, 13.5]})
expected_result =  [{'M': 10.5, 'N': 12.5}, {'M': 11.5, 'N': 13.5}]
result = test(df0)
assert result == expected_result, 'Test failed'