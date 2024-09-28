# Test 1
df0 = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [10, 20, 30, 40]})
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [20, 40]})
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'