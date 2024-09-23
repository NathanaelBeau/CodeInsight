arr4 = np.array([[7, 8], [9, 10]])
arr5 = arr4[:, 1]
expected_result =  True
result = test(arr4, arr5)
assert result == expected_result, 'Test failed'