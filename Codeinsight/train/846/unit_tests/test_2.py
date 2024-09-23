df0 = pd.DataFrame({'C': [10, 20, 10, 30, 40]})
var0 = 'C'
expected_result =  10
result = test(df0, var0)
assert result == expected_result, 'Test failed'