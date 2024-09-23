arr1 = np.array([[10, 20, 30], [40, 50, 60]])
var1 = 1
expected_result =  arr1[:, 0]
result = test(arr1, var1)
assert np.array_equal(result, expected_result), 'Test failed'