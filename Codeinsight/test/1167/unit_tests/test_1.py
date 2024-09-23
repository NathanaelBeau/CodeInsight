s2 = pd.Series([10, 20, 30])
func_map_3 = lambda x: str(x)
expected_result_map_3 = pd.Series(["10", "20", "30"])
result_map_3 = test(s2, func_map_3)
assert result_map_3.equals(expected_result_map_3), 'Test failed'