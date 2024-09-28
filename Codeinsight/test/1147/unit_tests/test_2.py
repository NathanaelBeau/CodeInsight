df0 = pd.DataFrame({'a': [1, 3, 2], 'b': [4, 6, 5]})
var0 = 'a'
var1 = False
expected_output = df0.sort_values('a', ascending=False)
output = test(df0, var0, var1)
assert output.equals( expected_output), 'Test failed'