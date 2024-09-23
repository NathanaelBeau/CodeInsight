arr0 = np.array([[0.0, 3.0], [0.1, 1.0], [0.2, -1.0]])
expected_output = np.array([[0.0, 3.0], [0.1, 1.0]])
assert (test(arr0)  == expected_output).all(), 'Test failed'