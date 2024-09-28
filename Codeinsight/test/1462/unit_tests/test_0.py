arr0 = np.array([0, -1, 0, 3])
expected_output = np.array([[0, -2, 0, 2],
                            [0, -1, 0, 3],
                            [0, 0, 0, 4]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'