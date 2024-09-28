arr0 = np.array([[11, 22, 33, 44], [55, 66, 77, 88]])
var0 = 3
expected_result =  np.array([[11, 22, 33], [55, 66, 77]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'