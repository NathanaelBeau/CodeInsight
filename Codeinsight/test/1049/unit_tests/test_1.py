arr1 = np.array([6, 7, 8, 9])
lst1 = [1, 2, 3]
expected_result1 = np.array([False, False, False, False])
result1 = test(arr1, lst1)
assert np.array_equal(result1, expected_result1), 'Test failed'