# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'A': [1, 2], 'B': [4, 5]})
expected_result =  pd.DataFrame({'A': [3], 'B': [6]}, index=[2])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'