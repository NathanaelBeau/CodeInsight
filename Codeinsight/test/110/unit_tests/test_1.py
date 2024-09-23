arr0 = np.array([[0,10],[20,30],[40,50]])
expected_output = np.array([[0., 0.2], [0.4, 0.6], [0.8, 1.]])
assert np.array_equal(test(arr0), expected_output), 'Test failed'