df2 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
expected_result2 = pd.DataFrame({'A': [1, 3, 4], 'B': [5, 7, 8]})
result2 = test(df2, 'A', 2)
assert result2.equals(expected_result2), 'Test failed'