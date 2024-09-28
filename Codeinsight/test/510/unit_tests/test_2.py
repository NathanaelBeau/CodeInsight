var0 = 'country'
var1 = 'log(country)'
expected_output = pd.DataFrame({'var1': ['France', 'Germany', 'Italy']})
df = pd.DataFrame({'var0': ['France', 'Germany', 'Italy']})
assert test(df) .equals(expected_output), 'Test failed'