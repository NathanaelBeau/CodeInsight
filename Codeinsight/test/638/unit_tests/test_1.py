from scipy.sparse import csr_matrix
mat1 = csr_matrix([[0, 0], [0, 0]])
expected_result =  np.matrix([[0, 0], [0, 0]])
result = test(mat1)
assert np.array_equal(result, expected_result), 'Test failed'