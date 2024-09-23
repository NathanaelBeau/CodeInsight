# Test 3
df0 = pd.DataFrame({'A': ['x', 'x', 'x'], 'B': [1, 2, 3]})
expected_result =  pd.DataFrame({'A': ['x'], 'B': [3]})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'