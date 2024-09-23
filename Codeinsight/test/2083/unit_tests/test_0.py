df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
result_1 = test(df1, 'A', 2, 4)
expected_1 = pd.Series([False, True, True, True, False])
assert result_1.equals(expected_1), 'Test failed'