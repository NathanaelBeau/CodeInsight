df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [5, 10, 15], 'C': [2, 4, 6]})
columns_list0 = ['A', 'B']
column_name0 = 'C'
expected_result =  pd.DataFrame({'A': [5.0, 5.0, 5.0], 'B': [2.5, 2.5, 2.5], 'C': [2, 4, 6]})
result = test(df0, columns_list0, column_name0)
assert result.equals(expected_result), 'Test failed'