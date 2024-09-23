mat2 = np.array([[1, 0], [0, 1]])
mat3 = np.array([[9, 8], [7, 6]])
expected_result =  np.array([9, 6])  # Diagonal elements of the full dot product
result = test(mat2, mat3)
assert np.array_equal(result, expected_result), 'Test failed'