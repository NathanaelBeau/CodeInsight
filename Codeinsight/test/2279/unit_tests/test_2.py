var2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
expected_result2 = (2, 2, 2)
result2 = test(var2)
assert result2 == expected_result2, 'Test failed'