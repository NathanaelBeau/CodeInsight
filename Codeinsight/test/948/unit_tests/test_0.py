arr0 = np.array([1, 2, 3, 4, 5])
arr1 = np.array([1, 2, 3, 5, 6])
expected_result =  3
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'