# Test 1
df0 = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
expected_result =  pd.DataFrame({'A': [1, "", 3], 'B': [4, 5, ""]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'