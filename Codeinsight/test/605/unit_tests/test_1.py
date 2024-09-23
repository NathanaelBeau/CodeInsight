df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result1 = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [3, 3, 4, 4]})
result1 = test(df1, 2)
assert result1.equals(expected_result1), 'Test failed'