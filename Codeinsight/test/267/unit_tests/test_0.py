# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
lst0 = [0, 3]
expected_result =  pd.DataFrame({'A': [2, 3], 'B': [6, 7]})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'