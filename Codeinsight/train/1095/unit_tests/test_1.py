mat0 = np.array([[7, 8], [9, 10]])
mat1 = np.array([[1, 0], [0, 1]])
expected_result =  np.array([7, 10])  # 7*1 + 8*0 = 7, 9*0 + 10*1 = 10
result = test(mat0, mat1)
assert np.array_equal(result, expected_result), 'Test failed'