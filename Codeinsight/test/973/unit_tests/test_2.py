df2 = pd.DataFrame({'C': [True, False, True, True, False]})
col2 = 'C'
var2 = False
expected_result =  1
result = test(df2, col2, var2)
assert result == expected_result, 'Test failed'