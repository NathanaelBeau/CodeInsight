df1 = pd.DataFrame({'scores': [50, 60, 70], 'weights': [5, 3, 2]})
col_values = 'scores'
col_weights = 'weights'
expected_result =  (50*5 + 60*3 + 70*2) / (5 + 3 + 2)
result = test(df1, col_values, col_weights)
assert result == expected_result, 'Test failed'