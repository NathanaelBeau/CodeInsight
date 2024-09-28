arr1 = np.array(['a', 'b', 'c', 'd'])
idx1 = np.array([2, 3, 0, 1])
expected_result =  np.array(['c', 'd', 'a', 'b'])
result = test(arr1, idx1)
assert np.array_equal(result, expected_result), 'Test failed'