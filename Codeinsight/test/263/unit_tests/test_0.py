columns_list0 = ['A', 'B']
n_rows0 = 2
expected_result =  pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]})
result = test(columns_list0, n_rows0)
assert result.equals(expected_result), 'Test failed'