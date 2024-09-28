arr0 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
expected_result =  (2, 2, 2)
result = test(arr0)
assert result == expected_result, 'Test failed'