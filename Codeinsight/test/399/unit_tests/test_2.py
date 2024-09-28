df0 = pd.DataFrame({'M': ['a', None, 'c'], 'N': [None, 'b', 'd']})
expected_result =  pd.DataFrame({'M': ['a', np.nan, 'c'], 'N': [np.nan, 'b', 'd']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'