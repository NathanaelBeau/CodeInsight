dict0 = {'a': 1, 'b': 2, 'c': 3}
dtype = object 
expected_output = np.array([('a', 1), ('b', 2), ('c', 3)], dtype=object)
assert (test(dict0,)  == expected_output).all(), 'Test failed'