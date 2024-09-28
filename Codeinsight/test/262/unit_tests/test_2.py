arr4 = np.array([2, 3, 4])
arr5 = np.array([3, 2, 1])
expected_result =  np.array([8, 9, 4])
result = test(arr4, arr5)
assert np.array_equal(result, expected_result), 'Test failed'