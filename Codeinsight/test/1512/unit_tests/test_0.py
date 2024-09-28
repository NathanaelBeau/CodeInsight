df0 = pd.DataFrame({'values': [10, 20, 30], 'weights': [1, 2, 3]})
col_values = 'values'
col_weights = 'weights'
expected_result =  (10*1 + 20*2 + 30*3) / (1 + 2 + 3)
result = test(df0, col_values, col_weights)
assert result == expected_result, 'Test failed'