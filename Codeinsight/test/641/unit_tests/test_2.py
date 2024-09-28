dict0 = {'key1': 'value1', 'key2': 'value2'}
expected_output = np.array([('key1', 'value1'), ('key2', 'value2')], dtype=object)
dtype = object
assert (test(dict0)  == expected_output).all(), 'Test failed'