# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
expected_result =  pd.DataFrame({'A': [4, 5], 'B': [40, 50]})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'