df_test_4 = pd.DataFrame({'A': [1], 'B': ['hello']})
dict_test_4 = {'A': 2, 'B': 'world'}
result_4 = test(df_test_4, dict_test_4)
expected_4 = pd.DataFrame({'A': [1, 2], 'B': ['hello', 'world']})
assert result_4.equals(expected_4), 'Test failed'