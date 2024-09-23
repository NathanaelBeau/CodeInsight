var0, var1, var2, var3 = 0, 5, 0, 5
expected_result =  np.array([[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]],
                            [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]])
result = test(var0, var1, var2, var3)
assert np.array_equal(result, expected_result), 'Test failed'