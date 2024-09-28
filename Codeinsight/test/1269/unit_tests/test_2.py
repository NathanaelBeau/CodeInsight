data = { 'group': [1, 2, 1, 1], 'value': [10., None, 30., 40.] }
df0 = pd.DataFrame(data)
var0 = 'group'
var1 = 'value'
expected_output = pd.DataFrame({ 'group': [1, 2, 1, 1], 'value': [10., 0., 30., 40.] })
assert test(df0, var0, var1).equals(expected_output), 'Test failed'