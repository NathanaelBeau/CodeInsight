mat1 = np.array([[5, 6], [7, 8]])
expected_result =  np.array([[25, 36], [49, 64]])
result = test(mat1)
assert np.array_equal(result, expected_result), 'Test failed'