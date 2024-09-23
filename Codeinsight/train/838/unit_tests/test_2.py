df0 = pd.DataFrame({'X': [6, 8, 10], 'Y': [3, 4, 5], 'Z': [2, 2, 2]})
columns_list0 = ['X', 'Y']
column_name0 = 'Z'
expected_result =  pd.DataFrame({'X': [3.0, 4.0, 5.0], 'Y': [1.5, 2.0, 2.5], 'Z': [2, 2, 2]})
result = test(df0, columns_list0, column_name0)
assert result.equals(expected_result), 'Test failed'