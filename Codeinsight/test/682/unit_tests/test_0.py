df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
func = lambda row: row.sum()
ax = 1
expected_result_apply = pd.Series([5, 7, 9])
result_apply = test(df0, func, ax)
assert result_apply.equals(expected_result_apply), 'Test failed'