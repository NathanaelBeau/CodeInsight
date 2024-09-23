data = { 'group': [1, 2, 1, 2, 3, 3, 4, 4], 'value': [10., 20., None, 40., 50., None, None, 80.] }
df0 = pd.DataFrame(data)
var0 = 'group'
var1 = 'value'
expected_output = pd.DataFrame({ 'group': [1, 2, 1, 2, 3, 3, 4, 4], 'value': [10., 20., 10., 40., 50., 50., 80., 80.] })
assert test(df0, var0, var1).equals(expected_output), 'Test failed'