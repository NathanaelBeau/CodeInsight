var0, var1, var2, var3 = 1, 4, 2, 4
expected_result =  np.array([[[1, 1], [2, 2], [3, 3]],
                            [[2, 3], [2, 3], [2, 3]]])
result = test(var0, var1, var2, var3)
assert np.array_equal(result, expected_result), 'Test failed'