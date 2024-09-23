arr0 = np.array([1, 2, 3])
arr1 = np.array([1, 2, 4])
expected_result =  False
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'