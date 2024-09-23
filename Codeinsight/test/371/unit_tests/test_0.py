df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'] })
column_name0 = 'A'
value_list0 = [2, 4]
expected_result =  pd.DataFrame({ 'A': [2, 4], 'B': ['b', 'd'] })
result = test(df0, column_name0, value_list0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'