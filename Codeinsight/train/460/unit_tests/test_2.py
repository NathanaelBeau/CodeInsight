from scipy.sparse import csr_matrix
mat2 = csr_matrix([[6], [7]])
expected_result =  np.matrix([[6], [7]])
result = test(mat2)
assert np.array_equal(result, expected_result), 'Test failed'