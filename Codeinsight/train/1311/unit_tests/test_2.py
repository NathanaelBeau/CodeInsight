df3 = pd.DataFrame({'A': [5, 6, 7]})
result_3 = test(df3, 'A', 1, 4)
expected_3 = pd.Series([False, False, False])
assert result_3.equals(expected_3), 'Test failed'