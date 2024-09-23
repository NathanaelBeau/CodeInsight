# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df1 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'z'])
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'