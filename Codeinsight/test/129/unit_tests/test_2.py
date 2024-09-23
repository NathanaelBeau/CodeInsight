var0 = np.array([[1, 2], [3, 4]])
expected_result =  csr_matrix(var0)
result = test(var0)
assert (result != expected_result).nnz == 0, 'Test failed'