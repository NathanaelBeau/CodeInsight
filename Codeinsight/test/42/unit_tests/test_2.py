df2_apply = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
func_apply_3 = lambda col: col.sum()
ax_col = 0
expected_result_apply_3 = pd.Series({'A': 6, 'B': 15})
result_apply_3 = test(df2_apply, func_apply_3, ax_col)
assert result_apply_3.equals(expected_result_apply_3), 'Test failed'