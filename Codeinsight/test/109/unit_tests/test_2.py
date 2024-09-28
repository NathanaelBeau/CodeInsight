# Test 3
mat0 = np.array([[10, 20], [30, 40]])
part = 'upper'
expected_result =  np.array([[10, 20], [0, 40]])
result = test(mat0, part)
assert np.array_equal(result, expected_result), 'Test failed'