arr0 = np.array([0.5, 1.5, 2.5])
arr1 = np.array([0.5, 1.5, 2.5])
expected_result =  3
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'