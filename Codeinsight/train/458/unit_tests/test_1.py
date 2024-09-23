df0_1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=['w', 'x', 'y', 'z'])
row_label_2 = 'x'
column_label_2 = 'B'
expected_result_2 = 6
result_4 = test(df0_1, row_label_2, column_label_2)
assert result_4 == expected_result_2, 'Test failed'