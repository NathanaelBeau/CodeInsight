df0 = pd.DataFrame({'tuple_col': [('a','b'), ('c','d'), ('e','f')]})
expected_result =  pd.DataFrame({'col0': ['a', 'c', 'e'], 'col1': ['b', 'd', 'f']})
result = test(df0, 'tuple_col')
assert result.equals(expected_result), 'Test failed'