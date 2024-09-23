df0 = pd.DataFrame({'C': [1, 2, 3, 4], 'D': [5, 6, 7, 8]})
col_condition = 'C'
condition_val = 3
col_update = 'D'
new_val = 15
expected_result =  pd.DataFrame({'C': [1, 2, 3, 4], 'D': [5, 6, 15, 15]})
result = test(df0.copy(), col_condition, condition_val, col_update, new_val)
assert result.equals(expected_result), 'Test failed'