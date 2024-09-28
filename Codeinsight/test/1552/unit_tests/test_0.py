df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result1 = [[1, 4], [2, 5], [3, 6]]
result1 = test(df1)
assert result1 == expected_result1, 'Test failed'