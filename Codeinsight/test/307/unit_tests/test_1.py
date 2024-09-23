arr0 = np.array([10, 20, 30, 40])
arr1 = np.array([10, 21, 30, 41])
expected_result =  2
result = test(arr0, arr1)
assert result == expected_result, 'Test failed'