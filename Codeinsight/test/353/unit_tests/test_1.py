df0 = pd.DataFrame({'AB': ['Apple Orange', 'Banana Cherry', 'Grapes']})
var0 = 'AB'
var1 = ['A', 'B']
expected_output = pd.DataFrame({'AB': ['Apple Orange', 'Banana Cherry', 'Grapes'],
                               'A': ['Apple', 'Banana', 'Grapes'],
                               'B': ['Orange', 'Cherry', None]})
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'