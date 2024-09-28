df0 = pd.DataFrame({'tuple_column': [(4, 'd'), (5, 'e'), (6, 'f')]})
expected_result =  pd.DataFrame({'A': [4, 5, 6], 'B': ['d', 'e', 'f']})
result = test(df0, 'tuple_column')
assert result.equals(expected_result), 'Test failed'