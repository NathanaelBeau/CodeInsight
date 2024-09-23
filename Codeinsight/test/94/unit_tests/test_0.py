var0 = 'gdp'
var1 = 'log(gdp)'
expected_output = pd.DataFrame({'var1': [1, 2, 3, 4, 5]})
df = pd.DataFrame({'var0': [1, 2, 3, 4, 5]})
assert test(df) .equals(expected_output), 'Test failed'