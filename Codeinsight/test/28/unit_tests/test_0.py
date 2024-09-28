data = {'a': [1, 2, 3, 4, 5],
        'b': [6, 7, 8, 9, 10]}
df0 = pd.DataFrame(data)
var0 = ['a']
var1 = [0, 2, 4]
expected_output = pd.DataFrame({'a': [1.0, 3.0, 5.0]}, index=var1)
output = test(df0, var0, var1)
output = output.round(2)
assert output .equals(expected_output), 'Test failed'