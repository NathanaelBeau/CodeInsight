df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
col_condition = 'A'
condition_val = 2
col_update = 'B'
new_val = 10
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 10, 10, 10]})
result_test1 = test(df0.copy(), col_condition, condition_val, col_update, new_val)
assert result_test1.equals(expected_result), 'Test failed'