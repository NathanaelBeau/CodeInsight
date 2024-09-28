df0 = pd.DataFrame({'A': [1, 2, np.nan, 4]})
expected_result =  [2]
result = test(df0)
assert result == expected_result, 'Test failed'