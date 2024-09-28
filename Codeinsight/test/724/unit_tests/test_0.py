df0 = pd.DataFrame({ 'A': [10, 20, 30, 40], 'B': ['a', 'b', 'c', 'd'] })
column_name0 = 'A'
some_value0 = 30
expected_result =  2
result = test(df0, column_name0, some_value0)
assert result == expected_result, 'Test failed'