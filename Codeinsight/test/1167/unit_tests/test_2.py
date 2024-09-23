s1 = pd.Series([4, 5, 6])
func_map_2 = lambda x: x**3
expected_result_map_2 = pd.Series([64, 125, 216])
result_map_2 = test(s1, func_map_2)
assert result_map_2.equals(expected_result_map_2), 'Test failed'