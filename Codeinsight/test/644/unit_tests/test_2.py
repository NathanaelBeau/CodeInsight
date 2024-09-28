np_array = np.array([[10, 20], [30, 40], [50, 60], [70, 80]])
value = 70
expected_output = (np.array([3]), np.array([0]))
assert test(np_array, value) == expected_output, 'Test failed'