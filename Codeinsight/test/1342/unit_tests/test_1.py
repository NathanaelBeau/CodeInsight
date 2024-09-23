arr0 = np.array([[10, 11, 12]])
lst0 = [13, 14, 15]
expected_result =  np.array([[10, 11, 12], [13, 14, 15]])
result = test(arr0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'