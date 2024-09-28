mat4 = np.array([[2, 4], [6, 8]])
mat5 = np.array([[10, 12], [14, 16]])
expected_result =  np.array([76, 200])  # Diagonal elements of the full dot product
result = test(mat4, mat5)
assert np.array_equal(result, expected_result), 'Test failed'