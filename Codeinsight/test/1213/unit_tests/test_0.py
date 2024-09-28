mat0 = np.array([[1, 2], [3, 4]])
mat1 = np.array([[5, 6], [7, 8]])
expected_result =  np.array([17, 53])  # 1*5 + 2*6 = 17, 3*7 + 4*8 = 53
result = test(mat0, mat1)
assert np.array_equal(result, expected_result), 'Test failed'