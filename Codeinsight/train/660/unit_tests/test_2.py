from scipy.sparse import csr_matrix
# Test case 3
sparse_matrix0 = csr_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
expected_result =  np.array([[1.    ,     0.79282497,0.77193024], [0.79282497, 1. ,        0.99819089], [0.77193024 ,0.99819089, 1.        ]])
result = test(sparse_matrix0)
assert np.allclose(result,expected_result), 'Test failed'