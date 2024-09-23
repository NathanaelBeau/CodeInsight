var0, var1 = 3, 3
expected_result =  (np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]]), np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2]]))
result = test(var0, var1)
assert np.array_equal(result[0], expected_result[0]) and np.array_equal(result[1], expected_result[1]), 'Test failed'