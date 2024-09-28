arr0 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
lst0 = [2, 0, 1]
expected_result =  np.array([12, 13, 17])
result = test(arr0, lst0)
assert result.tolist() == expected_result.tolist(), 'Test failed'