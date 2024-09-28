df0 = pd.DataFrame({ 'User': ['A', 'A', 'B', 'B', 'C', 'C'], 'X': [0, 1, 2, 3, 0, 0] })
var0 = 'User'
var1 = 'X'
expected_output = pd.DataFrame({ 'User': ['C', 'C'], 'X': [0, 0] })
result = test(df0, var0, var1)
assert expected_output.reset_index(drop=True, inplace=True)==result.reset_index(drop=True, inplace=True), 'Test failed'