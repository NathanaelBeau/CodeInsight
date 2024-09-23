arr0 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
expected_result =  (2, 1, 1)
result = test(arr0)
assert result == expected_result, 'Test failed'