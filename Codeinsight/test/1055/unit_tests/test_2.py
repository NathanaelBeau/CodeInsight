df0 = pd.DataFrame({'tuple_column': [(7, 'g'), (8, 'h'), (9, 'i')]})
expected_result =  pd.DataFrame({'A': [7, 8, 9], 'B': ['g', 'h', 'i']})
result = test(df0, 'tuple_column')
assert result.equals(expected_result), 'Test failed'