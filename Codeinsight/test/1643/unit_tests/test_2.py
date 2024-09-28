df0 = pd.DataFrame({ 'A': [10.5, 20.7, 30.9], 'B': [40.1, 38.15, 50.2], 'C': [60.3, 70.4, 38.15] })
df2 = pd.DataFrame({ 'P': [10, 11, 12], 'Q': [13, 14, 15], 'R': [16, 17, 18] })
var0 = 38.15
expected_result =  []
result = test(df2, var0)
assert result == expected_result, 'Test failed'