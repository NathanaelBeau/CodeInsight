arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst0 = [0, 1, 2]
expected_result =  np.array([1, 5, 9])
result = test(arr0, lst0)
assert result.tolist() == expected_result.tolist(), 'Test failed'