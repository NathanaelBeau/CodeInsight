columns_list0 = ['M', 'N', 'O']
n_rows0 = 1
expected_result =  pd.DataFrame({'M': [np.nan], 'N': [np.nan], 'O': [np.nan]})
result = test(columns_list0, n_rows0)
assert result.equals(expected_result), 'Test failed'