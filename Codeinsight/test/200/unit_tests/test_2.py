mat2 = np.array([[5, 6], [7, 8]])
expected_result =  np.log(mat2 + 1e-10)
result = test(mat2)
assert np.allclose(result, expected_result), 'Test failed'