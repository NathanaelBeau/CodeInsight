var0, var1 = 2, 3
expected_shape = (var0, var1)
result = test(var0, var1)
assert result.shape == expected_shape and isinstance(result, np.ndarray), 'Test failed'