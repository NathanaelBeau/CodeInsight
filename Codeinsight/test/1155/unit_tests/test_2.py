df0 = pd.DataFrame({ 'A': [6, 7, 8, 9, 10], 'B': ['f', 'g', 'h', 'i', 'j'] })
column_name0 = 'A'
value_list0 = [6, 8, 10]
expected_result =  pd.DataFrame({ 'A': [6, 8, 10], 'B': ['f', 'h', 'j'] })
result = test(df0, column_name0, value_list0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'