df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
func = lambda x: x + 1
expected_result_applymap = pd.DataFrame({'A': [2, 3, 4], 'B': [5, 6, 7]})
result_applymap = test(df0, func)
assert result_applymap.equals(expected_result_applymap), 'Test failed'