df0 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
var0 = 'a'
var1 = True
expected_output = df0.sort_values('a', ascending=True)
output = test(df0, var0, var1)
assert output.equals( expected_output), 'Test failed'