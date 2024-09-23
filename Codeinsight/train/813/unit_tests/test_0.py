var0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result =  pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'