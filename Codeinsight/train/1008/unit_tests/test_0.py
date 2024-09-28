arr0 = np.array([3, 1, 2])
arr1 = np.array(['c', 'a', 'b'])
expected_result0 = np.array([1, 2, 3])
expected_result1 = np.array(['a', 'b', 'c'])
result0, result1 = test(arr0, arr1)
assert np.array_equal(result0, expected_result0) and np.array_equal(result1, expected_result1), 'Test failed'