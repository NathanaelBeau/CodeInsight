np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
value = 5
expected_output = (np.array([1]), np.array([1]))
assert test(np_array, value) == expected_output, 'Test failed'