arr1 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
var1 = 3
expected_result =  np.array([7, 8, 9])
result = test(arr1, var1)
assert np.array_equal(result, expected_result), 'Test failed'