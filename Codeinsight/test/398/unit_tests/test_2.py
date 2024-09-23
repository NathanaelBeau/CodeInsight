df2_applymap = pd.DataFrame({'X': [8, 9, 10], 'Y': [11, 12, 13]})
func_applymap_3 = lambda x: str(x)
expected_result_applymap_3 = pd.DataFrame({'X': ["8", "9", "10"], 'Y': ["11", "12", "13"]})
result_applymap_3 = test(df2_applymap, func_applymap_3)
assert result_applymap_3.equals(expected_result_applymap_3), 'Test failed'