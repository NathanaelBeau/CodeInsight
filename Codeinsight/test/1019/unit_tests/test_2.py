arr2 = np.array([1.1, 2.2, 3.3])
idx2 = np.array([2, 0, 1])
expected_result =  np.array([3.3, 1.1, 2.2])
result = test(arr2, idx2)
assert np.array_equal(result, expected_result), 'Test failed'