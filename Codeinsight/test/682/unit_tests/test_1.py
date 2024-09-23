df1_apply = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
func_apply_2 = lambda row: row.product()
ax_row = 1
expected_result_apply_2 = pd.Series([4, 10, 18])
result_apply_2 = test(df1_apply, func_apply_2, ax_row)
assert result_apply_2.equals(expected_result_apply_2), 'Test failed'