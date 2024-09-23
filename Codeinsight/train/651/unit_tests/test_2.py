data = {'P': [0, 0, 0, 0, 0],
         'Q': [-1, -2, -3, -4, -5]}
df0 = pd.DataFrame(data)
var0 = 'P'
expected_output = 0.0
assert test(df0, var0) ==expected_output, 'Test failed'