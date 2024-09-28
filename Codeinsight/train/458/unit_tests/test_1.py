var0 = 'population'
var1 = 'log(population)'
expected_output = pd.DataFrame({'var1': [100, 200, 300, 400, 500]})
df = pd.DataFrame({'var0': [100, 200, 300, 400, 500]})
assert test(df) .equals(expected_output), 'Test failed'