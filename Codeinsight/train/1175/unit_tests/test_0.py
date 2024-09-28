df0 = pd.DataFrame({'tuple_column': [(1, 'a'), (2, 'b'), (3, 'c')]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
result = test(df0, 'tuple_column')
assert result.equals(expected_result), 'Test failed'