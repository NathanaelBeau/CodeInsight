columns_list0 = ['X']
n_rows0 = 3
expected_result =  pd.DataFrame({'X': [np.nan, np.nan, np.nan]})
result = test(columns_list0, n_rows0)
assert result.equals(expected_result), 'Test failed'