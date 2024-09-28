dict0 = {'One': 'Hello', 'Two': 'World'}
expected_output = np.array([('One', 'Hello'), ('Two', 'World')], dtype=object)
dtype= object
assert (test(dict0, dtype)  == expected_output).all(), 'Test failed'