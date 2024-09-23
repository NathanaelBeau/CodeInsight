df0 = pd.DataFrame({ 'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4], 'C': [1, 2, 3, 4] })
expected_result =  pd.Series({'A': 25.0, 'B': 25.0, 'C': 0.0})
result = test(df0)
assert result.equals(expected_result), 'Test failed'