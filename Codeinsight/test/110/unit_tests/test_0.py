arr0 = np.array([[1,2,3],[4,5,6],[7,8,9]])
expected_output = np.array([[0., 0.125, 0.25], [0.375, 0.5, 0.625], [0.75, 0.875, 1.]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'