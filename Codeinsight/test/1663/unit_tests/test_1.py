arr0 = np.array([[15, 16, 14], [17, 18, 19], [20, 21, 22]])
expected_result =  (0, 2)
result = test(arr0)
assert result == expected_result, 'Test failed'