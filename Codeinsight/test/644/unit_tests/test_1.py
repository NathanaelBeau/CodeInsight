np_array = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
value = 18
expected_output = (np.array([2]), np.array([1]))
assert test(np_array, value) == expected_output, 'Test failed'