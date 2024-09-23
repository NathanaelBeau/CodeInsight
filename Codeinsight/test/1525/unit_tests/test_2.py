arr0 = np.array([-1, 0, 1])
arr1 = np.array(['neg', 'zero', 'pos'])
expected_result0 = np.array([-1, 0, 1])
expected_result1 = np.array(['neg', 'zero', 'pos'])
result0, result1 = test(arr0, arr1)
assert np.array_equal(result0, expected_result0) and np.array_equal(result1, expected_result1), 'Test failed'