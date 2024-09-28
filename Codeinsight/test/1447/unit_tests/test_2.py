arr0 = np.array([np.nan, 2.0, 3.0])
arr1 = np.array([np.nan, 2.0, 3.0])
expected_result =  True
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'