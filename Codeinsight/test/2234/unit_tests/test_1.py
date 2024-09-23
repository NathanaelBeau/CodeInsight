var0, var1, var2, var3 = 0, 4, 0, 3
expected_result =  np.array([[[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]],
                            [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]])
result = test(var0, var1, var2, var3)
assert np.array_equal(result, expected_result), 'Test failed'