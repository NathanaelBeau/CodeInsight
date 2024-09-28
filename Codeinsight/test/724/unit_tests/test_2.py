df0 = pd.DataFrame({ 'C': [5, 6, 7, 8], 'D': ['i', 'j', 'k', 'l'] })
column_name0 = 'C'
some_value0 = 7
expected_result =  2
result = test(df0, column_name0, some_value0)
assert result == expected_result, 'Test failed'