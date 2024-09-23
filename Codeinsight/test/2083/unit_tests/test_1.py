df2 = pd.DataFrame({'A': [2, 3, 4]})
result_2 = test(df2, 'A', 2, 4)
expected_2 = pd.Series([True, True, True])
assert result_2.equals(expected_2),  'Test failed'