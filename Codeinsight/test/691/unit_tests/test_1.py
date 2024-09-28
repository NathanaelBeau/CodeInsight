df0 = pd.DataFrame({'a': [0., 0., 0.], 'b': [1., 1., 1.], 'c': [2., 2., 2.]})
expected_output = pd.DataFrame({'a': [-1., -1., -1.], 'b': [0., 0., 0.], 'c': [1., 1., 1.]})
assert test(df0) .equals(expected_output), 'Test failed'