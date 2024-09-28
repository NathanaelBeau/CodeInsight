df0 = pd.DataFrame({'a': [1.5, 2.5], 'b': [0.25, 2.75], 'c': [1.25, 0.75]})
expected_output = pd.DataFrame({'a': [0.5, 0.5], 'b': [-0.75, 0.75], 'c': [0.25, -1.25]})
assert test(df0) .equals(expected_output), 'Test failed'