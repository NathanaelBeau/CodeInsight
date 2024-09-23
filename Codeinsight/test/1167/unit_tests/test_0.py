s0 = pd.Series([1, 2, 3])
func = lambda x: x**2
expected_result_map = pd.Series([1, 4, 9])
result_map = test(s0, func)
assert result_map.equals(expected_result_map), 'Test failed'