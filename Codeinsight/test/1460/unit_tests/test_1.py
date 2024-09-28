mat1 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
var1 = 3
expected_result =  np.array([[10, 20, 30], [50, 60, 70]])
result = test(mat1, var1)
assert np.array_equal(result, expected_result), 'Test failed'