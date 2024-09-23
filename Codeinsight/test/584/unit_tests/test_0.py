var0 = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 4, 5]})
expected_result =  pd.DataFrame({'A': [6, 4, 5], 'B': [3, 1, 2]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'