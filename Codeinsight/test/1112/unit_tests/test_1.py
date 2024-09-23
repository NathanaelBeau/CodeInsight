arr2 = np.array([10, 20, 30])
arr3 = np.array([0, 1, 2])
expected_result =  np.array([1, 20, 900])
result = test(arr2, arr3)
assert np.array_equal(result, expected_result), 'Test failed'