data = {'X': [1, 2, 3, 4, 5],
         'Y': [0, -1, 2, -3, 4]}
df0 = pd.DataFrame(data)
var0 = 'X'
expected_output = 1.0
assert test(df0, var0) ==expected_output, 'Test failed'