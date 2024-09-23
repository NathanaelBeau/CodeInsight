df0 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
expected_result =  pd.DataFrame({'A': [2, np.nan], 'B': [np.nan, 6]}).reset_index(drop=True)
result = test(df0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'