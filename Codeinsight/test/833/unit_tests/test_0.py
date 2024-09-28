df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 100, 6]})
result = test(df0, 'B', 5, 100)
assert result.equals(expected_result), 'Test failed'