data = {'columnOne': ['Hello $#!', '@ World', 'Movie Night']}
df0 = pd.DataFrame(data)
var0 = 'columnOne'
var1 = 'column2'
expected_output = pd.DataFrame({ 'columnOne': ['Hello $#!', '@ World', 'Movie Night'], 'column2': ['Hello$#!', '@World', 'MovieNight'] })
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'