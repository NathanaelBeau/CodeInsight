mat0 = np.array([[0.5, 1.0], [1.5, 2.0]])
mat1 = np.array([[2.0, 3.0], [4.0, 5.0]])
expected_result =  np.array([4., 16.])
result = test(mat0, mat1)
assert np.array_equal(result, expected_result), 'Test failed'