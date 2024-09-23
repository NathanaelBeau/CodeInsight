arr0 = np.array([1, 5, 1, 5, 1])
expected_maxima = np.array([1, 3])
expected_minima = np.array([2])
maxima, minima = test(arr0)
assert np.array_equal(maxima, expected_maxima) and np.array_equal(minima, expected_minima), 'Test failed'