var0, var1 = 4, 2
expected_result =  (np.array([[0, 0], [1, 1], [2, 2], [3, 3]]), np.array([[0, 1], [0, 1], [0, 1], [0, 1]]))
result = test(var0, var1)
assert np.array_equal(result[0], expected_result[0]) and np.array_equal(result[1], expected_result[1]), 'Test failed'