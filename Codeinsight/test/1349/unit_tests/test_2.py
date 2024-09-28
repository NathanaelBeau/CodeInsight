df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]})
var0 = 'C'
expected_result =  240
assert test(df0, var0) == expected_result, 'Test failed'