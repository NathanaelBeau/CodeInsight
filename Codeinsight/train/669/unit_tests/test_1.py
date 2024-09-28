data = {'col1': ['Hello', 'World']}
df0 = pd.DataFrame(data)
var0 = 'col1'
var1 = 'newCol'
expected_output = pd.DataFrame({ 'col1': ['Hello', 'World'], 'newCol': ['Hello', 'World'] })
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'