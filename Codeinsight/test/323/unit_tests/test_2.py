df0 = pd.DataFrame({'A': [np.nan, np.nan, np.nan, np.nan]})
expected_result =  [0, 1, 2, 3]
result = test(df0)
assert result == expected_result, 'Test failed'