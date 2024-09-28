arr4 = np.array([[15], [16], [17]])
arr5 = np.array([18, 19, 20])
expected_result =  np.array([[15, 18], [16, 19], [17, 20]])
result = test(arr4, arr5)
assert np.array_equal(result, expected_result), 'Test failed'