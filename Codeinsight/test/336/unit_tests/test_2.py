arr2 = np.array([1.0, 2.0, 3.0])
expected_result2 = np.array([1.0, 2.0, 3.0])  # No NaN values to replace
result2 = test(arr2)
assert np.array_equal(result2, expected_result2), 'Test failed'