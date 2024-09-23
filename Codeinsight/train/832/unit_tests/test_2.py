df0 = pd.DataFrame({'P': [7, 8, 9]})
lst0 = ['Q', 'R', 'S']
expected_result =  pd.DataFrame({'P': [7, 8, 9], 'Q': [np.nan, np.nan, np.nan], 'R': [np.nan, np.nan, np.nan], 'S': [np.nan, np.nan, np.nan]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'