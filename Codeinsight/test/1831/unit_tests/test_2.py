df0 = pd.DataFrame({'a': [0.5, 2.5, 1.0], 'b': [1.0, 0.0, 3.0]})
expected_output = pd.DataFrame({'a': [-0.25, 1.25, -1.0], 'b': [0.25, -1.25, 1.0]})
assert test(df0) .equals(expected_output), 'Test failed'