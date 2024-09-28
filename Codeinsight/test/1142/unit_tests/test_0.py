arr0 = np.array([[10,20,30], [40,50,60]])
col0 = np.array([[1], [2]])
expected_result =  np.array([[10, 20, 30, 1], [40, 50, 60, 2]])
result = test(arr0, col0)
assert np.array_equal(result, expected_result), 'Test failed'