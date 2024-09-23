arr0 = np.array([[1.0, np.nan], [2.0, np.nan], [3.0, 4.0]])
expected_output = (np.array([0, 1]), np.array([1, 1]))
result = test(arr0)
assert np.array_equal(result, expected_output), 'Test failed'