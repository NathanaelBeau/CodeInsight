arr0 = np.array([1.0, 2.0, np.nan])
arr1 = np.array([1.0, 2.0, np.nan])
expected_result =  True
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'