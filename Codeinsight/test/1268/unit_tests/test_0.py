arr0 = np.array([1, 2, 3])
arr1 = np.array([4, 5])
expected_result =  [np.array([[1, 2, 3], [1, 2, 3]]), np.array([[4, 4, 4], [5, 5, 5]])]
result = test(arr0, arr1)
assert all([np.array_equal(res, exp) for res, exp in zip(result, expected_result)]), 'Test failed'