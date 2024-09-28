df0 = pd.DataFrame({'X': [None, 8, 9], 'Y': [10, 11, None]})
expected_result =  pd.DataFrame({'X': [np.nan, 8., 9.], 'Y': [10., 11., np.nan]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'