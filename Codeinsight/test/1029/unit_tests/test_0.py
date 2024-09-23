var0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'new_col': [0, 1, 2]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'