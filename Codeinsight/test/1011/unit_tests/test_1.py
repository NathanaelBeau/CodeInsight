dict0 = {'X': 100, 'Y': 200, 'Z': 300}
expected_output = np.array([('X', 100), ('Y', 200), ('Z', 300)], dtype=object)
dtype= object
assert (test(dict0, dtype)  == expected_output).all(), 'Test failed'