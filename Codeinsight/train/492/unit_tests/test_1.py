mat1 = np.array([[0, 0], [0, 0]])
expected_result =  np.log(mat1 + 1e-10)
result = test(mat1)
assert np.allclose(result, expected_result), 'Test failed'