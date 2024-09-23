arr0 = np.array([6, 7])
arr1 = np.array([8, 9, 10])
expected_result =  [np.array([[6, 7], [6, 7], [6, 7]]), np.array([[8, 8], [9, 9], [10, 10]])]
result = test(arr0, arr1)
assert all([np.array_equal(res, exp) for res, exp in zip(result, expected_result)]), 'Test failed'