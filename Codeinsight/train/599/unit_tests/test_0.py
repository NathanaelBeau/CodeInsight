df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result1 = [{'A': 1, 'B': 3}, {'A': 2, 'B': 4}]
result1 = test(df1)
assert result1 == expected_result1, 'Test failed'