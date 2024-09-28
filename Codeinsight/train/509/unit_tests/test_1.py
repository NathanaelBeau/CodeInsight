df1 = pd.DataFrame({ 'X': [np.nan, np.nan, np.nan, np.nan], 'Y': [1, 1, 1, 1], 'Z': [1, np.nan, 1, np.nan] })
expected_result =  pd.Series({'X': 100.0, 'Y': 0.0, 'Z': 50.0})
result = test(df1)
assert result.equals(expected_result), 'Test failed'