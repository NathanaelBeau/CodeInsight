# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 2, 1]})
expected_result =  pd.DataFrame({'A': [1, 2, 2, 1]})
result = test(df0, 'A').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'