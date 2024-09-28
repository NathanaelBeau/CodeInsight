from scipy.sparse import csr_matrix
# Test case 2
sparse_matrix0 = csr_matrix([[1, 2], [2, 3], [3, 4]])
expected_result =  np.array([[1.    ,     0.99227788 ,0.98386991], [0.99227788 ,1. ,        0.99846035], [0.98386991, 0.99846035 ,1.        ]])
result = test(sparse_matrix0)
assert np.allclose(result,expected_result), 'Test failed'