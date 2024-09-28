# Test 1
df0 = pd.DataFrame({'A': [1, 2, 1, 3], 'B': [4, 5, 4, 6]})
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'