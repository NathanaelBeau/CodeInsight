df0 = pd.DataFrame({'M': [6, 0, 7], 'N': [0, 8, 0]})
expected_result =  pd.DataFrame({'M': [1, 0, 1], 'N': [0, 1, 0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'