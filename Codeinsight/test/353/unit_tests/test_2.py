df0 = pd.DataFrame({'AB': ['One', 'Two Three Four', 'Five Six']})
var0 = 'AB'
var1 = ['A', 'B']
expected_output = pd.DataFrame({'AB': ['One', 'Two Three Four', 'Five Six'],
                               'A': ['One', 'Two', 'Five'],
                               'B': [None, 'Three Four', 'Six']})
assert test(df0, var0, var1) .equals(expected_output), 'Test failed'