dict0 = {'A': 1, 'B': 2, 'C': 3}
expected_output = np.array([('A', 1), ('B', 2), ('C', 3)], dtype=object)
dtype= object
assert (test(dict0, dtype)  == expected_output).all(), 'Test failed'