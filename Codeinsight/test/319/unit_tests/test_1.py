var0 = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3], 'B': ['a', 'b', 'b', 'c', 'c', 'c']})
col0 = 'B'
expected_result =  pd.Series({'c': 3, 'b': 2, 'a': 1})
result = test(var0, col0)
assert result.equals(expected_result), 'Test failed'