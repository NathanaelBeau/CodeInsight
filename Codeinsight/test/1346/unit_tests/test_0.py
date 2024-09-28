arr0 = np.array([1, 2, 3, 4, 5])
arr1 = np.array([5, 4, 3, 2, 1])
expected_result =  np.array([[ 2.5, -2.5], [-2.5,  2.5]])
result = test(arr0, arr1)
assert np.array_equal(result, expected_result), 'Test failed'