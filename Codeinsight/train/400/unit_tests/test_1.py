df0 = pd.DataFrame({'X': [4, 5, 6]})
lst0 = ['Y', 'Z']
expected_result =  pd.DataFrame({'X': [4, 5, 6], 'Y': [np.nan, np.nan, np.nan], 'Z': [np.nan, np.nan, np.nan]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'