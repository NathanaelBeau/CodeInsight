df0 = pd.DataFrame({ 'A': [50, 60, 70, 80], 'B': ['e', 'f', 'g', 'h'] })
column_name0 = 'B'
some_value0 = 'f'
expected_result =  1
result = test(df0, column_name0, some_value0)
assert result == expected_result, 'Test failed'