arr2 = np.array([4, 5, 6])
arr3 = arr2.copy()
expected_result =  False
result = test(arr2, arr3)
assert result == expected_result, 'Test failed'