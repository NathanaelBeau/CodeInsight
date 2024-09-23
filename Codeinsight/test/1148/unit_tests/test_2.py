mat2 = np.array([[100, 200], [300, 400], [500, 600]])
var2 = 1
expected_result =  np.array([[100], [300], [500]])
result = test(mat2, var2)
assert np.array_equal(result, expected_result), 'Test failed'