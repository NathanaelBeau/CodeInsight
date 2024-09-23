df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'A': [2], 'B': [5]})
expected_result1 = pd.DataFrame({'A': [2], 'B': [5]})
result = test(df0, df1)
assert result.equals(expected_result1), 'Test failed'