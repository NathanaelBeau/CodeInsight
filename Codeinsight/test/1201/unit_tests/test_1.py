df_test_3 = pd.DataFrame({'A': [1, 2]})
dict_test_3 = {'A': 3, 'B': 4}  # 'B' is a new column
result_3 = test(df_test_3, dict_test_3)
expected_3 = pd.DataFrame({'A': [1, 2, 3], 'B': [None, None, 4]})
assert result_3.equals(expected_3), 'Test failed'
