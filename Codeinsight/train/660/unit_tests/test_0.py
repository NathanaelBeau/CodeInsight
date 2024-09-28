from scipy.sparse import csr_matrix
# Test case 1
sparse_matrix0 = csr_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
expected_result =  [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]
result = test(sparse_matrix0)
assert (result == expected_result).all(), 'Test failed'