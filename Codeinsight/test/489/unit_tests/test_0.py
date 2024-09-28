# Test 1
df0 = pd.DataFrame({'A': [1, 11, 21], 'B': [4, 5, 6]})
condition = "A > 10 & B < 5"
expected_result =  pd.DataFrame({'A': [], 'B': []})
result = test(df0, condition)
assert result.shape == expected_result.shape and result.columns.equals(expected_result.columns), 'Test failed'