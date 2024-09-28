lst0 = [['x', 'y', 'z'], ['m', 'n']]
expected_output = [('x', 'm'), ('x', 'n'), ('y', 'm'), ('y', 'n'), ('z', 'm'), ('z', 'n')]
assert expected_output == list(itertools.product(*lst0)), 'Test failed'