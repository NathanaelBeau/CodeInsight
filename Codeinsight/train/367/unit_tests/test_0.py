data = {'A': [-1, 2, -3, 4, -5],
        'B': [0, 1, 0, 1, 0]}
df0 = pd.DataFrame(data)
var0 = 'A'
expected_output = 0.4
assert test(df0, var0) ==expected_output, 'Test failed'