df2 = pd.DataFrame({'grades': [80, 90, 100], 'weights': [0.5, 0.3, 0.2]})
col_values = 'grades'
col_weights = 'weights'
expected_result =  (80*0.5 + 90*0.3 + 100*0.2) / (0.5 + 0.3 + 0.2)
result = test(df2, col_values, col_weights)
assert result == expected_result, 'Test failed'