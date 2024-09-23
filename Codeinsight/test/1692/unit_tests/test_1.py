df0 = pd.DataFrame({'C': [7, -np.inf, 9], 'D': [10, 11, np.inf]})
expected_result =  pd.DataFrame({'C': [7, np.nan, 9], 'D': [10, 11, np.nan]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'