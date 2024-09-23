data = {'a': [5, 4, 3, 2, 1],
        'b': [10, 9, 8, 7, 6]}
df0 = pd.DataFrame(data)
var0 = ['a']
var1 = [1, 3]
expected_output = pd.DataFrame({'a': [4.0, 2.0]}, index=var1)
output = test(df0, var0, var1)
output = output.round(2)
assert output.equals(expected_output), 'Test failed'