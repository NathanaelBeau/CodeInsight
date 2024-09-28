df1_applymap = pd.DataFrame({'X': [2, 3, 4], 'Y': [5, 6, 7]})
func_applymap_2 = lambda x: x**2
expected_result_applymap_2 = pd.DataFrame({'X': [4, 9, 16], 'Y': [25, 36, 49]})
result_applymap_2 = test(df1_applymap, func_applymap_2)
assert result_applymap_2.equals(expected_result_applymap_2), 'Test failed'