df0_1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=['w', 'x', 'y', 'z'])
row_label_1 = 'z'
column_label_1 = 'A'
expected_result_1 = 4
result_1 = test(df0_1, row_label_1, column_label_1)
assert result_1 == expected_result_1, 'Test failed'