df0 = pd.DataFrame({ 'User': ['A', 'B', 'B', 'C', 'C', 'D'], 'X': [1, 1, 1, 0, 0, 0] })
var0 = 'User'
var1 = 'X'
var2 = 0
expected_output = pd.DataFrame({ 'User': ['D'], 'X': [0] })
result = test(df0, var0, var1, var2)
assert expected_output.reset_index(drop=True, inplace=True)==result.reset_index(drop=True, inplace=True), 'Test failed'