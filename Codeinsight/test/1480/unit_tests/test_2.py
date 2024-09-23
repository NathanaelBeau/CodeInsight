df0 = pd.DataFrame({'P': [np.nan, 14, 15], 'Q': [16, 17, 18]})
expected_result =  pd.DataFrame({'P': [np.nan], 'Q': [16]}).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'