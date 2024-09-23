df0 = pd.DataFrame({'A': [1, 0, 2], 'B': [0, 1, 0]})
expected_result =  pd.DataFrame({'A': [1, 0, 1], 'B': [0, 1, 0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'