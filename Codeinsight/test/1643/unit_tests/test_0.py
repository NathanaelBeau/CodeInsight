df0 = pd.DataFrame({ 'A': [10.5, 20.7, 30.9], 'B': [40.1, 38.15, 50.2], 'C': [60.3, 70.4, 38.15] })
var0 = 38.15
expected_result =  ['B', 'C']
result = test(df0, var0)
assert result == expected_result, 'Test failed'