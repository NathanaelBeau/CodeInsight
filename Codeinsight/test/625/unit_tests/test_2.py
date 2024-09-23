arr0 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
expected_output = (np.array([]),)
result = test(arr0)
assert np.array_equal(result, expected_output), 'Test failed'