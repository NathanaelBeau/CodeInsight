arr0 = np.array([-1, 0, 1])
arr1 = np.array([1, 0, -1])
expected_result =  np.array([[ 1., -1.], [-1.,  1.]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'