df0 = pd.DataFrame({'A': [1, 2, 3]})
lst0 = ['B', 'C']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [np.nan, np.nan, np.nan], 'C': [np.nan, np.nan, np.nan]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'