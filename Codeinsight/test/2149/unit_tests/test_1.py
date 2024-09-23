df0 = pd.DataFrame({ 'A': [10.5, 20.7, 30.9], 'B': [40.1, 38.15, 50.2], 'C': [60.3, 70.4, 38.15] })
df1 = pd.DataFrame({ 'X': [1, 2, 3], 'Y': [4, 5, 6], 'Z': [7, 38.15, 9] })
var0 = 38.15
expected_result =  ['Z']
result = test(df1, var0)
assert result == expected_result, 'Test failed'