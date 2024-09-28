var0, var1 = 2, 4
expected_result =  (np.array([[0, 0, 0, 0], [1, 1, 1, 1]]), np.array([[0, 1, 2, 3], [0, 1, 2, 3]]))
result = test(var0, var1)
assert np.array_equal(result[0], expected_result[0]) and np.array_equal(result[1], expected_result[1]), 'Test failed'