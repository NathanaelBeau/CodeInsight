dict0 = {'x': 10, 'y': 20, 'z': 30}
expected_output = np.array([('x', 10), ('y', 20), ('z', 30)], dtype=object)
dtype = object
assert (test(dict0)  == expected_output).all(), 'Test failed'