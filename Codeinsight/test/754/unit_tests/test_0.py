mat0 = np.array([[1, 2], [3, 4]])
mat1 = np.array([[5, 6], [7, 8]])
expected_result =  np.array([19, 50])  # Diagonal elements of the full dot product
result = test(mat0, mat1)
assert np.array_equal(result, expected_result), 'Test failed'