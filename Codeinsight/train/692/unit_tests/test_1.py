arr0 = np.array([1, 2, 3, 4, 5])
expected_output = np.array([[0, 1, 0, 3, 0],
                            [0, 2, 0, 4, 0],
                            [0, 3, 0, 5 ,0]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'