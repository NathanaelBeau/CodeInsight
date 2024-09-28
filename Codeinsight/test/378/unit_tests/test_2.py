df0 = pd.DataFrame({'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]})
column_name0 = 'C'
expected_result =  (0.325, 0.55, 0.775)
result = test(df0, column_name0)
assert result == expected_result, 'Test failed'