arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expected_result =  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
result = test(arr0)
assert result == expected_result, 'Test failed'