df0 = pd.DataFrame({ 'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8] })
expected_result =  pd.DataFrame({ 'A': [1.0, 4.0], 'B': [5.0, 8.0] }).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'