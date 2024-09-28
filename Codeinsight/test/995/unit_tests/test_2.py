df0 = pd.DataFrame({ 'A': [np.nan, np.nan, np.nan], 'B': [np.nan, 20, np.nan] })
expected_result =  pd.DataFrame({ 'A': [], 'B': [] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'