df0 = pd.DataFrame({ 'A': [1, 2], 'B': ['foo', 'bar'], 'C': [3.14, 2.71] })
lst0 = ['C', 'B']
expected_output = (test(df0, lst0))
assert test(df0, lst0).equals(expected_output), 'Test failed'