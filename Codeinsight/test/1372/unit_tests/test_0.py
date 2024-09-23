df0 = pd.DataFrame({'var0': [['a', 'b'], ['b'], ['a', 'c']]})
expected_result =  pd.DataFrame({'a': [1, 0, 1], 'b': [1, 1, 0], 'c': [0, 0, 1]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'