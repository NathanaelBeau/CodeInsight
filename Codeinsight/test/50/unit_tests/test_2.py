arr0 = np.array([[1, 2], [3, 4]])
arr1 = np.array([[1, 2], [3, 4]])
expected_result =  True
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'