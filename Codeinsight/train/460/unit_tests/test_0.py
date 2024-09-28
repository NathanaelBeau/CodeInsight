from scipy.sparse import csr_matrix
mat0 = csr_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
expected_result =  np.matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
result = test(mat0)
assert np.array_equal(result, expected_result), 'Test failed'