df0 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, np.nan, 12]})
expected_result =  pd.DataFrame({'X': [8], 'Y': [np.nan]}).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'