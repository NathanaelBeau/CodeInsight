arr0 = np.array([[0.5, 1.0], [1.5, 2.0], [2.5, 3.0]])
arr1 = np.array([1, 3, 2])
expected_result =  np.array([[0.5, 1.0], [2.5, 3.0], [1.5, 2.0]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'