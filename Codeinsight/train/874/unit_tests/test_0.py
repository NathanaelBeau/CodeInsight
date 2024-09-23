arr0 = np.array([1, 3, 7, 1, 2, 6, 3, 4, 5, 1])
expected_maxima = np.array([2, 5, 8])
expected_minima = np.array([3,6])
maxima, minima = test(arr0)
assert np.array_equal(maxima, expected_maxima) and np.array_equal(minima, expected_minima), 'Test failed'