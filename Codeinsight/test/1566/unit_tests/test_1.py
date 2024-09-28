df0 = pd.DataFrame({ 'User': ['A', 'A', 'B', 'B', 'C', 'C'], 'X': [1, 1, 2, 3, 0, 0] })
var0 = 'User'
var1 = 'X'
var2 = 0
expected_output = pd.DataFrame({ 'User': ['C', 'C'], 'X': [0, 0] })
result = test(df0, var0, var1, var2)
assert expected_output.reset_index(drop=True, inplace=True)==result.reset_index(drop=True, inplace=True), 'Test failed'