# Test 2
df0 = pd.DataFrame({'X': ['a', 'b', 'c', 'd'], 'Y': ['w', 'x', 'y', 'z']})
expected_result =  pd.DataFrame({'X': ['d'], 'Y': ['z']})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'