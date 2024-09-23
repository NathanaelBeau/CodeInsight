df0 = pd.DataFrame({'E': [10, 20, 30, 40], 'F': [50, 60, 70, 80]})
col_condition = 'E'
condition_val = 15
col_update = 'F'
new_val = 100
expected_result =  pd.DataFrame({'E': [10, 20, 30, 40], 'F': [50, 100, 100, 100]})
result = test(df0, col_condition, condition_val, col_update, new_val)
assert result.equals(expected_result), 'Test failed'