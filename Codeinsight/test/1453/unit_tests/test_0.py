arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row0 = np.array([4, 5, 6])
expected_result =  True
result = test(arr0, row0)
assert result == expected_result, 'Test failed'