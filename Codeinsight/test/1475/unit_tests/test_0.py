data = {'columnOne': ['Hello World', 'US Election', 'Movie Night']}
df0 = pd.DataFrame(data)
var0 = 'columnOne'
var1 = 'column2'
expected_output = pd.DataFrame({ 'columnOne': ['Hello World', 'US Election', 'Movie Night'], 'column2': ['HelloWorld', 'USElection', 'MovieNight'] })
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'