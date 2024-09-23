arr0 = np.array([30, 10, 20])
arr1 = np.array([3, 1, 2])
expected_result0 = np.array([10, 20, 30])
expected_result1 = np.array([1, 2, 3])
result0, result1 = test(arr0, arr1)
assert np.array_equal(result0, expected_result0) and np.array_equal(result1, expected_result1), 'Test failed'