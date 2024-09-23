var0 = np.array([[0, 0], [0, 1]])
expected_result =  csr_matrix(var0)
result = test(var0)
assert (result != expected_result).nnz == 0, 'Test failed'