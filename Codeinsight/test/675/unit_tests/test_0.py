df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
n0 = 2
expected_result1 = pd.DataFrame({'A': [1, 2], 'B': [6, 7]})
expected_result2 = pd.DataFrame({'A': [3, 4, 5], 'B': [8, 9, 10]})
result1, result2 = test(df0, n0)
assert result1.reset_index(drop=True).equals(expected_result1) and result2.reset_index(drop=True).equals(expected_result2), 'Test failed'