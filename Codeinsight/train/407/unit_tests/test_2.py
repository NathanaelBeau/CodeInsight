arr0 = np.array([2, 2, 2, 2, 2])
expected_maxima = np.array([])
expected_minima = np.array([])
maxima, minima = test(arr0)
assert np.array_equal(maxima, expected_maxima) and np.array_equal(minima, expected_minima), 'Test failed'