data = { 'group': [1, 2, 1, 2, 3, 3, 4, 4], 'value': [10., None, 30., 40., 50., None, 70., None] }
df0 = pd.DataFrame(data)
var0 = 'group'
var1 = 'value'
expected_output = pd.DataFrame({ 'group': [1, 2, 1, 2, 3, 3, 4, 4], 'value': [10., 40., 30., 40., 50., 50., 70., 70.] })
assert test(df0, var0, var1).equals(expected_output), 'Test failed'