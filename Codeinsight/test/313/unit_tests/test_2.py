df0 = pd.DataFrame({'A': ['-', '14', '15'], 'B': ['16', '17', '18']})
expected_result_3 = pd.DataFrame({'A': [np.nan, 14., 15.], 'B': [16., 17., 18.]})
result_3 = test(df0)
assert test(df0) .equals( expected_result_3), 'Test failed'