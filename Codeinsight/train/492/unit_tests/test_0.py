mat0 = np.array([[1, 2], [0, 4]])
expected_result =  np.log(mat0 + 1e-10)
result = test(mat0)
assert np.allclose(result, expected_result), 'Test failed'